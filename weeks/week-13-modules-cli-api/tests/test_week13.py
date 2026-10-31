"""Week 13 teaching reference tests (run explicitly, not unfinished TODOs)."""

import json
import subprocess
import sys
from pathlib import Path

import pytest

WEEK_ROOT = Path(__file__).resolve().parents[1]
if str(WEEK_ROOT) not in sys.path:
    sys.path.insert(0, str(WEEK_ROOT))

from bot_course.adapter import course_local_action  # noqa: E402
from bot_course.core import choose_action  # noqa: E402
from bot_course.http_foundation import parse_json_response  # noqa: E402


@pytest.mark.parametrize(
    ("position", "goal", "expected"),
    [(1, 4, "right"), (4, 1, "left"), (2, 2, "wait")],
)
def test_decision(position: int, goal: int, expected: str) -> None:
    assert choose_action(position, goal) == expected


@pytest.mark.parametrize(
    "state",
    [
        {"position": 1},
        {"position": -1, "goal": 2},
        {"position": 1, "goal": 99},
        {"position": True, "goal": 2},
        {"position": "1", "goal": 2},
    ],
)
def test_adapter_rejects_invalid_state(state: dict) -> None:
    with pytest.raises(ValueError):
        course_local_action(state)


def test_course_local_format_is_explicit() -> None:
    response = course_local_action({"position": 1, "goal": 4})
    assert response["action"] == "right"
    assert response["production_compatibility"] == "NOT VUACOC PRODUCTION FORMAT"


@pytest.mark.parametrize(
    ("status", "body"),
    [
        (404, b'{"error":"not found"}'),
        (200, b"not-json"),
        (200, b"[]"),
        (200, b"\xff"),
    ],
)
def test_http_rejects_status_or_body(status: int, body: bytes) -> None:
    with pytest.raises(ValueError):
        parse_json_response(status, body)


def test_http_accepts_valid_json_dict() -> None:
    assert parse_json_response(200, b'{"lesson":13}') == {"lesson": 13}


def test_cli_exit_code_and_json() -> None:
    cmd = [sys.executable, str(WEEK_ROOT / "cli.py")]
    valid = subprocess.run(
        [*cmd, "--position", "1", "--goal", "4"],
        capture_output=True, text=True, check=False, timeout=10
    )
    assert valid.returncode == 0
    assert json.loads(valid.stdout)["action"] == "right"
    invalid = subprocess.run(
        [*cmd, "--position", "9", "--goal", "4"],
        capture_output=True, text=True, check=False, timeout=10
    )
    assert invalid.returncode == 2
    assert "Traceback" not in invalid.stderr
