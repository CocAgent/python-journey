"""Offline stdlib smoke check for the advanced Week 13 Ticket Desk.

Runs in an isolated temporary directory. Does not test optional FastAPI.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]


def run(*args: str) -> subprocess.CompletedProcess[str]:
    """Run module-mode from week root; fail on unexpected timeout."""
    return subprocess.run(
        [sys.executable, "-m", "advanced_projects.ticketdesk", *args],
        cwd=WEEK_ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=15,
    )


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="week13-ticketdesk-") as name:
        path = str(Path(name) / "tickets.json")
        created = run("--db", path, "add", "--title", "Học pytest", "--priority", "high")
        assert created.returncode == 0, created.stderr
        assert json.loads(created.stdout)["id"] == 1

        summary = run("--db", path, "summary")
        assert summary.returncode == 0, summary.stderr
        assert json.loads(summary.stdout) == {"total": 1, "open": 1, "closed": 0}

        closed = run("--db", path, "close", "1")
        assert closed.returncode == 0, closed.stderr
        assert json.loads(closed.stdout)["status"] == "closed"

        rejected = run("--db", path, "close", "1")
        assert rejected.returncode == 2
        assert "Lỗi:" in rejected.stderr
        assert json.loads(Path(path).read_text(encoding="utf-8"))[0]["status"] == "closed"

        invalid = run("--db", path, "add", "--title", "  ")
        assert invalid.returncode == 2
        assert len(json.loads(Path(path).read_text(encoding="utf-8"))) == 1
    print("Week 13 advanced Ticket Desk: PASS (offline)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
