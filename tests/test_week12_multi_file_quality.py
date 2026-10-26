"""Maintainer checks: Week 12 multi-file examples and controlled fault injection."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEEK12 = ROOT / "weeks" / "week-12-testing-pytest"


def test_week12_multi_file_reference_cases_pass() -> None:
    """Reference tests must work without running incomplete student starter."""
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            str(WEEK12 / "examples" / "test_multi_file_lab.py"),
            "-q",
            "-p",
            "no:cacheprovider",
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "8 passed" in result.stdout


def test_week12_multi_file_faults_are_detected() -> None:
    """Fault demonstrations must detect every documented example mistake."""
    result = subprocess.run(
        [sys.executable, str(WEEK12 / "checks" / "check_multi_file_faults.py")],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        timeout=240,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "6/6 lỗi trong 3 tệp" in result.stdout
