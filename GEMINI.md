# GEMINI.md - DJ Workspace (AI + DJUCED Workflow)

This project is a structured workspace designed for generating AI music tracks (using MiniMax API) and practicing DJing with DJUCED software (and Hercules controllers).

## Project Overview (April 2026 Update)

- **Purpose:** Automate the "Idea → AI Generation → DJ Practice" workflow using 2026-gen music models.
- **Main Technologies:**
    - **Python:** For automation scripts.
    - **MiniMax Music 2.5 API:** 2026 flagship model for high-fidelity music generation with structure control.
    - **DJUCED 6.5.x:** Advanced DJ software with AI-assisted autohotcue and stem mixing.
- **Architecture:** A numbered directory structure (00-99) representing the full lifecycle of a track, from inbox to library and archives.

## Directory Structure Highlights

- `04_generations/`: Stores raw AI-generated audio and JSON metadata (Music 2.5 structure tags, prompts).
- `08_exports/dj_ready/`: 2026-ready tracks (MP3/WAV) with embedded C2PA metadata where applicable.
- `12_docs/`: Tutorials, checklists, and licensing information (updated for 2026 standards).
- `13_tools/`: Configuration templates and Python automation scripts.

## Building and Running

### Prerequisites
- Python 3.x
- MiniMax API Key (supports Music 2.5)

### Setup
1. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
2. Configure environment variables (in PowerShell):
   ```powershell
   $env:MINIMAX_API_KEY = "your_api_key_here"
   # Optional: Set API base for different regions
   $env:MINIMAX_API_BASE = "https://api.minimax.io" 
   ```

### Key Commands
- **Generate a DJ-ready track (Music 2.5):**
  ```powershell
  python 13_tools/scripts/make_dj_track_minimax.py --idea "Cyberpunk club" --model "music-2.5" --instrumental --play
  ```
  *Outputs will be saved to `08_exports/dj_ready/` and `04_generations/`.*

## Development & Workflow Conventions (2026)

- **Script Context:** Always run Python scripts from the repository root to ensure relative paths resolve correctly.
- **Naming Convention:** Generated tracks follow the pattern `YYYYMMDD_HHMMSS_slug.ext`.
- **DJ Readiness:** 
    - **Autohotcue:** Use DJUCED 6.5+'s autohotcue to automatically set markers at Intro/Chorus/Outro.
    - **Beatgrid:** AI tracks may still have "tempo drift". Use the **Prepare** mode in DJUCED to calibrate.
    - **Stems:** Prefer exporting from Udio/Suno for dedicated stem mixing in DJUCED.
- **File Management:** Ensure all exports contain **C2PA metadata** if intended for public release.

## Key Documentation
- `12_docs/ai_djuced_tutorial.md`: Updated 2026 beginner tutorial for AI + DJUCED.
- `12_docs/release_checklist/dj_ready_checklist.md`: Quality control for tracks.
- `12_docs/licenses/terms_checklist.md`: 2026 licensing, commercial rights, and C2PA requirements.
