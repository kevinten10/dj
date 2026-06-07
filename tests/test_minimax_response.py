import importlib.util
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "13_tools"
    / "scripts"
    / "make_dj_track_minimax.py"
)


def load_minimax_module():
    spec = importlib.util.spec_from_file_location("make_dj_track_minimax", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class MiniMaxResponseTests(unittest.TestCase):
    def test_writes_hex_audio_response_to_file(self):
        minimax = load_minimax_module()

        with tempfile.TemporaryDirectory() as tmp:
            out_path = Path(tmp) / "track.mp3"
            minimax._write_audio_payload("494433040000", out_path)

            self.assertEqual(out_path.read_bytes(), bytes.fromhex("494433040000"))

    def test_url_audio_response_uses_downloader(self):
        minimax = load_minimax_module()
        calls = []

        def fake_download(url, out_path):
            calls.append((url, out_path))
            out_path.write_bytes(b"downloaded")

        with tempfile.TemporaryDirectory() as tmp:
            out_path = Path(tmp) / "track.mp3"
            minimax._write_audio_payload(
                "https://example.com/audio.mp3",
                out_path,
                download_func=fake_download,
            )

            self.assertEqual(calls, [("https://example.com/audio.mp3", out_path)])
            self.assertEqual(out_path.read_bytes(), b"downloaded")

    def test_instrumental_main_uses_current_minimax_payload(self):
        minimax = load_minimax_module()
        captured = {}

        def fake_post(url, api_key, payload):
            captured["url"] = url
            captured["api_key"] = api_key
            captured["payload"] = payload
            return {"data": {"audio": "494433040000"}, "base_resp": {"status_code": 0}}

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            with mock.patch.dict(os.environ, {"MINIMAX_API_KEY": "test-key"}, clear=False):
                with mock.patch.object(minimax, "_repo_root", return_value=tmp_path):
                    with mock.patch.object(minimax, "_minimax_post", side_effect=fake_post):
                        exit_code = minimax.main(
                            [
                                "--idea",
                                "smoke",
                                "--style",
                                "House",
                                "--bpm",
                                "120",
                                "--instrumental",
                            ]
                        )

            self.assertEqual(exit_code, 0)
            self.assertEqual(captured["url"], "https://api.minimax.io/v1/music_generation")
            self.assertEqual(captured["api_key"], "test-key")
            self.assertEqual(captured["payload"]["model"], "music-2.6-free")
            self.assertEqual(captured["payload"]["output_format"], "url")
            self.assertIs(captured["payload"]["is_instrumental"], True)
            self.assertNotIn("lyrics", captured["payload"])
            self.assertNotIn("lyrics_optimizer", captured["payload"])
            self.assertTrue(list((tmp_path / "08_exports" / "dj_ready").glob("*.mp3")))

    def test_main_loads_project_minimax_env_file_when_process_env_missing(self):
        minimax = load_minimax_module()
        captured = {}

        def fake_post(url, api_key, payload):
            captured["url"] = url
            captured["api_key"] = api_key
            return {"data": {"audio": "494433040000"}, "base_resp": {"status_code": 0}}

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            config_dir = tmp_path / "13_tools" / "configs"
            config_dir.mkdir(parents=True)
            (config_dir / "minimax_env.ps1").write_text(
                '$env:MINIMAX_API_KEY = "file-key"\n'
                '$env:MINIMAX_API_BASE = "https://example.test"\n',
                encoding="utf-8",
            )

            with mock.patch.dict(os.environ, {}, clear=True):
                with mock.patch.object(minimax, "_repo_root", return_value=tmp_path):
                    with mock.patch.object(minimax, "_minimax_post", side_effect=fake_post):
                        exit_code = minimax.main(
                            [
                                "--idea",
                                "smoke",
                                "--style",
                                "House",
                                "--bpm",
                                "120",
                                "--instrumental",
                            ]
                        )

        self.assertEqual(exit_code, 0)
        self.assertEqual(captured["api_key"], "file-key")
        self.assertEqual(captured["url"], "https://example.test/v1/music_generation")

    def test_missing_lyrics_file_fails_before_api_call(self):
        minimax = load_minimax_module()

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            missing_lyrics = tmp_path / "missing_lyrics.txt"
            with mock.patch.dict(os.environ, {"MINIMAX_API_KEY": "test-key"}, clear=False):
                with mock.patch.object(minimax, "_repo_root", return_value=tmp_path):
                    with mock.patch.object(minimax, "_minimax_post") as post:
                        exit_code = minimax.main(
                            [
                                "--idea",
                                "smoke",
                                "--style",
                                "House",
                                "--lyrics-file",
                                str(missing_lyrics),
                            ]
                        )

        self.assertEqual(1, exit_code)
        post.assert_not_called()

    def test_custom_structure_is_included_in_prompt(self):
        minimax = load_minimax_module()
        captured = {}

        def fake_post(url, api_key, payload):
            captured["payload"] = payload
            return {"data": {"audio": "494433040000"}, "base_resp": {"status_code": 0}}

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            structure = "[Intro:16][Verse:32][Drop:32][Outro:16]"
            with mock.patch.dict(os.environ, {"MINIMAX_API_KEY": "test-key"}, clear=False):
                with mock.patch.object(minimax, "_repo_root", return_value=tmp_path):
                    with mock.patch.object(minimax, "_minimax_post", side_effect=fake_post):
                        exit_code = minimax.main(
                            [
                                "--idea",
                                "smoke",
                                "--style",
                                "House",
                                "--bpm",
                                "120",
                                "--structure",
                                structure,
                                "--instrumental",
                            ]
                        )

        self.assertEqual(0, exit_code)
        self.assertIn(f"Structure: {structure}", captured["payload"]["prompt"])


if __name__ == "__main__":
    unittest.main()
