"""HTTP client for the public GitHub Users API."""

import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class GitHubAPIError(RuntimeError):
    """Raised when GitHub returns an error or the request cannot complete."""


def get_user(username: str, timeout: float = 10.0) -> dict[str, object]:
    """Fetch one public GitHub user and return its JSON object.

    The timeout keeps the CLI from waiting forever. HTTP and network errors are
    converted into a clear application-level exception.
    """
    cleaned = username.strip()
    if not cleaned:
        raise ValueError("GitHub username cannot be empty")

    request = Request(
        f"https://api.github.com/users/{cleaned}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "python-journey-week13",
        },
        method="GET",
    )

    try:
        with urlopen(request, timeout=timeout) as response:
            payload = response.read()
    except HTTPError as error:
        if error.code == 404:
            raise GitHubAPIError(f"GitHub user '{cleaned}' was not found") from error
        raise GitHubAPIError(f"GitHub API returned HTTP {error.code}") from error
    except (TimeoutError, URLError, OSError) as error:
        raise GitHubAPIError(f"Could not connect to GitHub: {error}") from error

    try:
        data = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise GitHubAPIError("GitHub returned invalid JSON") from error

    if not isinstance(data, dict):
        raise GitHubAPIError("GitHub returned an unexpected JSON format")

    return data
