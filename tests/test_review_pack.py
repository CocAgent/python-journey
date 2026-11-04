"""Maintainer CI for optional Week01–11 review folder.

Reference solutions PASS, unfinished student starter TODOs FAIL intentionally.
No network, repo writes, or pytest dependency for learners themselves.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "review"
CHECKER = REVIEW / "practice" / "checks" / "check_review.py"


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CHECKER), *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=35,
    )


def test_review_reference_passes() -> None:
    result = run("--solutions")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Review reference: PASS (3/3)" in result.stdout


def test_student_todos_are_not_false_positive() -> None:
    result = run("--starter")
    assert result.returncode == 1, result.stdout + result.stderr
    assert "Review student: FAIL (0/3)" in result.stdout


@pytest.mark.parametrize(
    "path",
    [
        "README.md",
        "STUDY-PLAN.md",
        "QUICK-CHECK.md",
        "ANSWER-KEY.md",
        "EVIDENCE-TEMPLATE.md",
        "REMOTE-DESKTOP-SETUP.md",
        "practice/README.md",
        "practice/starter/lab01_gradebook.py",
        "practice/starter/lab02_json_report.py",
        "practice/starter/lab03_debugging.py",
        "practice/solutions/lab01_gradebook.py",
        "practice/solutions/lab02_json_report.py",
        "practice/solutions/lab03_debugging.py",
    ],
)
def test_review_navigation_and_files_exist(path: str) -> None:
    assert (REVIEW / path).is_file(), path


def test_review_in_main_readme() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "review/README.md" in readme
    guide = (REVIEW / "README.md").read_text(encoding="utf-8")
    assert "REMOTE-DESKTOP-SETUP.md" in guide
    assert "--starter" in guide and "--solutions" in guide
