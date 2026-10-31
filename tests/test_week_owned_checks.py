"""Cổng CI chung cho bài kiểm thử được sở hữu bởi từng tuần.

Logic và dữ liệu test nằm ở tuần tương ứng; file này chỉ gọi các lệnh
tham chiếu ổn định. Không thu thập starter/learner_tests vào pytest mặc định.
"""

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    ("label", "arguments", "expected", "timeout"),
    [
        ("Tuần 01 — lời giải và ba ví dụ", ["weeks/week-01-hello-python/checks/check_week.py"], "Week 01 reference checks: PASS", 60),
        ("Tuần 01 — test biên và mini-project mẫu", ["-m", "pytest", "weeks/week-01-hello-python/tests", "-q", "-p", "no:cacheprovider"], None, 60),
        ("Tuần 09 — danh mục 20 đề tài", ["weeks/week-09-midterm-project/checks/check_project_catalog.py"], "20 nguồn, 10 tiêu chí", 30),
        ("Tuần 12 — ví dụ kiểm thử nhiều file", ["-m","pytest","weeks/week-12-testing-pytest/examples/test_multi_file_lab.py","-q","-p","no:cacheprovider"], None, 60),
        ("Tuần 12 — kiểm lỗi mô phỏng 3 module", ["weeks/week-12-testing-pytest/checks/check_multi_file_faults.py"], "6/6 lỗi trong 3 tệp", 240),
        ("Tuần 14 — kiểm tra OOP tham chiếu", ["weeks/week-14-oop-essentials/checks/check_week.py"], "Week 14 reference checks: PASS", 120),
    ],
)
def test_week_owned_checks_run(label, arguments, expected, timeout) -> None:
    """Giữ CI mặc định nhất quán mà không nhân đôi bài test của mỗi tuần."""
    result = subprocess.run(
        [sys.executable, *arguments],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    assert result.returncode == 0, (
        f"{label}: exit={result.returncode}\n{result.stdout}\n{result.stderr}"
    )
    if expected is not None:
        assert expected in result.stdout, result.stdout + result.stderr
