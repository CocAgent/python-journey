"""Chạy bộ test tham chiếu Tuần 12; không chấm bài làm của sinh viên."""

import subprocess
import sys
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
REFERENCE_TESTS = WEEK_ROOT / "tests"


def main() -> int:
    """Trả mã thoát của pytest và thông báo rõ phạm vi kiểm tra."""
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            str(REFERENCE_TESTS),
            "-q",
            "-p",
            "no:cacheprovider",
        ],
        cwd=WEEK_ROOT.parents[1],
        check=False,
    )
    if result.returncode != 0:
        print("Week 12 reference tests: FAIL")
        return result.returncode

    print("Week 12 reference tests: PASS (không chấm bài sinh viên)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
