"""Behavior checks for official Week 02 solutions."""

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
    variables = load("ex01_variables_sol.py")
    conversion = load("ex02_type_conversion_sol.py")
    calculator = load("ex03_input_calc_sol.py")
    assert variables.build_profile("An", 18, 8.5, True)["age"] == 18
    assert conversion.parse_whole_number("42") == 42
    assert conversion.calculate_bmi(70, 1.75) == 22.9
    assert calculator.calculate_total(2, 3) == 5
    assert calculator.discounted_price(500_000, 20) == 400_000
    assert calculator.vnd_to_usd(250_000, 25_000) == 10
    print("Week 02 solution checks: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
