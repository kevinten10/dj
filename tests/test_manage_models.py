import tempfile
import unittest
from pathlib import Path
from unittest import mock

import manage_models


class ManageModelsTests(unittest.TestCase):
    def test_get_musicgen_python_prefers_dedicated_venv(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            venv_python = root / ".venv-musicgen" / "Scripts" / "python.exe"
            venv_python.parent.mkdir(parents=True)
            venv_python.write_text("", encoding="utf-8")

            result = manage_models.get_musicgen_python(root)

        self.assertEqual(str(venv_python), result)

    def test_get_musicgen_python_reports_missing_environment(self):
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch.object(manage_models, "python_has_audiocraft", return_value=False):
                result = manage_models.get_musicgen_python(Path(tmp))

        self.assertIsNone(result)

    def test_download_model_fails_without_musicgen_environment(self):
        with mock.patch.object(manage_models, "get_musicgen_python", return_value=None):
            result = manage_models.download_model("facebook/musicgen-small")

        self.assertFalse(result)

    def test_status_exits_nonzero_without_musicgen_environment(self):
        with mock.patch.object(manage_models, "get_musicgen_python", return_value=None):
            result = manage_models.main(["--status"])

        self.assertEqual(1, result)


if __name__ == "__main__":
    unittest.main()
