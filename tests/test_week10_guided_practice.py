"""CI acceptance for Week 10 guided filesystem/CSV/JSON practice.

Student starters intentionally contain TODO, only references are CI green.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "weeks" / "week-10-files-io"


def run(path: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(path), *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )


@pytest.mark.parametrize(
    ("filename", "expected"),
    [
        ("04_predict_text_paths.py", (
            "Relative to terminal? False", "Exists before save: False",
            "Read back: ['Chào Python', 'Dòng hai']",
            "Exists after save: True", "Missing file: FileNotFoundError (expected)",
        )),
        ("05_predict_csv_types.py", (
            "Score type after CSV: str", "Score sum after int: 17",
            "Invalid CSV score: ValueError (expected)",
        )),
        ("06_predict_json_validation.py", (
            "Round-trip valid: True", "Turns: 1",
            "JSON list accepted by parser: True",
            "JSON list valid as replay: False",
            "Malformed JSON: JSONDecodeError (expected)",
        )),
    ],
)
def test_worked_examples(filename: str, expected: tuple[str, ...]) -> None:
    result = run(WEEK / "examples" / filename)
    assert result.returncode == 0, result.stdout + result.stderr
    for line in expected:
        assert line in result.stdout


def test_reference_lab_checks() -> None:
    result = run(WEEK / "practice" / "checks" / "check_practice.py", "--solutions")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Week 10 reference practice: PASS (3/3)" in result.stdout


def test_starter_todos_cannot_be_false_positive() -> None:
    result = run(WEEK / "practice" / "checks" / "check_practice.py", "--starter")
    assert result.returncode == 1, result.stdout + result.stderr
    assert "Week 10 student practice: FAIL (0/3)" in result.stdout


def test_navigation_and_scopes() -> None:
    readme = (WEEK / "README.md").read_text(encoding="utf-8")
    guide = (WEEK / "WORKED-EXAMPLES.md").read_text(encoding="utf-8")
    practice = (WEEK / "practice" / "README.md").read_text(encoding="utf-8")
    assert "WORKED-EXAMPLES.md" in readme
    assert "practice/README.md" in readme
    assert "--starter" in practice and "--solutions" in practice
    for filename in (
        "04_predict_text_paths.py",
        "05_predict_csv_types.py",
        "06_predict_json_validation.py",
    ):
        assert filename in guide
