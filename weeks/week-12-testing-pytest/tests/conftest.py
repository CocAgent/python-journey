"""Make the Week 12 exercise package importable for learner-local tests."""

import sys
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
if str(WEEK_ROOT) not in sys.path:
    sys.path.insert(0, str(WEEK_ROOT))
