"""Behavior checks for official Week 05 solutions."""

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
    lists = load("ex01_lists_sol.py")
    copies = load("ex02_slicing_sol.py")
    tuples = load("ex03_tuples_sol.py")
    source = ["A", "B"]
    assert lists.add_subject(source, "C") == ["A", "B", "C"]
    assert source == ["A", "B"]
    original, alias, copied = copies.alias_and_copy([1, 2])
    assert original == alias == [1, 2, 3]
    assert copied == [1, 2]
    assert tuples.unpack_point((3, 7)) == "x=3, y=7"
    assert tuples.swap("A", "B") == ("B", "A")
    print("Week 05 solution checks: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
