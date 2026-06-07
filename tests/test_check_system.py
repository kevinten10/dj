import tempfile
import subprocess
import unittest
from pathlib import Path

import check_system


class CheckSystemTests(unittest.TestCase):
    def test_minimax_status_rejects_missing_and_placeholder_keys(self):
        missing_ready, missing_message = check_system.get_minimax_config_status({})
        placeholder_ready, placeholder_message = check_system.get_minimax_config_status(
            {"MINIMAX_API_KEY": "PASTE_YOUR_MINIMAX_API_KEY_HERE"}
        )

        self.assertFalse(missing_ready)
        self.assertIn("MINIMAX_API_KEY", missing_message)
        self.assertFalse(placeholder_ready)
        self.assertIn("placeholder", placeholder_message.lower())

    def test_minimax_status_accepts_real_looking_key(self):
        ready, message = check_system.get_minimax_config_status(
            {"MINIMAX_API_KEY": "sk-test-value"}
        )

        self.assertTrue(ready)
        self.assertIn("configured", message.lower())

    def test_ace_step_status_reports_missing_clone(self):
        with tempfile.TemporaryDirectory() as tmp:
            ready, issues = check_system.get_ace_step_status(Path(tmp))

        self.assertFalse(ready)
        self.assertIn("13_tools/ace_step", issues[0])

    def test_musicgen_status_reports_missing_venv_with_compatible_python(self):
        def runner(args, **kwargs):
            return subprocess.CompletedProcess(
                args,
                0,
                stdout="C:/Python311/python.exe|3.11\n",
                stderr="",
            )

        with tempfile.TemporaryDirectory() as tmp:
            ready, messages = check_system.get_musicgen_environment_status(
                Path(tmp),
                candidates=[["py", "-3.11"]],
                runner=runner,
            )

        self.assertFalse(ready)
        self.assertIn(".venv-musicgen is missing", messages[0])
        self.assertIn("Compatible runtime found", messages[1])

    def test_musicgen_status_reports_missing_compatible_python(self):
        def runner(args, **kwargs):
            return subprocess.CompletedProcess(
                args,
                0,
                stdout="C:/Python312/python.exe|3.12\n",
                stderr="",
            )

        with tempfile.TemporaryDirectory() as tmp:
            ready, messages = check_system.get_musicgen_environment_status(
                Path(tmp),
                candidates=[["python"]],
                runner=runner,
            )

        self.assertFalse(ready)
        self.assertTrue(any("No Python 3.10 or 3.11" in message for message in messages))
        self.assertTrue(any("Python 3.12" in message for message in messages))

    def test_musicgen_status_accepts_ready_venv(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            venv_python = root / ".venv-musicgen" / "Scripts" / "python.exe"
            venv_python.parent.mkdir(parents=True)
            venv_python.write_text("", encoding="utf-8")

            def runner(args, **kwargs):
                self.assertEqual(str(venv_python), args[0])
                return subprocess.CompletedProcess(args, 0, stdout="3.11|\n", stderr="")

            ready, messages = check_system.get_musicgen_environment_status(root, runner=runner)

        self.assertTrue(ready)
        self.assertIn("ready", messages[0])


if __name__ == "__main__":
    unittest.main()
