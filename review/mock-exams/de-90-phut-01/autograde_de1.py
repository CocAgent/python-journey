"""Formative self-check for the 90-minute Python practice examination.

Usage:
    python review/mock-exams/de-90-phut-01/autograde_de1.py --student
    python review/mock-exams/de-90-phut-01/autograde_de1.py --reference

Do not execute untrusted submissions on an unprotected host.
Subprocess timeout does NOT provide a safe execution sandbox.
"""

from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
import tempfile
from pathlib import Path

from test_de1 import CASES


ROOT = Path(__file__).resolve().parent
RUNNER = ROOT / "runner_de1.py"


def grade_one(file_path: Path, spec: dict, case: dict) -> tuple[bool, str]:
    process_args = [
        sys.executable,
        str(RUNNER),
        str(file_path),
        spec["kind"],
        spec.get("function", spec.get("class", "")),
        json.dumps(case["args"], ensure_ascii=False),
    ]
    try:
        with tempfile.TemporaryDirectory() as workdir:
            result = subprocess.run(
                process_args,
                cwd=workdir,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                check=False,
                timeout=4,
            )
    except subprocess.TimeoutExpired:
        return False, "Quá giới hạn 4 giây"
    if result.returncode:
        return False, f"Process exit={result.returncode}, stderr={result.stderr[:100]}"
    try:
        data = json.loads(result.stdout.strip())
    except json.JSONDecodeError:
        return False, "Không thể đọc kết quả từ worker"
    if data.get("printed"):
        return False, "Hàm bài tập không được print khi import hoặc gọi"
    if data.get("args_after") != case["args"]:
        return False, "Đã sửa dữ liệu đầu vào"

    if "raises" in case:
        if not data.get("ok") and data.get("error") == case["raises"]:
            return True, "Từ chối dữ liệu sai đúng exception"
        return False, f"Cần {case['raises']}, nhận {data.get('error') or data.get('value')!r}"

    if not data.get("ok"):
        return False, f"{data.get('error')}: {str(data.get('message'))[:100]}"
    if data.get("type") != case["type"]:
        return False, f"Kiểu trả về {data.get('type')!r}, cần {case['type']!r}"
    actual, expected = data.get("value"), case["returns"]
    if case["type"] == "float":
        valid = isinstance(actual, float) and math.isclose(
            actual, expected, rel_tol=1e-11, abs_tol=1e-11
        )
    else:
        valid = actual == expected
    if not valid:
        return False, f"Cần {expected!r}; nhận {actual!r}"
    return True, "Đúng"


def grade(folder: Path, verbose: bool = False) -> tuple[float, int, int]:
    earned = 0.0
    passed = total = 0
    for task, spec in CASES.items():
        path = folder / f"{task}.py"
        count = len(spec["cases"])
        total += count
        if not path.is_file():
            print(f"{task}: 0.00/1.00 — thiếu file {path.name}")
            continue
        successes = 0
        for index, case in enumerate(spec["cases"], 1):
            ok, why = grade_one(path, spec, case)
            successes += int(ok)
            if verbose or not ok:
                print(f"  {task} #{index:02d}: {'PASS' if ok else 'FAIL'} — {why}")
        score = successes / count
        earned += score
        passed += successes
        print(f"{task}: {score:.2f}/1.00 ({successes}/{count})")
    return earned, passed, total


def main() -> int:
    parser = argparse.ArgumentParser(description="90-minute Python self-study assessment")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--student", action="store_true", help="Evaluate starter code")
    mode.add_argument("--reference", action="store_true", help="Evaluate reference solutions")
    parser.add_argument("--verbose", action="store_true", help="Show passing cases too")
    args = parser.parse_args()

    folder = ROOT / ("submissions_de1" if args.student else "solutions_de1")
    points, passed, total = grade(folder, verbose=args.verbose)
    name = "STUDENT" if args.student else "REFERENCE"
    print(f"{name}: {points:.2f}/10.00 — {passed}/{total} cases PASS")
    print("FORMATIVE SELF-CHECK ONLY — NOT AN OFFICIAL EXAM GRADE.")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
