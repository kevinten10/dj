import importlib.util
import unittest
from contextlib import redirect_stdout
from io import StringIO
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
    def test_interactive_generator_cli_text_is_ascii(self):
        script_path = (
            Path(__file__).resolve().parents[1]
            / "13_tools"
            / "scripts"
            / "interactive_generator.py"
        )
        source = script_path.read_text(encoding="utf-8")

        self.assertTrue(source.isascii())

    def test_get_input_uses_default_on_eof(self):
        generator = load_interactive_generator()

        with patch("builtins.input", side_effect=EOFError):
            result = generator.get_input("option", "0")

        self.assertEqual(result, "0")

    def test_main_handles_eof_during_continue_prompt(self):
        generator = load_interactive_generator()

        with (
            patch.object(generator, "get_int_input", side_effect=[4, 0, 0]),
            patch.object(generator, "input", side_effect=EOFError),
            redirect_stdout(StringIO()),
        ):
            generator.main()

    def test_local_generate_uses_musicgen_venv_python(self):
        generator = load_interactive_generator()
        commands = []

        def fake_run(cmd):
            commands.append(cmd)

        with (
            patch.object(generator, "get_musicgen_python", return_value="musicgen-python", create=True),
            patch.object(generator, "get_input", side_effect=["Idea", "House"]),
            patch.object(generator, "get_int_input", side_effect=[128, 30]),
            patch.object(generator, "get_yes_no", side_effect=[False, False]),
            patch.object(generator.subprocess, "run", side_effect=fake_run),
        ):
            generator.run_local_generate("small")

        self.assertEqual("musicgen-python", commands[0][0])

    def test_local_generate_without_musicgen_venv_does_not_run(self):
        generator = load_interactive_generator()

        with (
            patch.object(generator, "get_musicgen_python", return_value=None, create=True),
            patch.object(generator, "print_musicgen_setup_hint", create=True) as print_hint,
            patch.object(generator, "get_input", side_effect=["Idea", "House"]),
            patch.object(generator, "get_int_input", side_effect=[128, 30]),
            patch.object(generator, "get_yes_no", side_effect=[False, False]),
            patch.object(generator.subprocess, "run") as run,
        ):
            generator.run_local_generate("small")

        print_hint.assert_called_once()
        run.assert_not_called()

    def test_cloud_generate_prints_copy_paste_safe_command(self):
        generator = load_interactive_generator()
        stdout = StringIO()

        with (
            patch.object(generator, "get_input", side_effect=["Idea", "Tech House"]),
            patch.object(generator, "get_int_input", return_value=126),
            patch.object(generator, "get_yes_no", side_effect=[False, True, False]),
            patch.object(generator.subprocess, "run") as run,
            redirect_stdout(stdout),
        ):
            generator.run_cloud_generate()

        run.assert_called_once()
        printed = stdout.getvalue()
        self.assertIn('--style "Tech House"', printed)
        self.assertIn('--idea Idea', printed)


if __name__ == "__main__":
    unittest.main()
