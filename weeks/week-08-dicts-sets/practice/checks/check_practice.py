"""Week 08 self-check: call learner functions, not only their printed demos.

--starter checks the student's TODO functions (initial FAIL by design).
--solutions checks the separate references for maintainer CI.
Uses Python standard library only: no pytest installation for students.
"""

from __future__ import annotations

import argparse
import importlib.util
import io
from contextlib import redirect_stdout
from pathlib import Path
from types import ModuleType
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]


def load(folder: str, filename: str) -> ModuleType:
    """Import the module without executing interactive demo output."""
    path = ROOT / folder / filename
    spec = importlib.util.spec_from_file_location(f"week08_{folder}_{path.stem}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Không thể import {path}")
    module = importlib.util.module_from_spec(spec)
    output = io.StringIO()
    with redirect_stdout(output):
        spec.loader.exec_module(module)
    assert output.getvalue() == "", "Import phải không in demo; dùng main guard"
    return module


def call(fn: Callable[..., Any], *args: object) -> Any:
    """Enforce return-value semantics, not print-only fake results."""
    output = io.StringIO()
    with redirect_stdout(output):
        result = fn(*args)
    assert output.getvalue() == "", "Hàm xử lý phải return, không print"
    return result


def expect_value_error(fn: Callable[..., Any], *args: object) -> None:
    try:
        call(fn, *args)
    except ValueError:
        return
    raise AssertionError(f"Cần ValueError với input {args!r}")


def lab01(folder: str) -> None:
    m = load(folder, "lab01_dict_frequency.py")
    assert call(m.count_words, "Python python  dict") == {"python": 2, "dict": 1}
    assert call(m.count_words, "   ") == {}
    assert call(m.count_words, "Set dict set") == {"set": 2, "dict": 1}
    original = {"dict": 7}
    updated = call(m.update_score, original, "dict", 9)
    assert updated == {"dict": 9}
    assert original == {"dict": 7}, "Không được sửa dict của caller"
    assert updated is not original, "Phải trả bản sao, không trả dict đầu vào"
    assert call(m.update_score, original, "set", 0) == {"dict": 7, "set": 0}
    for score in (-1, 11, True):
        expect_value_error(m.update_score, original, "dict", score)
    assert original == {"dict": 7}


def lab02(folder: str) -> None:
    m = load(folder, "lab02_nested_learner.py")
    learner: dict[str, object] = {
        "name": "An",
        "scores": [8, 9, 7],
        "progress": {"week": 8},
    }
    assert call(m.summarize_learner, learner) == "An: trung bình 8.0, tuần 8"
    assert learner == {"name": "An", "scores": [8, 9, 7], "progress": {"week": 8}}, (
        "Không sửa nested dữ liệu của caller"
    )
    assert call(m.summarize_learner, {"name": "An", "scores": [8, 9, 7]}) == (
        "An: trung bình 8.0, tuần chưa rõ"
    )
    assert call(m.summarize_learner, {"name": "Bình", "scores": [10], "progress": {}}) == (
        "Bình: trung bình 10.0, tuần chưa rõ"
    )
    for invalid in (
        {},
        {"name": "An"},
        {"name": "", "scores": [8]},
        {"name": "An", "scores": []},
        {"name": "An", "scores": [True, 8]},
        {"name": "An", "scores": [12]},
        {"name": "An", "scores": [8], "progress": "week08"},
        {"name": "An", "scores": [8], "progress": {"week": 0}},
        {"name": "An", "scores": [8], "progress": {"week": True}},
    ):
        assert call(m.summarize_learner, invalid) == "Dữ liệu không hợp lệ", invalid


def lab03(folder: str) -> None:
    m = load(folder, "lab03_set_skills.py")
    a = {"dict", "set"}
    b = {"set", "loop"}
    expected = {
        "common": {"set"},
        "only_first": {"dict"},
        "only_second": {"loop"},
        "all": {"dict", "set", "loop"},
    }
    actual = call(m.compare_skills, a, b)
    assert actual == expected
    assert all(type(value) is set for value in actual.values()), "Kết quả phải là set"
    assert a == {"dict", "set"} and b == {"set", "loop"}
    assert call(m.compare_skills, set(), set()) == {
        "common": set(),
        "only_first": set(),
        "only_second": set(),
        "all": set(),
    }
    tags = ["python", "git", "python", "dict", "git"]
    assert call(m.unique_in_order, tags) == ["python", "git", "dict"]
    assert tags == ["python", "git", "python", "dict", "git"], "Không sửa list nguồn"
    assert call(m.unique_in_order, []) == []
    assert call(m.unique_in_order, ["a", "a", "b", "a"]) == ["a", "b"]


def lab04(folder: str) -> None:
    m = load(folder, "lab04_state_decision.py")
    valid = (
        ({"position": 1, "goal": 4, "opponent_position": 3}, "right"),
        ({"position": 4, "goal": 4}, "wait"),
        ({"position": 3, "goal": 0}, "left"),
        ({"position": 2, "goal": 4, "opponent_position": 3}, "wait"),
        ({"position": 0, "goal": 4}, "right"),
    )
    assert m.ACTIONS == {"left", "right", "wait"}
    for state, expected in valid:
        before = state.copy()
        assert call(m.validate_state, state) is True
        first = call(m.choose_action, state)
        assert first == expected, (state, first)
        assert first in m.ACTIONS
        assert call(m.choose_action, state) == first, "Heuristic phải deterministic"
        assert call(m.explain_decision, state) == (
            f"position={state['position']}, goal={state['goal']}, action={expected}"
        )
        assert state == before, "Heuristic không sửa state đầu vào"

    invalid = (
        {},
        {"goal": 4},
        {"position": -1, "goal": 4},
        {"position": 5, "goal": 4},
        {"position": 1, "goal": True},
        {"position": "1", "goal": 4},
        {"position": 1, "goal": 4, "opponent_position": "3"},
    )
    for state in invalid:
        assert call(m.validate_state, state) is False
        assert call(m.choose_action, state) == "wait", "Invalid state cần fallback legal"
        assert call(m.explain_decision, state) == "State không hợp lệ", (
            "Không báo invalid là một quyết định bình thường"
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Week08 direct-call self-check (offline)")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--starter", action="store_true", help="Chấm trực tiếp hàm sinh viên")
    mode.add_argument("--solutions", action="store_true", help="Kiểm reference riêng")
    args = parser.parse_args(argv)
    folder = "starter" if args.starter else "solutions"
    passed = 0
    for number, check in enumerate((lab01, lab02, lab03, lab04), start=1):
        try:
            check(folder)
        except Exception as error:  # One failed lab must not block diagnosis of others.
            print(f"Lab {number:02d}: FAIL — {type(error).__name__}: {error}")
        else:
            passed += 1
            print(f"Lab {number:02d}: PASS")

    name = "student" if args.starter else "reference"
    if passed == 4:
        print(f"Week 08 {name} practice: PASS (4/4)")
        return 0
    print(f"Week 08 {name} practice: FAIL ({passed}/4)")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
