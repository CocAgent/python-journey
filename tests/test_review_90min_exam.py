"""CI acceptance of optional 90-minute Python formative exam."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
EXAM = ROOT / "review" / "mock-exams" / "de-90-phut-01"
GRADER = EXAM / "autograde_de1.py"


def run(mode: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(GRADER), mode],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=70,
    )


def test_reference_behaviour_90_minute_exam() -> None:
    result = run("--reference")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "REFERENCE: 10.00/10.00 — 78/78 cases PASS" in result.stdout


def test_unfinished_student_todos_do_not_pass_90_minute_exam() -> None:
    result = run("--student")
    assert result.returncode == 1, result.stdout + result.stderr
    assert "STUDENT: 0.00/10.00 — 0/78 cases PASS" in result.stdout


@pytest.mark.parametrize("task", [f"Cau{i}{letter}" for i in range(1, 6) for letter in "ab"])
def test_exact_starter_and_reference_files_exist(task: str) -> None:
    starter = EXAM / "submissions_de1" / f"{task}.py"
    reference = EXAM / "solutions_de1" / f"{task}.py"
    assert starter.is_file()
    assert reference.is_file()
    assert "NotImplementedError" in starter.read_text(encoding="utf-8")


def test_review_index_and_maintainer_readme_stay_distinct() -> None:
    review = (ROOT / "review" / "README.md").read_text(encoding="utf-8")
    tests = (ROOT / "tests" / "README.md").read_text(encoding="utf-8")
    assert "de-90-phut-01/README.md" in review
    assert "Hướng dẫn kiểm thử mã nguồn Python Journey" in tests
    assert "nhóm bảo trì quản lý" in tests
    assert "không phải" in tests.lower()
    guide = (EXAM / "README.md").read_text(encoding="utf-8")
    assert "90 phút" in guide and "78" in guide
