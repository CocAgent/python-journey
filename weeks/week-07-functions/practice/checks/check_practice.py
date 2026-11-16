"""Tự kiểm 4 bài hàm của Week07, KHÔNG cần pytest hoặc internet.

--starter: kiểm function do sinh viên viết; trước khi làm TODO sẽ FAIL.
--solutions: chỉ kiểm lời giải tham khảo cho maintainer CI.
Khác các tuần 02–06, checker này GỌI TRỰC TIẾP các function với nhiều input.
"""

from __future__ import annotations

import argparse
import importlib.util
import io
from contextlib import redirect_stdout
from pathlib import Path
from types import ModuleType
from typing import Any, Callable

BASE = Path(__file__).resolve().parents[1]


def load(folder: str, name: str) -> ModuleType:
    """Import file một lần; phát hiện đoạn code tự in khi bị import."""
    path = BASE / folder / name
    spec = importlib.util.spec_from_file_location(f"week07_{folder}_{path.stem}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Không thể import {path}")
    module = importlib.util.module_from_spec(spec)
    output = io.StringIO()
    with redirect_stdout(output):
        spec.loader.exec_module(module)
    assert not output.getvalue(), "Import module không được tự in demo; dùng main guard"
    return module


def call(function: Callable[..., Any], *args: object) -> Any:
    """Kiểm kết quả return: print không thể thay cho return."""
    output = io.StringIO()
    with redirect_stdout(output):
        result = function(*args)
    assert not output.getvalue(), "Hàm xử lý không được print thay cho return"
    return result


def must_reject(function: Callable[..., Any], *args: object) -> None:
    try:
        call(function, *args)
    except ValueError:
        return
    raise AssertionError(f"Expected ValueError cho input {args!r}")


def check_lab01(folder: str) -> None:
    m = load(folder, "lab01_return_total.py")
    assert call(m.calculate_total, 12_000, 2) == 24_000
    assert call(m.calculate_total, 12_000, 2, 5_000) == 29_000
    assert call(m.calculate_total, 0, 1) == 0
    for args in ((-1, 2), (10, 0), (10, 2, -1), (True, 2)):
        must_reject(m.calculate_total, *args)


def check_lab02(folder: str) -> None:
    m = load(folder, "lab02_decomposition.py")
    assert call(m.is_valid_order, 25_000, 2, 10) is True
    for bad in ((10, 0, 0), (-1, 2, 0), (10, 2, 101), (True, 2, 0)):
        assert call(m.is_valid_order, *bad) is False
    assert call(m.calculate_subtotal, 25_000, 2) == 50_000
    assert call(m.calculate_final, 25_000, 2) == 50_000
    assert call(m.calculate_final, 25_000, 2, 10) == 45_000
    assert call(m.calculate_final, 10_001, 1, 50) == 5_000  # làm tròn xuống
    assert call(m.calculate_final, 0, 1, 100) == 0
    must_reject(m.calculate_final, 25_000, 0, 10)
    must_reject(m.calculate_final, 25_000, 2, -1)
    must_reject(m.calculate_final, 25_000, 2, 101)
    # Chứng minh bước final thật sự TÁI SỬ DỤNG hàm subtotal.
    original = m.calculate_subtotal
    try:
        m.calculate_subtotal = lambda price, quantity: 30_000
        assert call(m.calculate_final, 25_000, 2, 10) == 27_000, (
            "calculate_final cần gọi lại calculate_subtotal, không copy logic"
        )
    finally:
        m.calculate_subtotal = original


def check_lab03(folder: str) -> None:
    m = load(folder, "lab03_scope_notes.py")
    first: list[str] = []
    second: list[str] = []
    assert call(m.add_note, first, "   ") is False
    assert first == []
    assert call(m.add_note, first, "  Học return  ") is True
    assert call(m.add_note, first, "Luyện scope") is True
    assert first == ["Học return", "Luyện scope"]
    assert call(m.count_notes, first) == 2
    assert call(m.count_notes, second) == 0
    assert call(m.search_notes, first, "RETURN") == ["Học return"]
    assert call(m.search_notes, first, "  ") == []
    assert call(m.search_notes, first, "missing") == []
    assert call(m.search_notes, second, "return") == []
    assert first == ["Học return", "Luyện scope"], "Tìm kiếm không được sửa list nguồn"


def check_lab04(folder: str) -> None:
    m = load(folder, "lab04_decision_validation.py")
    action = m.choose_study_action
    assert call(action, 0, True) == "stop"
    assert call(action, 0, False) == "stop"
    assert call(action, 15, True) == "review"
    assert call(action, 15, False) == "practice"
    assert call(action, 60, False) == "practice"
    for minutes, confused in ((-1, False), (61, False), (True, False), (5, "False")):
        must_reject(action, minutes, confused)
    for minutes, confused in ((0, True), (15, True), (15, False)):
        assert call(action, minutes, confused) == call(action, minutes, confused)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Week07 function-level offline self-check")
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--starter", action="store_true", help="Kiểm code sinh viên")
    modes.add_argument("--solutions", action="store_true", help="Kiểm lời giải tham khảo")
    args = parser.parse_args(argv)

    folder = "starter" if args.starter else "solutions"
    passed = 0
    for index, check in enumerate(
        (check_lab01, check_lab02, check_lab03, check_lab04), start=1
    ):
        try:
            check(folder)
        except Exception as error:  # Báo FAIL từng lab, không che lỗi.
            print(f"Lab {index:02d}: FAIL — {type(error).__name__}: {error}")
        else:
            print(f"Lab {index:02d}: PASS")
            passed += 1

    label = "student" if args.starter else "reference"
    if passed == 4:
        print(f"Week 07 {label} practice: PASS (4/4)")
        return 0
    print(f"Week 07 {label} practice: FAIL ({passed}/4)")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
