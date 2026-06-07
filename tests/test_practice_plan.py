import importlib.util
import unittest
from datetime import datetime as real_datetime
from pathlib import Path
from unittest import mock


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "13_tools"
    / "scripts"
    / "practice_plan.py"
)


def load_practice_plan():
    spec = importlib.util.spec_from_file_location("practice_plan", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class PracticePlanTests(unittest.TestCase):
    def test_start_day_uses_next_requested_weekday(self):
        practice_plan = load_practice_plan()

        class FixedDatetime(real_datetime):
            @classmethod
            def now(cls):
                return cls(2026, 6, 7, 9, 0, 0)  # Sunday

        with mock.patch.object(practice_plan, "datetime", FixedDatetime):
            plan_data = practice_plan.generate_practice_plan("beginner", start_day=1)

        self.assertEqual("2026-06-08", plan_data["schedule"][0]["date"])
        self.assertEqual("Monday", plan_data["schedule"][0]["weekday"])
        self.assertEqual("2026-06-09", plan_data["schedule"][1]["date"])
        self.assertEqual("Tuesday", plan_data["schedule"][1]["weekday"])


if __name__ == "__main__":
    unittest.main()
