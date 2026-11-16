"""Check 3 Week03 learner labs by executing them with many inputs.

--starter checks the student's code (intentionally FAIL before TODOs).
--solutions verifies the reference (used in CI). Python stdlib only.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]


def run_case(folder: str, filename: str, typed_input: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(BASE / folder / filename)],
        input=typed_input,
        text=True,
        capture_output=True,
        check=False,
        timeout=10,
    )


def check_cases(folder: str, filename: str, cases: tuple[tuple[str, str], ...]) -> None:
    for typed_input, expected in cases:
        result = run_case(folder, filename, typed_input)
        assert result.returncode == 0, (
            f"Input={typed_input!r}, exit={result.returncode}, stderr={result.stderr}"
        )
        # input() prompts may share a line with the output; compare its last line.
        assert result.stdout.strip().endswith(expected), (
            f"Input={typed_input!r}, expected last={expected!r}, "
            f"actual stdout={result.stdout!r}"
        )
        assert "Traceback" not in result.stderr


def lab01(folder: str) -> None:
    check_cases(
        folder,
        "lab01_score.py",
        (
            ("0\n", "Cần luyện tập"),
            ("4\n", "Cần luyện tập"),
            ("5\n", "Đạt"),
            ("7\n", "Đạt"),
            ("8\n", "Giỏi"),
            ("10\n", "Giỏi"),
            ("11\n", "Điểm không hợp lệ"),
            ("abc\n", "Điểm không hợp lệ"),
            ("-1\n", "Điểm không hợp lệ"),
            ("\n", "Điểm không hợp lệ"),
        ),
    )


def lab02(folder: str) -> None:
    check_cases(
        folder,
        "lab02_entry.py",
        (
            ("18\ny\nn\n", "Được vào"),
            ("17\ny\nn\n", "Không được vào"),
            ("120\ny\nn\n", "Được vào"),
            ("18\nn\nn\n", "Không được vào"),
            ("18\ny\ny\n", "Không được vào"),
            ("abc\ny\nn\n", "Dữ liệu không hợp lệ"),
            ("121\ny\nn\n", "Dữ liệu không hợp lệ"),
            ("-1\ny\nn\n", "Dữ liệu không hợp lệ"),
            ("18\nx\nn\n", "Dữ liệu không hợp lệ"),
            ("18\ny\nx\n", "Dữ liệu không hợp lệ"),
        ),
    )


def lab03(folder: str) -> None:
    check_cases(
        folder,
        "lab03_shipping.py",
        (
            ("0\nn\nn\n", "Phí giao hàng: 30,000 VND"),
            ("0\nn\ny\n", "Phí giao hàng: 50,000 VND"),
            ("99_999\ny\nn\n", "Dữ liệu không hợp lệ"),
            ("99999\ny\nn\n", "Phí giao hàng: 30,000 VND"),
            ("100000\ny\nn\n", "Phí giao hàng: 0 VND"),
            ("199999\nn\ny\n", "Phí giao hàng: 50,000 VND"),
            ("200000\nn\ny\n", "Phí giao hàng: 0 VND"),
            ("-1\nn\nn\n", "Dữ liệu không hợp lệ"),
            ("abc\nn\nn\n", "Dữ liệu không hợp lệ"),
            ("100000\nx\nn\n", "Dữ liệu không hợp lệ"),
            ("100000\ny\nx\n", "Dữ liệu không hợp lệ"),
        ),
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Week03 student practice check (offline)")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--starter", action="store_true", help="Kiểm bài sinh viên")
    mode.add_argument("--solutions", action="store_true", help="Kiểm lời giải tham khảo")
    args = parser.parse_args(argv)
    folder = "starter" if args.starter else "solutions"
    passed = 0
    for index, check in enumerate((lab01, lab02, lab03), 1):
        try:
            check(folder)
        except (AssertionError, OSError, subprocess.TimeoutExpired) as exc:
            print(f"Lab {index:02d}: FAIL — {type(exc).__name__}: {exc}")
        else:
            print(f"Lab {index:02d}: PASS")
            passed += 1
    mode_name = "student" if args.starter else "reference"
    if passed != 3:
        print(f"Week 03 {mode_name} practice: FAIL ({passed}/3)")
        return 1
    print(f"Week 03 {mode_name} practice: PASS (3/3)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
