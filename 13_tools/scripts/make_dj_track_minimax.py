#!/usr/bin/env python3
"""
DJ-ready track generator using MiniMax (2026 Edition).
Optimized for high-fidelity Music 2.5 models and professional workflow.
"""

from __future__ import annotations

import argparse
import copy
import datetime as _dt
import json
import logging
import os
import platform
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("ai-dj-gen")

def _repo_root() -> Path:
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

def _minimax_post(url: str, api_key: str, payload: dict, timeout_s: int = 180) -> dict:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    try:
        r = requests.post(url, headers=headers, json=payload, timeout=timeout_s)
        r.raise_for_status()
        data = r.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error during API call: {e}")
        raise RuntimeError(f"API Connection failed: {e}")

    base_resp = data.get("base_resp")
    if isinstance(base_resp, dict):
        status_code = base_resp.get("status_code")
        if isinstance(status_code, int) and status_code != 0:
            error_msg = base_resp.get("status_msg", "Unknown API Error")
            logger.error(f"MiniMax API Error {status_code}: {error_msg}")
            raise RuntimeError(f"MiniMax API logic error: {error_msg}")

    return data

def _download(url: str, out_path: Path, timeout_s: int = 300) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    logger.info(f"Downloading audio from {url[:50]}...")
    with requests.get(url, stream=True, timeout=timeout_s) as r:
        r.raise_for_status()
        with out_path.open("wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 512):
                if chunk:
                    f.write(chunk)

def _start_file(path: Path) -> None:
    system = platform.system().lower()
    try:
        if system.startswith("windows"):
            os.startfile(str(path))
        elif system == "darwin":
            subprocess.run(["open", str(path)], check=False)
        else:
            subprocess.run(["xdg-open", str(path)], check=False)
    except Exception as e:
        logger.warning(f"Failed to open file automatically: {e}")

def _slim_response(resp: dict) -> dict:
    resp2 = copy.deepcopy(resp)
    data = resp2.get("data")
    if isinstance(data, dict) and "audio" in data:
        audio = data.get("audio")
        if isinstance(audio, str) and len(audio) > 200:
            data["audio"] = f"<{len(audio)} chars omitted>"
    return resp2

def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description="Professional AI DJ Track Generator")
    p.add_argument("--idea", required=True, help="Idea or theme for the track.")
    p.add_argument("--style", default="", help="Genre, e.g. Techno, House, Melodic")
    p.add_argument("--bpm", type=int, default=128, help="BPM target.")
    p.add_argument("--key", default="", help="Musical key (e.g., Amin, 8A).")
    p.add_argument("--instrumental", action="store_true", help="Generate instrumental track (Music 2.5+ Recommended).")
    p.add_argument("--model", default="music-2.5", help="MiniMax model, default: music-2.5")
    p.add_argument("--play", action="store_true", help="Auto-play after generation.")
    p.add_argument("--verbose", action="store_true", help="Enable debug logging.")

    args = p.parse_args(argv)
    if args.verbose:
        logger.setLevel(logging.DEBUG)

    api_key = os.environ.get("MINIMAX_API_KEY", "").strip()
    if not api_key:
        logger.critical("MINIMAX_API_KEY environment variable is missing.")
        return 1

    base = os.environ.get("MINIMAX_API_BASE", "https://api.minimax.io")
    base_v1 = _ensure_v1(base)
    music_url = base_v1 + "/music_generation"

    root = _repo_root()
    stamp = _now_stamp()
    slug = _slugify(args.style or args.idea)

    raw_audio_path = root / "04_generations" / "audio" / "raw" / f"{stamp}_{slug}.mp3"
    out_audio_path = root / "08_exports" / "dj_ready" / f"{stamp}_{slug}.mp3"
    meta_path = root / "04_generations" / "metadata" / f"{stamp}_{slug}.json"

    # Precise structural prompt for Music 2.5
    prompt_parts = [f"Genre: {args.style or 'Electronic'}", f"BPM: {args.bpm}"]
    if args.key: prompt_parts.append(f"Key: {args.key}")
    prompt_parts.append("Structure: [Intro], [Verse], [Build Up], [Drop], [Break], [Drop], [Outro]")
    prompt_parts.append("Mix: Clear kicks, professional mixing, DJ-friendly")
    if args.instrumental: prompt_parts.append("Mode: Instrumental, no vocals")
    prompt_parts.append(f"Theme: {args.idea}")
    
    music_prompt = ", ".join(prompt_parts)
    logger.info(f"Generating track with model {args.model}...")
    logger.debug(f"Prompt: {music_prompt}")

    payload = {
        "model": args.model,
        "prompt": music_prompt,
        "lyrics": "[Inst]" if args.instrumental else "[Intro]\n[Verse]\n[Chorus]\n[Drop]\n[Outro]",
        "audio_setting": {"sample_rate": 44100, "bitrate": 320000, "format": "mp3"},
    }

    try:
        resp = _minimax_post(music_url, api_key, payload)
        audio_url = resp.get("data", {}).get("audio")
        if not audio_url:
            raise RuntimeError("No audio URL in response data.")

        _download(audio_url, raw_audio_path)
        
        # Deploy to exports
        out_audio_path.parent.mkdir(parents=True, exist_ok=True)
        out_audio_path.write_bytes(raw_audio_path.read_bytes())
        
        # Meta info
        meta_info = {
            "version": "2026.1",
            "timestamp": stamp,
            "params": vars(args),
            "prompt": music_prompt,
            "api_response": _slim_response(resp)
        }
        meta_path.parent.mkdir(parents=True, exist_ok=True)
        meta_path.write_text(json.dumps(meta_info, indent=2, ensure_ascii=False), encoding="utf-8")

        logger.info(f"Success! Track exported to: {out_audio_path}")
        if args.play:
            _start_file(out_audio_path)

    except Exception as e:
        logger.error(f"Generation failed: {e}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
