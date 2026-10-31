"""Direct-call checks for Week 11 exception and traceback labs.

Student TODOs initially fail; solution PASS is not learner completion.
No pytest, network or persistent files needed to run this checker.
"""

from __future__ import annotations

import argparse
import importlib.util
import io
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from types import ModuleType


BASE = Path(__file__).resolve().parents[1]


def load(folder: str, filename: str) -> ModuleType:
    path = BASE / folder / filename
    spec = importlib.util.spec_from_file_location(f"week11_{folder}_{path.stem}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    printed = io.StringIO()
    with redirect_stdout(printed):
        spec.loader.exec_module(module)
    assert not printed.getvalue(), "Import không được tự in demo"
    return module


def must_raise(expected: type[Exception], function, *args) -> Exception:
    try:
        function(*args)
    except expected as error:
        return error
    raise AssertionError(f"Expected {expected.__name__}: {args!r}")


def check_parse(folder: str) -> None:
    m = load(folder, "lab01_parse_number.py")
    assert m.safe_int("42") == 42
    assert m.safe_int(" -3 ") == -3
    assert m.safe_int("bad") is None
    assert m.safe_int("") is None
    # A programming/input-type bug should remain visible.
    must_raise(TypeError, m.safe_int, None)


def check_file(folder: str) -> None:
    m = load(folder, "lab02_read_score.py")
    with TemporaryDirectory() as directory:
        root = Path(directory)
        assert m.read_score(root / "missing.txt") is None
        path = root / "score.txt"
        for raw, expected in (("8", 8), (" 0 ", 0), ("10", 10),
                              ("eleven", None), ("11", None),
                              ("-1", None), ("", None)):
            path.write_text(raw, encoding="utf-8")
            assert m.read_score(path) == expected, (raw, expected)
        must_raise(AttributeError, m.read_score, "not-a-Path")


def check_action(folder: str) -> None:
    m = load(folder, "lab03_validate_action.py")
    assert m.ACTIONS == {"left", "right", "wait"}
    for action in ("left", "right", "wait"):
        assert m.validate_action(action) == action
    for action in ("teleport", "", 42, None):
        error = must_raise(ValueError, m.validate_action, action)
        assert repr(action) in str(error), "Error message phải chứa input sai"


def check_finally(folder: str) -> None:
    m = load(folder, "lab04_else_finally.py")
    events: list[str] = []
    assert m.valid_score("8", events) == 8
    assert events == ["converted", "attempt:'8'"], events
    assert m.valid_score("bad", events) is None
    assert events[-2:] == ["invalid", "attempt:'bad'"]
    assert m.valid_score("11", events) is None
    assert events[-2:] == ["converted", "attempt:'11'"]
    assert m.valid_score("0", events) == 0
    assert events[-2:] == ["converted", "attempt:'0'"]
    must_raise(TypeError, m.valid_score, None, events)
    assert events[-1] == "attempt:None", "finally chạy cả khi TypeError propagate"
    assert len(events) == 9, events


def main() -> int:
    parser = argparse.ArgumentParser(description="Week11 offline student/reference checks")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--starter", action="store_true")
    mode.add_argument("--solutions", action="store_true")
    args = parser.parse_args()
    folder = "starter" if args.starter else "solutions"
    passed = 0
    for number, check in enumerate(
        (check_parse, check_file, check_action, check_finally), start=1
    ):
        try:
            check(folder)
        except Exception as error:
            print(f"Lab {number:02d}: FAIL — {type(error).__name__}: {error}")
        else:
            passed += 1
            print(f"Lab {number:02d}: PASS")
    label = "student" if args.starter else "reference"
    print(f"Week 11 {label} practice: {'PASS' if passed == 4 else 'FAIL'} ({passed}/4)")
    return 0 if passed == 4 else 1


if __name__ == "__main__":
    raise SystemExit(main())
