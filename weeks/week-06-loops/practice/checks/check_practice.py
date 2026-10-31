"""Kiểm 3 bài tự luyện Week06 bằng stdlib, không cần pytest.

--starter: chạy chính bài sinh viên, ban đầu FAIL có chủ đích.
--solutions: kiểm lời giải mẫu, dùng trong maintainer CI.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_file(folder: str, filename: str, typed_input: str = "") -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(ROOT / folder / filename)],
        input=typed_input,
        capture_output=True,
        text=True,
        check=False,
        timeout=10,
    )


def expect_output(folder: str, filename: str, expected: tuple[str, ...], typed_input: str = "") -> None:
    result = run_file(folder, filename, typed_input)
    assert result.returncode == 0, f"{filename}: lỗi khi chạy: {result.stderr}"
    # input() prompt đôi khi nằm cùng dòng đầu tiên; tách phần prompt một cách rõ ràng.
    output = result.stdout.replace("Bắt đầu (0..5): ", "").strip().splitlines()
    assert output == list(expected), (
        f"{filename}; input={typed_input!r}; mong đợi={expected!r}; "
        f"thực tế={output!r}"
    )
    assert "Traceback" not in result.stderr


def check_lab01(folder: str) -> None:
    expect_output(
        folder,
        "lab01_numbered_scores.py",
        ("1. An: 8", "2. Bình: 9", "3. Chi: 7", "Tổng điểm: 24"),
    )


def check_lab02(folder: str) -> None:
    cases = (
        ("0\n", ("Kết thúc",)),
        ("1\n", ("Còn: 1", "Kết thúc")),
        ("3\n", ("Còn: 3", "Còn: 2", "Còn: 1", "Kết thúc")),
        ("5\n", ("Còn: 5", "Còn: 4", "Còn: 3", "Còn: 2", "Còn: 1", "Kết thúc")),
        ("abc\n", ("Dữ liệu không hợp lệ",)),
        ("-1\n", ("Dữ liệu không hợp lệ",)),
        ("6\n", ("Dữ liệu không hợp lệ",)),
        ("\n", ("Dữ liệu không hợp lệ",)),
        (" 3 \n", ("Còn: 3", "Còn: 2", "Còn: 1", "Kết thúc")),
    )
    for value, expected in cases:
        expect_output(folder, "lab02_safe_countdown.py", expected, value)


def check_lab03(folder: str) -> None:
    expect_output(
        folder,
        "lab03_filter_squares.py",
        (
            "Đã chọn: [1, 2, 4, 5, 7, 8]",
            "Bình phương chẵn: [4, 16, 64]",
        ),
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Week06 offline practice self-check")
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--starter", action="store_true", help="Kiểm code sinh viên")
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
        print(f"Week 06 {label} practice: PASS (3/3)")
        return 0
    print(f"Week 06 {label} practice: FAIL ({passed}/3)")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
