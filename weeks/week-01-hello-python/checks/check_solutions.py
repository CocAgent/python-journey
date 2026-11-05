"""Behavior checks for official Week 01 solutions."""

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
    hello = load("ex01_hello_sol.py")
    calculator = load("ex02_calculator_sol.py")
    conversation = load("ex03_input_sol.py")

    assert hello.greeting("An") == "Hello, An!"
    assert hello.favourite_lines(["phở"]) == ["Tôi thích phở"]
    assert hello.rectangle(5, 4) == ["*****", "*   *", "*   *", "*****"]

    assert calculator.remaining_balance(150_000, 35_000, 3) == 45_000
    assert round(calculator.circle_area(7), 2) == 153.94
    assert calculator.share_candy(100, 7) == (14, 2)
    assert calculator.celsius_to_fahrenheit(37) == 98.6

    assert conversation.birth_year(2026, 18) == 2008
    assert conversation.total_of(2, 3) == 5
    assert conversation.mad_lib("An", "vui", "mèo", "3")[0] == "An có một con mèo rất vui."

    print("Week 01 solution checks: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
