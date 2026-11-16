"""Week 13 reference checks: standard library, offline and independent of learner TODO."""

import json
import subprocess
import sys
from pathlib import Path
from urllib.request import Request

WEEK_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = WEEK_ROOT.parents[1]
# Infrastructure entry point may bootstrap import path. Core/adapter must not.
if str(WEEK_ROOT) not in sys.path:
    sys.path.insert(0, str(WEEK_ROOT))

from bot_course.adapter import course_local_action, validate_state  # noqa: E402
from bot_course.core import choose_action  # noqa: E402
from bot_course.http_foundation import (  # noqa: E402
    build_get_request,
    parse_json_response,
)
from cli import parse_args  # noqa: E402


def must_fail(fn, error_type: type[Exception] = ValueError) -> None:
    """Make expected failures observable, never hide unexpected exceptions."""
    try:
        fn()
    except error_type:
        return
    raise AssertionError(f"Expected {error_type.__name__}, but call succeeded")


def run(argv: list[str], *, cwd: Path = WEEK_ROOT) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *argv],
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
        timeout=15,
    )


def check_core_and_adapter() -> None:
    assert choose_action(1, 4) == "right"
    assert choose_action(4, 1) == "left"
    assert choose_action(3, 3) == "wait"

    assert validate_state({"position": 0, "goal": 4}) == (0, 4)
    assert course_local_action({"position": 1, "goal": 4})["action"] == "right"
    assert course_local_action({"position": 4, "goal": 1})["action"] == "left"
    output = course_local_action({"position": 2, "goal": 2})
    assert output["action"] == "wait"
    assert output["production_compatibility"] == "NOT VUACOC PRODUCTION FORMAT"

    must_fail(lambda: course_local_action({"position": 1}))
    must_fail(lambda: course_local_action({"position": 5, "goal": 4}))
    must_fail(lambda: course_local_action({"position": True, "goal": 4}))
    must_fail(lambda: course_local_action({"position": "1", "goal": 4}))
    must_fail(lambda: course_local_action({"position": 1, "goal": -1}))


def check_cli() -> None:
    args = parse_args(["--position", "1", "--goal", "4"])
    assert (args.position, args.goal) == (1, 4)

    ok = run([str(WEEK_ROOT / "cli.py"), "--position", "1", "--goal", "4"], cwd=REPO_ROOT)
    assert ok.returncode == 0, ok.stderr
    assert json.loads(ok.stdout)["action"] == "right"

    bad = run([str(WEEK_ROOT / "cli.py"), "--position", "99", "--goal", "4"], cwd=REPO_ROOT)
    assert bad.returncode == 2, bad.stderr
    assert "Lỗi dữ liệu" in bad.stderr
    assert "Traceback" not in bad.stderr

    wrong_type = run([str(WEEK_ROOT / "cli.py"), "--position", "x", "--goal", "4"], cwd=REPO_ROOT)
    assert wrong_type.returncode == 2
    assert "invalid int value" in wrong_type.stderr

    help_result = run([str(WEEK_ROOT / "cli.py"), "--help"], cwd=REPO_ROOT)
    assert help_result.returncode == 0
    assert "--position" in help_result.stdout


def check_http() -> None:
    request = build_get_request("https://example.invalid/course")
    assert isinstance(request, Request)
    assert request.get_method() == "GET"
    assert parse_json_response(200, b'{"ok": true}') == {"ok": True}
    assert parse_json_response(204, b"{}") == {}
    must_fail(lambda: build_get_request("http://example.invalid"))
    must_fail(lambda: parse_json_response(503, b"{}"))
    must_fail(lambda: parse_json_response(200, b"not-json"))
    must_fail(lambda: parse_json_response(200, b"[]"))
    must_fail(lambda: parse_json_response(200, b"\xff"))
    must_fail(lambda: parse_json_response(200, "wrong-type"))
    must_fail(lambda: parse_json_response(True, b"{}"))


def check_examples_and_solutions() -> None:
    cases = (
        (["-m", "examples.ex01_modules"], "Đi từ 1 đến 4: right"),
        (["-m", "examples.ex02_cli", "--position", "1", "--goal", "4"], '"action": "right"'),
        (["-m", "examples.offline_http"], "network_used"),
        (["-m", "examples.ex04_adapter"], "Case sai:"),
        (["-m", "solutions.ex01_modules"], "Hành động: right"),
        (["-m", "solutions.ex02_cli", "--turn", "3"], "Lượt: 3"),
        (["-m", "solutions.ex03_http"], "Lesson: 13"),
        (["-m", "solutions.ex04_adapter"], "Hành động: left"),
    )
    for argv, expected in cases:
        result = run(list(argv))
        assert result.returncode == 0, f"{argv}: {result.stderr}"
        assert expected in result.stdout, f"{argv}: {result.stdout}"

    # An imported demo must not execute main() as a side effect.
    imported = run(["-c", "import examples.ex01_modules; import solutions.ex01_modules"])
    assert imported.returncode == 0, imported.stderr
    assert imported.stdout == ""

    invalid = run(["-m", "solutions.ex02_cli", "--turn", "abc"])
    assert invalid.returncode == 2

    invalid_negative = run(["-m", "solutions.ex02_cli", "--turn", "-1"])
    assert invalid_negative.returncode == 2


def main() -> None:
    check_core_and_adapter()
    check_cli()
    check_http()
    check_examples_and_solutions()
    print("Week 13 solution checks: PASS")


if __name__ == "__main__":
    main()
