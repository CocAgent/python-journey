"""Week 11 CI acceptance: exception semantics and real learner/reference split."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "weeks" / "week-11-exceptions"
CHECK = WEEK / "practice" / "checks" / "check_practice.py"


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
        ("05_predict_traceback_regression.py", (
            "Bug reproduced: -3 != 3", "Fixed result: 3",
            "Regression: PASS", "Traceback exception type: ValueError",
            "Failing operation: int(\"bad\")",
        )),
        ("06_predict_specific_exceptions.py", (
            "Missing file -> None", "Valid score -> 8",
            "Invalid text -> None", "Out-of-range -> None",
            "Unexpected programming bugs should not be silenced",
        )),
        ("07_predict_else_finally.py", (
            "Success action: right",
            "Success events: ['else', 'finally']",
            "Invalid action: None",
            "Invalid events: ['except', 'finally']",
            "Programming type error: TypeError propagated",
            "Events after TypeError: ['except', 'finally', 'finally']",
        )),
    ],
)
def test_worked_examples(filename: str, expected: tuple[str, ...]) -> None:
    result = run(WEEK / "examples" / filename)
    assert result.returncode == 0, result.stdout + result.stderr
    for line in expected:
        assert line in result.stdout


def test_reference_labs_pass_exception_behavior() -> None:
    result = run(CHECK, "--solutions")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Week 11 reference practice: PASS (4/4)" in result.stdout


def test_unfinished_starters_do_not_fake_success() -> None:
    result = run(CHECK, "--starter")
    assert result.returncode == 1, result.stdout + result.stderr
    assert "Week 11 student practice: FAIL (0/4)" in result.stdout


def test_docs_link_examples_and_practice() -> None:
    readme = (WEEK / "README.md").read_text(encoding="utf-8")
    guide = (WEEK / "WORKED-EXAMPLES.md").read_text(encoding="utf-8")
    practice = (WEEK / "practice" / "README.md").read_text(encoding="utf-8")
    assert "WORKED-EXAMPLES.md" in readme
    assert "practice/README.md" in readme
    assert "--starter" in practice and "--solutions" in practice
    for filename in (
        "05_predict_traceback_regression.py",
        "06_predict_specific_exceptions.py",
        "07_predict_else_finally.py",
    ):
        assert filename in guide
