"""Maintainer CI protects the offline Week 13 learning path."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "weeks" / "week-13-modules-cli-api"


def test_week13_standard_library_reference_check() -> None:
    result = subprocess.run(
        [sys.executable, str(WEEK / "checks" / "check_week.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Week 13 solution checks: PASS" in result.stdout


def test_week13_explicit_pytest_reference_suite() -> None:
    """Reference pytest tests run explicitly; learner TODOs are not collected."""
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "weeks/week-13-modules-cli-api/tests",
            "-q",
            "-p",
            "no:cacheprovider",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=40,
    )
    assert result.returncode == 0, result.stdout + result.stderr

def test_week13_advanced_ticketdesk_offline_smoke() -> None:
    """The optional worked example must run fully offline under maintainer CI."""
    result = subprocess.run(
        [sys.executable, str(WEEK / "checks" / "check_advanced_ticketdesk.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Week 13 advanced Ticket Desk: PASS" in result.stdout
