"""Public CLI contract smoke tests, from a learner's perspective."""

import json
import subprocess
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]


def run_cli(db, *args):
    return subprocess.run(
        [sys.executable, "-m", "career_assistant", "--db", str(db), *args],
        cwd=PROJECT,
        capture_output=True,
        text=True,
        check=False,
    )


def test_cli_happy_path(tmp_path):
    db = tmp_path / "cli.db"
    added = run_cli(
        db, "add-note", "--title", "Git", "--body", "Commits", "--tags", "career"
    )
    assert added.returncode == 0, added.stderr
    assert json.loads(added.stdout)["id"] == 1
    searched = run_cli(db, "search", "git")
    assert searched.returncode == 0, searched.stderr
    assert len(json.loads(searched.stdout)) == 1


def test_cli_rejects_invalid_skill_level(tmp_path):
    result = run_cli(tmp_path / "cli.db", "skill", "Python", "--level", "9")
    assert result.returncode == 2
    assert "0 đến 5" in result.stderr


def test_cli_exports_json(tmp_path):
    db = tmp_path / "cli.db"
    output = tmp_path / "output.json"
    result = run_cli(db, "export", str(output))
    assert result.returncode == 0
    assert json.loads(output.read_text(encoding="utf-8"))["notes"] == []
