#!/usr/bin/env python3
"""
Generate readable ASCII diagrams for the AI-DJ documentation.
"""

from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


class VisualizationGenerator:
    def __init__(self):
        self.output_dir = Path(__file__).resolve().parents[2] / "12_docs" / "visualizations"
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_controller_diagram(self) -> str:
        """Generate a Hercules controller layout diagram."""
        return """
+------------------------------------------------------------------------------+
|                  HERCULES DJCONTROL INPULSE 200 MK2                          |
+----------------------------+------------------+------------------------------+
| DECK A                     | MIXER            | DECK B                       |
|                            |                  |                              |
|  +----------------------+  |  MASTER VOLUME   |  +----------------------+    |
|  |      JOG WHEEL       |  |                  |  |      JOG WHEEL       |    |
|  |      Scratch         |  |  CUE VOL         |  |      Scratch         |    |
|  +----------------------+  |  CUE MIX         |  +----------------------+    |
|                            |                  |                              |
|  [PAD 1] [PAD 2]           |  LOW MID HIGH    |  [PAD 1] [PAD 2]             |
|  [PAD 3] [PAD 4]           |  EQ CONTROLS     |  [PAD 3] [PAD 4]             |
|                            |                  |                              |
|  PLAY/PAUSE  SYNC  CUE     |  CROSSFADER      |  PLAY/PAUSE  SYNC  CUE       |
|  CHANNEL FADER             |                  |  CHANNEL FADER               |
|  PITCH +/-10%              |                  |  PITCH +/-10%                |
+----------------------------+------------------+------------------------------+
| Connections: USB to computer, master out to speakers, headphones             |
+------------------------------------------------------------------------------+

Legend:
  Pads = hot cues or loops
  Cue = headphone preview
  Pitch = tempo adjustment
  Crossfader = blend between Deck A and Deck B
"""

    def generate_bass_swap_timeline(self) -> str:
        """Generate a Bass Swap technique timeline."""
        return """
+------------------------------------------------------------------------------+
|                         BASS SWAP TECHNIQUE                                   |
+------------------------------------------------------------------------------+
| Goal: avoid muddy bass when two tracks overlap.                               |
|                                                                              |
| Time:        0s          5s          10s         15s         20s              |
| Track A vol: 100%        75%         50%         25%          0%              |
| Track A low: FULL        FULL        -6 dB       CUT         CUT              |
| Track B vol:   0%        25%         50%         75%        100%              |
| Track B low: CUT         CUT         -6 dB       FULL        FULL             |
|                                                                              |
| Mix result: one bassline owns the low end at any moment.                      |
+------------------------------------------------------------------------------+

Checklist:
  1. Cut low EQ on the incoming track before bringing it in.
  2. Blend volume gradually.
  3. Swap low EQ once phrasing lines up.
  4. Keep mids and highs stable for a smooth transition.
"""

    def generate_energy_curve(self) -> str:
        """Generate a set energy curve chart."""
        return """
+------------------------------------------------------------------------------+
|                         DJ SET ENERGY CURVE                                   |
+------------------------------------------------------------------------------+
| Energy                                                                       |
| 100 |                                      /\\                                 |
|  80 |                                  ___/  \\___                             |
|  60 |                             ____/          \\____                        |
|  40 |                        ____/                    \\___                    |
|  20 |                   ____/                            \\___                 |
|   0 +------------------+---------+----------+----------+----+--------------> |
|       Warm-up          Ramp-up   Peak 1     Peak 2     Cool Closing          |
+------------------------------------------------------------------------------+

Phase guide:
  Warm-up   : 15-20 min, Deep House / Tech House, 118-124 BPM
  Ramp-up   : 20-30 min, gradually increase to 128-130 BPM
  Peak 1    : 30-40 min, high-energy Techno / Trance
  Peak 2    : 20-30 min, biggest tracks and drops
  Cool-down : 15-20 min, more melodic and lower energy
  Closing   : 10-15 min, outro-friendly tracks
"""

    def generate_camelot_wheel(self) -> str:
        """Generate a Camelot Wheel guide for harmonic mixing."""
        return """
+------------------------------------------------------------------------------+
|                         CAMELOT WHEEL QUICK GUIDE                             |
+------------------------------------------------------------------------------+
| Minor keys: 1A  2A  3A  4A  5A  6A  7A  8A  9A  10A 11A 12A                 |
| Major keys: 1B  2B  3B  4B  5B  6B  7B  8B  9B  10B 11B 12B                 |
|                                                                              |
| Smooth moves from 8A:                                                         |
|   Same key family : 8A -> 8A                                                  |
|   Adjacent minor  : 8A -> 7A or 9A                                            |
|   Relative major  : 8A -> 8B                                                  |
|                                                                              |
| Avoid large jumps such as 8A -> 3A unless you want obvious tension.           |
+------------------------------------------------------------------------------+

Rule of thumb:
  Same number, adjacent number, or same number with A/B switch is usually safe.
"""

    def generate_learning_path_flowchart(self) -> str:
        """Generate a 12-week learning path flowchart."""
        return """
+------------------------------------------------------------------------------+
|                         12-WEEK DJ LEARNING PATH                              |
+------------------------------------------------------------------------------+
| Weeks 1-2: Foundation                                                         |
|   Device familiarity -> beat counting -> basic sync mixing                    |
|                                                                              |
| Weeks 3-4: Basic mixing                                                       |
|   EQ basics -> track structure -> hot cue setup                               |
|                                                                              |
| Weeks 5-8: Advanced techniques                                                |
|   Looping -> effects -> harmonic mixing -> cleaner transitions                |
|                                                                              |
| Weeks 9-12: Mastery                                                           |
|   Genre exploration -> set building -> performance practice                   |
+------------------------------------------------------------------------------+

Progression:
  Beatmatching    [####################] Expert
  EQ mixing       [################--]   Advanced
  Track selection [##############----]   Intermediate
  Effects         [############------]   Intermediate
  Scratching      [########----------]   Beginner
"""

    def generate_4_4_structure(self) -> str:
        """Generate a 4/4 time signature structure diagram."""
        return """
+------------------------------------------------------------------------------+
|                         4/4 TIME SIGNATURE                                    |
+------------------------------------------------------------------------------+
| One bar has four beats:                                                       |
|                                                                              |
|   Beat:      1          2          3          4                               |
|   Feel:      STRONG     weak       medium     weak                            |
|   Common:    KICK       CLAP       KICK       CLAP                            |
|                                                                              |
| Phrase structure:                                                             |
|   4 beats  = 1 bar                                                            |
|   4 bars   = 1 phrase, or 16 beats                                            |
|   8 bars   = 1 section, or 32 beats                                           |
|                                                                              |
| Mixing tip: start transitions at the beginning of a 32-beat section.          |
+------------------------------------------------------------------------------+
"""

    def save_all_visualizations(self) -> list[str]:
        """Generate and save all visualization files."""
        visualizations = {
            "controller_diagram.txt": self.generate_controller_diagram(),
            "bass_swap_timeline.txt": self.generate_bass_swap_timeline(),
            "energy_curve.txt": self.generate_energy_curve(),
            "camelot_wheel.txt": self.generate_camelot_wheel(),
            "learning_path_flowchart.txt": self.generate_learning_path_flowchart(),
            "4_4_structure.txt": self.generate_4_4_structure(),
        }

        for filename, content in visualizations.items():
            filepath = self.output_dir / filename
            filepath.write_text(content, encoding="utf-8")
            print(f"Generated: {filename}")

        print(f"\nAll visualizations saved to: {self.output_dir}")
        return list(visualizations.keys())


if __name__ == "__main__":
    generator = VisualizationGenerator()
    generator.save_all_visualizations()
