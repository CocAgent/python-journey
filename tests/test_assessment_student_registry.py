"""Registration contract: only own learner checkers, no fake scores."""

from __future__ import annotations

import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assessment.engine.cli import main  # noqa: E402
from assessment.engine.student_registry import CHECKS, REPO_ROOT, find  # noqa: E402
from assessment.engine.student_selfcheck import selfcheck  # noqa: E402


def test_registers_all_weeks_without_unsupported_numeric_grades():
    assert list(CHECKS) == [f"{n:02d}" for n in range(2, 16)]
    assert find("09").argv is None
    for week, spec in CHECKS.items():
        assert (REPO_ROOT / "weeks" / spec.directory / "README.md").is_file()
        if spec.argv is not None and week != "13":
            assert (REPO_ROOT / spec.argv[0]).is_file()
        if week == "13":
            assert (REPO_ROOT / spec.cwd / "practice" / "checks" / "check_lab.py").is_file()


@pytest.mark.parametrize("week", [f"{n:02d}" for n in range(1, 16)])
def test_guide_does_not_execute_learner_code(week, capsys):
    assert main(["guide", "--week", week]) == 0
    assert f"Week {week}" in capsys.readouterr().out or f"Tuần {week}" in capsys.readouterr().out


def test_student_selfcheck_requires_explicit_opt_in():
    with pytest.raises(SystemExit) as exc:
        main(["selfcheck", "--week", "02"])
    assert exc.value.code == 2


def test_week09_must_not_appear_to_be_autograded():
    with pytest.raises(SystemExit) as exc:
        main(["selfcheck", "--week", "09", "--acknowledge-local-code"])
    assert exc.value.code == 2


def test_grade_only_week01():
    with pytest.raises(SystemExit) as exc:
        main(["grade", "--week", "07", "--acknowledge-local-code"])
    assert exc.value.code == 2


def test_reference_mode_is_rejected_for_practice():
    with pytest.raises(SystemExit) as exc:
        main(["selfcheck", "--week", "04", "--mode", "reference", "--acknowledge-local-code"])
    assert exc.value.code == 2


def test_no_automatic_score_and_uses_correct_starter(monkeypatch, tmp_path: Path):
    seen = {}

    def fake_run(command, **kwargs):
        seen["command"] = command
        seen["cwd"] = kwargs["cwd"]
        return SimpleNamespace(returncode=0, stdout="student practice: PASS\n", stderr="")

    monkeypatch.setattr("assessment.engine.student_selfcheck.subprocess.run", fake_run)
    spec = CHECKS["07"]
    code, report = selfcheck(spec)
    assert code == 0
    assert report["auto_score"] is None
    assert report["official_score"] is None
    assert report["mode"] == "student"
    assert "practice/checks/check_practice.py" in str(seen["command"])
    assert "--starter" in seen["command"]
    assert "--solutions" not in seen["command"]
    assert seen["cwd"] == REPO_ROOT


def test_week13_runs_from_own_package_directory(monkeypatch):
    capture = {}

    def fake_run(command, **kwargs):
        capture["cmd"] = command
        capture["cwd"] = kwargs["cwd"]
        return SimpleNamespace(returncode=1, stdout="starter: FAIL", stderr="")

    monkeypatch.setattr("assessment.engine.student_selfcheck.subprocess.run", fake_run)
    code, report = selfcheck(CHECKS["13"])
    assert code == 1
    assert report["status"] == "RETRY"
    assert capture["cwd"] == REPO_ROOT / "weeks" / "week-13-modules-cli-api"
    assert capture["cmd"][-3:] == ["-m", "practice.checks.check_lab", "--starter"]


def test_capstone_requires_project_and_never_automatically_executes_tests(monkeypatch, tmp_path: Path):
    with pytest.raises(ValueError):
        selfcheck(CHECKS["15"])
    capture = {}

    def fake_run(command, **kwargs):
        capture["cmd"] = command
        return SimpleNamespace(returncode=0, stdout="readiness: PASS", stderr="")

    monkeypatch.setattr("assessment.engine.student_selfcheck.subprocess.run", fake_run)
    code, report = selfcheck(CHECKS["15"], project=tmp_path)
    assert code == 0
    assert "--run-tests" not in capture["cmd"]
    assert report["auto_score"] is None
    # The pre-existing checker still performs pytest --collect-only;
    # project code must therefore be trusted even without --run-tests.


def test_cli_still_supports_week01_reference():
    assert main(["grade", "--week", "01", "--mode", "reference"]) == 0


def test_report_writer_creates_private_local_file(tmp_path: Path):
    from assessment.engine.student_selfcheck import write_report

    target = tmp_path / ".learner-output" / "w02.json"
    write_report({"mode": "student", "auto_score": None}, target)
    assert '"auto_score": null' in target.read_text(encoding="utf-8")
