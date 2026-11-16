"""AG-02 guide contract — no learner code runs in these tests."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEEKS = {
    "02": "week-02-variables-types",
    "03": "week-03-conditionals",
    "04": "week-04-strings",
    "05": "week-05-lists-tuples",
    "06": "week-06-loops",
    "07": "week-07-functions",
    "08": "week-08-dicts-sets",
    "09": "week-09-midterm-project",
    "10": "week-10-files-io",
    "11": "week-11-exceptions",
    "12": "week-12-testing-pytest",
    "13": "week-13-modules-cli-api",
    "14": "week-14-oop-essentials",
    "15": "week-15-capstone-project",
}


def test_every_week_has_student_guide_and_readme_link() -> None:
    for week, directory in WEEKS.items():
        base = ROOT / "weeks" / directory
        guide = base / "assessment" / "STUDENT-GUIDE.md"
        assert guide.is_file(), week
        text = guide.read_text(encoding="utf-8")
        assert "Week " + week in text
        assert "sinh viên" in text.lower()
        assert "không" in text.lower()
        assert "assessment/STUDENT-GUIDE.md" in (
            base / "README.md"
        ).read_text(encoding="utf-8")


def test_portal_and_evidence_linked() -> None:
    portal = (ROOT / "assessment" / "STUDENT-PORTAL.md").read_text(
        encoding="utf-8"
    )
    evidence = (ROOT / "assessment" / "EVIDENCE-TEMPLATE.md").read_text(
        encoding="utf-8"
    )
    for week, directory in WEEKS.items():
        assert f"../weeks/{directory}/assessment/STUDENT-GUIDE.md" in portal, week
    assert "official_score" in portal
    assert "PASS" in evidence
    assert "rubric" in evidence


def test_no_claim_all_weeks_get_numeric_scores() -> None:
    for week, directory in WEEKS.items():
        text = (
            ROOT / "weeks" / directory / "assessment" / "STUDENT-GUIDE.md"
        ).read_text(encoding="utf-8")
        if week not in {"09", "15"}:
            assert f"selfcheck --week {week}" in text
            assert "auto_score" in text
            assert "không" in text.lower()
        else:
            assert "không" in text.lower() and "rubric" in text.lower()


def test_reference_commands_not_present_as_student_submission() -> None:
    for directory in WEEKS.values():
        text = (
            ROOT / "weeks" / directory / "assessment" / "STUDENT-GUIDE.md"
        ).read_text(encoding="utf-8")
        assert "--solutions" not in text or "không" in text.lower()
