"""Behavioral checks for the official Week 07 solutions."""

from importlib.util import module_from_spec, spec_from_file_location
from math import isclose, pi
from pathlib import Path
from types import ModuleType

SOLUTIONS_DIR = Path(__file__).resolve().parents[1] / "solutions"


def load_solution(filename: str) -> ModuleType:
    """Load one solution module directly from its file path."""
    path = SOLUTIONS_DIR / filename
    spec = spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Không thể load solution: {path}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_equal(label: str, actual: object, expected: object) -> None:
    """Raise a focused failure when two values differ."""
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def check_exercise_01() -> None:
    """Check return values and a basic boundary case."""
    solution = load_solution("ex01_basic_func_sol.py")
    check_equal("chao", solution.chao("An"), "Xin chào An!")
    check_equal("la_so_chan even", solution.la_so_chan(4), True)
    check_equal("la_so_chan odd", solution.la_so_chan(5), False)
    area = solution.tinh_dien_tich_hinh_tron(0)
    if not isclose(area, pi * 0**2):
        raise AssertionError("diện tích với bán kính 0 không đúng")


def check_exercise_02() -> None:
    """Check defaults, boundary behavior and composed calculation."""
    solution = load_solution("ex02_params_sol.py")
    check_equal("default parameter", solution.gioi_thieu("An"), "Tôi là An, 18 tuổi.")
    check_equal("zero quantity", solution.tinh_tam_tinh(10, 0), 0.0)
    check_equal("discount", solution.ap_dung_giam_gia(100_000, 10), 90_000)
    check_equal("composed invoice", solution.tao_hoa_don(25_000, 2, 10), "Tổng: 45,000 đ")


def check_exercise_03() -> None:
    """Check that caller-owned state is handled through parameters."""
    solution = load_solution("ex03_scope_sol.py")
    notes: list[str] = []
    check_equal("reject blank note", solution.them_ghi_chu(notes, "   "), False)
    check_equal("add note", solution.them_ghi_chu(notes, " Học return "), True)
    check_equal("caller list changed", notes, ["Học return"])
    check_equal("find note", solution.tim_ghi_chu(notes, "RETURN"), ["Học return"])
    check_equal("count note", solution.dem_ghi_chu(notes), 1)


def check_exercise_04() -> None:
    """Check the deterministic teaching policy and allowed outputs."""
    solution = load_solution("ex04_decision_function_sol.py")
    expected = {
        "danger": "defend",
        "opportunity": "advance",
        "neutral": "wait",
        "": "wait",
    }
    allowed_actions = {"defend", "advance", "wait"}
    for state, action in expected.items():
        first = solution.choose_action(state)
        second = solution.choose_action(state)
        check_equal(f"decision for {state!r}", first, action)
        check_equal(f"determinism for {state!r}", second, first)
        if first not in allowed_actions:
            raise AssertionError(f"action ngoài teaching set: {first!r}")


def main() -> int:
    """Run all solution checks and return a process exit code."""
    checks = (
        check_exercise_01,
        check_exercise_02,
        check_exercise_03,
        check_exercise_04,
    )
    try:
        for check in checks:
            check()
    except (AssertionError, AttributeError, FileNotFoundError, RuntimeError) as error:
        print(f"Week 07 solution checks: FAIL — {error}")
        return 1

    print("Week 07 solution checks: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
