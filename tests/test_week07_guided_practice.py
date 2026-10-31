"""Week 07 guided Functions maintainer gates — reference only.

Starter TODOs intentionally fail; these tests never conflate solution
success with learner completion. Runs via stdlib subprocess, offline.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "weeks" / "week-07-functions"
CHECK = WEEK / "practice" / "checks" / "check_practice.py"


def run_script(path: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(path), *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=35,
    )


@pytest.mark.parametrize(
    ("name", "lines"),
    [
        (
            "06_predict_return_and_default.py",
            (
                "show_price in: 24,000 VND",
                "Caller nhận từ show_price: None",
                "Caller nhận từ calculate_price: 24,000 VND",
                "Thêm phí 5,000: 29,000 VND",
                "Số dương đầu tiên: 7",
                "Không có số dương: None",
            ),
        ),
        (
            "07_scope_and_decomposition_trace.py",
            (
                "Giá ở caller trước: 20000",
                "Thanh toán: 45,000 VND",
                "Giá ở caller sau: 20000",
                "Đơn hàng không hợp lệ",
            ),
        ),
        (
            "08_type_hints_and_decision.py",
            (
                "Lặp chuỗi đúng kiểu: PyPy",
                "Annotation không chặn bool: Py",
                "Validator nhận 10: True",
                "Validator từ chối True: False",
                "Hết giờ, dù đang bối rối: stop",
                "Còn giờ và bối rối: review",
                "Còn giờ và rõ bài: practice",
            ),
        ),
    ],
)
def test_new_worked_examples_are_runnable(name: str, lines: tuple[str, ...]) -> None:
    result = run_script(WEEK / "examples" / name)
    assert result.returncode == 0, result.stdout + result.stderr
    for line in lines:
        assert line in result.stdout


def test_reference_functions_pass_direct_call_checks() -> None:
    result = run_script(CHECK, "--solutions")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Week 07 reference practice: PASS (4/4)" in result.stdout


def test_student_todos_fail_before_work_is_done() -> None:
    result = run_script(CHECK, "--starter")
    assert result.returncode == 1, result.stdout + result.stderr
    assert "Week 07 student practice: FAIL (0/4)" in result.stdout


def test_readme_links_to_guided_examples_and_practice() -> None:
    readme = (WEEK / "README.md").read_text(encoding="utf-8")
    guide = (WEEK / "WORKED-EXAMPLES.md").read_text(encoding="utf-8")
    practice = (WEEK / "practice" / "README.md").read_text(encoding="utf-8")
    assert "WORKED-EXAMPLES.md" in readme
    assert "practice/README.md" in readme
    assert "--starter" in practice and "--solutions" in practice
    for name in (
        "06_predict_return_and_default.py",
        "07_scope_and_decomposition_trace.py",
        "08_type_hints_and_decision.py",
    ):
        assert name in guide
