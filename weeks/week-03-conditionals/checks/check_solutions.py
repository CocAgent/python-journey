"""Behavior checks for official Week 03 solutions."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

SOLUTIONS = Path(__file__).resolve().parents[1] / "solutions"


def load(name: str):
    path = SOLUTIONS / name
    spec = spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    basic = load("ex01_if_else_sol.py")
    logic = load("ex02_logical_sol.py")
    guarded = load("ex03_nested_sol.py")
    assert basic.age_group(12) == "Thiếu nhi"
    assert basic.classify_score(11) == "Không hợp lệ"
    assert basic.is_leap_year(2000) is True
    assert basic.is_leap_year(1900) is False
    assert logic.can_drive(18, True, True) is True
    assert logic.triangle_type(1, 2, 9) == "Không hợp lệ"
    assert logic.fizzbuzz(15) == "FizzBuzz"
    assert guarded.withdraw_decision(100_000, -1) == "Số tiền không hợp lệ"
    assert guarded.ticket_price("vip", True, 20) == 124_800
    print("Week 03 solution checks: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
