"""Chạy bộ kiểm thử tham chiếu Tuần 14, không chấm bài sinh viên."""

import subprocess
import sys
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            str(WEEK_ROOT / "tests"),
            "-q",
            "-p",
            "no:cacheprovider",
        ],
        cwd=WEEK_ROOT.parents[1],
        check=False,
    )
    if result.returncode != 0:
        print("Week 14 reference checks: FAIL")
        return result.returncode
    print("Week 14 reference checks: PASS (không chấm bài sinh viên)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
