import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch


def load_interactive_generator():
    script_path = (
        Path(__file__).resolve().parents[1]
        / "13_tools"
        / "scripts"
        / "interactive_generator.py"
    )
    spec = importlib.util.spec_from_file_location("interactive_generator", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class InteractiveGeneratorTests(unittest.TestCase):
    def test_get_input_uses_default_on_eof(self):
        generator = load_interactive_generator()

        with patch("builtins.input", side_effect=EOFError):
            result = generator.get_input("option", "0")

        self.assertEqual(result, "0")


if __name__ == "__main__":
    unittest.main()
