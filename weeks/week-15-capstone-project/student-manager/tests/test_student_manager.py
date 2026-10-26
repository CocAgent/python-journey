"""Normal, edge, invalid and regression tests."""

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from student_manager import (  # noqa: E402
    add_student,
    calculate_average,
    classify_student,
    find_student,
    load_students,
    save_students,
)


def test_average_normal():
    assert calculate_average([8, 9, 7]) == 8


def test_average_empty():
    with pytest.raises(ValueError):
        calculate_average([])


def test_average_invalid():
    with pytest.raises(ValueError):
        calculate_average([11])


def test_classify_boundaries():
    assert classify_student(8) == "Excellent"
    assert classify_student(6.5) == "Good"
    assert classify_student(5) == "Average"
    assert classify_student(4.9) == "Needs improvement"


def test_add_find():
    students = add_student([], "S01", "Son", [7, 8])
    assert find_student(students, "S01")["name"] == "Son"
    assert find_student(students, "missing") is None


def test_duplicate_rejected():
    students = add_student([], "S01", "Son", [7])
    with pytest.raises(ValueError):
        add_student(students, "S01", "Another", [8])


def test_storage_roundtrip(tmp_path):
    path = tmp_path / "students.json"
    expected = add_student([], "S01", "Son", [7, 9])
    save_students(path, expected)
    assert load_students(path) == expected


def test_missing_file(tmp_path):
    assert load_students(tmp_path / "missing.json") == []


def test_invalid_json(tmp_path):
    path = tmp_path / "bad.json"
    path.write_text("{oops", encoding="utf-8")
    with pytest.raises(ValueError):
        load_students(path)


def test_incomplete_record(tmp_path):
    path = tmp_path / "bad.json"
    path.write_text(json.dumps([{"id": "S01"}]), encoding="utf-8")
    with pytest.raises(ValueError):
        load_students(path)
