"""Maintainer tests for Week03 observe-predict-transfer learning path.

Week03 student exercises are intentionally incomplete. CI verifies reference
solutions and examples, never claims student TODOs were completed.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "weeks" / "week-03-conditionals"
EXAMPLES = WEEK / "examples"
CHECK = WEEK / "practice" / "checks" / "check_practice.py"


def run(*command: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *command],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )


@pytest.mark.parametrize(
    ("filename", "expected"),
    [
        (
            "04_predict_branch_order.py",
            (
                "Điểm -1 -> Không hợp lệ",
                "Điểm 5 -> Đạt",
                "Điểm 8 -> Giỏi",
                "Sai thứ tự, điểm 9 -> Đạt",
                "Đúng thứ tự, điểm 9 -> Giỏi",
            ),
        ),
        (
            "05_boolean_reasoning.py",
            (
                "Đủ tuổi: True",
                "Có thể vào: True",
                "Cửa đã đóng: False",
                "Có giấy mời: True",
                "bool('False'): True",
            ),
        ),
        (
            "06_guard_before_decision.py",
            (
                "Input '12' -> Vé tiêu chuẩn",
                "Input '65' -> Vé người cao tuổi",
                "Input '121' -> Lỗi:",
                "Input 'abc' -> Lỗi:",
            ),
        ),
    ],
)
def test_worked_examples_execute_offline(
    filename: str, expected: tuple[str, ...]
) -> None:
    result = run(str(EXAMPLES / filename))
    assert result.returncode == 0, result.stdout + result.stderr
    for output in expected:
        assert output in result.stdout


def test_reference_solutions_cover_normal_boundary_and_invalid_cases() -> None:
    result = run(str(CHECK), "--solutions")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Week 03 reference practice: PASS (3/3)" in result.stdout


def test_initial_student_starters_are_not_false_positives() -> None:
    result = run(str(CHECK), "--starter")
    assert result.returncode == 1, result.stdout + result.stderr
    assert "Week 03 student practice: FAIL (0/3)" in result.stdout


def test_week03_workbook_is_linked() -> None:
    readme = (WEEK / "README.md").read_text(encoding="utf-8")
    workbook = (WEEK / "WORKED-EXAMPLES.md").read_text(encoding="utf-8")
    practice = (WEEK / "practice" / "README.md").read_text(encoding="utf-8")
    assert "WORKED-EXAMPLES.md" in readme
    assert "practice/README.md" in readme
    assert "--starter" in practice and "--solutions" in practice
    for name in (
        "04_predict_branch_order.py",
        "05_boolean_reasoning.py",
        "06_guard_before_decision.py",
    ):
        assert name in workbook
