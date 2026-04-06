# 🎧 AI-DJ Workspace (2026 Edition) - Complete Guide

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![MiniMax Music 2.5](https://img.shields.io/badge/AI--Model-MiniMax%20Music%202.5-orange.svg)](https://platform.minimax.io/)
[![Hercules Inpulse 200 MK2](https://img.shields.io/badge/Controller-Hercules%20Inpulse%20200%20MK2-green.svg)](https://www.hercules.com/dj)

> **The Bridge Between AI Creativity and Professional DJ Performance** 💫
>
> A structured workspace for generating, analyzing, and practicing with AI-generated tracks. Optimized for **Hercules DJControl Inpulse 200 MK2** and **DJUCED**.

---

## 📑 Table of Contents

**🚀 Quick Start**
- [30 Second Start](#-quick-start-30-seconds)
- [Learning Path Recommendations](#-learning-path-recommendations)

**📖 Complete Beginner Tutorial**
- [Step 1: Know Your Device](#-step-1-know-your-hercules-djcontrol-inpulse-200-mk2)
- [Step 2: 30-Minute Timeline](#-step-2-30-minute-timeline)
- [Step 3: Generate First Practice Track](#-step-3-generate-your-first-practice-track)
- [Step 4: Basic Operations](#-step-4-basic-operations-5-minutes)
- [Step 5: Your First Mix](#-step-5-your-first-mix-super-detailed)
- [Step 6: EQ Magic](#-step-6-eq-magic-make-your-mixes-professional)
- [Step 7: Week 1 Practice Plan](#-step-7-week-1-practice-plan)

**🎯 Systematic Learning Path**
- [Phase 1: Fundamentals (Weeks 1-2)](#-phase-1-fundamentals-weeks-1-2)
- [Phase 2: Basic Mixing (Weeks 3-4)](#-phase-2-basic-mixing-weeks-3-4)
- [Phase 3: Advanced Techniques (Weeks 5-8)](#-phase-3-advanced-techniques-weeks-5-8)
- [Phase 4: Style Exploration & Creation (Weeks 9-12)](#-phase-4-style-exploration--creation-weeks-9-12)

**🎨 DJ Techniques Library**
- [Beat Recognition & Counting](#1-beat-recognition--counting)
- [Beatgrid Calibration](#2-beatgrid-calibration)
- [Beatmatching Techniques](#3-beatmatching)
- [EQ Mixing Techniques](#-eq-transition-techniques)
- [Looping Techniques](#1-looping)
- [Harmonic Mixing](#2-harmonic-mixing)

**🛠️ Tool Usage**
- [Core Features](#-core-capabilities)
- [Getting Started](#-getting-started)
- [DJUCED Workflow](#-the-djuced-workflow-2026)

**❓ Help**
- [FAQ](#-faq)
- [Advanced Preview](#-advanced-preview)
- [Documentation Resources](#-documentation--resources)

---

## ⚡ Quick Start (30 Seconds)

### 🎯 If You're a Complete Beginner (Start Here!)

#### Method 1: Simplest (Windows Users)
```powershell
Double-click to run: start.ps1
```

#### Method 2: Universal
```powershell
python -m pip install -r requirements.txt
python 13_tools/scripts/interactive_generator.py
```

### 📚 Recommended Learning Path

| Your Level | Recommended Reading | Time |
|------------|---------------------|------|
| 🔰 Complete Beginner | [Complete Tutorial Below](#-complete-beginner-tutorial) | 30 min |
| 🎵 Just Started | [Phase 1 + Phase 2](#-phase-1-fundamentals-weeks-1-2) | 1 month |
| 🎧 Want to Improve | [Phase 3 + Techniques](#-phase-3-advanced-techniques-weeks-5-8) | Ongoing |

---

## 📖 Complete Tutorial (From Zero!)

> 💡 **Note**: This tutorial is designed specifically for **Hercules DJControl Inpulse 200 MK2**, completely beginner-friendly!

### 🎛️ Step 1: Know Your Hercules DJControl Inpulse 200 MK2

Just remember these most important parts:

```
┌─────────────────────────────────────────────────────────────┐
│  █████████████████████████████████████████████████████████  │
│                                                             │
│   ┌─ Deck A ─┐      ┌── Mixer ──┐      ┌─ Deck B ─┐       │
│   │          │      │           │      │          │       │
│   │ 🎛️ Jog    │      │ ↔️ Xfader │      │ 🎛️ Jog    │       │
│   │ ▶️ Play   │      │ 🔊 Master │      │ ▶️ Play   │       │
│   │ 🎚️ Fader  │      │ 🎧 Cue Vol│      │ 🎚️ Fader  │       │
│   │ 🎧 Cue    │      │ 🎚️ EQ    │      │ 🎧 Cue    │       │
│   │ 🔄 SYNC   │      │ L M H    │      │ 🔄 SYNC   │       │
│   │ 📊 Pitch  │      │           │      │ 📊 Pitch  │       │
│   └──────────┘      └───────────┘      └──────────┘       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Left Side (Deck A):**
- 🎛️ **Jog Wheel** - Scrub, search, adjust position
- ▶️ **Play/Pause Button** - Start/stop music
- 🎚️ **Channel Fader** - Control Deck A volume
- 🎧 **Cue Button** - Headphone monitoring (only you can hear!)
- 🔄 **SYNC Button** - Auto-align beats of two tracks ⭐
- 📊 **Pitch Fader** - Adjust speed (±10%)
- 🔴 **4 Pads** - Hot Cues / Loops / Samples

**Center (Mixer):**
- ↔️ **Crossfader** - Switch between Deck A and B
- 🔊 **Master Volume Knob** - Control total output volume
- 🎧 **Cue Volume Knob** - Control headphone volume
- 🎚️ **3-Band EQ**:
  - **Low (Left)** - Bass (kick drum, bass) 🔉 20-250Hz
  - **Mid (Center)** - Mids (vocals, main melody) 🎤 250Hz-4kHz
  - **High (Right)** - Highs (cymbals, hi-hats) ✨ 4kHz-20kHz

**Right Side (Deck B):**
- Exactly the same as left side!

---

### ⏱️ Step 2: 30-Minute Quick Start Timeline

| Time | Content | Difficulty |
|------|---------|:----------:|
| 0-5 min | Know device + Install DJUCED | ⭐ |
| 5-10 min | Generate first practice track + Import | ⭐ |
| 10-15 min | Basics: Play, Volume, Headphone Cue | ⭐ |
| 15-20 min | Beatmatch + **First Mix** | ⭐⭐ |
| 20-25 min | EQ basics: "Bass Swap" technique | ⭐⭐ |
| 25-30 min | Free practice + Record your first mix | ⭐⭐ |

---

### 🎵 Step 3: Generate Your First Practice Track

#### Method 1: Interactive Menu (Recommended for Beginners!)

1. **Double-click to run** `start.ps1`
2. Select menu:
   ```
   1 → 1 → Enter parameters → Y → Y
   ```
3. Wait for generation to complete ✅

#### Method 2: Command Line

```powershell
python 13_tools/scripts/make_dj_track_minimax.py `
  --idea "Beginner practice, clear kick drum, simple rhythm" `
  --style "House" `
  --bpm 120 `
  --instrumental `
  --play
```

#### Import into DJUCED

1. Open DJUCED software
2. Find **Folder Browser** on the left side
3. Navigate to: `08_exports/dj_ready/`
4. Drag the generated MP3 file **to Deck A**

---

### 🎮 Step 4: Basic Operations (Learn in 5 Minutes)

#### 1️⃣ Play & Pause
```
Action: Press Deck A's ▶️ button
Result: Music starts playing! Press again to pause
```

#### 2️⃣ Adjust Volume
```
Action: Slowly push up 🎚️ Channel Fader
Result: Sound gets louder, pull down to decrease
```

#### 3️⃣ Use Headphone Monitoring (Important Skill! ⭐)

```
Steps:
1. Plug in headphones 🎧
2. Press Deck A's Cue button
3. Adjust Cue Volume knob
Result: Only you can hear, audience cannot!
```

**Why use headphones?**
- ✅ Prepare next track without audience seeing
- ✅ Essential skill for professional DJs
- ✅ Makes mixing smoother and more natural

---

### 🎯 Step 5: Your First Mix! (Super Detailed Tutorial)

#### Preparation

1. Play a song on **Deck A** (imported using method above)
2. Generate another practice track, load it onto **Deck B**
3. Make sure both tracks have similar style and BPM

#### Step-by-Step Instructions (Follow Along!)

##### 📍 Step 1: Prepare Second Track in Headphones

```
┌─────────────────┐         ┌─────────────────┐
│   Deck A        │         │   Deck B        │
│                 │         │                 │
│  🟢 Playing     │    →    │  🔴 Preparing    │
│  👂 Audience    │         │  🎧 Only You     │
└─────────────────┘         └─────────────────┘
```

**Actions:**
1. Press Deck B's **Cue button** 🎧
2. You'll hear Deck B in your headphones
3. Press Deck B's **Play button** ▶️

##### 📍 Step 2: Beatmatch (Using SYNC Magic Key!)

**Action:**
- Press Deck B's **SYNC button** 🔄
- Both tracks' speeds will **auto-align**!
- Watch Pitch fader move automatically

**Amazing right? This is modern DJ's secret weapon!** ✨

##### 📍 Step 3: Start Mixing (Exciting Moment!)

**Method 1: Using Channel Faders**
```
Timeline:
0s ──────→ 10s ──────→ 20s
  ↓              ↓              ↓
Deck A: 100%        50%            0%
Deck B:  0%         50%          100%
```

**Actions:**
1. Slowly push up Deck B's **Channel Fader** 📈
2. Slowly pull down Deck A's **Channel Fader** 📉
3. Keep smooth, about 15-20 seconds to complete transition

**Method 2: Using Crossfader (Cooler!)**
```
Action: Move ↔️ Crossfader slowly from left to right
Effect: Smooth transition from Deck A to Deck B
```

**🎉 Congratulations! You completed your first DJ mix!**

---

### 🎛️ Step 6: EQ Magic (Make Your Mixes Professional)

#### What is EQ?

Three knobs control different frequencies:

| Knob | Frequency Range | Sounds Like | Icon |
|------|-----------------|-------------|------|
| **Low** | 20-250 Hz | Kick drum, bass (boom boom boom) | 🔉 |
| **Mid** | 250-4000 Hz | Vocals, main instruments | 🎤 |
| **High** | 4000-20000 Hz | Cymbals, Hi-Hat (ts ts ts) | ✨ |

#### "Bass Swap" Technique (Most Common Professional Technique! ⭐⭐⭐)

**Why do you need this technique?**
- Two tracks' bass overlapping makes sound muddy ❌
- "Bass Swap" keeps transition clean and clear ✅

**Detailed Steps:**

```
Timeline:
T=0s        T=5s        T=10s       T=15s       T=20s
  ↓           ↓           ↓           ↓           ↓
Deck B Low:  -∞dB       -∞dB       -6dB        0dB         0dB
Deck A Low:   0dB        0dB       -6dB       -∞dB        -∞dB
Deck B Vol:   0%         25%        50%        75%        100%
Deck A Vol: 100%        75%        50%        25%          0%
```

**Actions:**
1. **Preparation**: Turn Deck B's **Low** knob all the way left (-∞)
2. **Start mixing**: Slowly push up Deck B volume (no bass yet!)
3. **Swap low frequencies**:
   - Slowly cut Deck A's **Low**
   - Slowly open Deck B's **Low**
4. **Complete**: Pull down Deck A volume fully

**Result: Perfect professional-grade mix without muddy bass!** 🎊

---

### 📅 Step 7: Week 1 Practice Plan (Daily Task Checklist)

#### 📅 Monday: Device Familiarization Day
Goal: Know every button, no longer afraid of pressing wrong ones

- [ ] Learn name of each button (refer to diagram above)
- [ ] Practice play/pause **10 times**
- [ ] Practice moving channel fader up/down (feel resistance)
- [ ] Practice headphone cue (press Cue button)
- [ ] **Challenge**: Close your eyes and find each button

#### 📅 Tuesday: Beat Recognition Day
Goal: Develop "counting beats" feeling

- [ ] Play a song, count out loud **1-2-3-4**
- [ ] Nod or tap foot to the beat
- [ ] Find kick drum position in waveform (big peaks)
- [ ] Generate a simple practice track with AI
- [ ] **Challenge**: Count beats by ear only, don't look at screen

#### 📅 Wednesday: First Mix Day
Goal: Complete one full SYNC mix

- [ ] Load two similar songs into Deck A and B
- [ ] Use **SYNC** to align both tracks
- [ ] Complete one full channel fader mix
- [ ] Try doing it again with crossfader
- [ ] **Challenge**: Record it, listen back to check results

#### 📅 Thursday: EQ Mixing Day
Goal: Master "Bass Swap" technique

- [ ] Practice **"Bass Swap"** technique **5 times**
- [ ] Use crossfader combined with EQ for transitions
- [ ] Full mix two tracks (with EQ)
- [ ] Compare difference between with-EQ and without-EQ
- [ ] **Challenge**: Try adjusting only Mid or High changes

#### 📅 Friday: Hot Cues Day
Goal: Master cue point setup and usage

- [ ] Set **4 Cue points** on one song:
  - Cue 1: Intro start
  - Cue 2: First Drop (most exciting part)
  - Cue 3: Breakdown (quiet part)
  - Cue 4: Outro start
- [ ] Start playback from different cues
- [ ] Jump quickly between cue points
- [ ] **Challenge**: Use only Hot Cues to mix 3 songs

#### 📅 Saturday-Sunday: Comprehensive Practice Day
Goal: Integrate this week's learning, enjoy the process!

- [ ] Review all techniques learned this week
- [ ] Full mix **3-4 songs** (continuous)
- [ ] Try different combination approaches
- [ ] **Final challenge**: Record a 15-minute Mini Set!
- [ ] 🎉 Celebrate completing your first week of DJ training!

---

## 🎯 Systematic Learning Path (Full Version)

> This learning path combines AI-generated practice tracks to help you systematically master DJ skills.

### 🎯 Phase 1: Fundamentals (Weeks 1-2)

#### Goals
- ✅ Familiarize with DJ controller and DJUCED software
- ✅ Understand basic beat and rhythm
- ✅ Learn beatmatching

#### Day 1: Device Familiarity
- [ ] Understand Hercules controller parts (refer to device diagram above)
- [ ] Install and configure DJUCED
- [ ] Import a practice track
- [ ] Play, pause, volume adjustment practice

**AI Practice Track Generation:**
```powershell
python 13_tools/scripts/make_dj_track_minimax.py `
  --idea "Simple House music, clear kick drum, beginner-friendly" `
  --style "House" --bpm 120 --instrumental --play
```

#### Days 2-3: Beat Recognition
- [ ] Learn to identify **4/4 time signature**
- [ ] Practice counting beats (1-2-3-4)
- [ ] Identify drum hits in waveform
- [ ] Use Beatgrid tool

**4/4 Structure:**
```
1 (Strong) - 2 (Weak) - 3 (Medium Strong) - 4 (Weak)
●          - ●         - ●            - ●
Kick usually on 1 and 3
Clap/Snare usually on 2 and 4
```

#### Days 4-7: Beatmatching Introduction
- [ ] Use **SYNC function** to assist beatmatching
- [ ] Manually adjust **Pitch control**
- [ ] Align beats of two tracks
- [ ] Understand **Phrasing (phrase structure)**

**Practice Points:**
- Choose two tracks with similar BPM (±5 BPM)
- Start practicing from same BPM
- Practice listening for speed differences
- Stay synced for at least 30 seconds

---

### 🎯 Phase 2: Basic Mixing (Weeks 3-4)

#### Goals
- ✅ Master basic mixing techniques
- ✅ Learn to use EQ (equalizer)
- ✅ Understand track structure
- ✅ Master Hot Cue usage

#### Weeks 1-2: EQ & Transitions

**Learn 3-band EQ:**
- **Low (Bass)**: Kick drum, bass, 20-250Hz
- **Mid (Mids)**: Vocals, instruments, 250Hz-4kHz
- **High (Highs)**: Cymbals, Hi-Hat, 4kHz-20kHz

**Must-master techniques:**

1. **Bass Swap** - Most common!
   ```
   Track A (playing)    Track B (waiting to mix)
   Low: 0dB    →        Low: -∞dB (completely cut)
   Mid: 0dB             Mid: 0dB
   High: 0dB            High: 0dB
   ```

2. **Gradual Transition**
   ```
   Time →
   Track A: Low ↓  Mid →  High ↓
   Track B: Low ↑  Mid →  High ↑
   ```

**AI Practice Tracks (EQ-specific):**
```powershell
# Generate two tracks with similar style
python 13_tools/scripts/make_dj_track_minimax.py `
  --idea "Tech House practice track A, good for EQ transition" `
  --style "Tech House" --bpm 126 --instrumental

python 13_tools/scripts/make_dj_track_minimax.py `
  --idea "Tech House practice track B, good for EQ transition" `
  --style "Tech House" --bpm 126 --instrumental
```

#### Weeks 3-4: Track Structure Analysis

**Standard electronic music structure:**
```
[Intro] → [Verse] → [Build Up] → [Drop] → [Breakdown] → [Drop] → [Outro]
  16beats    32beats    16beats      32beats    16beats      32beats    16beats
```

**Essential Hot Cue Setup:**
- **Cue 1**: Intro start
- **Cue 2**: First Drop (most exciting part)
- **Cue 3**: Breakdown (quiet part)
- **Cue 4**: Outro start

**Common mixing points:**
- **Intro → Intro**: Good for opening set
- **Verse → Drop**: Energy boost
- **Drop → Drop**: Maintain energy
- **Breakdown → Build**: Dramatic transition
- **Outro → Intro**: Smooth transition

**8/16/32 beat phrases:**
```
[8b]  [8b]  [8b]  [8b]
Intro Verse Build Drop
```
**Mix timing**: Usually start mixing at **32-beat boundaries**

---

### 🎯 Phase 3: Advanced Techniques (Weeks 5-8)

#### Goals
- ✅ Master Looping techniques
- ✅ Learn to use Effects
- ✅ Understand Key matching
- ✅ Try Scratching

#### Looping Techniques

**Basic loop lengths:**
- **4-beat loop**: Good for quick fills
- **8-beat loop**: Standard length
- **16-beat loop**: Longer loop sections

**Loop transition steps:**
1. Start **8-beat loop** at Drop of track A
2. Introduce track B
3. When track B reaches Drop
4. Stop loop, switch to track B

**Half-beat loop effect:**
- Creates tension
- Good for Build-up phase
- Works great with Filter effect

#### Harmonic Mixing

**Camelot Wheel:**
```
Major → 1B-12B
Minor → 1A-12A
```

**Basic rules:**
- Same number can be mixed (e.g., 8A → 8B)
- Adjacent numbers can be mixed (e.g., 8A → 9A or 7A)
- Ensures harmonic harmony

#### Effects

**Common effects:**

| Effect | Name | Usage | When to Use |
|--------|------|-------|-------------|
| **Filter** | Filter LPF/HPF | Fade sound in/out | Transitions, Build-up |
| **Reverb** | Reverb | Add space | Breakdown, ending |
| **Delay** | Delay | Echo effect | Special sections |
| **Flanger** | Flanger | Metallic modulation | Creative effects |

---

### 🎯 Phase 4: Style Exploration & Creation (Weeks 9-12)

#### Electronic Music Genre Overview

| Genre | BPM Range | Characteristics | Representative Artists |
|-------|-----------|-----------------|------------------------|
| **Deep House** | 118-124 | Warm, groovy | Kerri Chandler |
| **Tech House** | 125-128 | Mechanical, repetitive | Fisher, Camelphat |
| **Techno** | 130-140 | Industrial, dark | Charlotte de Witte |
| **Progressive House** | 126-132 | Progressive, epic | Eric Prydz |
| **Trance** | 134-142 | Emotional, high energy | Armin van Buuren |
| **Drum & Bass** | 174-180 | Fast tempo, complex drums | Netsky, Sub Focus |

#### Set Building

**Energy curve design:**
```
Energy ↑
     │           ╱╲
     │         ╱    ╲
     │       ╱        ╲
     │     ╱            ╲_______
     │   ╱
     │ ╱
     └──────────────────────────→ Time
     Warm-up  Ramp-up  Peak  Cool-down  Closing
```

**Set structure suggestions:**
1. **Warm-up**: Deep House / Tech House, lower BPM
2. **Ramp-up**: Gradually increase BPM and energy
3. **Peak Time**: Techno / Trance, highest energy
4. **Cool-down**: Lower BPM, more melodic
5. **Closing**: Outro-friendly, easy for next DJ to take over

---

## 🎨 DJ Techniques Library

### 1. Beat Recognition & Counting

**4/4 time signature structure:**
```
1 (Strong) - 2 (Weak) - 3 (Medium Strong) - 4 (Weak)
●          - ●         - ●            - ●
```

**Practice methods:**
- Count 1-2-3-4 when listening to music
- Focus on kick drum (usually on 1 and 3)
- Clap/Snare usually on 2 and 4
- Look for regular peaks in waveform

### 2. Beatgrid Calibration

**Steps:**
1. Find first kick drum in waveform
2. Align first Beatgrid line to that point
3. Playback to check subsequent drum hits
4. Fine-tune BPM to align all drum hits

**Common issues:**
- AI-generated tracks may have tempo drift
- Adjust Beatgrid in sections if needed
- Disable Snap to grid for fine adjustments

### 3. Beatmatching

#### Using SYNC Assist
1. Load two tracks
2. One playing, one paused
3. Press SYNC to auto-align
4. Observe Pitch changes

#### Manual Beatmatching (Advanced)
1. Headphone monitor the incoming track
2. Adjust Pitch to match speeds
3. Play both at Cue point simultaneously
4. Fine-tune Pitch to stay in sync

**Practice points:**
- Start from same BPM
- Gradually increase difficulty to ±5 BPM
- Practice listening for speed differences
- Stay synced for at least 30 seconds

### EQ Transition Techniques

#### Bass Swap (Detailed Version)
1. Track A playing, Track B ready
2. Cut Track B's Low completely (-∞)
3. Slowly push up Track B's fader
4. Simultaneously lower Track A's Low
5. Simultaneously raise Track B's Low
6. Fully pull down Track A's fader

#### Other EQ Techniques

| Technique Name | When to Use | Action |
|---------------|-------------|--------|
| **High Swap** | Maintain clarity during transition | Swap highs instead of lows |
| **Mid Scoop** | Create space | Slightly reduce mids |
| **Full Kill** | Dramatic effect | Cut all frequencies at once |
| **Sweep** | Gradual effect | Slowly rotate one EQ knob |

### 1. Looping

**Basic loops:**
- **4-beat loop**: Good for quick fills
- **8-beat loop**: Standard length
- **16-beat loop**: Longer loop sections

**Loop transition:**
1. Start 8-beat loop at Drop of track A
2. Introduce track B
3. When track B reaches Drop
4. Stop loop, switch to track B

**Half-beat loop effect:**
- Creates tension
- Good for Build-up phase
- Works great with Filter effect

### 2. Harmonic Mixing

**Camelot Wheel Basics:**
```
Major → 1B-12B
Minor → 1A-12A
```

**Basic rules:**
- Same number can be mixed (e.g., 8A → 8B)
- Adjacent numbers can be mixed (e.g., 8A → 9A or 7A)
- Diagonal also works (more energy change)

---

## 🌟 Core Capabilities

### 🤖 AI Music Generation

| Feature | Cloud API | Local Model |
|---------|-----------|-------------|
| **Model** | MiniMax Music 2.5 | MusicGen (Meta) |
| **Quality** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ ~ ⭐⭐⭐⭐⭐ |
| **Speed** | Fast (~1min) | Depends on hardware (CPU/GPU) |
| **Network** | Requires internet | Completely offline |
| **Cost** | Requires API Key | Free |
| **Best For** | High quality tracks | Batch generation / privacy needs |

### 🎚️ DJ-Ready Features

- ✅ Auto-generates `[Intro]` and `[Outro]` segments
- ✅ Clear kick drum and beat structure
- ✅ Supports 14+ structural tags for precise arrangement
- ✅ 320kbps MP3 or WAV high-fidelity output
- ✅ 44.1kHz sample rate (club standard)

### 📊 Smart Management

- 📁 **Auto-metadata archiving**: Every track saves complete prompts and parameters
- 🎨 **12+ style presets**: Deep House, Techno, Trance, etc.
- 📋 **Personalized practice plans**: Customized by skill level
- 🔍 **Library filtering system**: Filter by style/BPM/date
- 📝 **Set List creator**: Organize performance playlists

---

## 🚀 Getting Started

### 1️⃣ Install Dependencies

```powershell
git clone https://github.com/kevinten10/dj.git
cd dj
python -m pip install -r requirements.txt
```

### 2️⃣ Configure Cloud API (Optional)

If using MiniMax cloud API:

```powershell
# Copy config template
cp 13_tools/configs/minimax_env.example.ps1 13_tools/configs/minimax_env.ps1

# Edit and add your API Key
notepad 13_tools/configs/minimax_env.ps1

# Load config
. .\13_tools\configs\minimax_env.ps1
```

Get API Key: [platform.minimax.io](https://platform.minimax.io/)

### 3️⃣ Generate Music (Multiple Methods)

#### 🎯 Method 1: Interactive Menu (Highly Recommended for Beginners!)

```powershell
.\start.ps1
# Or
python 13_tools/scripts/interactive_generator.py
```

**Pros:** No need to remember commands, menu-guided, suitable for all levels!

#### ☁️ Method 2: Cloud API (High Quality)

```powershell
# Basic
python 13_tools/scripts/make_dj_track_minimax.py `
  --idea "Peak hour techno, industrial warehouse vibe" `
  --style "Techno" --bpm 128 --instrumental --play

# Advanced (custom structure)
python 13_tools/scripts/make_dj_track_minimax.py `
  --idea "Epic trance journey with emotional buildup" `
  --style "Trance" --bpm 138 --duration 180 `
  --structure "[Intro:8][BuildUp:16][Drop:32][Breakdown:16][Drop:32][Outro:8]" `
  --play
```

#### 🏠 Method 3: Local Model (Offline / Free)

```powershell
# Small model (fast, good for testing)
python 13_tools/scripts/make_dj_track_local.py `
  --idea "Deep house groove for late night" `
  --style "Deep House" --bpm 120 --duration 90 --play

# Large model + GPU (best quality)
python 13_tools/scripts/make_dj_track_local.py `
  --idea "Melodic techno with atmospheric pads" `
  --style "Techno" --bpm 128 --model facebook/musicgen-large `
  --cuda --temperature 0.9 --play
```

Detailed guide: [Local Models Guide](12_docs/local_models.md)

#### 🎨 Method 4: Style Presets (One-click Generation)

```powershell
# View all presets
python 13_tools/scripts/generate_with_preset.py --list

# Use preset
python 13_tools/scripts/generate_with_preset.py `
  --preset tech_house --idea "Friday night party" --instrumental --play
```

Available presets: `tech_house`, `deep_house`, `techno`, `progressive_house`, `trance`, `drum_and_bass`, etc.

### 4️⃣ Get Practice Plans

```powershell
# Beginner plan (Weeks 1-2)
python 13_tools/scripts/practice_plan.py --level beginner --save

# Intermediate plan (Weeks 3-8)
python 13_tools/scripts/practice_plan.py --level intermediate --save

# Advanced plan (Week 9+)
python 13_tools/scripts/practice_plan.py --level advanced --save
```

### 5️⃣ Manage Your Library

```powershell
# List all tracks
python 13_tools/scripts/library_manager.py list

# Filter: Techno style, BPM 125-135
python 13_tools/scripts/library_manager.py list --style "Techno" --bpm-min 125 --bpm-max 135

# Create Set List
python 13_tools/scripts/library_manager.py setlist --name "My First Set" --tracks 1,3,5,7
```

---

## 🎧 The DJUCED Workflow (2026)

### Standard Flow

```
1️⃣ Generate Track     2️⃣ Import to DJUCED   3️⃣ Analyze Markers    4️⃣ Calibrate Beatgrid
   ↓                     ↓                      ↓                     ↓
AI generates MP3     Drag to Deck          Autohotcue auto-mark   Manual fine-tune grid
                                        
5️⃣ Set Hot Cues      6️⃣ Practice Mixing   7️⃣ Record Mix        8️⃣ Share!
   ↓                     ↓                      ↓                     ↓
Mark key points      Apply EQ/SYNC        Export audio file      Publish/review
```

### Detailed Steps

1. **Import**: Drag files from `08_exports/dj_ready/` into DJUCED
2. **Analyze**: Use **DJUCED 6.5+ Autohotcue** to automatically set Intro/Chorus/Outro markers
3. **Calibrate**: Check **Beatgrid** in Prepare mode (AI tracks may need minor adjustments)
4. **Mix**: Use dedicated **Stems view** in DJUCED for real-time separation of AI-generated vocals and drums

---

## ❓ FAQ

### 🚀 Installation & Running

**Q: What should I install first?**
```
A: Order as follows:
   1. Python 3.9+ (from python.org)
   2. Project dependencies: pip install -r requirements.txt
   3. DJUCED software (from hercules.com)
   4. Connect your Hercules controller
```

**Q: Error when running start.ps1?**
```
A: Possible causes:
   - PowerShell execution policy restriction
   Solution: Run PowerShell as Administrator, execute:
   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**Q: Local model installation failed?**
```
A: MusicGen requires large dependencies:
   - PyTorch (~2GB)
   - Audiocraft (~500MB)
   
   Solutions:
   1. Ensure Python version >= 3.9
   2. Install PyTorch first: pip install torch torchvision torchaudio
   3. Then install audiocraft: pip install audiocraft
   
   Detailed guide: 12_docs/local_models.md
```

### 🎵 Music Generation

**Q: Cloud API vs Local Model, which to choose?**
```
A: Recommendation:

   Scenario               Recommended Option    Reason
   ──────────────────────────────────────────────────
   Complete beginner       Cloud API             Simple, high quality
   Batch practice tracks   Local Model           Free, unlimited
   Need best quality       Cloud API             Best results
   No internet / privacy   Local Model           Fully offline
   Good GPU                Local Model Large     Fast & free
```

**Q: Generated music doesn't sound good?**
```
A: Improvement methods:
   
   1. Optimize prompts (more specific):
      Bad: "Good music"
      Good: "Deep House, 118 BPM, warm bassline, crisp hi-hats, soulful vocal chops"
   
   2. Adjust parameters:
      - temperature: 0.7-1.2 (lower = more conservative)
      - Generate multiple times, pick best
   
   3. Use style presets (already optimized)
   
   4. Choose appropriate BPM and duration
```

**Q: How to generate specific song structures?**
```
A: Use --structure parameter:
   
   Example:
   --structure "[Intro:16][Verse:32][Chorus:32][Bridge:16][Outro:16]"
   
   Available tags:
   [Intro], [Verse], [Chorus], [Bridge], [Drop],
   [Breakdown], [BuildUp], [Outro]
```

### 🎧 DJ Operations

**Q: Still sounds wrong after SYNC alignment?**
```
A: Possible causes and solutions:
   
   1. Beatgrid inaccurate
      → Enter Prepare mode, manually adjust
   
   2. Too much structural difference between tracks
      → Choose structurally similar songs
   
   3. Pitch adjustment too large (over ±6%)
      → Choose closer BPM tracks
```

**Q: Sounds weird after EQ adjustment?**
```
A: Common mistakes:
   
   ❌ All EQ maxed out → Distorted sound
   ❌ Cut too much Low → Thin sound
   ✅ ±3dB fine-tune usually enough
   ✅ Adjust only one frequency at a time
```

**Q: Can't hear Deck B in headphones?**
```
A: Checklist:
   
   1. Is Cue button pressed (light on?)
   2. Are headphones plugged in?
   3. Is Cue Volume knob open?
   4. Is Cue Mix knob centered?
```

### 💻 Technical Issues

**Q: Where are generated files?**
```
A:
   Original files: 04_generations/audio/raw/
   DJ-ready:       08_exports/dj_ready/
   Metadata:       04_generations/metadata/
```

**Q: How to batch generate multiple songs?**
```
A: Create script batch_generate.ps1:
   
   $ideas = @(
       "Tech House, driving beat",
       "Deep House, soulful",
       "Techno, industrial"
   )
   
   foreach ($idea in $ideas) {
       python make_dj_track_minimax.py --idea $idea --style House
   }
```

**Q: Out of memory error (OOM)?**
```
A: Solutions:
   
   1. Use smaller local model (small instead of large)
   2. Reduce duration (--duration 60)
   3. Close other programs to free memory
   4. Use CPU instead of GPU (remove --cuda)
```

---

## 💡 Advanced Preview

Once you've mastered the basics, try these advanced techniques:

### 🎯 Week 2: Manual Beatmatching

Don't use SYNC, manually adjust Pitch to align beats!

**Steps:**
1. Play reference track on Deck A
2. Press Cue on Deck B to monitor
3. Listen if kick drums are synchronized
4. If Deck B too fast → Pull Pitch down
5. If Deck B too slow → Push Pitch up
6. When perfectly aligned → Start mixing

**Practice goal:** Error < 5ms (virtually undetectable to humans)

### 🎨 Week 3: Advanced EQ Techniques

Besides "Bass Swap", try these:

| Technique Name | When to Use | Action |
|---------------|-------------|--------|
| **High Swap** | Maintain clarity during transition | Swap highs instead of lows |
| **Mid Scoop** | Create space | Slightly reduce mids |
| **Full Kill** | Dramatic effect | Cut all frequencies at once |
| **Sweep** | Gradual effect | Slowly rotate one EQ knob |

### 🔥 Week 4: Creative Hot Cue Uses

- **Looping**: Set Loop at Drop section to extend climax
- **Jump Cut**: Quickly jump between different sections
- **Mashup**: Create new combinations from different song fragments

### 🎪 Week 5+: Effects & Creativity

- **Filter**: Fade sound in/out
- **Reverb**: Add spatial feel
- **Delay**: Echo effect
- **Flanger**: Metallic modulation

View complete advanced tutorial: [DJ Techniques Library](12_docs/techniques_library.md)

---

## 📂 Workspace Structure

```text
dj/
├── 04_generations/              # 📦 Track Archive
│   ├── audio/raw/               # Original generated audio
│   └── metadata/                # Generation logs and metadata
│
├── 08_exports/                  # 🎵 DJ Library
│   ├── dj_ready/                # Processed, ready for DJUCED import
│   └── set_lists/               # Created Set Lists
│
├── 12_docs/                     # 📚 Knowledge Base
│   ├── quickstart_guide.md      # ⚡ 30-minute quick start (Must read!)
│   ├── hercules_inpulse_200_mk2_guide.md  # 🎛️ Device-specific guide
│   ├── learning_path.md         # 📖 Complete learning path
│   ├── techniques_library.md    # 🎯 Comprehensive DJ techniques
│   ├── local_models.md          # 🏠 Local model usage guide
│   └── checklists/              # ✅ Quality and compliance checks
│
└── 13_tools/                    # 🛠️ Automation Tools
    ├── scripts/
    │   ├── interactive_generator.py    # 🎮 Interactive menu (Recommended!)
    │   ├── make_dj_track_minimax.py    # ☁️ Cloud generator
    │   ├── make_dj_track_local.py      # 🏠 Local model generator
    │   ├── generate_with_preset.py     # 🎨 Preset generator
    │   ├── practice_plan.py            # 📋 Practice plan generator
    │   └── library_manager.py          # 📁 Library manager
    │
    ├── presets/
    │   └── styles.json           # 12+ style presets
    │
    └── configs/
        └── minimax_env.*        # API config templates
```

---

## 📘 Documentation & Resources

### 🚀 Must-Read for Beginners (In Order)

1. **[This Document (README.md)]** ⭐ - **One-stop complete guide!**
2. **[30-Minute Quick Start Guide](12_docs/quickstart_guide.md)** - Beginner's choice
3. **[Hercules Device Guide](12_docs/hercules_inpulse_200_mk2_guide.md)** - Your controller details

### 📚 Advanced Learning

4. **[DJ Learning Path](12_docs/learning_path.md)** - Complete beginner-to-advanced curriculum
5. **[DJ Techniques Library](12_docs/techniques_library.md)** - Comprehensive technique reference
6. **[Local Models Guide](12_docs/local_models.md)** - Offline generation detailed tutorial
7. **[AI-DJ Tutorial](12_docs/ai_djuced_tutorial.md)** - From prompt to performance

### ✅ Compliance & Quality

8. **[Quality Checklist](12_docs/release_checklist/dj_ready_checklist.md)** - Pre-release track checks
9. **[Licensing Guide](12_docs/licenses/terms_checklist.md)** - 2026 commercial rights and C2PA

---

## 🤝 Contributing & License

### Contributing

Contributions welcome! Whether it's:
- ✨ Better prompt templates
- 🛠️ Improved scripts or tools
- 📖 New tutorials or documentation
- 🐛 Bug fixes

Submit a Pull Request!

### License

This project is open-sourced under the **MIT License**.

See `LICENSE` file for more information.

---

## 🎉 Start Your DJ Journey Now!

**Remember these three things:**

1. 😊 **Enjoy the process** - DJ is an art, not a competition
2. 📈 **Improve a little every day** - 30 minutes > occasional long sessions
3. 🎵 **Use AI as a tool** - It's your creative partner, not a replacement

**Start now!**

```powershell
.\start.ps1
```

---

*Created with ❤️ for the AI-DJ Community | Built for Hercules Inpulse 200 MK2 | 2026*
