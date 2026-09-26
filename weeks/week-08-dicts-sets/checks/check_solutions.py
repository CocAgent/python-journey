"""Behavioral checks for official Week 08 solutions."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import ModuleType

SOLUTIONS_DIR = Path(__file__).resolve().parents[1] / "solutions"


def load_solution(filename: str) -> ModuleType:
    """Load one solution directly from its file path."""
    path = SOLUTIONS_DIR / filename
    spec = spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Không thể load solution: {path}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_equal(label: str, actual: object, expected: object) -> None:
    """Raise a focused failure when values differ."""
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def check_dicts() -> None:
    """Check lookup, copied update, average and frequency behavior."""
    solution = load_solution("ex01_dicts_sol.py")
    original = {"Toán": 8.0, "Văn": 7.0}
    updated = solution.cap_nhat_diem(original, "Văn", 9.0)
    check_equal("updated score", updated["Văn"], 9.0)
    check_equal("original unchanged", original["Văn"], 7.0)
    check_equal("empty average", solution.diem_trung_binh({}), 0.0)
    check_equal("frequency", solution.dem_tan_suat("a b a"), {"a": 2, "b": 1})


def check_nested_data() -> None:
    """Check nested score and product models."""
    solution = load_solution("ex02_nested_dicts_sol.py")
    classroom = {
        "An": {"scores": [8, 9, 7]},
        "Bình": {"scores": [9, 9, 9]},
    }
    check_equal("best learner", solution.hoc_sinh_tot_nhat(classroom), "Bình")
    products = {
        "book": {"price": 20_000, "quantity": 2},
        "pen": {"price": 5_000, "quantity": 3},
    }
    check_equal("inventory value", solution.tong_gia_tri_kho(products), 55_000.0)


def check_sets() -> None:
    """Check set operations and order-preserving uniqueness."""
    solution = load_solution("ex03_sets_sol.py")
    analysis = solution.phan_tich_mon_hoc({"Toán", "Văn"}, {"Văn", "Anh"})
    check_equal("set common", analysis["common"], {"Văn"})
    check_equal("set all", analysis["all"], {"Toán", "Văn", "Anh"})
    words = ["dict", "set", "dict", "loop"]
    check_equal(
        "unique order",
        solution.loai_trung_giu_thu_tu(words),
        ["dict", "set", "loop"],
    )
    check_equal(
        "common words",
        solution.tu_chung("Học Python", "python tốt"),
        {"python"},
    )
    check_equal("anagram", solution.la_anagram("listen", "silent"), True)


def check_bot_heuristic() -> None:
    """Check deterministic legal actions for useful state cases."""
    solution = load_solution("ex04_bot_state_heuristic_sol.py")
    cases = (
        ({"position": 0, "opponent_position": 4, "goal": 4}, "right"),
        ({"position": 4, "opponent_position": 2, "goal": 4}, "wait"),
        ({"position": 3, "goal": 0}, "left"),
        ({}, "wait"),
    )
    for state, expected in cases:
        first = solution.choose_action(state)
        second = solution.choose_action(state)
        check_equal(f"action for {state}", first, expected)
        check_equal(f"determinism for {state}", second, first)
        if first not in solution.LOCAL_ACTIONS:
            raise AssertionError(f"action ngoài course-local set: {first!r}")


def main() -> int:
    """Run all checks and return a process exit code."""
    checks = (check_dicts, check_nested_data, check_sets, check_bot_heuristic)
    try:
        for check in checks:
            check()
    except (AssertionError, AttributeError, FileNotFoundError, RuntimeError) as error:
        print(f"Week 08 solution checks: FAIL — {error}")
        return 1

    print("Week 08 solution checks: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
