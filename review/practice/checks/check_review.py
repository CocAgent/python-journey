"""Python Journey ôn tập Week 01–11: kiểm trực tiếp hàm người học.

Chạy từ repository root:
    python review/practice/checks/check_review.py --starter
    python review/practice/checks/check_review.py --solutions

--starter: bài chưa làm => FAIL có chủ đích; --solutions: chỉ kiểm reference.
Không cần pytest, mạng, tài khoản hay ghi dữ liệu bền vững.
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
from typing import Any, Callable

BASE = Path(__file__).resolve().parents[1]


def load(folder: str, name: str) -> ModuleType:
    path = BASE / folder / name
    spec = importlib.util.spec_from_file_location(f"review_{folder}_{path.stem}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Không import được {path}")
    module = importlib.util.module_from_spec(spec)
    printed = io.StringIO()
    with redirect_stdout(printed):
        spec.loader.exec_module(module)
    assert not printed.getvalue(), "Import module không được tự in demo"
    return module


def call(function: Callable[..., Any], *args: object) -> Any:
    output = io.StringIO()
    with redirect_stdout(output):
        result = function(*args)
    assert not output.getvalue(), "Hàm xử lý cần return, không print kết quả giả"
    return result


def must_raise(error_type: type[Exception], function: Callable[..., Any], *args: object) -> Exception:
    try:
        call(function, *args)
    except error_type as error:
        return error
    raise AssertionError(f"Cần {error_type.__name__} với input={args!r}")


def check_lab01(folder: str) -> None:
    m = load(folder, "lab01_gradebook.py")
    rows = [
        {"name": " An ", "score": 8},
        {"name": "Bình", "score": 4},
        {"name": "Chi", "score": 9},
    ]
    original = [row.copy() for row in rows]
    result = call(m.summarize_students, rows)
    assert result == {"count": 3, "average": 7.0, "passed": ["An", "Chi"]}
    assert rows == original, "Không sửa dữ liệu nguồn"
    assert call(m.summarize_students, []) == {
        "count": 0,
        "average": None,
        "passed": [],
    }
    assert call(m.summarize_students, [{"name": "Mít", "score": 5}]) == {
        "count": 1,
        "average": 5.0,
        "passed": ["Mít"],
    }
    invalid = (
        None,
        {},
        [{"name": "", "score": 8}],
        [{"name": "An"}],
        [{"name": "An", "score": True}],
        [{"name": "An", "score": -1}],
        [{"name": "An", "score": 11}],
        [{"name": "An", "score": 8}, {"name": " an ", "score": 9}],
    )
    for case in invalid:
        must_raise(ValueError, m.summarize_students, case)


def check_lab02(folder: str) -> None:
    m = load(folder, "lab02_json_report.py")
    payload = {
        "format": "PYTHON JOURNEY REVIEW V1",
        "count": 3,
        "average": 7.0,
        "passed": ["An", "Chi"],
    }
    assert m.FORMAT == payload["format"]
    assert call(m.validate_report, payload) is True
    assert call(m.validate_report, {
        "format": m.FORMAT, "count": 0, "average": None, "passed": [],
    }) is True
    bads = (
        [],
        {},
        {"format": m.FORMAT, "count": 1, "average": 7, "passed": ["An", "Bình"]},
        {**payload, "format": "UNKNOWN"},
        {**payload, "average": "7.0"},
        {**payload, "count": True},
        {**payload, "count": -1},
        {**payload, "passed": ["An", " an "]},
        {**payload, "passed": [""]},
        {**payload, "passed": "An"},
    )
    for bad in bads:
        assert call(m.validate_report, bad) is False, f"Không được nhận: {bad!r}"
    with TemporaryDirectory() as directory:
        path = Path(directory) / "new" / "summary.json"
        must_raise(FileNotFoundError, m.load_report, path)
        assert call(m.save_report, path, payload) == path
        assert call(m.load_report, path) == payload
        assert json.loads(path.read_text(encoding="utf-8")) == payload
        must_raise(ValueError, m.save_report, path, {"count": 2})
        assert call(m.load_report, path) == payload, "Không được ghi đè file đúng bằng dữ liệu sai"
        path.write_text("{oops", encoding="utf-8")
        must_raise(json.JSONDecodeError, m.load_report, path)
        path.write_text("[]", encoding="utf-8")
        must_raise(ValueError, m.load_report, path)


def check_lab03(folder: str) -> None:
    m = load(folder, "lab03_debugging.py")
    assert call(m.distance, 4, 1) == 3, "Regression: trừ hai chiều không lấy trị tuyệt đối"
    assert call(m.distance, 1, 4) == 3
    assert call(m.distance, 0, 0) == 0
    assert call(m.distance, 0, 10) == 10
    for start, end in ((-1, 2), (1, 11), (True, 1), (2, "3")):
        must_raise(ValueError, m.distance, start, end)

    log: list[str] = []
    assert call(m.parse_score, "8", log) == 8
    assert log == ["accepted", "attempt:'8'"], log
    assert call(m.parse_score, "bad", log) is None
    assert log[-2:] == ["invalid", "attempt:'bad'"]
    assert call(m.parse_score, "11", log) is None
    assert log[-2:] == ["out_of_range", "attempt:'11'"]
    assert call(m.parse_score, "0", log) == 0
    assert log[-2:] == ["accepted", "attempt:'0'"]
    must_raise(TypeError, m.parse_score, None, log)
    assert log[-1] == "attempt:None", "finally phải chạy khi TypeError nổi lên"
    assert len(log) == 9, log


def main() -> int:
    parser = argparse.ArgumentParser(description="Python Journey review self-check (offline)")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--starter", action="store_true", help="Kiểm code người học")
    mode.add_argument("--solutions", action="store_true", help="Chỉ kiểm lời giải tham khảo")
    args = parser.parse_args()
    folder = "starter" if args.starter else "solutions"
    passed = 0
    for index, check in enumerate((check_lab01, check_lab02, check_lab03), 1):
        try:
            check(folder)
        except Exception as error:
            print(f"Lab {index:02d}: FAIL — {type(error).__name__}: {error}")
        else:
            print(f"Lab {index:02d}: PASS")
            passed += 1
    kind = "student" if args.starter else "reference"
    print(f"Review {kind}: {'PASS' if passed == 3 else 'FAIL'} ({passed}/3)")
    return 0 if passed == 3 else 1


if __name__ == "__main__":
    raise SystemExit(main())
