"""Maintainer: bảo đảm kiểm thử OOP mẫu hoạt động trong GitHub CI."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "weeks" / "week-14-oop-essentials" / "checks" / "check_week.py"


def test_week14_reference_passes():
    result = subprocess.run(
        [sys.executable, str(CHECKER)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=90,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Week 14 reference checks: PASS" in result.stdout
