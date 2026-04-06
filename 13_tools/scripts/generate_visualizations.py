#!/usr/bin/env python3
"""
Visualization Generator for AI-DJ README
Generates ASCII art diagrams and charts for better understanding.
"""

from pathlib import Path

class VisualizationGenerator:
    def __init__(self):
        self.output_dir = Path(__file__).parent.parent.parent / "12_docs" / "visualizations"
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_controller_diagram(self):
        """Generate detailed Hercules controller diagram"""
        diagram = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                    HERCULES DJCONTROL INPULSE 200 MK2                        ║
║                                                                              ║
║  ┌─────────────────────────┐    ┌─────────────────┐    ┌─────────────────┐  ║
║  │        DECK A           │    │     MIXER       │    │     DECK B      │  ║
║  │                         │    │                 │    │                 │  ║
║  │  ┌─────────────────┐   │    │  ┌───────────┐  │    │  ┌───────────┐   │  ║
║  │  │   JOG WHEEL     │   │    │  │  MASTER   │  │    │  │   JOG     │   │  ║
║  │  │   (Scratch)     │   │    │  │  VOLUME   │  │    │  │  WHEEL    │   │  ║
║  │  └─────────────────┘   │    │  └───────────┘  │    │  └───────────┘   │  ║
║  │                        │    │                 │    │                  │  ║
║  │  [PAD 1] [PAD 2]      │    │  ┌───────────┐  │    │  [PAD 1] [PAD 2] │  ║
║  │  [PAD 3] [PAD 4]      │    │  │ CUE VOL   │  │    │  [PAD 3] [PAD 4] │  ║
║  │  Hot Cues / Loops     │    │  └───────────┘  │    │  Hot Cues/Loops  │  ║
║  │                        │    │                 │    │                  │  ║
║  │  ▶️ PLAY/PAUSE        │    │  ┌───────────┐  │    │  ▶️ PLAY/PAUSE  │  ║
║  │  🔄 SYNC              │    │  │  CUE MIX  │  │    │  🔄 SYNC         │  ║
║  │  🎧 CUE               │    │  └───────────┘  │    │  🎧 CUE          │  ║
║  │                        │    │                 │    │                  │  ║
║  │  🎚️ CHANNEL FADER    │    │  ═══════════════│    │  🎚️ CHANNEL     │  ║
║  │                        │    │  ↔️ CROSSFADER │    │     FADER        │  ║
║  │  📊 PITCH (±10%)      │    │  ═══════════════│    │  📊 PITCH        │  ║
║  │                        │    │                 │    │                  │  ║
║  └─────────────────────────┘    │  LOW  MID HIGH │    └──────────────────┘  ║
║                                 │  🎚️   🎚️   🎚️  │                         ║
║                                 │  (EQ Controls) │                         ║
║                                 └─────────────────┘                         ║
║                                                                              ║
║  CONNECTIONS:                                                                ║
║  • USB (to computer)    • Master Out (to speakers)    • Headphones          ║
╚══════════════════════════════════════════════════════════════════════════════╝

LEGEND:
  ▶️  = Play/Pause Button    🔄 = Sync Button       🎧 = Headphone Cue
  🎚️  = Fader/Slider         📊 = Pitch Control     ↔️  = Crossfader
"""
        return diagram
    
    def generate_bass_swap_timeline(self):
        """Generate Bass Swap technique timeline"""
        timeline = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                    BASS SWAP TECHNIQUE - TIMELINE                            ║
║                                                                              ║
║  This technique prevents muddy bass when mixing two tracks                   ║
║                                                                              ║
║  TIME:    0s         5s         10s        15s        20s                    ║
║           │          │          │          │          │                      ║
║           ▼          ▼          ▼          ▼          ▼                      ║
║                                                                              ║
║  TRACK A: ████████████████████████████████████████░░░░░                      ║
║  Volume:  100%       75%        50%        25%        0%                     ║
║  Low EQ:  ████████████████████████░░░░░░░░░░░░░░░░░░░░░                      ║
║           (Full)     (Full)     (-6dB)    (Cut)     (Cut)                    ║
║                                                                              ║
║  TRACK B: ░░░░░░░░░░░░░░░░░░░░░░████████████████████████                     ║
║  Volume:   0%        25%        50%        75%       100%                    ║
║  Low EQ:  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███████████████                      ║
║           (Cut)      (Cut)     (-6dB)    (Full)     (Full)                   ║
║                                                                              ║
║  MIX RESULT:                                                                 ║
║  ┌─────────────────────────────────────────────────────────────────────────┐ ║
║  │  Clean transition with NO bass overlap! Professional sound guaranteed   │ ║
║  └─────────────────────────────────────────────────────────────────────────┘ ║
║                                                                              ║
║  KEY POINTS:                                                                 ║
║  ✓ Always cut Low on incoming track before starting transition              ║
║  ✓ Gradually swap bass frequencies over 15-20 seconds                       ║
║  ✓ Keep Mid and High EQ unchanged for smoothness                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        return timeline
    
    def generate_energy_curve(self):
        """Generate set energy curve chart"""
        chart = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                    DJ SET ENERGY CURVE DESIGN                                ║
║                                                                              ║
║  Energy                                                                      ║
║    ↑                                                                         ║
║ 100│                                          ╱╲                            ║
║    │                                        ╱    ╲                          ║
║  80│                                      ╱        ╲                        ║
║    │                                    ╱            ╲                      ║
║  60│                                  ╱                ╲                    ║
║    │                                ╱                    ╲                  ║
║  40│                              ╱                        ╲                ║
║    │                            ╱                            ╲              ║
║  20│                          ╱                                ╲            ║
║    │                        ╱                                    ╲          ║
║   0│______________________╱________________________________________╲________║
║    │          │           │            │            │              │         ║
║    │   Warm   │   Ramp    │   Peak     │   Peak     │   Cool      │ Closing ║
║    │   Up     │   Up      │   Time 1   │   Time 2   │   Down      │         ║
║    └──────────┴───────────┴────────────┴────────────┴──────────────┴─────────║
║                                                                              ║
║  PHASE BREAKDOWN:                                                            ║
║  ┌─────────────┬─────────────┬─────────────────────────────────────────────┐ ║
║  │   PHASE     │    TIME     │              DESCRIPTION                    │ ║
║  ├─────────────┼─────────────┼─────────────────────────────────────────────┤ ║
║  │ Warm-up     │ 15-20 min   │ Deep House/Tech House, BPM 118-124          │ ║
║  │ Ramp-up     │ 20-30 min   │ Gradually increase BPM to 128-130           │ ║
║  │ Peak Time 1 │ 30-40 min   │ High energy Techno/Trance, BPM 130-138      │ ║
║  │ Peak Time 2 │ 20-30 min   │ Maximum energy, biggest drops               │ ║
║  │ Cool-down   │ 15-20 min   │ Lower BPM, more melodic, prepare for end    │ ║
║  │ Closing     │ 10-15 min   │ Outro-friendly tracks, easy transition      │ ║
║  └─────────────┴─────────────┴─────────────────────────────────────────────┘ ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        return chart
    
    def generate_camelot_wheel(self):
        """Generate Camelot Wheel for harmonic mixing"""
        wheel = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                    CAMELOT WHEEL - HARMONIC MIXING GUIDE                     ║
║                                                                              ║
║                         MINOR KEYS (A)                                       ║
║                                                                              ║
║                              1A                                              ║
║                            /    \\                                           ║
║                         12A      2A                                          ║
║                         /          \\                                        ║
║                      11A            3A                                       ║
║                      │               │                                       ║
║                   10A │               │ 4A                                   ║
║                      │               │                                       ║
║                       9A ────┬─── 5A                                         ║
║                              │                                               ║
║                           8A─┴─6A                                            ║
║                              7A                                              ║
║                                                                              ║
║                         MAJOR KEYS (B)                                       ║
║                                                                              ║
║                              1B                                              ║
║                            /    \\                                           ║
║                         12B      2B                                          ║
║                         /          \\                                        ║
║                      11B            3B                                       ║
║                      │               │                                       ║
║                   10B │               │ 4B                                   ║
║                      │               │                                       ║
║                       9B ────┬─── 5B                                         ║
║                              │                                               ║
║                           8B─┴─6B                                            ║
║                              7B                                              ║
║                                                                              ║
║  MIXING RULES:                                                               ║
║  ✓ Same number: 8A → 8B (perfect match, same key)                           ║
║  ✓ Adjacent: 8A → 9A or 7A (smooth transition)                              ║
║  ✓ Relative: 8A → 8B (major/minor switch)                                   ║
║  ✗ Avoid: 8A → 3A (tritone, sounds dissonant)                               ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        return wheel
    
    def generate_learning_path_flowchart(self):
        """Generate 12-week learning path flowchart"""
        flowchart = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                    12-WEEK DJ LEARNING PATH                                   ║
║                                                                              ║
║  WEEK 1-2: FOUNDATION                                                        ║
║  ┌──────────────────────────────────────────────────────────────────────┐   ║
║  │  • Device familiarity    • Beat counting    • Basic SYNC mixing      │   ║
║  │  Status: ████████████████████░░░░░░░░░░  40%                         │   ║
║  └──────────────────────────────────────────────────────────────────────┘   ║
║                                    ↓                                         ║
║  WEEK 3-4: BASIC MIXING                                                      ║
║  ┌──────────────────────────────────────────────────────────────────────┐   ║
║  │  • EQ techniques         • Track structure    • Hot Cues setup       │   ║
║  │  Status: ████████████████████████░░░░░░░░  60%                       │   ║
║  └──────────────────────────────────────────────────────────────────────┘   ║
║                                    ↓                                         ║
║  WEEK 5-8: ADVANCED TECHNIQUES                                               ║
║  ┌──────────────────────────────────────────────────────────────────────┐   ║
║  │  • Looping               • Effects usage      • Harmonic mixing      │   ║
║  │  Status: ████████████████████████████░░░░  80%                       │   ║
║  └──────────────────────────────────────────────────────────────────────┘   ║
║                                    ↓                                         ║
║  WEEK 9-12: MASTERY                                                          ║
║  ┌──────────────────────────────────────────────────────────────────────┐   ║
║  │  • Genre exploration     • Set building       • Performance skills   │   ║
║  │  Status: ████████████████████████████████  100% 🎉                   │   ║
║  └──────────────────────────────────────────────────────────────────────┘   ║
║                                                                              ║
║  SKILL PROGRESSION:                                                          ║
║                                                                              ║
║  Beatmatching    ████████████████████████████████████████████████  Expert   ║
║  EQ Mixing       ██████████████████████████████████████████        Advanced ║
║  Track Selection ████████████████████████████████████              Intermediate
║  Effects         ██████████████████████████                        Intermediate
║  Scratching      ████████████████                                  Beginner  ║
║                                                                              ║
║  ESTIMATED TIME TO PERFORMANCE READY: 12-16 weeks                          ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        return flowchart
    
    def generate_4_4_structure(self):
        """Generate 4/4 time signature structure diagram"""
        diagram = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                    4/4 TIME SIGNATURE - THE FOUNDATION                       ║
║                                                                              ║
║  In electronic music, almost everything follows 4/4 time:                    ║
║                                                                              ║
║  ONE BAR (4 beats):                                                          ║
║  ┌─────────────────────────────────────────────────────────────────────────┐ ║
║  │                                                                         │ ║
║  │   BEAT 1        BEAT 2        BEAT 3        BEAT 4                     │ ║
║  │   ═══════       ═══════       ═══════       ═══════                    │ ║
║  │      ●             ●             ●             ●                        │ ║
║  │     KICK          CLAP          KICK          CLAP                     │ ║
║  │    (Strong)      (Weak)       (Medium)       (Weak)                    │ ║
║  │      ▼             ▼             ▼             ▼                        │ ║
║  │   [====]        [----]        [====]        [----]                     │ ║
║  │                                                                         │ ║
║  └─────────────────────────────────────────────────────────────────────────┘ ║
║                                                                              ║
║  VISUAL REPRESENTATION IN WAVEFORM:                                          ║
║                                                                              ║
║  Volume ↑                                                                    ║
║       │    ╱╲           ╱╲           ╱╲           ╱╲                        ║
║       │   ╱  ╲         ╱  ╲         ╱  ╲         ╱  ╲                       ║
║       │  ╱    ╲       ╱    ╲       ╱    ╲       ╱    ╲                      ║
║       │ ╱      ╲     ╱      ╲     ╱      ╲     ╱      ╲                     ║
║       │╱        ╲___╱        ╲___╱        ╲___╱        ╲___                 ║
║       └──────────────────────────────────────────────────────────→ Time     ║
║              1         2         3         4                                 ║
║                                                                              ║
║  PHRASE STRUCTURE:                                                           ║
║  • 4 beats = 1 bar                                                           ║
║  • 4 bars = 1 phrase (16 beats)                                              ║
║  • 2 phrases = 1 section (32 beats) ← Most common mixing point!              ║
║                                                                              ║
║  MIXING TIP: Always start your mix at the beginning of a 32-beat section!    ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        return diagram
    
    def save_all_visualizations(self):
        """Generate and save all visualizations"""
        visualizations = {
            "controller_diagram.txt": self.generate_controller_diagram(),
            "bass_swap_timeline.txt": self.generate_bass_swap_timeline(),
            "energy_curve.txt": self.generate_energy_curve(),
            "camelot_wheel.txt": self.generate_camelot_wheel(),
            "learning_path_flowchart.txt": self.generate_learning_path_flowchart(),
            "4_4_structure.txt": self.generate_4_4_structure()
        }
        
        for filename, content in visualizations.items():
            filepath = self.output_dir / filename
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Generated: {filename}")
        
        print(f"\nAll visualizations saved to: {self.output_dir}")
        return list(visualizations.keys())

if __name__ == "__main__":
    generator = VisualizationGenerator()
    generator.save_all_visualizations()
