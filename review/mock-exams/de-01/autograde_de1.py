"""Tự chấm Đề ôn tập 01 — 60 phút, 5 câu × 2 điểm, 10 ý × 1 điểm.

python review/mock-exams/de-01/autograde_de1.py --student
python review/mock-exams/de-01/autograde_de1.py --reference

Đây là bộ TỰ ĐÁNH GIÁ (không phải điểm thi chính thức).
Dùng đúng Python interpreter đang chạy; file sinh viên chạy trong
subprocess với timeout nhưng KHÔNG phải sandbox bảo mật.
Chỉ chấm code của chính mình hoặc code đã được tin cậy.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from test_de1 import CASES

ROOT = Path(__file__).resolve().parent
RUNNER = ROOT / "runner_de1.py"


def one_case(file_path: Path, function: str, case: dict) -> tuple[bool, str]:
    command = [
        sys.executable, str(RUNNER), str(file_path), function,
        json.dumps(case["args"], ensure_ascii=False),
    ]
    try:
        with tempfile.TemporaryDirectory() as directory:
            proc = subprocess.run(
                command,
                text=True,
                encoding="utf-8",
                errors="replace",
                capture_output=True,
                cwd=directory,
                check=False,
                timeout=4,
            )
    except subprocess.TimeoutExpired:
        return False, "Quá thời gian (4 giây)"
    if proc.returncode != 0:
        return False, f"Python exit={proc.returncode}: {proc.stderr.strip()[:120]}"
    try:
        data = json.loads(proc.stdout.strip())
    except json.JSONDecodeError:
        return False, "Không đọc được kết quả máy kiểm"
    if data.get("printed"):
        return False, "Hàm/đoạn import đã in ra terminal; bài yêu cầu return"
    if data.get("args_after") != case["args"]:
        return False, "Đã sửa dữ liệu nguồn (không được mutate input)"
    if "raises" in case:
        if not data.get("ok") and data.get("error") == case["raises"]:
            return True, "Đã từ chối input sai đúng loại exception"
        return False, f"Cần ném {case['raises']}; nhận {data.get('error') or data.get('value')}"
    if not data.get("ok"):
        return False, f"{data.get('error')}: {str(data.get('message'))[:110]}"
    if data.get("type") != case["type"]:
        return False, f"Kiểu trả về {data.get('type')} thay vì {case['type']}"
    if data.get("value") != case["returns"]:
        return False, f"Expected={case['returns']!r}; actual={data.get('value')!r}"
    return True, "Đúng"


def grade(folder: Path, *, verbose: bool) -> tuple[float, int, int]:
    total = 0.0
    passed_cases = 0
    all_cases = 0
    for name, spec in CASES.items():
        path = folder / f"{name}.py"
        if not path.is_file():
            print(f"{name}: 0.00/1.00 — thiếu file {path.name}")
            all_cases += len(spec["cases"])
            continue
        passed = 0
        for i, case in enumerate(spec["cases"], 1):
            ok, reason = one_case(path, spec["function"], case)
            passed += int(ok)
            if verbose or not ok:
                print(f"  {name} test {i:02d}: {'PASS' if ok else 'FAIL'} — {reason}")
        n = len(spec["cases"])
        all_cases += n
        passed_cases += passed
        points = passed / n
        total += points
        print(f"{name}: {points:.2f}/1.00 ({passed}/{n} cases)")
    return total, passed_cases, all_cases


def main() -> int:
    parser = argparse.ArgumentParser(description="Đề ôn tập CBPython — tự chấm /10")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--student", action="store_true", help="Chấm submissions_de1")
    mode.add_argument("--reference", action="store_true", help="Kiểm solutions_de1")
    parser.add_argument("--verbose", action="store_true", help="In mọi test")
    args = parser.parse_args()
    folder = ROOT / ("submissions_de1" if args.student else "solutions_de1")
    total, passed, count = grade(folder, verbose=args.verbose)
    print("-" * 48)
    print(f"{'BÀI SINH VIÊN' if args.student else 'LỜI GIẢI THAM KHẢO'}")
    print(f"Tổng điểm tự kiểm: {total:.2f}/10.00 — {passed}/{count} tests PASS")
    print("Lưu ý: đây là điểm tự luyện, KHÔNG phải điểm thi chính thức.")
    return 0 if passed == count else 1


if __name__ == "__main__":
    raise SystemExit(main())
