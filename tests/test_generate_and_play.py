import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import generate_and_play


class GenerateAndPlayTests(unittest.TestCase):
    def test_generate_music_returns_export_path_from_child_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            exports_dir = repo_root / "08_exports" / "dj_ready"
            exports_dir.mkdir(parents=True)
            generated_file = exports_dir / "generated.mp3"
            stale_file = exports_dir / "stale.mp3"
            generated_file.write_bytes(b"new")
            stale_file.write_bytes(b"old")
            stale_mtime = generated_file.stat().st_mtime + 100
            os.utime(stale_file, (stale_mtime, stale_mtime))

            def fake_run(args, **kwargs):
                return subprocess.CompletedProcess(
                    args,
                    0,
                    stdout=f"2026-06-07 [INFO] Success! Track exported to: {generated_file}\n",
                    stderr="",
                )

            with (
                mock.patch.object(generate_and_play, "get_repo_root", return_value=repo_root),
                mock.patch.object(generate_and_play.subprocess, "run", side_effect=fake_run),
            ):
                result = generate_and_play.generate_music("smoke")

        self.assertEqual(generated_file, result)


if __name__ == "__main__":
    unittest.main()
