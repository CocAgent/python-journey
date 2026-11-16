"""Replay helpers for the course-local Line Arena."""

import json
from pathlib import Path

from local_arena.arena import LOCAL_ACTIONS, MAX_POSITION, MIN_POSITION
from local_arena.models import MatchResult

FORMAT_LABEL = "COURSE LOCAL FORMAT"
PRODUCTION_LABEL = "NOT VUACOC PRODUCTION FORMAT"
STATE_KEYS = {"bot_a_position", "bot_b_position"}
TURN_KEYS = {
    "turn_number",
    "state_before",
    "bot_a_action",
    "bot_b_action",
    "state_after",
}


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _validate_state(value: object, label: str) -> None:
    if not isinstance(value, dict) or not STATE_KEYS <= value.keys():
        raise ValueError(f"{label} must contain both bot positions")
    if not all(_is_int(value[key]) for key in STATE_KEYS):
        raise ValueError(f"{label} positions must be integers")
    if not all(MIN_POSITION <= value[key] <= MAX_POSITION for key in STATE_KEYS):
        raise ValueError(f"{label} positions are outside the local board")


def validate_replay(data: dict[str, object]) -> None:
    """Validate required course-local replay fields and turn records."""
    if data.get("status") not in {"completed", "bot_failure"}:
        raise ValueError("Replay status is invalid")
    if data.get("winner") not in {None, "A", "B"}:
        raise ValueError("Replay winner is invalid")
    if not isinstance(data.get("reason"), str):
        raise ValueError("Replay reason must be a string")
    max_turns = data.get("max_turns")
    if not _is_int(max_turns) or max_turns < 1:
        raise ValueError("Replay max_turns must be a positive integer")
    _validate_state(data.get("final_state"), "final_state")

    turns = data.get("turns")
    if not isinstance(turns, list):
        raise ValueError("Replay turns must be a list")
    if len(turns) > max_turns:
        raise ValueError("Replay has more turns than max_turns")
    for expected_number, turn in enumerate(turns, start=1):
        if not isinstance(turn, dict) or not TURN_KEYS <= turn.keys():
            raise ValueError(f"Replay turn {expected_number} is incomplete")
        if turn["turn_number"] != expected_number:
            raise ValueError("Replay turn numbers must be consecutive")
        if turn["bot_a_action"] not in LOCAL_ACTIONS:
            raise ValueError(f"Replay turn {expected_number} has invalid bot A action")
        if turn["bot_b_action"] not in LOCAL_ACTIONS:
            raise ValueError(f"Replay turn {expected_number} has invalid bot B action")
        _validate_state(turn["state_before"], f"turn {expected_number} state_before")
        _validate_state(turn["state_after"], f"turn {expected_number} state_after")


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


def load_replay(source: Path) -> dict[str, object]:
    """Load and validate a course-local replay JSON object."""
    data = json.loads(source.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Replay must be a JSON object")
    if data.get("format") != FORMAT_LABEL:
        raise ValueError("Unknown replay format")
    if data.get("production_compatibility") != PRODUCTION_LABEL:
        raise ValueError("Replay compatibility label is missing")
    validate_replay(data)
    return data


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
