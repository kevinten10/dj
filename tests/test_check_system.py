import tempfile
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


if __name__ == "__main__":
    unittest.main()
