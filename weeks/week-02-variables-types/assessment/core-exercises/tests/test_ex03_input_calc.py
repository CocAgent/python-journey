"""Independent tests for original Week02 ex03 calculator, circle and discount."""
from __future__ import annotations

import sys
from pathlib import Path

CORE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CORE))

from autograde_w02 import (  # noqa: E402
    check_one,
    contains_all_numbers,
    load_test_cases,
    split_todos,
    test_suite_audit,
)

REFERENCE = CORE / "fixtures" / "reference" / "ex03_input_calc.py"
CRITERIA = ("W02.EX03.FOUR", "W02.EX03.CIRCLE", "W02.EX03.DISCOUNT")


def test_ex03_bank_covers_all_three_todos_with_six_inputs_each() -> None:
    audit = test_suite_audit()
    third = audit["tasks"][2]
    assert third["exercise"] == "ex03_input_calc.py"
    assert [case["id"] for case in third["criteria"]] == list(CRITERIA)
    assert sum(case["points"] for case in third["criteria"]) == 3.5
    assert [case["input_cases"] for case in third["criteria"]] == [6, 6, 6]
    assert all(len(load_test_cases()[name]) == 6 for name in CRITERIA)


def test_ex03_all_reference_todos_pass_full_bank() -> None:
    source = split_todos(REFERENCE.read_text(encoding="utf-8"))
    for cid, todo in zip(CRITERIA, (1, 2, 3)):
        fraction, reason, obs = check_one(cid, source[todo])
        assert fraction == 1, (cid, reason)
        assert len(obs) == 6


def test_ex03_order_matters_without_overfitting_formatting() -> None:
    assert contains_all_numbers("Tong: 10 Hieu 6 Tich 16 Thuong 4", [10, 6, 16, 4])
    assert not contains_all_numbers(
        "Tich 16 Tong 10 Hieu 6 Thuong 4", [10, 6, 16, 4]
    )
    code = (
        "a = float(input())\nb = float(input())\n"
        "print('Tích', a*b)\nprint('Tổng', a+b)\n"
        "print('Hiệu', a-b)\nprint('Thương', a/b)\n"
    )
    assert check_one("W02.EX03.FOUR", code)[0] == 0


def test_ex03_alternative_text_labels_work_for_four_operations() -> None:
    original = split_todos(REFERENCE.read_text(encoding="utf-8"))[1]
    changed = original.replace('print("Tổng:",', 'print("A+B =",')
    changed = changed.replace('print("Hiệu:",', 'print("A-B =",')
    fraction, reason, _ = check_one("W02.EX03.FOUR", changed)
    assert fraction == 1, reason


def test_ex03_hardcoded_discount_is_not_pass() -> None:
    code = (
        "price = float(input())\ndiscount = float(input())\n"
        "print('400000 175000 75000 90000 400 899.1')\n"
    )
    fraction, reason, _ = check_one("W02.EX03.DISCOUNT", code)
    assert fraction == 0
    assert "REVIEW" in reason or "Thiếu" in reason


def test_ex03_wrong_circle_calculation_fails_multi_case_check() -> None:
    code = (
        "radius = float(input())\n"
        "pi = 3.14159\n"
        "print('Dien tich', pi * radius)\n"
        "print('Chu vi', 2 * pi * radius)\n"
    )
    fraction, _reason, _ = check_one("W02.EX03.CIRCLE", code)
    assert fraction < 1
