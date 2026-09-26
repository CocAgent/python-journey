"""Run the Week 12 reference tests as an executable behavior check."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TESTS = ROOT / "tests"

result = subprocess.run(
    [sys.executable, "-m", "pytest", str(TESTS), "-q", "-p", "no:cacheprovider"],
    cwd=ROOT.parents[1],
    check=False,
)
if result.returncode != 0:
    raise SystemExit(result.returncode)
print("Week 12 solution checks: PASS")
