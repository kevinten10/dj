import importlib.util
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

    def test_optional_runtime_dependency_check_reports_torchcodec(self):
        ace_step = load_ace_step_module()

        with mock.patch.object(ace_step.importlib.util, "find_spec") as find_spec:
            find_spec.side_effect = lambda name: None if name == "torchcodec" else object()

            missing = ace_step._missing_ace_step_runtime_packages()

        self.assertEqual(missing, ["torchcodec"])

    def test_runtime_dependency_check_reports_broken_torchcodec(self):
        ace_step = load_ace_step_module()

        with mock.patch.object(ace_step.importlib.util, "find_spec", return_value=object()):
            with mock.patch.object(ace_step.importlib, "import_module") as import_module:
                import_module.side_effect = RuntimeError("Could not load libtorchcodec")

                issues = ace_step._ace_step_runtime_package_issues()

        self.assertIn("torchcodec", issues)
        self.assertIn("Could not load libtorchcodec", issues["torchcodec"])


if __name__ == "__main__":
    unittest.main()
