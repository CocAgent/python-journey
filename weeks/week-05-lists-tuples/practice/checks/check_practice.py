"""Week 05 self-check: chạy trực tiếp bài sinh viên hoặc lời giải tham khảo.

--starter: cố ý FAIL trước khi TODO được hoàn thiện.
--solutions: CI kiểm reference; không thay kết quả bài sinh viên.
Không cần pytest, pip hoặc network để chạy.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_file(folder: str, filename: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(ROOT / folder / filename)],
        capture_output=True,
        text=True,
        check=False,
        timeout=10,
    )


def assert_output(folder: str, filename: str, expected: tuple[str, ...]) -> None:
    result = run_file(folder, filename)
    assert result.returncode == 0, f"{filename}: {result.stderr}"
    actual = result.stdout.strip().splitlines()
    assert actual == list(expected), (
        f"{filename}: kết quả chưa khớp.\nMong đợi: {expected!r}\nThực tế: {actual!r}"
    )
    assert "Traceback" not in result.stderr


def check_lab01(folder: str) -> None:
    assert_output(
        folder,
        "lab01_shopping_list.py",
        (
            "Sau CRUD: ['Sách Python', 'Thước', 'Bút']",
            "Đã lấy: Vở",
            "Đầu: Sách Python",
            "Cuối: Bút",
        ),
    )


def check_lab02(folder: str) -> None:
    assert_output(
        folder,
        "lab02_alias_copy.py",
        (
            "Đầu: [10, 20]",
            "Cuối: [40, 50]",
            "Gốc: [99, 20, 30, 40, 50, 60]",
            "Alias: [99, 20, 30, 40, 50, 60]",
            "Copy: [10, 20, 30, 40, 50]",
            "Cùng đối tượng: True",
        ),
    )


def check_lab03(folder: str) -> None:
    assert_output(
        folder,
        "lab03_tuple.py",
        (
            "Tọa độ: x=3, y=7",
            "Học viên: An, 20 tuổi, học Python",
            "Đổi chỗ: B, A",
            "Tuple một phần tử: ('Cóc',)",
            "Kiểu: tuple",
        ),
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Week05 guided practice self-check")
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--starter", action="store_true", help="Kiểm chính bài sinh viên")
    modes.add_argument("--solutions", action="store_true", help="Kiểm lời giải mẫu")
    args = parser.parse_args(argv)
    folder = "starter" if args.starter else "solutions"

    passed = 0
    for index, check in enumerate((check_lab01, check_lab02, check_lab03), start=1):
        try:
            check(folder)
        except (AssertionError, OSError, subprocess.TimeoutExpired) as error:
            print(f"Lab {index:02d}: FAIL — {type(error).__name__}: {error}")
        else:
            passed += 1
            print(f"Lab {index:02d}: PASS")
    label = "student" if args.starter else "reference"
    if passed == 3:
        print(f"Week 05 {label} practice: PASS (3/3)")
        return 0
    print(f"Week 05 {label} practice: FAIL ({passed}/3)")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
