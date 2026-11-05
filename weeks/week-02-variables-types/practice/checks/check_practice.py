"""Tự kiểm ba bài tương tự (standard library, chạy offline).

--starter: kiểm code sinh viên viết (ban đầu FAIL có chủ đích).
--solutions: chỉ kiểm lời giải tham khảo (CI gọi mode này).
Sinh viên không cần hiểu subprocess/argparse để dùng checker.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

PRACTICE_ROOT = Path(__file__).resolve().parents[1]


def run_script(folder: str, script: str, typed_input: str = "") -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(PRACTICE_ROOT / folder / script)],
        input=typed_input,
        text=True,
        capture_output=True,
        check=False,
        timeout=10,
    )


def check_lab01(folder: str) -> None:
    result = run_script(folder, "lab01_profile.py")
    assert result.returncode == 0, result.stderr
    for expected in ("Tên: An", "Tuổi năm sau: 19", "Kiểu tuổi: int", "Đang học: True"):
        assert expected in result.stdout, f"Thiếu output: {expected}"


def check_lab02(folder: str) -> None:
    result = run_script(folder, "lab02_shop.py")
    assert result.returncode == 0, result.stderr
    for expected in (
        "Thành tiền: 75,000 VND",
        "Tình huống sai: ba không phải số lượng hợp lệ",
    ):
        assert expected in result.stdout, f"Thiếu output: {expected}"


def check_lab03(folder: str) -> None:
    valid = run_script(folder, "lab03_ticket.py", "Lan\n2\n")
    assert valid.returncode == 0, valid.stderr
    assert "Lan: 2 vé, tổng 24,000 VND" in valid.stdout

    for number_text in ("abc", "0", "-1"):
        invalid = run_script(folder, "lab03_ticket.py", f"Lan\n{number_text}\n")
        assert invalid.returncode == 0, invalid.stderr
        assert "Số vé không hợp lệ" in invalid.stdout
        assert "vé, tổng" not in invalid.stdout, "Sai: báo hóa đơn cho số vé không hợp lệ"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Week02 practice offline self-check")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--starter", action="store_true", help="Kiểm bài đã tự viết")
    mode.add_argument("--solutions", action="store_true", help="Kiểm đáp án tham khảo")
    args = parser.parse_args(argv)

    folder = "starter" if args.starter else "solutions"
    passed = 0
    for number, check in enumerate((check_lab01, check_lab02, check_lab03), 1):
        try:
            check(folder)
        except (AssertionError, OSError, subprocess.TimeoutExpired) as error:
            print(f"Lab {number:02d}: FAIL — {type(error).__name__}: {error}")
        else:
            passed += 1
            print(f"Lab {number:02d}: PASS")

    mode_name = "student" if args.starter else "reference"
    if passed != 3:
        print(f"Week 02 {mode_name} practice: FAIL ({passed}/3)")
        return 1
    print(f"Week 02 {mode_name} practice: PASS (3/3)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
