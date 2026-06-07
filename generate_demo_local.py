#!/usr/bin/env python3
"""
Generate a short local MusicGen demo track.
"""

from __future__ import annotations

import argparse
import os
import platform
import re
import subprocess
import sys
from pathlib import Path

from manage_models import get_musicgen_python, print_musicgen_setup_hint


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def get_repo_root() -> Path:
    return Path(__file__).resolve().parent


def play_audio(file_path: Path) -> bool:
    system = platform.system().lower()
    try:
        if system.startswith("windows"):
            os.startfile(str(file_path))
        elif system == "darwin":
            subprocess.run(["open", str(file_path)], check=False)
        else:
            subprocess.run(["xdg-open", str(file_path)], check=False)
        return True
    except Exception as exc:
        print(f"Failed to open audio automatically: {exc}")
        return False


def build_demo_command(python_executable: str, repo_root: Path) -> list[str]:
    return [
        python_executable,
        str(repo_root / "13_tools" / "scripts" / "make_dj_track_local.py"),
        "--idea",
        "AI DJ Demo, clear kick drum, tech house groove, DJ practice track",
        "--style",
        "Tech House",
        "--bpm",
        "124",
        "--duration",
        "30",
        "--model",
        "facebook/musicgen-small",
    ]


def find_latest_demo_file(repo_root: Path) -> Path | None:
    exports_dir = repo_root / "08_exports" / "dj_ready"
    if not exports_dir.exists():
        return None

    files = sorted(exports_dir.glob("*.wav"), key=lambda item: item.stat().st_mtime, reverse=True)
    return files[0] if files else None


def extract_exported_path(output: str) -> Path | None:
    match = re.search(r"Track exported to:\s*(.+)", output)
    if not match:
        return None
    return Path(match.group(1).strip())


def child_failure_message(result: subprocess.CompletedProcess) -> str:
    messages = []
    for stream in (result.stderr, result.stdout):
        if stream:
            text = str(stream).strip()
            if text:
                messages.append(text)
    return "\n".join(messages) or f"child process exited with code {result.returncode}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a short local MusicGen Tech House demo")
    parser.add_argument("--no-play", action="store_true", help="Do not open the generated audio automatically")
    args = parser.parse_args(argv)

    print("=" * 60)
    print("AI-DJ Local Demo Generator")
    print("=" * 60)
    print()

    repo_root = get_repo_root()
    python_executable = get_musicgen_python(repo_root)
    if python_executable is None:
        print_musicgen_setup_hint()
        return 1

    print("Generating demo music...")
    print("Style: Tech House")
    print("BPM: 124")
    print("Duration: 30 seconds")
    print()

    cmd = build_demo_command(python_executable, repo_root)

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=repo_root,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        print(f"Generation failed: {exc}")
        return 1

    if result.returncode != 0:
        print(f"Generation failed: {child_failure_message(result)}")
        print()
        print("Possible causes:")
        print("  1. MusicGen/AudioCraft dependencies are not installed in .venv-musicgen.")
        print("  2. The model download failed or memory/VRAM is insufficient.")
        print()
        print("Fix:")
        print("  .\\setup_local_models.ps1")
        return 1

    music_file = extract_exported_path(result.stdout)
    if music_file is not None and not music_file.exists():
        music_file = None
    if music_file is None:
        music_file = find_latest_demo_file(repo_root)
    if music_file is None:
        print("Generation command completed, but no WAV file was found in 08_exports/dj_ready/.")
        return 1

    print()
    print("Demo generated successfully.")
    print(f"File: {music_file}")

    if args.no_play:
        return 0

    if play_audio(music_file):
        print("Opened generated audio.")
    else:
        print(f"Open this file manually: {music_file}")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
