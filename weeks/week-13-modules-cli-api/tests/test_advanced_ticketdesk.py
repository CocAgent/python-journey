"""Advanced Week 13 example: tests for logic, storage, CLI and HTTP fixture."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

WEEK_ROOT = Path(__file__).resolve().parents[1]
if str(WEEK_ROOT) not in sys.path:
    sys.path.insert(0, str(WEEK_ROOT))

from advanced_projects.ticketdesk import service, storage  # noqa: E402
from advanced_projects.ticketdesk.http_demo import make_get_response  # noqa: E402


def test_empty_summary() -> None:
    assert service.summarize([]) == {"total": 0, "open": 0, "closed": 0}


def test_create_ticket_does_not_mutate_original() -> None:
    original: list[dict] = []
    updated = service.add_ticket(original, "  Học API  ", "high")
    assert original == []
    assert updated == [
        {"id": 1, "title": "Học API", "priority": "high", "status": "open"}
    ]


def test_ids_remain_unique_after_close() -> None:
    items = service.add_ticket([], "Một")
    items = service.add_ticket(items, "Hai")
    closed = service.close_ticket(items, 1)
    result = service.add_ticket(closed, "Ba")
    assert [item["id"] for item in result] == [1, 2, 3]
    assert items[0]["status"] == "open"
    assert service.summarize(result) == {"total": 3, "open": 2, "closed": 1}


@pytest.mark.parametrize(
    ("title", "priority"),
    [("", "normal"), ("   ", "low"), ("OK", "urgent"), (None, "normal")],
)
def test_reject_invalid_new_ticket(title: object, priority: str) -> None:
    with pytest.raises(ValueError):
        service.add_ticket([], title, priority)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "data",
    [
        {"id": 0, "title": "a", "priority": "normal", "status": "open"},
        {"id": True, "title": "a", "priority": "normal", "status": "open"},
        {"id": 1, "title": "a", "priority": ["normal"], "status": "open"},
        {"id": 1, "title": "a", "priority": "normal", "status": ["open"]},
    ],
)
def test_reject_invalid_persisted_record(data: dict) -> None:
    with pytest.raises(ValueError):
        service.validate_tickets([data])


def test_reject_duplicate_ids() -> None:
    items = service.add_ticket([], "Same")
    with pytest.raises(ValueError, match="trùng"):
        service.validate_tickets([*items, dict(items[0])])


def test_close_missing_or_already_closed() -> None:
    items = service.add_ticket([], "Có thật")
    with pytest.raises(ValueError, match="Không tìm thấy"):
        service.close_ticket(items, 99)
    closed = service.close_ticket(items, 1)
    with pytest.raises(ValueError, match="đã đóng"):
        service.close_ticket(closed, 1)


def test_roundtrip_utf8_json(tmp_path: Path) -> None:
    path = tmp_path / "tickets.json"
    items = service.add_ticket([], "Yêu cầu mới", "high")
    storage.save_tickets(path, items)
    assert storage.load_tickets(path) == items
    assert "Yêu cầu mới" in path.read_text(encoding="utf-8")


def test_corrupted_json_does_not_become_empty(tmp_path: Path) -> None:
    path = tmp_path / "tickets.json"
    path.write_text("not-json", encoding="utf-8")
    with pytest.raises(ValueError, match="JSON"):
        storage.load_tickets(path)


def test_http_fixture_status_and_payload(tmp_path: Path) -> None:
    path = tmp_path / "tickets.json"
    storage.save_tickets(path, service.add_ticket([], "Help"))
    status, body = make_get_response(path, 1)
    assert status == 200
    assert json.loads(body.decode("utf-8"))["title"] == "Help"
    missing_status, missing_body = make_get_response(path, 999)
    assert missing_status == 404
    assert json.loads(missing_body.decode("utf-8"))["error"] == "ticket not found"


def _run_cli(path: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable, "-m", "advanced_projects.ticketdesk",
            "--db", str(path), *args,
        ],
        cwd=WEEK_ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=10,
    )


def test_cli_end_to_end_and_fail_closed(tmp_path: Path) -> None:
    path = tmp_path / "cli.json"
    added = _run_cli(path, "add", "--title", "Git", "--priority", "high")
    assert added.returncode == 0, added.stderr
    assert json.loads(added.stdout)["id"] == 1

    closed = _run_cli(path, "close", "1")
    assert closed.returncode == 0, closed.stderr
    assert json.loads(closed.stdout)["status"] == "closed"

    repeated = _run_cli(path, "close", "1")
    assert repeated.returncode == 2
    assert "Lỗi:" in repeated.stderr and "Traceback" not in repeated.stderr
    assert storage.load_tickets(path)[0]["status"] == "closed"


def test_import_has_no_cli_side_effect() -> None:
    result = subprocess.run(
        [
            sys.executable, "-c",
            "import advanced_projects.ticketdesk; "
            "import advanced_projects.ticketdesk.cli; "
            "import advanced_projects.ticketdesk.http_demo",
        ],
        cwd=WEEK_ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=10,
    )
    assert result.returncode == 0, result.stderr
    assert not result.stdout
