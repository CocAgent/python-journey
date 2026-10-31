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
