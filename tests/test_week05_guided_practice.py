"""Week05 maintainer test: inspect runnable examples and reference practice.

Learner starter exercises contain TODO intentionally; CI never reports their
reference solution pass as proof of student completion.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "weeks" / "week-05-lists-tuples"
EXAMPLES = WEEK / "examples"
CHECK = WEEK / "practice" / "checks" / "check_practice.py"


def run_script(path: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(path), *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )


@pytest.mark.parametrize(
    ("name", "expected_lines"),
    [
        (
            "04_predict_alias_and_copy.py",
            (
                "List gốc: ['Tin', 'Văn', 'Anh']",
                "Alias: ['Tin', 'Văn', 'Anh']",
                "Copy: ['Toán', 'Văn']",
                "Alias cùng đối tượng: True",
                "Copy cùng đối tượng: False",
                "List lồng nhau sau sửa: [['A', 'C'], ['B']]",
            ),
        ),
        (
            "05_list_crud_and_slice.py",
            (
                "Bước 3 — sửa/xóa: ['Mai', 'Lan', 'Bình']",
                "Đã lấy bằng pop(): Dũng",
                "Hai người đầu: ['Mai', 'Lan']",
                "Không có 'Nam', không gọi remove()",
                "sorted() trả: [4, 7, 9]; gốc: [7, 4, 9]",
                "sort() trả: None; gốc sau sort(): [4, 7, 9]",
            ),
        ),
        (
            "06_tuple_unpack_and_guard.py",
            (
                "Tọa độ: x=3, y=7",
                "Học viên: An, 20 tuổi, học Python",
                "Sau đổi chỗ: B, A",
                "Kiểu một phần tử có dấu phẩy: tuple",
                "Không có dấu phẩy: str",
                "Không unpack: cần chính xác hai giá trị",
            ),
        ),
    ],
)
def test_new_examples_are_runnable(
    name: str, expected_lines: tuple[str, ...]
) -> None:
    run = run_script(EXAMPLES / name)
    assert run.returncode == 0, run.stdout + run.stderr
    for expected in expected_lines:
        assert expected in run.stdout


def test_reference_practice_passes() -> None:
    result = run_script(CHECK, "--solutions")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Week 05 reference practice: PASS (3/3)" in result.stdout


def test_unfinished_starters_do_not_fake_success() -> None:
    result = run_script(CHECK, "--starter")
    assert result.returncode == 1, result.stdout + result.stderr
    assert "Week 05 student practice: FAIL (0/3)" in result.stdout


def test_workbook_is_linked_and_has_three_examples() -> None:
    readme = (WEEK / "README.md").read_text(encoding="utf-8")
    guide = (WEEK / "WORKED-EXAMPLES.md").read_text(encoding="utf-8")
    practice = (WEEK / "practice" / "README.md").read_text(encoding="utf-8")
    assert "WORKED-EXAMPLES.md" in readme
    assert "practice/README.md" in readme
    assert "--starter" in practice and "--solutions" in practice
    for filename in (
        "04_predict_alias_and_copy.py",
        "05_list_crud_and_slice.py",
        "06_tuple_unpack_and_guard.py",
    ):
        assert filename in guide
