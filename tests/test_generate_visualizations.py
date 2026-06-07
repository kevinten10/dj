import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "13_tools"
    / "scripts"
    / "generate_visualizations.py"
)


def load_visualization_module():
    spec = importlib.util.spec_from_file_location("generate_visualizations", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class GenerateVisualizationsTests(unittest.TestCase):
    def test_generated_visualizations_are_readable_ascii(self):
        module = load_visualization_module()
        generator = module.VisualizationGenerator()
        visualizations = {
            "controller": generator.generate_controller_diagram(),
            "bass_swap": generator.generate_bass_swap_timeline(),
            "energy": generator.generate_energy_curve(),
            "camelot": generator.generate_camelot_wheel(),
            "learning_path": generator.generate_learning_path_flowchart(),
            "structure": generator.generate_4_4_structure(),
        }

        mojibake_markers = ["鈺", "鈹", "馃", "鉁", "鈥"]
        for name, content in visualizations.items():
            with self.subTest(name=name):
                self.assertTrue(content.strip())
                self.assertTrue(content.isascii())
                for marker in mojibake_markers:
                    self.assertNotIn(marker, content)

    def test_save_all_visualizations_writes_expected_ascii_files(self):
        module = load_visualization_module()
        generator = module.VisualizationGenerator()

        with tempfile.TemporaryDirectory() as tmp:
            generator.output_dir = Path(tmp)
            filenames = generator.save_all_visualizations()

            self.assertEqual(
                {
                    "controller_diagram.txt",
                    "bass_swap_timeline.txt",
                    "energy_curve.txt",
                    "camelot_wheel.txt",
                    "learning_path_flowchart.txt",
                    "4_4_structure.txt",
                },
                set(filenames),
            )
            for filename in filenames:
                content = (Path(tmp) / filename).read_text(encoding="utf-8")
                self.assertTrue(content.strip())
                self.assertTrue(content.isascii())


if __name__ == "__main__":
    unittest.main()
