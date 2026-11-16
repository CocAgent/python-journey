"""Protect the runnable Week 15 reference capstone in maintainer CI."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT = (
    ROOT
    / "weeks"
    / "week-15-capstone-project"
    / "reference-projects"
    / "career-knowledge-assistant"
)


def test_reference_capstone_pytest_suite() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "tests"],
        cwd=PROJECT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_reference_capstone_passes_week15_readiness() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "weeks/week-15-capstone-project/checks/check_capstone_readiness.py",
            str(PROJECT),
            "--run-tests",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
