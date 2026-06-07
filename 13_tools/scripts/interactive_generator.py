#!/usr/bin/env python3
"""
Interactive DJ Track Generator.

Menu-driven entry point for MiniMax, MusicGen, ACE-Step, practice-plan,
library, and documentation workflows.
"""

import importlib.util
import os
import platform
import subprocess
import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _format_command(cmd: list[str]) -> str:
    return subprocess.list2cmdline(cmd)


def _ace_step_path() -> Path:
    return _repo_root() / "13_tools" / "ace_step"


def _ace_step_importable(ace_step_path: Path) -> bool:
    path_text = str(ace_step_path)
    added_path = False
    if path_text not in sys.path:
        sys.path.insert(0, path_text)
        added_path = True

    try:
        return importlib.util.find_spec("acestep") is not None
    finally:
        if added_path:
            try:
                sys.path.remove(path_text)
            except ValueError:
                pass


def get_musicgen_python() -> str | None:
    root = _repo_root()
    root_text = str(root)
    added_path = False
    if root_text not in sys.path:
        sys.path.insert(0, root_text)
        added_path = True

    try:
        from manage_models import get_musicgen_python as _get_musicgen_python

        return _get_musicgen_python(root)
    finally:
        if added_path:
            try:
                sys.path.remove(root_text)
            except ValueError:
                pass


def print_musicgen_setup_hint() -> None:
    print("MusicGen/AudioCraft environment is not ready.")
    print("Run:")
    print("  .\\setup_local_models.ps1")
    print("Then retry local MusicGen generation.")


def load_presets() -> dict:
    try:
        import json

        presets_path = _repo_root() / "13_tools" / "presets" / "styles.json"
        with presets_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"presets": {}}


def print_header() -> None:
    print("\n" + "=" * 60)
    print("AI-DJ Interactive Generator")
    print("=" * 60)


def print_main_menu() -> None:
    print("\nChoose an action:")
    print("1. Cloud generation with MiniMax")
    print("2. Local instrumental generation with MusicGen")
    print("3. Local lyrics/song generation with ACE-Step")
    print("4. Create a practice plan")
    print("5. Manage the DJ-ready track library")
    print("6. Open documentation")
    print("0. Exit")


def print_cloud_menu() -> None:
    print("\n--- Cloud Generation ---")
    print("1. Custom MiniMax generation")
    print("2. Use a style preset")
    print("0. Back to main menu")


def print_local_menu() -> None:
    print("\n--- Local MusicGen Generation ---")
    print("1. Basic generation with the small model")
    print("2. Use the medium model")
    print("3. Use the large model")
    print("4. Custom MusicGen parameters")
    print("0. Back to main menu")


def get_input(prompt: str, default: str = "") -> str:
    try:
        if default:
            result = input(f"{prompt} [{default}]: ").strip()
            return result if result else default
        return input(f"{prompt}: ").strip()
    except EOFError:
        return default


def get_int_input(
    prompt: str,
    default: int,
    min_val: int | None = None,
    max_val: int | None = None,
) -> int:
    while True:
        try:
            val = get_input(prompt, str(default))
            result = int(val)
            if min_val is not None and result < min_val:
                print(f"Warning: value cannot be less than {min_val}.")
                continue
            if max_val is not None and result > max_val:
                print(f"Warning: value cannot be greater than {max_val}.")
                continue
            return result
        except ValueError:
            print("Warning: enter a valid integer.")


def get_float_input(
    prompt: str,
    default: float,
    min_val: float | None = None,
    max_val: float | None = None,
) -> float:
    while True:
        try:
            val = get_input(prompt, str(default))
            result = float(val)
            if min_val is not None and result < min_val:
                print(f"Warning: value cannot be less than {min_val}.")
                continue
            if max_val is not None and result > max_val:
                print(f"Warning: value cannot be greater than {max_val}.")
                continue
            return result
        except ValueError:
            print("Warning: enter a valid number.")


def get_yes_no(prompt: str, default: bool = False) -> bool:
    default_str = "Y/n" if default else "y/N"
    while True:
        val = get_input(f"{prompt} [{default_str}]", "").lower().strip()
        if val in ["y", "yes"]:
            return True
        if val in ["n", "no"]:
            return False
        if val == "":
            return default
        print("Warning: enter y or n.")


def wait_for_continue() -> None:
    try:
        input("\nPress Enter to continue...")
    except EOFError:
        return


def run_cloud_generate() -> None:
    print("\n--- Custom MiniMax Generation ---")

    idea = get_input("Track idea/theme", "Midnight Tech House party")
    style = get_input("Music style", "Tech House")
    bpm = get_int_input("BPM", 128, 60, 200)
    with_lyrics = get_yes_no("Generate with lyrics?", False)

    if with_lyrics:
        play = get_yes_no("Play after generation?", True)
        cmd = [
            sys.executable,
            str(_repo_root() / "13_tools" / "scripts" / "make_dj_track_with_lyrics.py"),
            "--idea",
            idea,
            "--style",
            style,
            "--bpm",
            str(bpm),
            "--with-lyrics",
        ]
        if play:
            cmd.append("--play")
    else:
        instrumental = get_yes_no("Generate an instrumental track?", True)
        play = get_yes_no("Play after generation?", True)
        cmd = [
            sys.executable,
            str(_repo_root() / "13_tools" / "scripts" / "make_dj_track_minimax.py"),
            "--idea",
            idea,
            "--style",
            style,
            "--bpm",
            str(bpm),
        ]
        if instrumental:
            cmd.append("--instrumental")
        if play:
            cmd.append("--play")

    print(f"\nRunning command: {_format_command(cmd)}")
    subprocess.run(cmd)


def run_cloud_preset() -> None:
    print("\n--- Style Preset Generation ---")

    presets = load_presets()
    if not presets["presets"]:
        print("Warning: no preset file was found.")
        return

    print("\nAvailable presets:")
    preset_list = list(presets["presets"].items())
    for i, (key, preset) in enumerate(preset_list, 1):
        print(f"{i}. {preset['name']} ({preset['default_bpm']} BPM)")
    print("0. Back")

    choice = get_int_input("Choose preset", 0, 0, len(preset_list))
    if choice == 0:
        return

    preset_key, preset = preset_list[choice - 1]
    idea = get_input("Extra idea (optional)", "")
    instrumental = get_yes_no("Generate an instrumental track?", True)
    play = get_yes_no("Play after generation?", True)

    cmd = [
        sys.executable,
        str(_repo_root() / "13_tools" / "scripts" / "generate_with_preset.py"),
        "--preset",
        preset_key,
        "--idea",
        idea if idea else preset["description"],
    ]
    if instrumental:
        cmd.append("--instrumental")
    if play:
        cmd.append("--play")

    print(f"\nRunning command: {_format_command(cmd)}")
    subprocess.run(cmd)


def run_local_generate(model_size: str = "small") -> None:
    model_map = {
        "small": "facebook/musicgen-small",
        "medium": "facebook/musicgen-medium",
        "large": "facebook/musicgen-large",
    }

    print(f"\n--- Local MusicGen Generation ({model_size}) ---")

    idea = get_input("Track idea/theme", "Midnight Tech House party")
    style = get_input("Music style", "Tech House")
    bpm = get_int_input("BPM", 128, 60, 200)
    duration = get_int_input("Duration in seconds", 90, 10, 600)
    use_cuda = get_yes_no("Use GPU acceleration with CUDA?", False)
    play = get_yes_no("Play after generation?", True)

    python_executable = get_musicgen_python()
    if python_executable is None:
        print_musicgen_setup_hint()
        return

    cmd = [
        python_executable,
        str(_repo_root() / "13_tools" / "scripts" / "make_dj_track_local.py"),
        "--idea",
        idea,
        "--style",
        style,
        "--bpm",
        str(bpm),
        "--duration",
        str(duration),
        "--model",
        model_map[model_size],
    ]
    if use_cuda:
        cmd.append("--cuda")
    if play:
        cmd.append("--play")

    print(f"\nRunning command: {_format_command(cmd)}")
    subprocess.run(cmd)


def run_local_custom() -> None:
    print("\n--- Custom MusicGen Generation ---")

    idea = get_input("Track idea/theme", "Midnight Tech House party")
    style = get_input("Music style", "Tech House")
    bpm = get_int_input("BPM", 128, 60, 200)
    duration = get_int_input("Duration in seconds", 90, 10, 600)

    print("\nModel choice:")
    print("1. Small (300M, fastest)")
    print("2. Medium (1.5B, balanced)")
    print("3. Large (3.3B, highest quality)")
    model_choice = get_int_input("Choose model", 1, 1, 3)

    model_map = {
        1: "facebook/musicgen-small",
        2: "facebook/musicgen-medium",
        3: "facebook/musicgen-large",
    }

    temperature = get_float_input("Temperature (0.0-2.0)", 1.0, 0.0, 2.0)
    cfg = get_float_input("CFG scale (1.0-10.0)", 3.0, 1.0, 10.0)
    use_cuda = get_yes_no("Use GPU acceleration with CUDA?", False)
    play = get_yes_no("Play after generation?", True)

    python_executable = get_musicgen_python()
    if python_executable is None:
        print_musicgen_setup_hint()
        return

    cmd = [
        python_executable,
        str(_repo_root() / "13_tools" / "scripts" / "make_dj_track_local.py"),
        "--idea",
        idea,
        "--style",
        style,
        "--bpm",
        str(bpm),
        "--duration",
        str(duration),
        "--model",
        model_map[model_choice],
        "--temperature",
        str(temperature),
        "--cfg",
        str(cfg),
    ]
    if use_cuda:
        cmd.append("--cuda")
    if play:
        cmd.append("--play")

    print(f"\nRunning command: {_format_command(cmd)}")
    subprocess.run(cmd)


def run_practice_plan() -> None:
    print("\n--- Practice Plan ---")
    print("1. Beginner plan")
    print("2. Intermediate plan")
    print("3. Advanced plan")
    print("0. Back")

    choice = get_int_input("Choose plan", 0, 0, 3)
    if choice == 0:
        return

    level_map = {1: "beginner", 2: "intermediate", 3: "advanced"}
    save = get_yes_no("Save to file?", True)

    cmd = [
        sys.executable,
        str(_repo_root() / "13_tools" / "scripts" / "practice_plan.py"),
        "--level",
        level_map[choice],
    ]
    if save:
        cmd.append("--save")

    print(f"\nRunning command: {_format_command(cmd)}")
    subprocess.run(cmd)


def run_library_manager() -> None:
    print("\n--- Track Library Manager ---")
    print("1. List all tracks")
    print("2. Filter by style")
    print("3. Create a set list")
    print("0. Back")

    choice = get_int_input("Choose action", 0, 0, 3)
    if choice == 0:
        return

    cmd = [
        sys.executable,
        str(_repo_root() / "13_tools" / "scripts" / "library_manager.py"),
    ]

    if choice == 1:
        cmd.append("list")
    elif choice == 2:
        style = get_input("Enter style", "Tech House")
        cmd.extend(["list", "--style", style])
    elif choice == 3:
        print("Run 'list' first to inspect track indexes.")
        name = get_input("Set list name", "My Set")
        tracks = get_input("Track indexes, comma-separated", "1,2,3")
        cmd.extend(["setlist", "--name", name, "--tracks", tracks])

    print(f"\nRunning command: {_format_command(cmd)}")
    subprocess.run(cmd)


def show_docs() -> None:
    print("\n--- Documentation ---")
    print("1. DJ learning path")
    print("2. DJ techniques library")
    print("3. Local model guide")
    print("4. Local lyrics model guide")
    print("5. ACE-Step deployment report")
    print("6. AI-DJ tutorial")
    print("0. Back")

    choice = get_int_input("Choose document", 0, 0, 6)
    if choice == 0:
        return

    doc_map = {
        1: "12_docs/learning_path.md",
        2: "12_docs/techniques_library.md",
        3: "12_docs/local_models.md",
        4: "12_docs/local_lyrics_models.md",
        5: "12_docs/ace_step_deployment_report.md",
        6: "12_docs/ai_djuced_tutorial.md",
    }

    doc_path = _repo_root() / doc_map[choice]
    if doc_path.exists():
        print(f"\nOpening: {doc_path}")
        system = platform.system().lower()
        if system.startswith("windows"):
            os.startfile(str(doc_path))
        elif system == "darwin":
            subprocess.run(["open", str(doc_path)], check=False)
        else:
            subprocess.run(["xdg-open", str(doc_path)], check=False)
    else:
        print(f"Warning: document not found: {doc_path}")


def print_ace_menu() -> None:
    print("\n--- ACE-Step Local Lyrics/Song Generation ---")
    print("Note: RTX 5060 Ti may require compatibility tuning.")
    print("1. Generate House with lyrics")
    print("2. Generate Techno with lyrics")
    print("3. Generate Trance with lyrics")
    print("4. Custom ACE-Step generation")
    print("5. Start ACE-Step Web UI (Gradio)")
    print("6. Check ACE-Step environment")
    print("0. Back to main menu")


def run_ace_step_generate(style: str = "House") -> None:
    print(f"\n--- ACE-Step Generation ({style}) ---")

    theme = get_input("Theme/idea", "DJ party")
    duration = get_int_input("Duration in seconds (-1 for random)", 30, -1, 300)
    steps = get_int_input("Inference steps (10-100)", 30, 10, 100)

    print("\nAdvanced settings:")
    cpu_offload = get_yes_no("Enable CPU offload?", True)
    bf16 = get_yes_no("Use BF16 precision?", True)

    cmd = [
        sys.executable,
        str(_repo_root() / "13_tools" / "scripts" / "make_dj_track_ace_step.py"),
        "--theme",
        theme,
        "--style",
        style,
        "--duration",
        str(duration),
        "--steps",
        str(steps),
    ]

    if not cpu_offload:
        cmd.append("--no-cpu-offload")
    if not bf16:
        cmd.append("--fp32")

    print(f"\nRunning command: {_format_command(cmd)}")
    subprocess.run(cmd)


def run_ace_step_custom() -> None:
    print("\n--- Custom ACE-Step Generation ---")

    lyrics = get_input("Lyrics (leave blank to use template)", "")
    prompt = get_input("Style prompt", "Electronic House music, upbeat, dance, 120 BPM")
    duration = get_int_input("Duration in seconds", 30, -1, 300)
    steps = get_int_input("Inference steps", 30, 10, 100)
    guidance = get_float_input("Guidance scale", 7.0, 1.0, 20.0)
    seed = get_int_input("Seed (-1 for random)", -1, -1, 999999)

    cmd = [
        sys.executable,
        str(_repo_root() / "13_tools" / "scripts" / "make_dj_track_ace_step.py"),
        "--prompt",
        prompt,
        "--duration",
        str(duration),
        "--steps",
        str(steps),
        "--guidance",
        str(guidance),
        "--seed",
        str(seed),
    ]

    if lyrics:
        cmd.extend(["--lyrics", lyrics])

    print(f"\nRunning command: {_format_command(cmd)}")
    subprocess.run(cmd)


def run_ace_step_webui() -> None:
    print("\n--- Start ACE-Step Web UI ---")
    print("Open this URL after startup: http://localhost:7865")

    ace_step_path = _ace_step_path()
    if not ace_step_path.exists():
        print(f"Error: ACE-Step directory does not exist: {ace_step_path}")
        print(
            "Clone ACE-Step first, or run: "
            "python 13_tools/scripts/make_dj_track_ace_step.py --check"
        )
        return

    if not _ace_step_importable(ace_step_path):
        print("Error: Python package 'acestep' is not importable.")
        print(
            "Install ACE-Step dependencies first, or run: "
            "python 13_tools/scripts/make_dj_track_ace_step.py --check"
        )
        return

    port = get_int_input("Port", 7865, 1000, 99999)
    cpu_offload = get_yes_no("Enable CPU offload?", True)

    cmd = [
        sys.executable,
        "-m",
        "acestep.gui",
        "--port",
        str(port),
    ]

    if cpu_offload:
        cmd.extend(["--cpu_offload", "true"])

    cmd.extend(["--bf16", "true", "--overlapped_decode", "true"])

    print(f"\nRunning command: {_format_command(cmd)}")
    print("After the Web UI starts, use the browser to generate music.")

    try:
        subprocess.run(cmd, cwd=str(ace_step_path), check=False)
    except OSError as exc:
        print(f"Error: ACE-Step Web UI failed to start: {exc}")
        print("Run the environment check before retrying.")


def run_ace_step_check() -> None:
    print("\n--- Check ACE-Step Environment ---")
    cmd = [
        sys.executable,
        str(_repo_root() / "13_tools" / "scripts" / "make_dj_track_ace_step.py"),
        "--check",
    ]
    print(f"\nRunning command: {_format_command(cmd)}")
    subprocess.run(cmd)


def main() -> None:
    while True:
        print_header()
        print_main_menu()

        choice = get_int_input("\nEnter option", 0, 0, 6)

        if choice == 0:
            print("\nGoodbye.")
            break
        if choice == 1:
            while True:
                print_cloud_menu()
                sub_choice = get_int_input("Enter option", 0, 0, 2)
                if sub_choice == 0:
                    break
                if sub_choice == 1:
                    run_cloud_generate()
                elif sub_choice == 2:
                    run_cloud_preset()
        elif choice == 2:
            while True:
                print_local_menu()
                sub_choice = get_int_input("Enter option", 0, 0, 4)
                if sub_choice == 0:
                    break
                if sub_choice == 1:
                    run_local_generate("small")
                elif sub_choice == 2:
                    run_local_generate("medium")
                elif sub_choice == 3:
                    run_local_generate("large")
                elif sub_choice == 4:
                    run_local_custom()
        elif choice == 3:
            while True:
                print_ace_menu()
                sub_choice = get_int_input("Enter option", 0, 0, 6)
                if sub_choice == 0:
                    break
                if sub_choice == 1:
                    run_ace_step_generate("House")
                elif sub_choice == 2:
                    run_ace_step_generate("Techno")
                elif sub_choice == 3:
                    run_ace_step_generate("Trance")
                elif sub_choice == 4:
                    run_ace_step_custom()
                elif sub_choice == 5:
                    run_ace_step_webui()
                elif sub_choice == 6:
                    run_ace_step_check()
        elif choice == 4:
            run_practice_plan()
        elif choice == 5:
            run_library_manager()
        elif choice == 6:
            show_docs()

        wait_for_continue()


if __name__ == "__main__":
    main()
