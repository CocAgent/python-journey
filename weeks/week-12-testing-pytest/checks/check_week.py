"""Check required Week 12 testing foundations."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tests = (ROOT / "tests" / "test_decision.py").read_text(encoding="utf-8")
required = ("Arrange", "pytest.raises", "edge_case", "regression")

missing = [marker for marker in required if marker not in tests]
if missing:
    raise SystemExit(f"Missing testing foundations: {missing}")
print("Week 12 solution checks: PASS")
