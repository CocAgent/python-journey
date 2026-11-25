"""Independent tests for original Week02 ex02 conversion/BMI TODOs.

All execution below uses trusted source stored in fixtures/reference, never student work.
"""
from __future__ import annotations

import sys
from pathlib import Path

CORE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CORE))

import autograde_w02 as ag  # noqa: E402

REFERENCE = CORE / "fixtures" / "reference" / "ex02_type_conversion.py"
CRITERIA = (
    "W02.EX02.TEXT", "W02.EX02.PI", "W02.EX02.BOOL", "W02.EX02.BMI",
)


def test_ex02_bank_covers_all_four_todos_and_six_bmi_inputs() -> None:
    audit = ag.test_suite_audit()
    second = audit["tasks"][1]
    assert second["exercise"] == "ex02_type_conversion.py"
    assert [x["id"] for x in second["criteria"]] == list(CRITERIA)
    assert sum(x["points"] for x in second["criteria"]) == 3.5
    assert [x["input_cases"] for x in second["criteria"]] == [0, 0, 0, 6]
    assert len(ag.load_test_cases()["W02.EX02.BMI"]) == 6


def test_ex02_four_reference_todos_pass_all_cases() -> None:
    source = ag.split_todos(REFERENCE.read_text(encoding="utf-8"))
    for cid, todo in zip(CRITERIA, (1, 2, 3, 4)):
        fraction, reason, obs = ag.check_one(cid, source[todo])
        assert fraction == 1, (cid, reason)
        if cid == "W02.EX02.BMI":
            assert len(obs) == 6
            assert all(x["ok"] for x in obs)


def test_ex02_bmi_accepts_alternate_output_label_and_number_format() -> None:
    code = (
        "h = float(input())\n"
        "w = float(input())\n"
        "bmi = w / (h ** 2)\n"
        "print('Kết quả:', format(bmi, '.1f'))\n"
    )
    fraction, reason, _ = ag.check_one("W02.EX02.BMI", code)
    assert fraction == 1, reason


def test_ex02_bmi_constant_25_is_not_full_credit() -> None:
    code = "h = float(input())\nw = float(input())\nprint(25.0)\n"
    fraction, _reason, _ = ag.check_one("W02.EX02.BMI", code)
    assert fraction == 0


def test_ex02_wrong_conversions_and_bool_order_fail() -> None:
    assert ag.check_one("W02.EX02.TEXT", 'so_text = "42"\nprint(50)\n')[0] == 0
    assert ag.check_one("W02.EX02.PI", "pi = 3.14159\nprint(3)\n")[0] == 0
    original = ag.split_todos(REFERENCE.read_text(encoding="utf-8"))[3]
    wrong = original.replace("print(bool(1))", "print(bool(0))", 1)
    assert ag.check_one("W02.EX02.BOOL", wrong)[0] == 0
