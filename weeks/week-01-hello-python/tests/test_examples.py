"""Chạy ví dụ giáo trình và mini-project mẫu độc lập."""

import subprocess
import sys
from pathlib import Path

import pytest

WEEK = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    ("filename", "expected"),
    [
        ("01_print_and_comments.py", "Hello, World!"),
        ("02_arithmetic.py", "10 // 3 = 3"),
        ("03_first_error.py", "Tổng: 5"),
    ],
)
def test_demo_runs(filename, expected):
    result = subprocess.run(
        [sys.executable, "-B", str(WEEK / "examples" / filename)],
        capture_output=True,
        text=True,
        check=False,
        timeout=15,
    )
    assert result.returncode == 0, result.stderr
    assert expected in result.stdout


@pytest.mark.parametrize("name", ["An", "Binh"])
def test_reference_ascii_card_has_matching_border(name):
    result = subprocess.run(
        [sys.executable, "-B", str(WEEK / "mini-project" / "reference.py")],
        input=name + "\n",
        capture_output=True,
        text=True,
        check=False,
        timeout=15,
    )
    assert result.returncode == 0, result.stderr
    top, middle, bottom = result.stdout.splitlines()
    border = top.removeprefix("Tên của bạn: ")
    assert border == bottom
    assert middle == f"| Xin chào {name}! |"
    assert len(middle) == len(border)
