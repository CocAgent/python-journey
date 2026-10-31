"""Self-check cho bốn bài TƯƠNG TỰ Week 13.

--starter: kiểm file sinh viên; trước khi viết TODO, FAIL là đúng.
--solutions: kiểm đáp án tham khảo; CI chỉ gọi mode này.

Không cần pytest và không gọi mạng.
"""

from __future__ import annotations

import argparse
import importlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Callable

WEEK_ROOT = Path(__file__).resolve().parents[2]


def must_raise(action: Callable[[], object]) -> None:
    try:
        action()
    except ValueError:
        return
    raise AssertionError("Expected ValueError, nhưng chương trình không từ chối input")


def run_module(module: str, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", module, *args],
        cwd=WEEK_ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=10,
    )


def check_lab01(package: str) -> None:
    module = importlib.import_module(f"practice.{package}.lab01_module")
    assert module.describe_score(7.5) == "Điểm 7.5: Đạt"
    assert module.describe_score(3) == "Điểm 3: Cần luyện tập"

    imported = run_module(
        "practice.checks.import_probe",
        f"practice.{package}.lab01_module",
    )
    assert imported.returncode == 0, imported.stderr
    assert imported.stdout == "", "Import module không được tự in dòng demo"


def check_lab02(package: str) -> None:
    name = f"practice.{package}.lab02_cli"
    valid = run_module(name, "--score", "7.5")
    assert valid.returncode == 0, valid.stderr
    parsed = json.loads(valid.stdout)
    assert parsed == {"score": 7.5, "status": "Đạt"}
    for args in ((), ("--score", "12"), ("--score", "-1"), ("--score", "abc")):
        failed = run_module(name, *args)
        assert failed.returncode == 2, f"{args}: cần exit code 2"
        assert failed.stdout.strip() == "", f"{args}: không in JSON thành công"


def check_lab03(package: str) -> None:
    module = importlib.import_module(f"practice.{package}.lab03_http")
    expected = module.read_score_response(200, b'{"score": 8}')
    assert expected == {"score": 8, "status": "Đạt"}
    for status, body in (
        (404, b'{"score": 8}'),
        (200, b"not-json"),
        (200, b"{}"),
        (200, b'{"score": 15}'),
    ):
        must_raise(lambda status=status, body=body: module.read_score_response(status, body))


def check_lab04(package: str) -> None:
    module = importlib.import_module(f"practice.{package}.lab04_adapter")
    result = module.make_student_report({"student": "  An  ", "score": 7.5})
    assert result == {"student": "An", "score": 7.5, "status": "Đạt"}
    for payload in (
        {"student": " ", "score": 7.5},
        {"student": "An"},
        {"student": "An", "score": True},
        {"student": "An", "score": 15},
    ):
        must_raise(lambda payload=payload: module.make_student_report(payload))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Week 13 self-check (offline)")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--starter", action="store_true", help="Kiểm bài sinh viên")
    group.add_argument("--solutions", action="store_true", help="Kiểm đáp án tham khảo")
    args = parser.parse_args(argv)

    package = "starter" if args.starter else "solutions"
    label = "student" if args.starter else "reference"
    checks = (check_lab01, check_lab02, check_lab03, check_lab04)
    passed = 0
    for index, check in enumerate(checks, 1):
        try:
            check(package)
        except Exception as error:
            print(f"Lab {index}: FAIL — {type(error).__name__}: {error}")
        else:
            passed += 1
            print(f"Lab {index}: PASS")
    if passed != len(checks):
        print(f"Week 13 guided {label} labs: FAIL ({passed}/4)")
        return 1
    print(f"Week 13 guided {label} labs: PASS (4/4)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
