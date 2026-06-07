# AI-DJ Project Handoff Status

Date: 2026-06-07

This document summarizes the current handoff state for `D:\projects\dj` and the GitHub repository `kevinten10/dj`.

## Current State

- Local branch: `master`
- Remote default branch: `master`
- GitHub repository: `https://github.com/kevinten10/dj`
- Repository visibility: public
- Latest reviewed master commit before this update: `3373061`
- Latest reviewed master workflow before this update: `CLI smoke tests`, success, run `27089542566`
- Open GitHub PRs: none
- Open GitHub issues: none
- Local working tree: clean

## Project Shape

- `README.md` / `README_CN.md`: main user guides.
- `minimax_config.py`: shared MiniMax local environment-file loader.
- `13_tools/scripts/`: CLI tools for cloud generation, local generation, ACE-Step lyrics generation, presets, practice plans, library management, and docs helpers.
- `13_tools/configs/minimax_env.example.ps1`: MiniMax API environment template.
- `13_tools/configs/minimax_env.ps1`: local MiniMax API secret file, ignored by Git.
- `13_tools/presets/styles.json`: DJ style presets.
- `13_tools/ace_step/`: optional third-party ACE-Step clone, ignored by Git.
- `04_generations/`: generated raw audio and metadata runtime output, ignored except `.gitkeep`.
- `08_exports/dj_ready/`: user-facing export target, ignored except `.gitkeep`.
- `12_docs/`: learning guides, model guides, local deployment notes, release checklist, visualizations, and licensing notes.
- `.github/workflows/cli-smoke.yml`: Windows smoke workflow for Python entrypoints and safe CLI commands.

## Technology Stack

- Python 3 scripts, currently verified locally on Python `3.12.10`.
- MiniMax Music API for cloud generation, default model `music-2.6-free`.
- ACE-Step local lyrics model through an ignored third-party clone.
- MusicGen/AudioCraft as an optional local instrumental path.
- DJUCED and Hercules DJControl Inpulse 200 MK2 guides for DJ practice workflow.
- No database is used by this workspace.
- No web server or deploy target is required for normal operation.

## Configuration And Runtime Dependencies

- Base project dependencies are in `requirements.txt`: `requests`, `mutagen`, `soundfile`.
- MiniMax generation requires `MINIMAX_API_KEY`; `MINIMAX_API_BASE` defaults to `https://api.minimax.io`.
- Python MiniMax tools read missing `MINIMAX_API_KEY` / `MINIMAX_API_BASE` values from the ignored local `13_tools/configs/minimax_env.ps1` file.
- Commit only `13_tools/configs/minimax_env.example.ps1`; keep the real `13_tools/configs/minimax_env.ps1` local.
- ACE-Step requires the local clone under `13_tools/ace_step/`, PyTorch, and `soundfile`.
- MusicGen/AudioCraft should use a separate Python 3.10 or 3.11 virtual environment because AudioCraft 1.3.0 pins `torch==2.1.0`, which is not available for Python 3.12 on current pip indexes. Use `setup_local_models.ps1` to create `.venv-musicgen`; that venv is ignored by Git.

## Verified Locally

- `python -m unittest discover -s tests`
- Python entrypoint compilation for the top-level and `13_tools/scripts` CLIs.
- PowerShell parser checks for `start.ps1` and `setup_local_models.ps1`.
- `python check_system.py`
- `git check-ignore 13_tools/configs/minimax_env.ps1`
- `git check-ignore .venv-musicgen`
- MusicGen environment status check in `check_system.py`: reports `.venv-musicgen` readiness and Python 3.10/3.11 availability.
- `manage_models.py` uses the dedicated `.venv-musicgen` Python when downloading or testing MusicGen models.
- `manage_models.py` has a clean ASCII CLI surface for model listing, cache size, environment status, download, and smoke testing.
- `generate_demo_local.py` uses the dedicated `.venv-musicgen` Python for local MusicGen demo generation.
- `interactive_generator.py` uses the dedicated `.venv-musicgen` Python for local MusicGen menu generation.
- Safe CLI smoke commands matching `.github/workflows/cli-smoke.yml`
- MiniMax missing-key path: exits with `MINIMAX_API_KEY environment variable is missing.`
- MiniMax local config path: `make_dj_track_minimax.py` and `check_system.py` can read ignored local PowerShell config values without printing secrets.
- `generate_and_play.py` returns the exact MiniMax child-process export path instead of selecting a potentially stale newest file.
- ACE-Step preflight: `python 13_tools/scripts/make_dj_track_ace_step.py --check`
- ACE-Step local generation smoke:
  - Command: `python 13_tools/scripts/make_dj_track_ace_step.py --style House --duration 10 --steps 5 --seed 123 --output 04_generations/audio/raw/ace_step_10s_smoke.wav`
  - Result: success
  - WAV evidence before cleanup: 48 kHz, 477031 frames, 9.938 seconds, 2 channels

## GitHub Work Completed Before This Document

- PR #5: clarified AudioCraft setup compatibility.
- PR #6: updated MiniMax Music API compatibility and tests.
- PR #7: fixed ACE-Step sampling defaults and preflight.
- PR #8: detected unusable TorchCodec runtime.
- PR #9: added soundfile fallback for ACE-Step WAV output.
- PR #10: expanded system readiness checks.
- PR #11: added this project handoff/status document.
- PR #12: fixed the Windows launcher path and added launcher smoke coverage.
- PR #13: ignored the local MiniMax secret config and added CI ignore checks.
- PR #14: hardened the MusicGen setup script and dedicated `.venv-musicgen` path.
- PR #15: added MusicGen environment readiness reporting to `check_system.py`.
- PR #16: routed the model manager through the dedicated MusicGen venv.
- PR #17: cleaned the local model manager CLI and removed duplicate model operations.
- PR #18: routed the local demo generator through the dedicated MusicGen venv.
- PR #19: routed the interactive local MusicGen menu through the dedicated MusicGen venv.
- PR #20: added shared MiniMax local config loading from the ignored PowerShell env file.

All merged PRs were followed by successful master `CLI smoke tests`.

## Remaining Risks

- MiniMax full cloud generation is not verified in this environment because no `MINIMAX_API_KEY` is set.
- MusicGen/AudioCraft full generation is not verified in the current Python 3.12 environment by design; use the documented Python 3.10/3.11 venv.
- ACE-Step was verified with short smoke settings. Longer/high-quality settings should be tested before using generated tracks in a performance workflow.
- Generated AI tracks still need DJ readiness review: beatgrid, clipping, structure, intro/outro usability, and licensing/platform disclosure checks.

## Suggested Next Steps

1. Configure a real MiniMax API key and run one cloud generation through `make_dj_track_minimax.py`.
2. Run a longer ACE-Step generation, then import it into DJUCED and apply the DJ ready checklist.
3. Create a Python 3.11 MusicGen venv if local instrumental generation remains a required path.
4. Keep `python check_system.py` as the first support command for future setup/debugging.
