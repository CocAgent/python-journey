"""Full-bank integrity and safe CLI tests, using only maintainer fixtures."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

CORE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CORE))

import autograde_w02 as ag  # noqa: E402
from grader import main as grader_main  # noqa: E402

REFERENCE = CORE / "fixtures" / "reference"


def test_full_bank_matches_all_rubric_criteria() -> None:
    audit = ag.test_suite_audit()
    assert audit["exercises_count"] == 3
    assert audit["criteria_count"] == 10
    assert audit["dynamic_case_count"] == 24
    assert audit["rubric_points"] == 10
    assert len(audit["test_suite_sha256"]) == 64
    assert audit["official_score"] is None


def test_full_bank_and_golden_reference_score_ten() -> None:
    result = ag.grade(REFERENCE, "reference")
    assert result["auto_score"] == 10
    assert result["official_score"] is None
    assert result["test_suite_sha256"] == ag.test_suite_audit()["test_suite_sha256"]
    assert [len(task["criteria"]) for task in result["tasks"]] == [3, 4, 3]


def test_bank_rejects_missing_criterion(tmp_path: Path, monkeypatch) -> None:
    for source in ag.TEST_CASE_DIR.glob("cases_ex*.json"):
        (tmp_path / source.name).write_bytes(source.read_bytes())
    filename = tmp_path / "cases_ex02_type_conversion.json"
    data = json.loads(filename.read_text(encoding="utf-8"))
    del data["cases"]["W02.EX02.BMI"]
    filename.write_text(json.dumps(data), encoding="utf-8")
    monkeypatch.setattr(autograde_w02, "TEST_CASE_DIR", tmp_path)
    with pytest.raises(ValueError, match="TEST_SUITE_MISMATCH"):
        ag.test_suite_audit()


def test_bank_rejects_missing_dynamic_cases(tmp_path: Path, monkeypatch) -> None:
    for source in ag.TEST_CASE_DIR.glob("cases_ex*.json"):
        (tmp_path / source.name).write_bytes(source.read_bytes())
    filename = tmp_path / "cases_ex03_input_calc.json"
    data = json.loads(filename.read_text(encoding="utf-8"))
    data["cases"]["W02.EX03.DISCOUNT"] = data["cases"]["W02.EX03.DISCOUNT"][:2]
    filename.write_text(json.dumps(data), encoding="utf-8")
    monkeypatch.setattr(autograde_w02, "TEST_CASE_DIR", tmp_path)
    with pytest.raises(ValueError, match="TEST_SUITE_INCOMPLETE"):
        ag.test_suite_audit()


def test_full_suite_audit_cli_does_not_run_student_code(
    monkeypatch, capsys,
) -> None:
    import grader  # noqa: PLC0415

    def forbid_execution(*_args, **_kwargs):
        raise AssertionError("audit-tests must not execute any Python submission")

    monkeypatch.setattr(grader, "grade", forbid_execution)
    assert grader_main(["--audit-tests"]) == 0
    report = json.loads(capsys.readouterr().out)
    assert report["criteria_count"] == 10
    assert report["dynamic_case_count"] == 24


def test_external_submission_requires_explicit_local_trust(tmp_path: Path) -> None:
    with pytest.raises(SystemExit) as exc:
        grader_main(["--student", "--submission", str(tmp_path)])
    assert exc.value.code == 2


def test_student_cli_blank_workspace_creates_private_reports(
    tmp_path: Path,
) -> None:
    workspace = tmp_path / "student"
    exercises = workspace / "exercises"
    exercises.mkdir(parents=True)
    for filename, size in [
        ("ex01_variables.py", 4),
        ("ex02_type_conversion.py", 5),
        ("ex03_input_calc.py", 4),
    ]:
        (exercises / filename).write_text(
            "\n".join(f"# TODO {n}: trống" for n in range(1, size + 1))
            + "\n",
            encoding="utf-8",
        )
    html_path = tmp_path / "week02.html"
    json_path = tmp_path / "week02.json"
    assert grader_main([
        "--student", "--submission", str(workspace),
        "--acknowledge-local-code",
        "--report", str(html_path), "--json-out", str(json_path),
    ]) == 1
    data = json.loads(json_path.read_text(encoding="utf-8"))
    html = html_path.read_text(encoding="utf-8")
    assert data["auto_score"] == 0
    assert data["official_score"] is None
    assert "0.00/10" in html
    assert html.count('class="stage"') == 3
    assert '<script' not in html
    assert "stdout" not in json.dumps(data)


def test_learner_solutions_and_grader_fixtures_stay_separate() -> None:
    assert REFERENCE != CORE.parent.parent / "exercises"
    audit = ag.test_suite_audit()
    assert all(
        item["exercise"].startswith("ex0")
        for item in audit["tasks"]
    )
