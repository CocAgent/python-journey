"""Maintainer gate for the 60-minute self-study exam in review/mock-exams/de-01.

Checks real reference behavior (58 cases) and ensures TODO starters cannot
claim success. This is not an official exam security / anti-cheat system.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAM = ROOT / "review" / "mock-exams" / "de-01"


def run(mode: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(EXAM / "autograde_de1.py"), mode],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=60,
    )


def test_reference_exam_scores_full_ten() -> None:
    result = run("--reference")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Tổng điểm tự kiểm: 10.00/10.00 — 58/58 tests PASS" in result.stdout


def test_unfinished_starters_do_not_get_false_pass() -> None:
    result = run("--student")
    assert result.returncode == 1, result.stdout + result.stderr
    assert "Tổng điểm tự kiểm: 0.00/10.00 — 0/58 tests PASS" in result.stdout


def test_exam_has_all_ten_files_and_teacher_student_separation() -> None:
    for i in range(1, 6):
        for letter in "ab":
            name = f"Cau{i}{letter}.py"
            starter = EXAM / "submissions_de1" / name
            solution = EXAM / "solutions_de1" / name
            assert starter.is_file()
            assert solution.is_file()
            assert "NotImplementedError" in starter.read_text(encoding="utf-8")
    readme = (ROOT / "review" / "README.md").read_text(encoding="utf-8")
    assert "mock-exams/de-01/README.md" in readme
    assert (EXAM / "DE-01.md").is_file()
    assert (EXAM / "HUONG-DAN-SINH-VIEN.md").is_file()
