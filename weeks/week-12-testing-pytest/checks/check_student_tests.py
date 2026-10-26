"""Tự kiểm tra xem bài test của sinh viên có phát hiện được lỗi hay không.

Chương trình không sửa file gốc. Mỗi lần thử dùng một thư mục tạm riêng
chứa bản sao module và bài test do sinh viên viết.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

WEEK_ROOT = Path(__file__).resolve().parents[1]
SOURCE = WEEK_ROOT / "exercises" / "decision.py"
STUDENT_TEST = WEEK_ROOT / "exercises" / "test_decision_starter.py"

# Mỗi lỗi làm sai một quy tắc khác nhau. Đây là ví dụ để học về chất lượng test.
MUTATIONS = {
    "Bot đứng yên sai khi cần đi phải": (
        'return "right" if position < goal else "left"',
        'return "wait" if position < goal else "left"',
    ),
    "Bot đi tiếp dù đã tới đích": (
        'return "wait"',
        'return "right"',
    ),
    "Bot luôn đi phải, kể cả khi đích ở bên trái": (
        'return "right" if position < goal else "left"',
        'return "right"',
    ),
    "Chấp nhận lượt chơi bằng 0": (
        'raise ValueError("turn must be positive")',
        "return turn",
    ),
}


def run_tests(module_text: str, test_text: str) -> subprocess.CompletedProcess[str]:
    """Chạy test trên hai bản sao trong thư mục tạm, không sửa bài gốc."""
    with TemporaryDirectory(prefix="python-journey-week12-") as directory:
        workdir = Path(directory)
        (workdir / "decision.py").write_text(module_text, encoding="utf-8")
        (workdir / "test_decision_starter.py").write_text(
            test_text, encoding="utf-8"
        )

        # Mỗi lần chạy tạo process mới, tránh tái sử dụng module đã import.
        return subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                "test_decision_starter.py",
                "-q",
                "-p",
                "no:cacheprovider",
            ],
            cwd=workdir,
            text=True,
            capture_output=True,
            check=False,
            timeout=30,
        )


def main() -> int:
    """PASS khi test đúng với module gốc và bắt được cả bốn lỗi cố ý."""
    source = SOURCE.read_text(encoding="utf-8")
    student = STUDENT_TEST.read_text(encoding="utf-8")

    try:
        baseline = run_tests(source, student)
    except subprocess.TimeoutExpired:
        print("FAIL: bộ test chạy quá thời gian cho phép (30 giây).")
        return 1

    if baseline.returncode != 0:
        print("CHƯA ĐẠT: test sinh viên phải PASS trên chương trình đúng.")
        print("Nếu còn pytest.fail(...), hãy hoàn thành các TODO trước.")
        print((baseline.stdout + baseline.stderr)[-3000:])
        return 1

    print("1/2: Bài test PASS trên chương trình đúng.")
    missed = []

    for label, (old, new) in MUTATIONS.items():
        if source.count(old) != 1:
            print(f"KHÔNG KIỂM TRA ĐƯỢC: mẫu lỗi '{label}' đã thay đổi.")
            return 2

        mutated_source = source.replace(old, new, 1)
        try:
            result = run_tests(mutated_source, student)
        except subprocess.TimeoutExpired:
            print(f"CHƯA ĐẠT: test bị treo khi thử lỗi '{label}'.")
            return 1

        if result.returncode == 1:
            print(f"  PHÁT HIỆN LỖI: {label}")
        else:
            # exit 0: test không phát hiện; exit 2/3/...: bản test bị lỗi
            # khi thu thập hoặc chạy; không tính đó là phát hiện lỗi đúng.
            print(f"  CHƯA ĐẠT: {label} (pytest exit {result.returncode})")
            missed.append(label)

    if missed:
        print(f"2/2: Còn {len(missed)} lỗi cố ý chưa được phát hiện.")
        print("Gợi ý: kiểm tra hành động CHÍNH XÁC trong mỗi tình huống.")
        return 1

    print("2/2: Đã phát hiện cả bốn lỗi cố ý.")
    print("Week 12 student self-check: PASS (không thay thế đánh giá giảng viên)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
