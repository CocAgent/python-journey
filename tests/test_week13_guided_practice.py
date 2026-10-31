"""Protect Week 13 guided reference solutions; never grade learner TODOs.

The starter is intentionally incomplete. CI runs only --solutions.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "weeks" / "week-13-modules-cli-api"


def test_guided_reference_labs_pass_offline() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "practice.checks.check_lab", "--solutions"],
        cwd=WEEK,
        capture_output=True,
        text=True,
        check=False,
        timeout=35,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Week 13 guided reference labs: PASS (4/4)" in result.stdout


def test_guided_workbook_has_all_four_labs() -> None:
    workbook = (WEEK / "GUIDED-LABS.md").read_text(encoding="utf-8")
    assert all(
        marker in workbook
        for marker in (
            "Lab 1 —",
            "Lab 2 —",
            "Lab 3 —",
            "Lab 4 —",
            "--starter",
            "--solutions",
        )
    )
