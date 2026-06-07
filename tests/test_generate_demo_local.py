import subprocess
import tempfile
import unittest
import os
from pathlib import Path
from unittest import mock

import generate_demo_local


class GenerateDemoLocalTests(unittest.TestCase):
    def test_main_fails_when_musicgen_environment_is_missing(self):
        with mock.patch.object(generate_demo_local, "get_musicgen_python", return_value=None):
            result = generate_demo_local.main(["--no-play"])

        self.assertEqual(1, result)

    def test_main_uses_musicgen_python_and_skips_playback(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            exports_dir = repo_root / "08_exports" / "dj_ready"
            exports_dir.mkdir(parents=True)
            demo_file = exports_dir / "demo.wav"
            demo_file.write_bytes(b"RIFF")

            calls = []

            def fake_run(args, **kwargs):
                calls.append(args)
                return subprocess.CompletedProcess(args, 0, stdout="", stderr="")

            with (
                mock.patch.object(generate_demo_local, "get_repo_root", return_value=repo_root),
                mock.patch.object(generate_demo_local, "get_musicgen_python", return_value="musicgen-python"),
                mock.patch.object(generate_demo_local.subprocess, "run", side_effect=fake_run),
                mock.patch.object(generate_demo_local, "play_audio") as play_audio,
            ):
                result = generate_demo_local.main(["--no-play"])

        self.assertEqual(0, result)
        self.assertEqual("musicgen-python", calls[0][0])
        play_audio.assert_not_called()

    def test_main_uses_export_path_from_child_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            exports_dir = repo_root / "08_exports" / "dj_ready"
            exports_dir.mkdir(parents=True)
            generated_file = exports_dir / "generated.wav"
            stale_file = exports_dir / "stale.wav"
            generated_file.write_bytes(b"RIFF-new")
            stale_file.write_bytes(b"RIFF-old")
            stale_mtime = generated_file.stat().st_mtime + 100
            os.utime(stale_file, (stale_mtime, stale_mtime))

            def fake_run(args, **kwargs):
                return subprocess.CompletedProcess(
                    args,
                    0,
                    stdout=f"Track exported to: {generated_file}\n",
                    stderr="",
                )

            with (
                mock.patch.object(generate_demo_local, "get_repo_root", return_value=repo_root),
                mock.patch.object(generate_demo_local, "get_musicgen_python", return_value="musicgen-python"),
                mock.patch.object(generate_demo_local.subprocess, "run", side_effect=fake_run),
                mock.patch.object(generate_demo_local, "play_audio") as play_audio,
            ):
                result = generate_demo_local.main([])

        self.assertEqual(0, result)
        play_audio.assert_called_once_with(generated_file)


if __name__ == "__main__":
    unittest.main()
