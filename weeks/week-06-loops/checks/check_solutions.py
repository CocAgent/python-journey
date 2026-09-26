"""Behavior checks for official Week 06 solutions."""

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
    for_loops = load("ex01_for_loop_sol.py")
    while_loops = load("ex02_while_loop_sol.py")
    comprehensions = load("ex03_patterns_sol.py")
    assert for_loops.numbered_pairs(["A", "B"], [7, 9]) == [
        "1. A: 7",
        "2. B: 9",
    ]
    assert len(for_loops.multiplication_table(3)) == 10
    assert while_loops.countdown(3) == [3, 2, 1]
    assert while_loops.selected_numbers() == [1, 2, 4, 5, 7, 8]
    assert comprehensions.squares([1, 2, 3]) == [1, 4, 9]
    assert comprehensions.even_numbers([1, 2, 3, 4]) == [2, 4]
    print("Week 06 solution checks: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
