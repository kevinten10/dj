import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "13_tools"
    / "scripts"
    / "make_dj_track_with_lyrics.py"
)


def load_lyrics_module():
    spec = importlib.util.spec_from_file_location("make_dj_track_with_lyrics", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class MakeDjTrackWithLyricsTests(unittest.TestCase):
    def test_with_lyrics_passes_generated_lyrics_file_to_minimax(self):
        lyrics_module = load_lyrics_module()
        commands = []

        def fake_run(cmd, **kwargs):
            commands.append(cmd)
            return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")

        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            with (
                mock.patch.object(lyrics_module, "_repo_root", return_value=repo_root),
                mock.patch.object(lyrics_module, "_now_stamp", return_value="20260607_181500"),
                mock.patch.object(lyrics_module, "generate_lyrics", return_value="[Verse]\nSmoke test"),
                mock.patch.object(lyrics_module.subprocess, "run", side_effect=fake_run),
            ):
                result = lyrics_module.main(
                    [
                        "--idea",
                        "smoke",
                        "--style",
                        "House",
                        "--bpm",
                        "124",
                        "--with-lyrics",
                    ]
                )

            lyrics_path = repo_root / "04_generations" / "metadata" / "20260607_181500_House_lyrics.txt"
            lyrics_text = lyrics_path.read_text(encoding="utf-8")

        self.assertEqual(0, result)
        self.assertIn("--lyrics-file", commands[0])
        lyrics_file_arg = commands[0][commands[0].index("--lyrics-file") + 1]
        self.assertEqual(str(lyrics_path), lyrics_file_arg)
        self.assertEqual("[Verse]\nSmoke test", lyrics_text)


if __name__ == "__main__":
    unittest.main()
