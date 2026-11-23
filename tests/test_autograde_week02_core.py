"""Week 02 autograder: only trusted fixtures run in these CI tests."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "weeks/week-02-variables-types/assessment/core-exercises"
sys.path.insert(0, str(CHECKER))

from autograde_w02 import (  # noqa: E402
    ROOT as GRADER_ROOT,
    RUBRIC,
    check_one,
    grade,
    main,
    split_todos,
)

REFERENCE = CHECKER / "fixtures/reference"


def test_golden_fixtures_full_score() -> None:
    result = grade(REFERENCE, "reference")
    assert result["auto_score"] == 10
    assert result["auto_max_points"] == 10
    assert result["official_score"] is None
    assert [len(item["criteria"]) for item in result["tasks"]] == [3, 4, 3]
    assert all(
        c["passed"] for task in result["tasks"] for c in task["criteria"]
    )


def test_blank_starters_score_zero(tmp_path: Path) -> None:
    for filename, headings in (
        ("ex01_variables.py", [1, 2, 3, 4]),
        ("ex02_type_conversion.py", [1, 2, 3, 4, 5]),
        ("ex03_input_calc.py", [1, 2, 3, 4]),
    ):
        source = "\n".join(f"# TODO {n}: chưa làm" for n in headings)
        (tmp_path / filename).write_text(source, encoding="utf-8")
    result = grade(tmp_path, "student")
    assert result["auto_score"] == 0
    assert all(
        not c["passed"] for task in result["tasks"] for c in task["criteria"]
    )


def test_optional_tasks_are_not_executed_or_scored(tmp_path: Path) -> None:
    for path in REFERENCE.glob("*.py"):
        source = path.read_text(encoding="utf-8")
        # Optional code must never run; it is outside mandatory TODO sections.
        source += "\nraise RuntimeError('optional part must not be executed')\n"
        (tmp_path / path.name).write_text(source, encoding="utf-8")
    result = grade(tmp_path, "student")
    assert result["auto_score"] == 10
    assert len(result["optional_excluded"]) == 4


def test_constant_answer_fails_second_discount_case(tmp_path: Path) -> None:
    for path in REFERENCE.glob("*.py"):
        (tmp_path / path.name).write_text(
            path.read_text(encoding="utf-8"), encoding="utf-8"
        )
    target = tmp_path / "ex03_input_calc.py"
    code = target.read_text(encoding="utf-8")
    code = code.replace(
        'print(f"Giá sau giảm: {gia_goc * (1 - phan_tram_giam / 100):.2f}")',
        'print("Giá sau giảm: 400000")',
    )
    target.write_text(code, encoding="utf-8")
    result = grade(tmp_path, "student")
    last = result["tasks"][-1]["criteria"][-1]
    assert last["id"] == "W02.EX03.DISCOUNT"
    assert last["earned"] == 0.5
    assert result["auto_score"] == 9.5


def test_syntax_error_treated_as_retry() -> None:
    fraction, reason, _ = check_one("W02.EX01.SWAP", "a = (\n")
    assert fraction == 0
    assert "SyntaxError" in reason


def test_no_output_is_not_false_pass() -> None:
    fraction, _, _ = check_one("W02.EX02.TEXT", 'so_text = "42"\n')
    assert fraction == 0


def test_splitting_uses_existing_todo_markers() -> None:
    text = (
        "# TODO 1: bắt buộc\nx = 100\n"
        "# TODO 2: bắt buộc\nprint(2)\n"
        "# TODO 3 (Thử thách): tự chọn\nraise Exception()\n"
    )
    sections = split_todos(text)
    assert sorted(sections) == [1, 2, 3]
    assert "raise Exception()" not in sections[1]


def test_rubric_tracks_exact_original_todos() -> None:
    rubric = json.loads(RUBRIC.read_text(encoding="utf-8"))
    assert GRADER_ROOT == CHECKER
    assert [item["file"] for item in rubric["tasks"]] == [
        "ex01_variables.py",
        "ex02_type_conversion.py",
        "ex03_input_calc.py",
    ]
    assert [
        [criterion["source_todo"] for criterion in task["criteria"]]
        for task in rubric["tasks"]
    ] == [[1, 2, 3], [1, 2, 3, 4], [1, 2, 3]]
    assert sum(
        criterion["points"] for task in rubric["tasks"]
        for criterion in task["criteria"]
    ) == 10


def test_cli_reference_output_json(tmp_path: Path) -> None:
    target = tmp_path / "week02.json"
    assert main(["--reference", "--json-out", str(target)]) == 0
    report = json.loads(target.read_text(encoding="utf-8"))
    assert report["mode"] == "reference"
    assert report["auto_score"] == 10
    assert report["official_score"] is None
    assert report["rubric_sha256"]


def test_missing_exercise_is_zero_without_crash(tmp_path: Path) -> None:
    result = grade(tmp_path, "student")
    assert result["auto_score"] == 0


def test_reference_is_not_the_student_folder() -> None:
    rubric = json.loads(RUBRIC.read_text(encoding="utf-8"))
    assert rubric["source"] == "weeks/week-02-variables-types/exercises/"
    assert REFERENCE != ROOT / "weeks/week-02-variables-types/exercises"


def test_no_unapproved_practice_or_miniproject_paths() -> None:
    rubric = json.loads(RUBRIC.read_text(encoding="utf-8"))
    assert all(
        "/" not in task["file"]
        and task["file"].startswith("ex0")
        for task in rubric["tasks"]
    )
    assert all(
        "mini-project" not in criterion["id"]
        for task in rubric["tasks"]
        for criterion in task["criteria"]
    )
