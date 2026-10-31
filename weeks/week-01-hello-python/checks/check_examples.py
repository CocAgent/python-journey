"""Kiểm tra ví dụ giảng viên bằng thư viện chuẩn; không chấm starter."""

import subprocess
import sys
from pathlib import Path

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"
CASES = {
    "01_print_and_comments.py": [
        "Hello, World!",
        "Python khởi động 2026",
        "",
        "Mỗi lệnh print() kết thúc bằng một dòng mới",
    ],
    "02_arithmetic.py": [
        "2 + 3 = 5",
        "10 - 4 = 6",
        "6 * 7 = 42",
        "10 / 2 = 5.0",
        "10 // 3 = 3",
        "10 % 3 = 1",
        "2 ** 10 = 1024",
    ],
    "03_first_error.py": ["Tổng: 5", "Tổng: 5"],
}


def main() -> int:
    for filename, expected in CASES.items():
        result = subprocess.run(
            [sys.executable, "-B", str(EXAMPLES / filename)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
            timeout=15,
        )
        if result.returncode or result.stdout.splitlines() != expected:
            print(f"Week 01 examples: FAIL — {filename}")
            print(f"Expected: {expected!r}")
            print(f"Actual: {result.stdout.splitlines()!r}")
            print(result.stderr)
            return 1
    print("Week 01 examples: PASS — 3/3 (reference only)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
