"""Maintainer checks for Week04 beginner worked examples and self-check.

Learner starter files intentionally contain TODOs. Only reference solutions
need to pass CI; the starter checker must not claim success prematurely.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "weeks" / "week-04-strings"
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
    ("filename", "outputs"),
    [
        (
            "04_predict_slice_and_find.py",
            (
                "Ký tự đầu: P",
                "Ký tự cuối: n",
                "Ba ký tự đầu: Pyt",
                "Đảo chuỗi: nohtyP",
                "find('th'): 2",
                "find('Java'): -1",
                "Index 99 có hợp lệ? False",
                "Chuỗi rỗng: không đọc được ký tự đầu",
            ),
        ),
        (
            "05_normalize_words_step_by_step.py",
            (
                "Sau join: 'python la python'",
                "Số từ: 3",
                "Số từ 'python': 2",
                "Đếm chuỗi con: 3",
                "Đếm từ đơn giản: 2",
                "Chuỗi gốc vẫn giữ: python la python",
            ),
        ),
        (
            "06_regex_search_vs_fullmatch.py",
            (
                "'EV-123': search=True, fullmatch=True",
                "'EV-123X': search=True, fullmatch=False",
                "'XEV-123': search=True, fullmatch=False",
                "Mã tìm được: ['EV-123', 'EV-456']",
                "Không tìm thấy: True",
            ),
        ),
    ],
)
def test_examples_explain_success_and_failure(
    filename: str, outputs: tuple[str, ...]
) -> None:
    result = run_script(EXAMPLES / filename)
    assert result.returncode == 0, result.stdout + result.stderr
    for output in outputs:
        assert output in result.stdout


def test_reference_practice_passes_multiple_boundary_cases() -> None:
    result = run_script(CHECK, "--solutions")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Week 04 reference practice: PASS (3/3)" in result.stdout


def test_unfinished_starter_cannot_fake_success() -> None:
    result = run_script(CHECK, "--starter")
    assert result.returncode == 1, result.stdout + result.stderr
    assert "Week 04 student practice: FAIL (0/3)" in result.stdout


def test_workbook_links_examples_and_self_check() -> None:
    readme = (WEEK / "README.md").read_text(encoding="utf-8")
    workbook = (WEEK / "WORKED-EXAMPLES.md").read_text(encoding="utf-8")
    practice = (WEEK / "practice" / "README.md").read_text(encoding="utf-8")
    assert "WORKED-EXAMPLES.md" in readme
    assert "practice/README.md" in readme
    assert "--starter" in practice and "--solutions" in practice
    for name in (
        "04_predict_slice_and_find.py",
        "05_normalize_words_step_by_step.py",
        "06_regex_search_vs_fullmatch.py",
    ):
        assert name in workbook
