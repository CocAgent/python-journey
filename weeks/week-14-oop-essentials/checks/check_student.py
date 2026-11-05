"""Chạy bộ kiểm thử bài sinh viên; starter chưa xong phải FAIL."""

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
            str(WEEK_ROOT / "learner_tests"),
            "-q",
            "-p",
            "no:cacheprovider",
        ],
        cwd=WEEK_ROOT.parents[1],
        check=False,
    )
    if result.returncode != 0:
        print("Week 14 student checks: CHƯA ĐẠT (xem lỗi ở trên)")
        return result.returncode
    print("Week 14 student checks: PASS (cần giảng viên đánh giá thêm)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
