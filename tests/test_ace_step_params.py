import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "13_tools"
    / "scripts"
    / "make_dj_track_ace_step.py"
)


def load_ace_step_module():
    spec = importlib.util.spec_from_file_location("make_dj_track_ace_step", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class AceStepParameterTests(unittest.TestCase):
    def test_ace_step_cli_text_is_ascii(self):
        source = SCRIPT_PATH.read_text(encoding="utf-8")

        self.assertTrue(source.isascii())

    def test_generation_kwargs_use_ace_step_sampling_defaults(self):
        ace_step = load_ace_step_module()

        kwargs = ace_step._build_generation_kwargs(
            duration=5,
            prompt="Electronic House music",
            lyrics="[Verse]\nSmoke test",
            infer_steps=1,
            guidance_scale=7.0,
            seed=42,
            output_path="out.wav",
        )

        self.assertEqual(kwargs["scheduler_type"], "euler")
        self.assertEqual(kwargs["omega_scale"], 10.0)
        self.assertEqual(kwargs["guidance_interval"], 0.5)
        self.assertEqual(kwargs["guidance_interval_decay"], 0.0)
        self.assertEqual(kwargs["manual_seeds"], "42")

    def test_optional_runtime_dependency_check_reports_soundfile(self):
        ace_step = load_ace_step_module()

        with mock.patch.object(ace_step.importlib.util, "find_spec") as find_spec:
            find_spec.side_effect = lambda name: None if name == "soundfile" else object()

            missing = ace_step._missing_ace_step_runtime_packages()

        self.assertEqual(missing, ["soundfile"])

    def test_runtime_dependency_check_reports_broken_soundfile(self):
        ace_step = load_ace_step_module()

        with mock.patch.object(ace_step.importlib.util, "find_spec", return_value=object()):
            with mock.patch.object(ace_step.importlib, "import_module") as import_module:
                import_module.side_effect = RuntimeError("Could not load soundfile")

                issues = ace_step._ace_step_runtime_package_issues()

        self.assertIn("soundfile", issues)
        self.assertIn("Could not load soundfile", issues["soundfile"])

    def test_soundfile_wav_save_accepts_channels_first_tensor(self):
        ace_step = load_ace_step_module()
        numpy = __import__("numpy")
        soundfile = __import__("soundfile")

        audio = numpy.array(
            [
                [0.0, 0.25, -0.25],
                [0.5, -0.5, 0.0],
            ],
            dtype=numpy.float32,
        )

        with tempfile.TemporaryDirectory() as tmp:
            out_path = Path(tmp) / "smoke.wav"
            result = ace_step._save_wav_with_soundfile(
                str(out_path),
                audio,
                sample_rate=48000,
                format="wav",
            )

            data, sample_rate = soundfile.read(str(out_path), always_2d=True)

        self.assertEqual(result, str(out_path))
        self.assertEqual(sample_rate, 48000)
        self.assertEqual(data.shape, (3, 2))


if __name__ == "__main__":
    unittest.main()
