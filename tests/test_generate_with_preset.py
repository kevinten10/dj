import contextlib
import importlib.util
import io
import subprocess
import unittest
from pathlib import Path
from unittest import mock


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "13_tools"
    / "scripts"
    / "generate_with_preset.py"
)


def load_preset_module():
    spec = importlib.util.spec_from_file_location("generate_with_preset", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class GenerateWithPresetTests(unittest.TestCase):
    def test_dry_run_prints_copy_paste_safe_command(self):
        presets = load_preset_module()

        stdout = io.StringIO()
        with mock.patch.object(presets.subprocess, "run") as run:
            with contextlib.redirect_stdout(stdout):
                exit_code = presets.main(
                    [
                        "--preset",
                        "tech_house",
                        "--idea",
                        "Friday night party",
                        "--instrumental",
                        "--dry-run",
                    ]
                )

        self.assertEqual(0, exit_code)
        run.assert_not_called()
        printed = stdout.getvalue()
        self.assertIn('--style "Tech House"', printed)
        self.assertIn('--idea "Tech House, driving beat', printed)


if __name__ == "__main__":
    unittest.main()
