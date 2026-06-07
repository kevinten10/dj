import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "13_tools"
    / "scripts"
    / "library_manager.py"
)


def load_library_manager():
    spec = importlib.util.spec_from_file_location("library_manager", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class LibraryManagerTests(unittest.TestCase):
    def test_scan_library_includes_wav_tracks_with_metadata(self):
        manager = load_library_manager()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            exports_dir = root / "08_exports" / "dj_ready"
            metadata_dir = root / "04_generations" / "metadata"
            exports_dir.mkdir(parents=True)
            metadata_dir.mkdir(parents=True)

            track_path = exports_dir / "local_demo.wav"
            track_path.write_bytes(b"RIFF")
            (metadata_dir / "local_demo.json").write_text(
                json.dumps(
                    {
                        "params": {
                            "style": "Tech House",
                            "bpm": 124,
                            "idea": "demo",
                        }
                    }
                ),
                encoding="utf-8",
            )

            with mock.patch.object(manager, "_repo_root", return_value=root):
                tracks = manager.scan_library()

        self.assertEqual(1, len(tracks))
        self.assertEqual("local_demo.wav", tracks[0]["filename"])
        self.assertEqual("Tech House", tracks[0]["style"])
        self.assertEqual(124, tracks[0]["bpm"])

    def test_show_missing_track_exits_nonzero(self):
        manager = load_library_manager()

        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch.object(manager, "_repo_root", return_value=Path(tmp)):
                result = manager.main(["show", "missing.mp3"])

        self.assertEqual(1, result)

    def test_setlist_with_no_valid_tracks_exits_nonzero(self):
        manager = load_library_manager()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            exports_dir = root / "08_exports" / "dj_ready"
            exports_dir.mkdir(parents=True)
            (exports_dir / "track.mp3").write_bytes(b"ID3")

            with mock.patch.object(manager, "_repo_root", return_value=root):
                result = manager.main(["setlist", "--name", "Test", "--tracks", "99"])

        self.assertEqual(1, result)


if __name__ == "__main__":
    unittest.main()
