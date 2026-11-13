"""Week 01 beginner guide must match the real AutoGrade CLI and rubric."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "weeks" / "week-01-hello-python"
GUIDE = WEEK / "assessment" / "STUDENT-GUIDE.md"


def test_student_entry_points_are_linked() -> None:
    assert GUIDE.is_file()
    assert "assessment/STUDENT-GUIDE.md" in (WEEK / "README.md").read_text(
        encoding="utf-8"
    )
    assert "STUDENT-GUIDE.md" in (WEEK / "assessment" / "README.md").read_text(
        encoding="utf-8"
    )
    assert "STUDENT-GUIDE.md" in (WEEK / "exercises" / "README.md").read_text(
        encoding="utf-8"
    )
    assert "STUDENT-GUIDE.md" in (WEEK / "mini-project" / "README.md").read_text(
        encoding="utf-8"
    )


def test_guide_uses_student_mode_and_does_not_confuse_reference() -> None:
    doc = GUIDE.read_text(encoding="utf-8")
    assert "python -m assessment grade --week 01 --acknowledge-local-code" in doc
    assert "--mode reference" in doc
    assert "không phải bài em viết" in doc
    assert "Exit code `1`" in doc
    assert "không tạo sandbox" in doc
    assert "5 điểm" in doc and "11 tiêu chí" in doc


def test_evidence_collects_real_student_self_check() -> None:
    template = (WEEK / "evidence-template.md").read_text(encoding="utf-8")
    assert "Số tiêu chí PASS" in template
    assert "Chế độ hiển thị: STUDENT" in template
    assert "chờ giảng viên duyệt" in template
