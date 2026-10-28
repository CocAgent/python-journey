"""Optional HTTP smoke tests (skip cleanly when extras are not installed)."""

import pytest

pytest.importorskip("fastapi")
pytest.importorskip("httpx")

from fastapi.testclient import TestClient

from career_assistant.api import create_app


def test_api_can_add_and_read_note(tmp_path):
    client = TestClient(create_app(tmp_path / "api.db"))
    assert client.get("/health").json()["status"] == "ok"
    created = client.post("/notes", json={"title": "Python", "body": "Test it"})
    assert created.status_code == 201
    assert client.get("/notes").json()[0]["title"] == "Python"


def test_api_validates_bad_skill_level(tmp_path):
    client = TestClient(create_app(tmp_path / "api.db"))
    result = client.put("/skills", json={"name": "Python", "level": 100})
    assert result.status_code == 422
