"""Document regressions for optional AI tool guides in Week 01.

Never invokes Antigravity, ChatGPT, an API, or learner-submitted code.
"""

from pathlib import Path

import pytest

WEEK = Path(__file__).resolve().parents[1]
OPTIONAL = WEEK / "optional-tools"


@pytest.mark.parametrize(
    "name",
    ["README.md", "google-antigravity.md", "chatgpt-github.md"],
)
def test_optional_guide_exists_and_is_substantive(name: str) -> None:
    content = (OPTIONAL / name).read_text(encoding="utf-8")
    assert len(content) > 700


def test_antigravity_requires_review_not_auto_push() -> None:
    text = (OPTIONAL / "google-antigravity.md").read_text(encoding="utf-8")
    for token in ("antigravity.google", "git diff", "không bắt buộc", "Không tự commit"):
        assert token.casefold() in text.casefold()


def test_chatgpt_connection_is_not_git_push() -> None:
    text = (OPTIONAL / "chatgpt-github.md").read_text(encoding="utf-8")
    for token in ("Settings", "Plugins", "GitHub", "Không", "token", "git push"):
        assert token.casefold() in text.casefold()


def test_week01_marked_ai_tools_optional() -> None:
    readme = (WEEK / "README.md").read_text(encoding="utf-8")
    assert "công cụ tùy chọn" in readme
    assert "Không cần cài" in readme
    assert "optional-tools/google-antigravity.md" in readme
    assert "optional-tools/chatgpt-github.md" in readme
