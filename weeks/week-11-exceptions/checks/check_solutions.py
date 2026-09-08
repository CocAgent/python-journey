"""Behavior checks for official Week 11 solutions."""

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
    parsing = load("ex01_try_except_sol.py")
    validation = load("ex02_multiple_sol.py")
    debugging = load("ex03_custom_sol.py")
    cleanup = load("ex04_else_finally_sol.py")
    assert parsing.safe_int("42") == 42
    assert parsing.safe_int("bad") is None
    assert validation.validate_action("wait") == "wait"
    try:
        validation.validate_action("teleport")
    except ValueError as error:
        assert "teleport" in str(error)
    else:
        raise AssertionError("illegal action was accepted")
    assert debugging.distance(1, 4) == 3
    audit_log: list[str] = []
    assert cleanup.parse_score("8", audit_log) == 8
    assert cleanup.parse_score("bad", audit_log) is None
    assert cleanup.parse_score("11", audit_log) is None
    assert audit_log == ["parsed='8'", "parsed='bad'", "parsed='11'"]
    print("Week 11 solution checks: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
