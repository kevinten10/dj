"""ACE-Step local lyrics/song generation entry point.

Examples:
    python make_dj_track_ace_step.py --lyrics "your lyrics" --prompt "style prompt"
    python make_dj_track_ace_step.py --theme "DJ party" --style House
"""

import argparse
import datetime
import importlib
import importlib.util
import subprocess
import sys
import time
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
ACE_STEP_PATH = REPO_ROOT / "13_tools" / "ace_step"


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


LYRICS_TEMPLATES = {
    "House": {
        "prompt": "Electronic House music, upbeat, dance, club, bass, 120 BPM",
        "lyrics": """[Verse 1]
Feel the rhythm in the night
Lights are flashing, everything's right
Moving to the beat we own
In this house we call our home

[Chorus]
Let the bass drop, feel the flow
House music makes us glow
Dancing till the morning light
This is our night, feel so right

[Drop]
Feel the beat
Feel the bass
Move your body
Feel the space

[Verse 2]
Turn the music up so loud
Lost inside this happy crowd
Every beat connects our hearts
This is where the magic starts

[Chorus]
Let the bass drop, feel the flow
House music makes us glow
Dancing till the morning light
This is our night, feel so right

[Bridge]
When the DJ plays our song
We all know where we belong
In the rhythm of the night
Everything will be alright

[Outro]
Keep on dancing
Keep on moving
House music
Forever grooving
""",
    },
    "Techno": {
        "prompt": "Electronic Techno music, dark, industrial, repetitive, heavy bass, 130 BPM",
        "lyrics": """[Verse 1]
Dark beats echo through the night
Machine sounds, industrial might
Pulse is rising, feel the power
This is our electric hour

[Chorus]
Techno beats, techno dreams
Nothing's ever what it seems
Lost inside the digital sound
Where the lost ones can be found

[Drop]
Beat drops
System overload
Feel the power
Explode

[Verse 2]
Synthesizers paint the dark
Every beat becomes a spark
In this world of code and wire
We become the electric fire

[Chorus]
Techno beats, techno dreams
Nothing's ever what it seems
Lost inside the digital sound
Where the lost ones can be found

[Bridge]
When the machines take control
Let the rhythm move your soul
In the darkness we unite
Techno is our light tonight

[Outro]
Repeat
Reset
Reload
Techno
""",
    },
    "Trance": {
        "prompt": "Electronic Trance music, uplifting, melodic, ethereal, emotional, 138 BPM",
        "lyrics": """[Verse 1]
Floating through the starlit sky
Euphoria is drawing nigh
Melodies that touch the soul
Trance music makes us whole

[Chorus]
Take me higher, take me far
Beyond the moon, beyond the star
In this trance we find our way
To a better brighter day

[Drop]
Ascend
Elevate
Transcend
Liberate

[Verse 2]
Hands are reaching for the light
We are infinite tonight
Every note a sacred prayer
Music takes us anywhere

[Chorus]
Take me higher, take me far
Beyond the moon, beyond the star
In this trance we find our way
To a better brighter day

[Bridge]
When the melody unfolds
Stories waiting to be told
In the arms of sound we trust
This is more than just a must

[Outro]
Fly away
Dream again
Trance forever
Amen
""",
    },
}


def create_dj_lyrics(theme: str, style: str = "House") -> tuple[str, str]:
    """Create lyrics and a generation prompt for a supported style."""
    if style in LYRICS_TEMPLATES:
        template = LYRICS_TEMPLATES[style]
        return template["lyrics"], template["prompt"]

    return LYRICS_TEMPLATES["House"]["lyrics"], LYRICS_TEMPLATES["House"]["prompt"]


def resolve_lyrics_and_prompt(args: argparse.Namespace) -> tuple[str, str]:
    """Resolve user input while allowing prompt-only or lyrics-only custom runs."""
    template_lyrics, template_prompt = create_dj_lyrics(args.theme or "DJ party", args.style)
    lyrics = args.lyrics if args.lyrics else template_lyrics
    prompt = args.prompt if args.prompt else template_prompt
    return lyrics, prompt


def _git_value(args: list[str]) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(ACE_STEP_PATH), *args],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
    except FileNotFoundError:
        return "git not found"

    if result.returncode != 0:
        return (result.stderr or result.stdout).strip() or "unavailable"
    return result.stdout.strip()


def _ace_step_runtime_package_issues() -> dict[str, str]:
    required_runtime_packages = ["soundfile"]
    issues = {}
    for package in required_runtime_packages:
        if importlib.util.find_spec(package) is None:
            issues[package] = "not installed"
            continue

        if package == "soundfile":
            try:
                importlib.import_module("soundfile")
            except Exception as exc:
                issues[package] = str(exc).splitlines()[0]

    return issues


def _missing_ace_step_runtime_packages() -> list[str]:
    return list(_ace_step_runtime_package_issues())


def _print_ace_step_runtime_install_hint(missing_packages: list[str]) -> None:
    if not missing_packages:
        return

    issues = _ace_step_runtime_package_issues()
    print("ACE-Step runtime dependencies are missing or unavailable.")
    for package in missing_packages:
        issue = issues.get(package, "unknown issue")
        print(f"  - {package}: {issue}")
    print("Suggested install command:")
    print(f"  python -m pip install {' '.join(missing_packages)}")


def check_ace_step_setup() -> int:
    """Run a lightweight preflight without loading the ACE-Step model."""
    print("ACE-Step local environment check")
    print("=" * 50)
    print(f"Project root: {REPO_ROOT}")
    print(f"ACE-Step directory: {ACE_STEP_PATH}")

    if not ACE_STEP_PATH.exists():
        print("Status: not installed")
        print("Install command:")
        print("  git clone https://github.com/ace-step/ACE-Step.git 13_tools/ace_step")
        return 1

    print("Status: local clone found")
    remote = _git_value(["remote", "get-url", "origin"])
    revision = _git_value(["rev-parse", "--short", "HEAD"])
    branch = _git_value(["branch", "--show-current"])
    print(f"Remote: {remote}")
    print(f"Branch: {branch}")
    print(f"Revision: {revision}")

    if str(ACE_STEP_PATH) not in sys.path:
        sys.path.insert(0, str(ACE_STEP_PATH))

    ace_spec = importlib.util.find_spec("acestep")
    torch_spec = importlib.util.find_spec("torch")
    print(f"Python package 'acestep': {'importable' if ace_spec else 'not importable'}")
    print(f"Python package 'torch': {'installed' if torch_spec else 'not installed'}")

    if not ace_spec:
        print("Suggestion: confirm 13_tools/ace_step/acestep exists, or reclone ACE-Step.")
        return 1
    if not torch_spec:
        print("Suggestion: install PyTorch according to the ACE-Step documentation.")
        return 1

    missing_runtime_packages = _missing_ace_step_runtime_packages()
    if missing_runtime_packages:
        _print_ace_step_runtime_install_hint(missing_runtime_packages)
        return 1

    print("Preflight passed: generation or Web UI startup can be attempted.")
    return 0


def _build_generation_kwargs(
    *,
    duration: int,
    prompt: str,
    lyrics: str,
    infer_steps: int,
    guidance_scale: float,
    seed: int,
    output_path: str,
) -> dict:
    return {
        "audio_duration": duration,
        "prompt": prompt,
        "lyrics": lyrics,
        "infer_step": infer_steps,
        "guidance_scale": guidance_scale,
        "scheduler_type": "euler",
        "cfg_type": "cfg",
        "omega_scale": 10.0,
        "manual_seeds": str(seed) if seed != -1 else "",
        "guidance_interval": 0.5,
        "guidance_interval_decay": 0.0,
        "min_guidance_scale": 3.0,
        "use_erg_tag": False,
        "use_erg_lyric": False,
        "use_erg_diffusion": True,
        "oss_steps": [],
        "guidance_scale_text": 3.0,
        "guidance_scale_lyric": 3.0,
        "save_path": output_path,
    }


def _save_wav_with_soundfile(
    output_path: str,
    target_wav,
    *,
    sample_rate: int,
    format: str = "wav",
) -> str:
    if format != "wav":
        raise ValueError(f"soundfile fallback only supports wav output, got: {format}")

    import numpy as np
    import soundfile as sf

    if hasattr(target_wav, "detach"):
        audio = target_wav.detach().cpu().float().numpy()
    else:
        audio = np.asarray(target_wav, dtype=np.float32)

    if audio.ndim == 2:
        audio = audio.T
    elif audio.ndim != 1:
        raise ValueError(f"Expected 1D or 2D audio, got shape: {audio.shape}")

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(output), audio, sample_rate)
    return str(output)


def _patch_torchaudio_wav_save() -> None:
    import torchaudio

    if getattr(torchaudio.save, "_ai_dj_soundfile_fallback", False):
        return

    original_save = torchaudio.save

    def save_with_soundfile_fallback(uri, src, sample_rate, *args, **kwargs):
        output_format = kwargs.get("format")
        backend = kwargs.get("backend")
        uri_text = str(uri)
        if (output_format == "wav" or uri_text.lower().endswith(".wav")) and backend == "soundfile":
            return _save_wav_with_soundfile(
                uri_text,
                src,
                sample_rate=sample_rate,
                format="wav",
            )

        return original_save(uri, src, sample_rate, *args, **kwargs)

    save_with_soundfile_fallback._ai_dj_soundfile_fallback = True
    torchaudio.save = save_with_soundfile_fallback


def generate_with_ace_step(
    lyrics: str,
    prompt: str,
    duration: int = -1,
    infer_steps: int = 50,
    guidance_scale: float = 7.0,
    seed: int = -1,
    output_path: str | None = None,
    cpu_offload: bool = True,
    bf16: bool = True,
):
    """Generate a lyrics-driven track with ACE-Step."""

    if not ACE_STEP_PATH.exists():
        raise FileNotFoundError(f"ACE-Step directory does not exist: {ACE_STEP_PATH}")

    if str(ACE_STEP_PATH) not in sys.path:
        sys.path.insert(0, str(ACE_STEP_PATH))

    from acestep.pipeline_ace_step import ACEStepPipeline

    _patch_torchaudio_wav_save()

    if output_path is None:
        output_dir = REPO_ROOT / "04_generations" / "audio" / "raw"
        output_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = str(output_dir / f"ace_step_{timestamp}.wav")

    print("ACE-Step local lyrics/song generator")
    print("=" * 50)
    print(f"Lyrics length: {len(lyrics)} characters")
    print(f"Prompt: {prompt}")
    print(f"Duration: {duration if duration > 0 else 'random'} seconds")
    print(f"Inference steps: {infer_steps}")
    print(f"Guidance scale: {guidance_scale}")
    print(f"Seed: {seed}")
    print(f"Output: {output_path}")
    print("=" * 50)

    print("Loading model...")
    pipeline = ACEStepPipeline(
        checkpoint_dir=None,
        dtype="bfloat16" if bf16 else "float32",
        torch_compile=False,
        cpu_offload=cpu_offload,
        overlapped_decode=False,
    )

    print("Model loaded.")
    print("Starting audio generation...")
    start_time = time.time()

    try:
        pipeline(
            **_build_generation_kwargs(
                duration=duration,
                prompt=prompt,
                lyrics=lyrics,
                infer_steps=infer_steps,
                guidance_scale=guidance_scale,
                seed=seed,
                output_path=output_path,
            )
        )
    except ImportError:
        raise

    elapsed = time.time() - start_time
    print("=" * 50)
    print("Generation succeeded.")
    print(f"Elapsed: {elapsed:.2f} seconds")
    print(f"File: {output_path}")
    print("=" * 50)

    return output_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="ACE-Step local lyrics/song generator")
    parser.add_argument("--check", action="store_true", help="Check the ACE-Step environment without loading the model")
    parser.add_argument("--lyrics", type=str, help="Lyrics text")
    parser.add_argument("--prompt", type=str, help="Style prompt")
    parser.add_argument("--theme", type=str, help="Theme name")
    parser.add_argument(
        "--style",
        type=str,
        default="House",
        choices=["House", "Techno", "Trance"],
        help="Music style",
    )
    parser.add_argument("--duration", type=int, default=-1, help="Audio duration in seconds; -1 means random")
    parser.add_argument("--steps", type=int, default=50, help="Inference step count")
    parser.add_argument("--guidance", type=float, default=7.0, help="Guidance scale")
    parser.add_argument("--seed", type=int, default=-1, help="Random seed; -1 means random")
    parser.add_argument("--output", type=str, help="Output file path")
    parser.add_argument("--no-cpu-offload", action="store_true", help="Disable CPU offload; requires more VRAM")
    parser.add_argument("--fp32", action="store_true", help="Use float32 precision; slower but more compatible")
    parser.add_argument("--dry-run", action="store_true", help="Resolve parameters and print configuration without loading the model")

    args = parser.parse_args(argv)

    if args.check:
        return check_ace_step_setup()

    lyrics, prompt = resolve_lyrics_and_prompt(args)

    if args.dry_run:
        print("ACE-Step parameter preview")
        print("=" * 50)
        print(f"Style: {args.style}")
        print(f"Prompt: {prompt}")
        print(f"Lyrics characters: {len(lyrics)}")
        print(f"Duration: {args.duration if args.duration > 0 else 'random'}")
        print(f"Inference steps: {args.steps}")
        print(f"Guidance scale: {args.guidance}")
        print(f"Seed: {args.seed}")
        print(f"CPU offload: {not args.no_cpu_offload}")
        print(f"Precision: {'float32' if args.fp32 else 'bfloat16'}")
        return 0

    try:
        output_path = generate_with_ace_step(
            lyrics=lyrics,
            prompt=prompt,
            duration=args.duration,
            infer_steps=args.steps,
            guidance_scale=args.guidance,
            seed=args.seed,
            output_path=args.output,
            cpu_offload=not args.no_cpu_offload,
            bf16=not args.fp32,
        )
    except ImportError:
        raise

    print(f"\nDone. Music saved to: {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
