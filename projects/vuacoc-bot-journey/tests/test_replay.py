"""Behavior tests for course-local replay evidence."""

import json

from baselines.forward_bot import choose_action as forward_bot
from baselines.wait_bot import choose_action as wait_bot
from local_arena.arena import run_match
from local_arena.replay import (
    FORMAT_LABEL,
    PRODUCTION_LABEL,
    concise_summary,
    replay_data,
    save_replay,
)


def test_replay_length_matches_completed_engine_turns() -> None:
    result = run_match(forward_bot, wait_bot)
    data = replay_data(result)

    assert len(data["turns"]) == len(result.turns)
    assert len(result.turns) == 4


def test_replay_is_json_compatible_and_clearly_labeled() -> None:
    result = run_match(forward_bot, wait_bot)
    data = replay_data(result)

    encoded = json.dumps(data, ensure_ascii=False)

    assert FORMAT_LABEL in encoded
    assert PRODUCTION_LABEL in encoded


def test_replay_can_be_saved_after_match(tmp_path) -> None:
    result = run_match(forward_bot, wait_bot)
    destination = save_replay(result, tmp_path / "replay.json")

    saved = json.loads(destination.read_text(encoding="utf-8"))

    assert len(saved["turns"]) == len(result.turns)
    assert saved["format"] == FORMAT_LABEL
    assert saved["production_compatibility"] == PRODUCTION_LABEL


def test_concise_summary_contains_each_required_turn_field() -> None:
    result = run_match(forward_bot, wait_bot)
    summary = concise_summary(result)

    assert "turn=1" in summary
    assert "before=" in summary
    assert "actions=" in summary
    assert "after=" in summary
