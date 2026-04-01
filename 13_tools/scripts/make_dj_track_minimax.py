#!/usr/bin/env python3
"""Generate a DJ-ready track using MiniMax Lyrics + Music Generation APIs.

This script is meant to be run from the repo root, but it will also work from
anywhere by resolving paths relative to this file.

Required env:
  - MINIMAX_API_KEY
Optional env:
  - MINIMAX_API_BASE  (default: https://api.minimax.io)

Examples:
  python 13_tools/scripts/make_dj_track_minimax.py --idea "neon rainy night club, 128bpm, clean drums intro"
  python 13_tools/scripts/make_dj_track_minimax.py --idea "industrial techno" --bpm 132 --style techno --instrumental --play
"""

from __future__ import annotations

import argparse
import copy
import datetime as _dt
import json
import os
import platform
import re
import subprocess
import sys
from pathlib import Path

import requests


def _repo_root() -> Path:
    # .../13_tools/scripts/make_dj_track_minimax.py -> repo root is 2 levels up
    return Path(__file__).resolve().parents[2]


def _now_stamp() -> str:
    return _dt.datetime.now().strftime("%Y%m%d_%H%M%S")


_slug_re = re.compile(r"[^a-zA-Z0-9_-]+")


def _slugify(s: str, max_len: int = 48) -> str:
    s = s.strip().replace(" ", "_")
    s = _slug_re.sub("_", s)
    s = s.strip("_-")
    if not s:
        return "track"
    return s[:max_len]


def _ensure_v1(base: str) -> str:
    base = base.strip().rstrip("/")
    if not base:
        return "https://api.minimax.io/v1"
    if base.endswith("/v1"):
        return base
    return base + "/v1"


def _minimax_post(url: str, api_key: str, payload: dict, timeout_s: int = 120) -> dict:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    r = requests.post(url, headers=headers, json=payload, timeout=timeout_s)
    try:
        data = r.json()
    except Exception:
        raise RuntimeError(f"MiniMax API returned non-JSON (HTTP {r.status_code}): {r.text[:2000]}")

    if not r.ok:
        raise RuntimeError(
            "MiniMax API HTTP error\n"
            f"url: {url}\n"
            f"status: {r.status_code}\n"
            f"body: {json.dumps(data, ensure_ascii=False)[:4000]}"
        )

    base_resp = data.get("base_resp")
    if isinstance(base_resp, dict):
        status_code = base_resp.get("status_code")
        if isinstance(status_code, int) and status_code != 0:
            raise RuntimeError(
                "MiniMax API error\n"
                f"url: {url}\n"
                f"base_resp: {json.dumps(base_resp, ensure_ascii=False)}\n"
            )

    return data


def _download(url: str, out_path: Path, timeout_s: int = 180) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with requests.get(url, stream=True, timeout=timeout_s) as r:
        r.raise_for_status()
        with out_path.open("wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 256):
                if chunk:
                    f.write(chunk)


def _start_file(path: Path) -> None:
    # Cross-platform "open with default application".
    system = platform.system().lower()
    if system.startswith("windows"):
        os.startfile(str(path))  # type: ignore[attr-defined]
        return
    if system == "darwin":
        subprocess.run(["open", str(path)], check=False)
        return
    subprocess.run(["xdg-open", str(path)], check=False)


def _slim_response(resp: dict) -> dict:
    resp2 = copy.deepcopy(resp)
    data = resp2.get("data")
    if isinstance(data, dict) and "audio" in data:
        audio = data.get("audio")
        if isinstance(audio, str) and len(audio) > 200:
            data["audio"] = f"<{len(audio)} chars omitted>"
    return resp2


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description="Generate a track via MiniMax music_generation")
    p.add_argument("--idea", required=True, help="Your idea/theme. Can be Chinese.")
    p.add_argument("--style", default="", help="Optional: e.g. techno / house / drum and bass")
    p.add_argument("--bpm", type=int, default=128, help="Target BPM hint for prompt (not guaranteed).")
    p.add_argument("--key", default="", help="Optional: e.g. A minor / 8A")
    p.add_argument("--instrumental", action="store_true", help="Try to minimize vocals by using mostly [Inst] lyrics.")
    p.add_argument("--no-lyrics-api", action="store_true", help="Do not call lyrics_generation; use template lyrics.")
    p.add_argument("--lyrics", default="", help="Provide your own lyrics (overrides --no-lyrics-api).")
    p.add_argument("--prompt", default="", help="Override the music prompt sent to music_generation.")
    p.add_argument("--model", default="music-2.5", help="MiniMax music model, default: music-2.5")
    p.add_argument("--format", default="mp3", help="Audio format hint, default: mp3")
    p.add_argument("--output-format", default="url", choices=["url", "hex"], help="MiniMax output_format")
    p.add_argument("--base-url", default="", help="API base, e.g. https://api.minimax.io or https://api.minimaxi.com")
    p.add_argument("--play", action="store_true", help="Open the generated file with the default player.")

    args = p.parse_args(argv)

    api_key = os.environ.get("MINIMAX_API_KEY", "").strip()
    if not api_key:
        print("ERROR: MINIMAX_API_KEY is not set.", file=sys.stderr)
        return 2

    base = args.base_url.strip() or os.environ.get("MINIMAX_API_BASE", "https://api.minimax.io")
    base_v1 = _ensure_v1(base)
    lyrics_url = base_v1 + "/lyrics_generation"
    music_url = base_v1 + "/music_generation"

    root = _repo_root()
    stamp = _now_stamp()
    slug = _slugify(args.style or args.idea)

    raw_dir = root / "04_generations" / "audio" / "raw"
    meta_dir = root / "04_generations" / "metadata"
    out_dir = root / "08_exports" / "dj_ready"

    ext = args.format.strip().lower()
    if not ext:
        ext = "mp3"

    raw_audio_path = raw_dir / f"{stamp}_{slug}.{ext}"
    out_audio_path = out_dir / f"{stamp}_{slug}.{ext}"
    meta_path = meta_dir / f"{stamp}_{slug}.json"

    # 1) Lyrics
    if args.lyrics.strip():
        lyrics = args.lyrics.strip()
        lyrics_resp = {"note": "lyrics provided via --lyrics; lyrics_generation skipped"}
    elif args.no_lyrics_api or args.instrumental:
        # Template lyrics. Some models still sing even with [Inst], but this usually reduces vocals.
        lyrics = "\n".join(
            [
                "[Intro]",
                "[Inst]",
                "",
                "[Break]",
                "[Inst]",
                "",
                "[Build Up]",
                "[Inst]",
                "",
                "[Drop]",
                "[Inst]",
                "",
                "[Outro]",
                "[Inst]",
            ]
        )
        lyrics_resp = {"note": "template lyrics used; lyrics_generation skipped"}
    else:
        lp_parts = []
        if args.style:
            lp_parts.append(f"风格：{args.style}")
        lp_parts.append(f"主题：{args.idea}")
        lp_parts.append("写一首适合DJ播放的电子舞曲歌词，段落清晰，尽量短句可重复，避免过长叙事。")
        lp_parts.append("请用标签组织段落（例如 [Intro], [Verse], [Chorus], [Break], [Build Up], [Drop], [Outro]）。")
        lyrics_prompt = "\n".join(lp_parts)

        lyrics_payload = {"mode": "write_full_song", "prompt": lyrics_prompt}
        lyrics_resp = _minimax_post(lyrics_url, api_key=api_key, payload=lyrics_payload)
        lyrics = (lyrics_resp.get("lyrics") or "").strip()
        if not lyrics:
            # Some responses may nest it differently; keep a best-effort fallback.
            raise RuntimeError(f"lyrics_generation returned empty lyrics: {json.dumps(_slim_response(lyrics_resp), ensure_ascii=False)}")

    # 2) Music prompt
    if args.prompt.strip():
        music_prompt = args.prompt.strip()
    else:
        # A pragmatic default prompt that tends to yield DJ-friendly structure.
        prompt_parts = []
        if args.style:
            prompt_parts.append(args.style)
        prompt_parts.append("electronic dance music")
        prompt_parts.append(f"{args.bpm} BPM")
        if args.key:
            prompt_parts.append(f"key: {args.key}")
        prompt_parts.append("DJ-friendly arrangement")
        prompt_parts.append("clean steady kick and drums")
        prompt_parts.append("clear intro and outro for mixing")
        if args.instrumental:
            prompt_parts.append("instrumental, minimal vocals")
        prompt_parts.append(f"theme: {args.idea}")
        music_prompt = ", ".join(prompt_parts)

    music_payload = {
        "model": args.model,
        "prompt": music_prompt,
        "lyrics": lyrics,
        "output_format": args.output_format,
        "audio_setting": {"sample_rate": 44100, "bitrate": 256000, "format": ext},
    }

    music_resp = _minimax_post(music_url, api_key=api_key, payload=music_payload, timeout_s=180)

    # 3) Save audio
    data = music_resp.get("data")
    if not isinstance(data, dict):
        raise RuntimeError(f"music_generation response missing data: {json.dumps(_slim_response(music_resp), ensure_ascii=False)}")

    audio_field = data.get("audio")
    if not isinstance(audio_field, str) or not audio_field:
        raise RuntimeError(f"music_generation response missing audio: {json.dumps(_slim_response(music_resp), ensure_ascii=False)}")

    raw_audio_path.parent.mkdir(parents=True, exist_ok=True)
    out_audio_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.parent.mkdir(parents=True, exist_ok=True)

    if args.output_format == "hex":
        audio_bytes = bytes.fromhex(audio_field)
        raw_audio_path.write_bytes(audio_bytes)
    else:
        # url
        _download(audio_field, raw_audio_path)

    # Copy to DJ-ready exports
    out_audio_path.write_bytes(raw_audio_path.read_bytes())

    meta = {
        "created_at": stamp,
        "idea": args.idea,
        "style": args.style,
        "bpm": args.bpm,
        "key": args.key,
        "instrumental": bool(args.instrumental),
        "model": args.model,
        "prompt": music_prompt,
        "output_format": args.output_format,
        "audio_setting": music_payload["audio_setting"],
        "paths": {
            "raw_audio": str(raw_audio_path.relative_to(root)),
            "dj_ready": str(out_audio_path.relative_to(root)),
        },
        "lyrics": lyrics,
        "lyrics_response": _slim_response(lyrics_resp),
        "music_response": _slim_response(music_resp),
    }

    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"OK: {out_audio_path}")
    print(f"META: {meta_path}")

    if args.play:
        _start_file(out_audio_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
