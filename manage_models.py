#!/usr/bin/env python3
"""
Manage local MusicGen models for the AI-DJ workspace.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


REPO_ROOT = Path(__file__).resolve().parent
MUSICGEN_VENV_DIR = ".venv-musicgen"

MODELS = {
    "1": {
        "name": "MusicGen Small",
        "id": "facebook/musicgen-small",
        "size": "~1GB",
        "quality": "starter",
        "speed": "fast",
        "vram": "4GB",
    },
    "2": {
        "name": "MusicGen Medium",
        "id": "facebook/musicgen-medium",
        "size": "~3GB",
        "quality": "balanced",
        "speed": "medium",
        "vram": "8GB",
    },
    "3": {
        "name": "MusicGen Large",
        "id": "facebook/musicgen-large",
        "size": "~6GB",
        "quality": "best",
        "speed": "slow",
        "vram": "12GB+",
    },
    "4": {
        "name": "MusicGen Melody",
        "id": "facebook/musicgen-melody",
        "size": "~6GB",
        "quality": "best",
        "speed": "slow",
        "vram": "12GB+",
    },
}


def musicgen_venv_python(repo_root: Path = REPO_ROOT) -> Path:
    if os.name == "nt":
        return repo_root / MUSICGEN_VENV_DIR / "Scripts" / "python.exe"
    return repo_root / MUSICGEN_VENV_DIR / "bin" / "python"


def python_has_audiocraft(python_executable: str | Path = sys.executable) -> bool:
    try:
        result = subprocess.run(
            [
                str(python_executable),
                "-c",
                "import importlib.util; raise SystemExit(0 if importlib.util.find_spec('audiocraft') else 1)",
            ],
            capture_output=True,
            text=True,
            timeout=20,
        )
    except (OSError, subprocess.SubprocessError):
        return False
    return result.returncode == 0


def get_musicgen_python(repo_root: Path = REPO_ROOT) -> str | None:
    venv_python = musicgen_venv_python(repo_root)
    if venv_python.exists():
        return str(venv_python)
    if python_has_audiocraft(sys.executable):
        return sys.executable
    return None


def print_musicgen_setup_hint() -> None:
    print("MusicGen/AudioCraft environment is not ready.")
    print("Run:")
    print("  .\\setup_local_models.ps1")
    print("Then retry this command.")


def child_failure_message(result: subprocess.CompletedProcess) -> str:
    messages = []
    for stream in (result.stderr, result.stdout):
        if stream:
            text = str(stream).strip()
            if text:
                messages.append(text)
    return "\n".join(messages) or f"child process exited with code {result.returncode}"


def print_header() -> None:
    print("=" * 60)
    print("AI-DJ Local Model Manager")
    print("=" * 60)
    print()


def list_models() -> None:
    print("Available models:")
    print()
    print(f"{'ID':<4} {'Name':<20} {'Size':<8} {'Quality':<10} {'Speed':<8} {'VRAM':<8}")
    print("-" * 70)
    for key, model in MODELS.items():
        print(
            f"{key:<4} {model['name']:<20} {model['size']:<8} "
            f"{model['quality']:<10} {model['speed']:<8} {model['vram']:<8}"
        )
    print()


def download_model(model_id: str) -> bool:
    print(f"Downloading model: {model_id}")
    print("This may take a few minutes.")
    print()

    python_executable = get_musicgen_python()
    if python_executable is None:
        print_musicgen_setup_hint()
        return False

    try:
        result = subprocess.run(
            [
                python_executable,
                "-c",
                (
                    "import sys; "
                    "from audiocraft.models import MusicGen; "
                    "MusicGen.get_pretrained(sys.argv[1]); "
                    "print('Model ready.')"
                ),
                model_id,
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=REPO_ROOT,
            timeout=60 * 60,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        print(f"Download failed: {exc}")
        return False

    if result.returncode != 0:
        print(f"Download failed: {child_failure_message(result)}")
        return False

    if result.stdout:
        print(result.stdout.strip())
    print(f"Model downloaded: {model_id}")
    return True


def test_model(model_id: str) -> bool:
    print(f"Testing model: {model_id}")

    python_executable = get_musicgen_python()
    if python_executable is None:
        print_musicgen_setup_hint()
        return False

    cmd = [
        python_executable,
        str(REPO_ROOT / "13_tools" / "scripts" / "make_dj_track_local.py"),
        "--idea",
        "test audio",
        "--duration",
        "5",
        "--model",
        model_id,
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=REPO_ROOT,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        print(f"Test failed: {exc}")
        return False

    if result.returncode == 0:
        print("Test succeeded.")
        return True

    print(f"Test failed: {child_failure_message(result)}")
    return False


def get_model_cache_size() -> float:
    cache_dir = Path.home() / ".cache" / "huggingface" / "hub"
    if not cache_dir.exists():
        return 0.0

    total_size = 0
    for dirpath, _, filenames in os.walk(cache_dir):
        for filename in filenames:
            file_path = Path(dirpath) / filename
            try:
                total_size += file_path.stat().st_size
            except OSError:
                continue

    return total_size / (1024**3)


def choose_model() -> str | None:
    list_models()
    model_choice = input("Enter model ID (1-4): ").strip()
    if model_choice not in MODELS:
        print("Invalid model option.")
        return None
    return MODELS[model_choice]["id"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="AI-DJ local MusicGen model manager")
    parser.add_argument("--list", action="store_true", help="List available models and exit")
    parser.add_argument("--cache-size", action="store_true", help="Show Hugging Face model cache size and exit")
    parser.add_argument("--status", action="store_true", help="Check MusicGen/AudioCraft environment")
    args = parser.parse_args(argv)

    print_header()

    if args.list:
        list_models()
        return 0

    if args.cache_size:
        size = get_model_cache_size()
        print(f"Model cache size: {size:.2f} GB")
        print("Cache location: ~/.cache/huggingface/hub/")
        return 0

    if args.status:
        python_executable = get_musicgen_python()
        if python_executable:
            print(f"MusicGen Python: {python_executable}")
            return 0
        print_musicgen_setup_hint()
        return 1

    try:
        while True:
            print("Choose an action:")
            print("1. List available models")
            print("2. Download model")
            print("3. Test model")
            print("4. Show cache size")
            print("0. Exit")
            print()

            choice = input("Enter option: ").strip()

            if choice == "0":
                print("Goodbye.")
                return 0
            if choice == "1":
                list_models()
            elif choice == "2":
                model_id = choose_model()
                if model_id and download_model(model_id):
                    if input("Run a 5-second smoke test? (y/N): ").strip().lower() == "y":
                        test_model(model_id)
            elif choice == "3":
                model_id = choose_model()
                if model_id:
                    test_model(model_id)
            elif choice == "4":
                size = get_model_cache_size()
                print(f"Model cache size: {size:.2f} GB")
                print("Cache location: ~/.cache/huggingface/hub/")
                print()
            else:
                print("Invalid option.")

            input("\nPress Enter to continue...")
            print()
    except EOFError:
        print("\nNo interactive input received. Use --help for non-interactive commands.")
        return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
