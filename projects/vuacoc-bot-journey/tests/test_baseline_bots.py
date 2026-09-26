"""Behavior tests for exactly three transparent local baselines."""

import pytest
from baselines.cautious_bot import choose_action as cautious_bot
from baselines.forward_bot import choose_action as forward_bot
from baselines.wait_bot import choose_action as wait_bot
from local_arena.arena import LOCAL_ACTIONS

BASELINES = (wait_bot, forward_bot, cautious_bot)


def teaching_state(**changes: int) -> dict[str, int]:
    """Return a complete local state with optional field changes."""
    state = {
        "turn": 1,
        "max_turns": 6,
        "position": 0,
        "opponent_position": 4,
        "goal": 4,
        "min_position": 0,
        "max_position": 4,
    }
    state.update(changes)
    return state


def test_exactly_three_baselines_are_registered_for_checks() -> None:
    assert len(BASELINES) == 3


@pytest.mark.parametrize("bot", BASELINES)
def test_baseline_bots_are_deterministic_and_return_local_actions(bot) -> None:
    state = teaching_state()

    first = bot(state)
    second = bot(state)

    assert first == second
    assert first in LOCAL_ACTIONS


def test_wait_bot_always_waits() -> None:
    assert wait_bot(teaching_state()) == "wait"


def test_forward_bot_moves_toward_each_goal() -> None:
    assert forward_bot(teaching_state(position=1, goal=4)) == "right"
    assert forward_bot(teaching_state(position=3, goal=0)) == "left"
    assert forward_bot(teaching_state(position=4, goal=4)) == "wait"


def test_cautious_bot_waits_when_opponent_is_near() -> None:
    state = teaching_state(position=1, opponent_position=2, goal=4)

    assert cautious_bot(state) == "wait"
