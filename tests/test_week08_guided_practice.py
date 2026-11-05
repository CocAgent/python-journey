"""Maintainer acceptance gates for new Week 08 worked examples.

Student TODOs are deliberately incomplete: CI verifies references, never
confuses '--solutions' with a learner's own '--starter' results.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "weeks" / "week-08-dicts-sets"
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
    ("filename", "expected_lines"),
    [
        (
            "06_predict_dict_get_copy.py",
            (
                "Key 'name' tồn tại: True",
                "Value 'An' là key: False",
                "Optional level: beginner",
                "Thiếu key bắt buộc: id",
                "Original score: 9",
                "Snapshot score: 8",
                "Frequency: {'python': 2, 'dict': 1}",
                "Empty frequency: {}",
            ),
        ),
        (
            "07_predict_set_and_order.py",
            (
                "Union sorted: ['dict', 'function', 'loop', 'set']",
                "Intersection sorted: ['dict']",
                "Empty set type: set",
                "Empty braces type: dict",
                "Unique with order: ['python', 'git', 'dict']",
                "Length of set: 3",
                "Set cannot count repeats: 2",
            ),
        ),
        (
            "08_nested_state_validated.py",
            (
                "COURSE TEACHING MODEL",
                "position=1, goal=4, action=right",
                "position=4, goal=4, action=wait",
                "position=3, goal=0, action=left",
                "State không hợp lệ",
            ),
        ),
    ],
)
def test_examples_are_executable_and_explain_outcomes(
    filename: str, expected_lines: tuple[str, ...]
) -> None:
    result = run_script(WEEK / "examples" / filename)
    assert result.returncode == 0, result.stdout + result.stderr
    for line in expected_lines:
        assert line in result.stdout


def test_reference_solutions_pass_function_level_checks() -> None:
    result = run_script(CHECK, "--solutions")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Week 08 reference practice: PASS (4/4)" in result.stdout


def test_unfinished_student_todos_do_not_fake_success() -> None:
    result = run_script(CHECK, "--starter")
    assert result.returncode == 1, result.stdout + result.stderr
    assert "Week 08 student practice: FAIL (0/4)" in result.stdout


def test_readme_links_guide_and_guide_links_each_example() -> None:
    readme = (WEEK / "README.md").read_text(encoding="utf-8")
    guide = (WEEK / "WORKED-EXAMPLES.md").read_text(encoding="utf-8")
    practice = (WEEK / "practice" / "README.md").read_text(encoding="utf-8")
    assert "WORKED-EXAMPLES.md" in readme
    assert "practice/README.md" in readme
    assert "--starter" in practice and "--solutions" in practice
    for filename in (
        "06_predict_dict_get_copy.py",
        "07_predict_set_and_order.py",
        "08_nested_state_validated.py",
    ):
        assert filename in guide
