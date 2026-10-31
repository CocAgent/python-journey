"""Maintainer acceptance tests for Week 02 beginner worked examples.

Only reference solutions are required to PASS; learner TODO files intentionally fail.
All runs are offline and use only the Python standard library.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "weeks" / "week-02-variables-types"
EXAMPLES = WEEK / "examples"
CHECK = WEEK / "practice" / "checks" / "check_practice.py"


def run_script(script: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script), *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=25,
    )


@pytest.mark.parametrize(
    ("filename", "expected"),
    [
        (
            "04_predict_types.py",
            ("Chuỗi cộng chuỗi: 123", "Số cộng số: 15", "bool('False'): True"),
        ),
        (
            "05_conversion_trace.py",
            ("Input đang là: str", "Thành tiền: 75,000 VND", "Ví dụ sai '0'"),
        ),
        (
            "06_fstring_ticket.py",
            ("Vé của An: 2 × 12,000 = 24,000 VND", "Tình huống sai: 'hai'"),
        ),
    ],
)
def test_worked_examples_have_expected_output(
    filename: str, expected: tuple[str, ...]
) -> None:
    result = run_script(EXAMPLES / filename)
    assert result.returncode == 0, result.stdout + result.stderr
    for text in expected:
        assert text in result.stdout


def test_reference_practice_is_correct() -> None:
    result = run_script(CHECK, "--solutions")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Week 02 reference practice: PASS (3/3)" in result.stdout


def test_unfinished_student_starter_does_not_fake_success() -> None:
    result = run_script(CHECK, "--starter")
    assert result.returncode == 1, result.stdout + result.stderr
    assert "Week 02 student practice: FAIL (0/3)" in result.stdout


def test_workbook_is_connected_from_readme() -> None:
    readme = (WEEK / "README.md").read_text(encoding="utf-8")
    workbook = (WEEK / "WORKED-EXAMPLES.md").read_text(encoding="utf-8")
    assert "WORKED-EXAMPLES.md" in readme
    assert "practice/README.md" in readme
    for filename in (
        "04_predict_types.py",
        "05_conversion_trace.py",
        "06_fstring_ticket.py",
    ):
        assert filename in workbook
