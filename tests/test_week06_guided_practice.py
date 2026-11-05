"""Week06 maintainer tests: runnable worked examples and reference solutions.

Student starter files intentionally contain TODO. Their FAIL before completion
is not a repository CI failure, and --solutions does not grade learner work.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "weeks" / "week-06-loops"
EXAMPLES = WEEK / "examples"
CHECK = WEEK / "practice" / "checks" / "check_practice.py"


def run_script(path: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(path), *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )


@pytest.mark.parametrize(
    ("file", "lines"),
    [
        (
            "04_predict_range_break_continue.py",
            (
                "range(1, 6): [1, 2, 3, 4, 5]",
                "Sau continue/break: [1, 2, 4, 5, 7, 8]",
                "while: còn 3",
                "while: còn 1",
                "while kết thúc tại: 0",
                "while(0): không có lượt nào",
            ),
        ),
        (
            "05_enumerate_zip_strict.py",
            (
                "1. An: 8",
                "2. Bình: 9",
                "3. Chi: 7",
                "Số bạn: 3",
                "zip mặc định (mất Chi): [('An', 8), ('Bình', 9)]",
                "zip(strict=True): từ chối danh sách lệch độ dài",
            ),
        ),
        (
            "06_comprehension_nested_loop.py",
            (
                "for thường: [4, 16, 36]",
                "comprehension: [4, 16, 36]",
                "Hai cách như nhau: True",
                "Số ô: 6",
                "Không có số: []",
            ),
        ),
    ],
)
def test_new_examples_explain_behavior(file: str, lines: tuple[str, ...]) -> None:
    result = run_script(EXAMPLES / file)
    assert result.returncode == 0, result.stdout + result.stderr
    for line in lines:
        assert line in result.stdout


def test_practice_reference_passes() -> None:
    result = run_script(CHECK, "--solutions")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Week 06 reference practice: PASS (3/3)" in result.stdout


def test_unfinished_student_starters_cannot_fake_pass() -> None:
    result = run_script(CHECK, "--starter")
    assert result.returncode == 1, result.stdout + result.stderr
    assert "Week 06 student practice: FAIL (0/3)" in result.stdout


def test_workbook_links_executable_examples_and_starters() -> None:
    readme = (WEEK / "README.md").read_text(encoding="utf-8")
    guide = (WEEK / "WORKED-EXAMPLES.md").read_text(encoding="utf-8")
    practice = (WEEK / "practice" / "README.md").read_text(encoding="utf-8")
    assert "WORKED-EXAMPLES.md" in readme
    assert "practice/README.md" in readme
    assert "--starter" in practice and "--solutions" in practice
    for file in (
        "04_predict_range_break_continue.py",
        "05_enumerate_zip_strict.py",
        "06_comprehension_nested_loop.py",
    ):
        assert file in guide
