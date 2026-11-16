"""Behavioral tests: database isolation and real edge cases."""

import json

import pytest

from career_assistant import service


def test_new_database_is_empty(tmp_path):
    assert service.list_notes(tmp_path / "new.db") == []
    assert service.summary(tmp_path / "new.db")["note_count"] == 0


def test_add_and_list_note(tmp_path):
    db = tmp_path / "notes.db"
    note_id = service.add_note(db, "Python", "Learn functions", "python,work")
    notes = service.list_notes(db)
    assert notes[0]["id"] == note_id
    assert notes[0]["tags"] == ["python", "work"]


def test_empty_note_is_rejected(tmp_path):
    with pytest.raises(ValueError, match="Tiêu đề"):
        service.add_note(tmp_path / "notes.db", " ", "valid")


def test_empty_body_is_rejected(tmp_path):
    with pytest.raises(ValueError, match="Nội dung"):
        service.add_note(tmp_path / "notes.db", "Title", "")


def test_search_is_case_insensitive_and_literal(tmp_path):
    db = tmp_path / "notes.db"
    service.add_note(db, "REST API", "Web basics", "backend")
    assert len(service.search_notes(db, "rest")) == 1
    assert len(service.search_notes(db, "BACKEND")) == 1
    assert service.search_notes(db, "%") == []


def test_delete_only_existing_note(tmp_path):
    db = tmp_path / "notes.db"
    note_id = service.add_note(db, "X", "Y")
    assert service.delete_note(db, note_id)
    assert not service.delete_note(db, note_id)


def test_skill_is_updated_not_duplicated(tmp_path):
    db = tmp_path / "skills.db"
    service.set_skill(db, "pytest", 2, "first")
    service.set_skill(db, "pytest", 4, "practiced")
    assert service.list_skills(db) == [
        {"name": "pytest", "level": 4, "comment": "practiced"}
    ]


@pytest.mark.parametrize("level", [-1, 6, True, 2.5])
def test_invalid_skill_levels(tmp_path, level):
    with pytest.raises(ValueError, match="0 đến 5"):
        service.set_skill(tmp_path / "skills.db", "Python", level)


def test_summary_aggregates(tmp_path):
    db = tmp_path / "summary.db"
    service.add_note(db, "One", "First", "python,project")
    service.add_note(db, "Two", "Second", "python")
    service.set_skill(db, "Python", 4)
    service.set_skill(db, "Git", 2)
    report = service.summary(db)
    assert report["note_count"] == 2
    assert report["skill_count"] == 2
    assert report["average_level"] == 3
    assert ["python", 2] in [list(pair) for pair in report["popular_tags"]]


def test_export_json_is_valid_utf8(tmp_path):
    db = tmp_path / "notes.db"
    service.add_note(db, "Kiểm thử", "Dữ liệu tiếng Việt", "python")
    path = service.export_json(db, tmp_path / "exports" / "notes.json")
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["schema_version"] == 1
    assert payload["notes"][0]["title"] == "Kiểm thử"


def test_sql_injection_string_is_data(tmp_path):
    db = tmp_path / "safe.db"
    service.add_note(db, "'; DROP TABLE notes; --", "Text")
    assert len(service.list_notes(db)) == 1
    service.add_note(db, "Still here", "Text")
    assert len(service.list_notes(db)) == 2
