"""Independent tests for all original Week02 ex01 mandatory TODOs.

Fixtures are trusted maintainer code; NEVER execute downloaded student submissions in CI.
"""
from __future__ import annotations

import sys
from pathlib import Path

CORE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CORE))

from autograde_w02 import (  # noqa: E402
    check_one,
    grade,
    load_test_cases,
    split_todos,
    test_suite_audit,
)

REFERENCE = CORE / "fixtures" / "reference" / "ex01_variables.py"
CRITERIA = ("W02.EX01.PROFILE", "W02.EX01.SWAP", "W02.EX01.AUG")


def test_ex01_bank_covers_all_three_todos_without_stdin() -> None:
    audit = test_suite_audit()
    assert audit["criteria_count"] == 10
    assert audit["exercises_count"] == 3
    assert audit["dynamic_case_count"] == 24
    first = audit["tasks"][0]
    assert first["exercise"] == "ex01_variables.py"
    assert [case["id"] for case in first["criteria"]] == list(CRITERIA)
    assert sum(case["points"] for case in first["criteria"]) == 3
    assert all(case["input_cases"] == 0 for case in first["criteria"])
    assert all(name not in load_test_cases() for name in CRITERIA)


def test_ex01_all_reference_todos_pass_individually() -> None:
    source = split_todos(REFERENCE.read_text(encoding="utf-8"))
    for cid, todo in zip(CRITERIA, (1, 2, 3)):
        fraction, reason, _observations = check_one(cid, source[todo])
        assert fraction == 1, (cid, reason)
    result = grade(REFERENCE.parent, "reference")
    assert sum(c["earned"] for c in result["tasks"][0]["criteria"]) == 3


def test_ex01_wrong_profile_variable_type_is_rejected() -> None:
    code = (
        "ten = 123\n"
        "tuoi = 18\n"
        "diem_tb = 8.5\n"
        "dang_hoc = True\n"
        "for var in [ten, tuoi, diem_tb, dang_hoc]:\n"
        "    print(var, type(var))\n"
    )
    fraction, _reason, _observations = check_one("W02.EX01.PROFILE", code)
    assert fraction == 0


def test_ex01_swap_with_forbidden_temporary_variable_is_not_pass() -> None:
    code = "a = 10\nb = 20\ntam = a\na = b\nb = tam\nprint(a, b)\n"
    fraction, _reason, _observations = check_one("W02.EX01.SWAP", code)
    assert fraction == 0


def test_ex01_augmentation_without_all_four_operators_fails() -> None:
    code = "x = 100\nx += 1\nprint(x)\nx -= 1\nprint(x)\n"
    fraction, _reason, _observations = check_one("W02.EX01.AUG", code)
    assert fraction == 0


def test_ex01_blank_and_syntax_errors_do_not_pass() -> None:
    assert check_one("W02.EX01.PROFILE", "# chưa làm\n")[0] == 0
    fraction, reason, _ = check_one("W02.EX01.AUG", "x = (\n")
    assert fraction == 0
    assert "SyntaxError" in reason
