"""Offline tests for the Week 13 GitHub Profile CLI."""

import io
import json
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

PROJECT_ROOT = (
    Path(__file__).resolve().parents[1]
    / "weeks"
    / "week-13-modules-cli-api"
    / "mini-project"
)
sys.path.insert(0, str(PROJECT_ROOT))

from github_profile_cli.client import GitHubAPIError, get_user  # noqa: E402


class FakeResponse:
    def __init__(self, payload: bytes) -> None:
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self) -> bytes:
        return self.payload


def test_get_user_parses_json_and_sets_timeout() -> None:
    payload = json.dumps({"login": "octocat", "public_repos": 8}).encode()
    with patch(
        "github_profile_cli.client.urlopen",
        return_value=FakeResponse(payload),
    ) as mocked:
        result = get_user(" octocat ")

    assert result["login"] == "octocat"
    assert result["public_repos"] == 8
    request, timeout = mocked.call_args.args
    assert request.full_url == "https://api.github.com/users/octocat"
    assert request.get_method() == "GET"
    assert timeout == 10.0


def test_get_user_rejects_empty_username() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        get_user("  ")


def test_get_user_rejects_invalid_json() -> None:
    with patch(
        "github_profile_cli.client.urlopen",
        return_value=FakeResponse(b"not-json"),
    ):
        with pytest.raises(GitHubAPIError, match="invalid JSON"):
            get_user("octocat")


def test_cli_prints_profile_without_network() -> None:
    from github_profile_cli.cli import main

    profile = {
        "login": "octocat",
        "name": "The Octocat",
        "public_repos": 8,
        "followers": 100,
        "following": 5,
        "html_url": "https://github.com/octocat",
    }
    output = io.StringIO()
    with (
        patch("github_profile_cli.cli.get_user", return_value=profile),
        patch("sys.stdout", output),
    ):
        exit_code = main(["octocat"])

    assert exit_code == 0
    assert "Username: octocat" in output.getvalue()
    assert "Public repositories: 8" in output.getvalue()
