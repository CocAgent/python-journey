"""Đảm bảo bốn ví dụ có thể chạy trực tiếp bằng Python."""

import subprocess
import sys
from pathlib import Path

import pytest

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"


@pytest.mark.parametrize(
    ("filename", "expected"),
    [
        ("01_class_object.py", ("75.0", "Progress: 3/4")),
        ("02_composition.py", ("wait", "left")),
        ("03_basic_inheritance.py", ("Milo: woof", "True")),
        ("04_dien_thoai.py", ("DT01", "DT02", "Apple", "Samsung")),
    ],
)
def test_examples_run(filename, expected):
    result = subprocess.run(
        [sys.executable, str(EXAMPLES / filename)],
        capture_output=True,
        text=True,
        check=False,
        timeout=15,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert all(word in result.stdout for word in expected)
