"""Behavior tests for the bounded course-local arena."""

from baselines.forward_bot import choose_action as forward_bot
from baselines.wait_bot import choose_action as wait_bot
from local_arena.arena import LOCAL_ACTIONS, run_match
from student_bot.bot import choose_action as student_bot


def illegal_action_bot(state: dict[str, int]) -> str:
    """Return the required negative-control action."""
    return "teleport"


def exception_bot(state: dict[str, int]) -> str:
    """Raise the required negative-control exception."""
    raise RuntimeError("negative control")


def test_engine_max_turns_bounds_non_progressing_strategies() -> None:
    result = run_match(wait_bot, wait_bot, max_turns=3)

    assert result.status == "completed"
    assert result.winner is None
    assert result.reason == "max_turns_reached"
    assert len(result.turns) == 3


def test_same_inputs_produce_same_result_and_replay() -> None:
    first = run_match(forward_bot, wait_bot)
    second = run_match(forward_bot, wait_bot)

    assert first.to_dict() == second.to_dict()


def test_illegal_local_action_fails_closed() -> None:
    result = run_match(illegal_action_bot, wait_bot)

    assert result.status == "bot_failure"
    assert result.winner == "B"
    assert result.reason == "bot A returned illegal local action: 'teleport'"
    assert result.turns == []


def test_bot_exception_is_recorded_not_silently_swallowed() -> None:
    result = run_match(exception_bot, wait_bot)

    assert result.status == "bot_failure"
    assert result.winner == "B"
    assert "RuntimeError: negative control" in result.reason
    assert result.turns == []


def test_student_starter_participates_with_a_legal_action() -> None:
    result = run_match(student_bot, forward_bot)

    assert student_bot({}) in LOCAL_ACTIONS
    assert result.status == "completed"
    assert 1 <= len(result.turns) <= result.max_turns
