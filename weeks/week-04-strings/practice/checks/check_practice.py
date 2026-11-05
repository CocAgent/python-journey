"""Week04 learner exercises checker, Python standard library only.

--starter: checks what students actually wrote (FAIL before TODO completion).
--solutions: reference acceptance checks only (used by maintainer CI).
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_script(folder: str, filename: str, typed_input: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(ROOT / folder / filename)],
        input=typed_input,
        capture_output=True,
        text=True,
        check=False,
        timeout=10,
    )


def assert_case(folder: str, file: str, typed_input: str, expected: str) -> None:
    result = run_script(folder, file, typed_input)
    assert result.returncode == 0, f"Input={typed_input!r}: {result.stderr}"
    # input prompt may appear on the same stdout line as the result.
    assert result.stdout.strip().endswith(expected), (
        f"Input={typed_input!r}; expected ending={expected!r}; actual={result.stdout!r}"
    )
    assert "Traceback" not in result.stderr


def lab01(folder: str) -> None:
    filename = "lab01_keyword.py"
    for value, last_line in (
        ("Python\n", "Độ dài: 6"),
        ("Cóc\n", "Độ dài: 3"),
        ("  Python  \n", "Độ dài: 6"),
        ("\n", "Từ khóa không được rỗng"),
        ("   \n", "Từ khóa không được rỗng"),
    ):
        assert_case(folder, filename, value, last_line)
    valid = run_script(folder, filename, "Python\n")
    for line in ("Đầu: P", "Cuối: n", "Đảo: nohtyP"):
        assert line in valid.stdout, f"Thiếu output: {line}"


def lab02(folder: str) -> None:
    filename = "lab02_word_counter.py"
    for value, expected_lines in (
        ("  PYTHON   la  Python \n", ("Chuẩn hóa: python la python", "Số từ: 3", "Từ python: 2")),
        ("python pythonic python\n", ("Chuẩn hóa: python pythonic python", "Số từ: 3", "Từ python: 2")),
        ("Xin   chào\n", ("Chuẩn hóa: xin chào", "Số từ: 2", "Từ python: 0")),
        ("\n", ("Câu không được rỗng",)),
        ("   \n", ("Câu không được rỗng",)),
    ):
        result = run_script(folder, filename, value)
        assert result.returncode == 0, result.stderr
        for line in expected_lines:
            assert line in result.stdout, f"Input={value!r}: thiếu {line!r}"
        if expected_lines == ("Câu không được rỗng",):
            assert "Chuẩn hóa:" not in result.stdout, "Input rỗng vẫn in kết quả thành công"


def lab03(folder: str) -> None:
    filename = "lab03_event_code.py"
    for value, expected in (
        ("EV-123\n", "Mã hợp lệ: EV-123"),
        (" EV-000 \n", "Mã hợp lệ: EV-000"),
        ("EV-999\n", "Mã hợp lệ: EV-999"),
        ("EV-12\n", "Mã không hợp lệ"),
        ("EV-1234\n", "Mã không hợp lệ"),
        ("EV-123X\n", "Mã không hợp lệ"),
        ("XEV-123\n", "Mã không hợp lệ"),
        ("ev-123\n", "Mã không hợp lệ"),
        ("EV-１２３\n", "Mã không hợp lệ"),
        ("\n", "Mã không hợp lệ"),
    ):
        assert_case(folder, filename, value, expected)
        result = run_script(folder, filename, value)
        if expected == "Mã không hợp lệ":
            assert "Mã hợp lệ:" not in result.stdout, f"Không được báo thành công: {value!r}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Week04 similar exercises self-check")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--starter", action="store_true", help="Kiểm code sinh viên")
    mode.add_argument("--solutions", action="store_true", help="Kiểm lời giải tham khảo")
    args = parser.parse_args(argv)

    folder = "starter" if args.starter else "solutions"
    passed = 0
    for index, check in enumerate((lab01, lab02, lab03), 1):
        try:
            check(folder)
        except (AssertionError, OSError, subprocess.TimeoutExpired) as error:
            print(f"Lab {index:02d}: FAIL — {type(error).__name__}: {error}")
        else:
            passed += 1
            print(f"Lab {index:02d}: PASS")

    name = "student" if args.starter else "reference"
    if passed != 3:
        print(f"Week 04 {name} practice: FAIL ({passed}/3)")
        return 1
    print(f"Week 04 {name} practice: PASS (3/3)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
