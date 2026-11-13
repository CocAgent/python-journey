"""AG-01 acceptance tests; only trusted test fixtures are ever executed."""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
# pytest's console entrypoint can omit the repository root from sys.path.
# Keep this confined to this acceptance module, not the production package.
sys.path.insert(0, str(ROOT))

from assessment.engine.cli import main  # noqa: E402
from assessment.engine.report import grade_week01, load_rubric  # noqa: E402
RUBRIC = ROOT / "weeks/week-01-hello-python/assessment/rubric.json"
REFERENCE = ROOT / "assessment/fixtures/week01/reference"
WEEK = Path("weeks/week-01-hello-python")


def test_reference_fixture_is_full_score():
    result = grade_week01(REFERENCE, RUBRIC, reference=True)
    assert result["auto_score"] == 5
    assert result["passed_criteria"] == result["total_criteria"] == 11
    assert result["manual_score"] is None
    assert result["official_score"] is None
    assert result["mode"] == "reference"


def test_week01_starters_are_not_graded_as_solution():
    result = grade_week01(ROOT, RUBRIC)
    assert result["auto_score"] == 0
    assert result["passed_criteria"] == 0
    assert result["mode"] == "student"


def test_missing_file_reports_zero_without_crash(tmp_path: Path):
    result = grade_week01(tmp_path, RUBRIC)
    assert result["auto_score"] == 0
    assert result["passed_criteria"] == 0
    assert result["tasks"][0]["checks"][0]["reason"] == "Thiếu tệp bài làm."


def test_partial_hardcoded_answer_needs_arithmetic_syntax(tmp_path: Path):
    dst = tmp_path / WEEK / "exercises"
    dst.mkdir(parents=True)
    (dst / "ex02_calculator.py").write_text(
        "print(3024)\nprint(45000)\nprint(153.94)\nprint(14)\nprint(2)\n",
        encoding="utf-8",
    )
    result = grade_week01(tmp_path, RUBRIC)
    arithmetic = result["tasks"][1]["checks"]
    assert all(not criterion["passed"] for criterion in arithmetic)


def test_syntax_error_is_reported(tmp_path: Path):
    file = tmp_path / WEEK / "exercises" / "ex01_hello.py"
    file.parent.mkdir(parents=True)
    file.write_text("print(\n", encoding="utf-8")
    result = grade_week01(tmp_path, RUBRIC)
    assert "Lỗi cú pháp" in result["tasks"][0]["checks"][0]["reason"]


def test_json_report_and_cli_gate(tmp_path: Path):
    assert main([
        "grade", "--week", "01", "--mode", "reference",
        "--json-out", str(tmp_path / "report.json"),
    ]) == 0
    data = json.loads((tmp_path / "report.json").read_text(encoding="utf-8"))
    assert data["auto_score"] == 5
    assert data["mode"] == "reference"
    assert data["rubric_sha256"]
    assert all(task["source_sha256"] for task in data["tasks"])


def test_local_student_fixtures_work_when_acknowledged(tmp_path: Path):
    shutil.copytree(REFERENCE / "weeks", tmp_path / "weeks")
    assert main([
        "grade", "--week", "01", "--submission", str(tmp_path),
        "--acknowledge-local-code",
    ]) == 0


def test_rubric_matches_original_week01_weights():
    rubric = load_rubric(RUBRIC)
    assert [sum(c["points"] for c in task["criteria"]) for task in rubric["tasks"]] == [2, 2, 1]


def test_student_mode_requires_explicit_local_execution_opt_in():
    with pytest.raises(SystemExit) as exc:
        main(["grade", "--week", "01"])
    assert exc.value.code == 2


def test_symlink_cannot_escape_submission_root(tmp_path: Path):
    outside = tmp_path.parent / "other_work"
    outside.mkdir(exist_ok=True)
    link = tmp_path / WEEK / "exercises" / "ex01_hello.py"
    link.parent.mkdir(parents=True)
    link.symlink_to(outside / "missing.py")
    with pytest.raises(ValueError, match="ngoài thư mục"):
        grade_week01(tmp_path, RUBRIC)
