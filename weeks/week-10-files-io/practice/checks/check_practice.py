"""Week 10 beginner self-check, direct function calls and isolated temp files.

--starter runs the student's code, intentionally FAIL until TODOs are solved.
--solutions verifies references. No live network, pytest, or persistent files.
"""

from __future__ import annotations

import argparse
import importlib.util
import io
import json
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from types import ModuleType


BASE = Path(__file__).resolve().parents[1]


def load(folder: str, filename: str) -> ModuleType:
    path = BASE / folder / filename
    spec = importlib.util.spec_from_file_location(f"week10_{folder}_{path.stem}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    output = io.StringIO()
    with redirect_stdout(output):
        spec.loader.exec_module(module)
    assert not output.getvalue(), "Import module không được tự chạy demo"
    return module


def must_raise(exception: type[Exception], function, *args) -> None:
    try:
        function(*args)
    except exception:
        return
    raise AssertionError(f"Expected {exception.__name__}: {args!r}")


def check_text(folder: str) -> None:
    m = load(folder, "lab01_text_notes.py")
    with TemporaryDirectory() as directory:
        root = Path(directory)
        path = root / "notes" / "session.txt"
        must_raise(FileNotFoundError, m.load_notes, path)
        assert m.save_notes(path, ["Chào", "Tạm biệt"]) == path
        assert path.read_text(encoding="utf-8") == "Chào\nTạm biệt\n"
        assert m.load_notes(path) == ["Chào", "Tạm biệt"]
        assert m.save_notes(path, []) == path
        assert m.load_notes(path) == []
        assert path.read_text(encoding="utf-8") == ""
        second = root / "nested" / "data.txt"
        assert m.save_notes(second, ["Một"]) == second
        assert m.load_notes(second) == ["Một"]


def check_csv(folder: str) -> None:
    m = load(folder, "lab02_csv_scores.py")
    with TemporaryDirectory() as directory:
        root = Path(directory)
        path = root / "tables" / "scores.csv"
        must_raise(FileNotFoundError, m.load_scores, path)
        rows = [{"name": "An", "score": 8}, {"name": "Bình", "score": 9}]
        assert m.save_scores(path, rows) == path
        assert m.load_scores(path) == rows, "CSV load phải chuyển score về int"
        raw = path.read_text(encoding="utf-8")
        assert raw.startswith("name,score"), "CSV cần header đúng thứ tự"
        assert m.save_scores(path, []) == path
        assert m.load_scores(path) == []
        for invalid in (
            [{"name": "", "score": 8}],
            [{"name": "An", "score": True}],
            [{"name": "An", "score": 11}],
        ):
            must_raise(ValueError, m.save_scores, path, invalid)
        # Invalid writes should not overwrite an existing valid CSV.
        assert m.load_scores(path) == []
        for bad_content in (
            "name,score\nAn,wrong\n",
            "name,score\nAn,11\n",
            "name,score\nAn,\n",
            "score,name\n8,An\n",
            "name,score\nAn,8,extra\n",
        ):
            path.write_text(bad_content, encoding="utf-8")
            must_raise(ValueError, m.load_scores, path)


def check_json(folder: str) -> None:
    m = load(folder, "lab03_json_replay.py")
    assert m.FORMAT == "COURSE LOCAL FORMAT"
    assert m.COMPAT == "NOT VUACOC PRODUCTION FORMAT"
    payload = {
        "format": m.FORMAT,
        "production_compatibility": m.COMPAT,
        "turns": [{"turn": 1, "action": "wait"}],
    }
    assert m.validate_replay(payload) is True
    assert m.validate_replay({"format": m.FORMAT, "turns": []}) is False
    for bad in (
        [],
        {},
        {"format": m.FORMAT, "production_compatibility": m.COMPAT, "turns": {}},
        {**payload, "turns": [{"turn": True, "action": "wait"}]},
        {**payload, "turns": [{"turn": 0, "action": "wait"}]},
        {**payload, "turns": [{"turn": 1, "action": "teleport"}]},
    ):
        assert m.validate_replay(bad) is False
    with TemporaryDirectory() as directory:
        root = Path(directory)
        path = root / "replays" / "match.json"
        must_raise(FileNotFoundError, m.load_replay, path)
        assert m.save_replay(path, payload) == path
        assert m.load_replay(path) == payload
        assert json.loads(path.read_text(encoding="utf-8")) == payload
        must_raise(ValueError, m.save_replay, path, {"turns": []})
        assert m.load_replay(path) == payload, "Reject invalid before overwriting"
        path.write_text("{broken", encoding="utf-8")
        must_raise(json.JSONDecodeError, m.load_replay, path)
        path.write_text("[]", encoding="utf-8")
        must_raise(ValueError, m.load_replay, path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Week10 offline learner/reference checks")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--starter", action="store_true")
    group.add_argument("--solutions", action="store_true")
    args = parser.parse_args()
    folder = "starter" if args.starter else "solutions"
    passed = 0
    for number, check in enumerate((check_text, check_csv, check_json), 1):
        try:
            check(folder)
        except Exception as error:
            print(f"Lab {number:02d}: FAIL — {type(error).__name__}: {error}")
        else:
            passed += 1
            print(f"Lab {number:02d}: PASS")
    label = "student" if args.starter else "reference"
    print(f"Week 10 {label} practice: {'PASS' if passed == 3 else 'FAIL'} ({passed}/3)")
    return 0 if passed == 3 else 1


if __name__ == "__main__":
    raise SystemExit(main())
