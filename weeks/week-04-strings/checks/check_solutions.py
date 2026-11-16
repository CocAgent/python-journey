"""Behavior checks for official Week 04 solutions."""

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
    indexing = load("ex01_indexing_sol.py")
    methods = load("ex02_methods_sol.py")
    formatting = load("ex03_fstrings_sol.py")
    regex = load("ex04_regex_mini_lab_sol.py")
    assert indexing.reverse_text("Python") == "nohtyP"
    assert indexing.is_palindrome("Never odd or even") is True
    assert methods.normalize_email(" User@Example.COM ") == "user@example.com"
    assert methods.supported_filename("lesson.py") is True
    assert formatting.student_summary("An", 20, 8.567).endswith("8.57")
    assert regex.extract_codes("PJ-101 X PJ-205") == ["PJ-101", "PJ-205"]
    assert regex.is_week_code("W04") is True
    assert regex.is_week_code("W4") is False
    print("Week 04 solution checks: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
