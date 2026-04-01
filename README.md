# AI-DJ Workspace (2026 Edition) 🎧

> **Idea → AI Generation → DJ Practice**
> A professional-grade workspace for the future of DJing. Optimized for Hercules controllers and DJUCED.

---

## 🌟 Key Features

- 🤖 **MiniMax Music 2.5 Integration**: Precise control over 14+ track structure tags (Intro, Drop, Outro, etc.).
- 🎚️ **DJ-Friendly Workflow**: Automated export to specialized directories recognized by DJ software.
- 📜 **Lyrics & Metadata Tracking**: Automated archiving of generation prompts, lyrics, and API responses.
- ⚖️ **Compliance Ready**: Includes checklists for 2026 C2PA and commercial licensing standards.
- 🚀 **Python Automation**: One-command generation with auto-play and high-fidelity 320kbps output.

## 📂 Workspace Structure

```text
├── 04_generations/      # Raw AI output and technical metadata
├── 08_exports/          # Final tracks (MP3/WAV) ready for DJUCED
├── 12_docs/             # Master tutorials and compliance checklists
└── 13_tools/            # Generation scripts and environment configs
```

## 🛠️ Quick Start

### 1. Prerequisites
- Python 3.9+
- [MiniMax API Key](https://platform.minimax.io/)

### 2. Setup Environment
```powershell
# Install dependencies
python -m pip install -r requirements.txt

# Configure API Key
$env:MINIMAX_API_KEY = "your_key"
```

### 3. Generate Your First Track
```powershell
python 13_tools/scripts/make_dj_track_minimax.py --idea "Cyberpunk neon club" --style "Melodic Techno" --bpm 126 --play
```

## 📘 Documentation
- [Full DJUCED Tutorial](./12_docs/ai_djuced_tutorial.md)
- [DJ-Ready Checklist](./12_docs/release_checklist/dj_ready_checklist.md)
- [Licensing & Compliance](./12_docs/licenses/terms_checklist.md)

## ⚖️ License
[MIT License](./LICENSE)
