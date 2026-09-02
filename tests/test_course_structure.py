"""Maintainer tests for stable Python Journey repository structure."""

import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_WEEK_PREFIXES = [f"week-{number:02d}-" for number in range(1, 16)]
REQUIRED_ROOT_FILES = {
    "AGENTS.md",
    "CONTRIBUTING.md",
    "FINAL_PROJECT.md",
    "PROGRESS.md",
    "README.md",
    "SETUP.md",
    "STYLE_GUIDE.md",
    "SYLLABUS.md",
}


def test_required_root_documents_exist() -> None:
    actual = {path.name for path in ROOT.iterdir() if path.is_file()}
    assert REQUIRED_ROOT_FILES <= actual


def test_agents_contract_is_locked() -> None:
    contract = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    required_lines = {
        "PROJECT = Python Journey V2",
        "DEFAULT_WORK_BRANCH = upgrade/python-journey-v2",
        "PYTHON_BASELINE = >=3.12",
        "LEARNING_LOOP = Learn → Build → Test → Debug → Improve → Commit → Prove",
    }

    assert all(line in contract for line in required_lines)


def test_week_directories_cover_exactly_01_through_15() -> None:
    week_names = sorted(
        path.name
        for path in (ROOT / "weeks").iterdir()
        if path.is_dir() and path.name.startswith("week-")
    )

    assert len(week_names) == 15
    assert all(
        name.startswith(prefix)
        for name, prefix in zip(week_names, EXPECTED_WEEK_PREFIXES, strict=True)
    )


def test_syllabus_has_exactly_15_numbered_week_headings() -> None:
    headings = []
    for line in (ROOT / "SYLLABUS.md").read_text(encoding="utf-8").splitlines():
        heading = line.lstrip("#").strip()
        if heading.startswith("Tuần "):
            headings.append(heading)

    assert len(headings) == 15
    assert all(
        heading.startswith(f"Tuần {number:02d}")
        for number, heading in enumerate(headings, start=1)
    )


def test_capstone_sources_are_present() -> None:
    assert (ROOT / "FINAL_PROJECT.md").stat().st_size > 0
    week_15_readmes = list((ROOT / "weeks").glob("week-15-*/README.md"))
    assert len(week_15_readmes) == 1


def test_python_baseline_is_consistent() -> None:
    config = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    assert (ROOT / ".python-version").read_text(encoding="utf-8").strip() == "3.12"
    assert config["tool"]["python-journey"]["python-requires"] == ">=3.12"
    assert config["tool"]["ruff"]["target-version"] == "py312"


def test_course_health_verifier_passes() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/verify_course.py"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr
