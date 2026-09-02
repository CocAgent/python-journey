"""Replay helpers for the course-local Line Arena."""

import json
from pathlib import Path

from local_arena.models import MatchResult

FORMAT_LABEL = "COURSE LOCAL FORMAT"
PRODUCTION_LABEL = "NOT VUACOC PRODUCTION FORMAT"


def replay_data(result: MatchResult) -> dict[str, object]:
    """Return a labeled JSON-compatible replay."""
    data = result.to_dict()
    return {
        "format": FORMAT_LABEL,
        "production_compatibility": PRODUCTION_LABEL,
        **data,
    }


def save_replay(result: MatchResult, destination: Path) -> Path:
    """Write replay data after a match and return the destination path."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(replay_data(result), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return destination


def concise_summary(result: MatchResult) -> str:
    """Return a short human-readable replay summary."""
    lines = [
        FORMAT_LABEL,
        PRODUCTION_LABEL,
        f"status={result.status} winner={result.winner} reason={result.reason}",
    ]
    for turn in result.turns:
        before = turn.state_before
        after = turn.state_after
        lines.append(
            f"turn={turn.turn_number} "
            f"before=({before['bot_a_position']},{before['bot_b_position']}) "
            f"actions=({turn.bot_a_action},{turn.bot_b_action}) "
            f"after=({after['bot_a_position']},{after['bot_b_position']})"
        )
    return "\n".join(lines)
