"""CI verifies the three optional worked examples are executable and offline.

Do not use learner starter TODOs here; they are intentionally unfinished.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "weeks" / "week-13-modules-cli-api"


def run_python(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        cwd=WEEK,
        capture_output=True,
        text=True,
        check=False,
        timeout=15,
    )


@pytest.mark.parametrize(
    ("module", "expected_lines"),
    [
        (
            "examples.ex05_trace_student_flow",
            ("Bước 3: action = right", "Từ chối: position phải từ 0 đến 4"),
        ),
        (
            "examples.ex06_http_error_cases",
            ("200 + JSON hợp lệ => OK: lesson=13", "503 + JSON hợp lệ => LỖI",
             "200 + thiếu lesson => LỖI"),
        ),
        (
            "examples.ex07_json_roundtrip",
            ("Python cơ bản: 3 quyển", "copies phải là số nguyên không âm",
             "thư mục tạm đã được dọn"),
        ),
    ],
)
def test_worked_examples_run_offline(module: str, expected_lines: tuple[str, ...]) -> None:
    result = run_python("-m", module)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Traceback" not in result.stderr
    assert all(line in result.stdout for line in expected_lines), result.stdout


def test_worked_examples_can_be_imported_without_running_demo() -> None:
    result = run_python(
        "-c",
        "import examples.ex05_trace_student_flow; "
        "import examples.ex06_http_error_cases; "
        "import examples.ex07_json_roundtrip",
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout == ""


def test_rejected_inputs_are_not_silent_successes() -> None:
    script = (
        "from examples.ex05_trace_student_flow import build_action\n"
        "from examples.ex06_http_error_cases import read_lesson\n"
        "for action in [lambda: build_action('{'), "
        "lambda: build_action('[]'), "
        "lambda: read_lesson(200, b'{\"lesson\": true}'), "
        "lambda: read_lesson(200, b'[]')]:\n"
        "    try:\n"
        "        action()\n"
        "    except ValueError:\n"
        "        pass\n"
        "    else:\n"
        "        raise AssertionError('Sai: invalid input was accepted')\n"
        "print('FAIL-CLOSED: PASS')\n"
    )
    result = run_python("-c", script)
    assert result.returncode == 0, result.stderr
    assert "FAIL-CLOSED: PASS" in result.stdout


def test_walkthrough_is_linked_from_week13_readme() -> None:
    readme = (WEEK / "README.md").read_text(encoding="utf-8")
    walkthrough = (WEEK / "WALKTHROUGH-EXAMPLES.md").read_text(encoding="utf-8")
    assert "WALKTHROUGH-EXAMPLES.md" in readme
    for module in (
        "examples.ex05_trace_student_flow",
        "examples.ex06_http_error_cases",
        "examples.ex07_json_roundtrip",
    ):
        assert module in walkthrough
