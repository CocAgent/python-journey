"""Cấu hình sys.path cho mini-project Tuần 14."""

import sys
from pathlib import Path

MINI_PROJECT_DIR = Path(__file__).resolve().parent
if str(MINI_PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(MINI_PROJECT_DIR))
