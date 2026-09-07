"""Behavior tests for the course-local Week 15 tournament."""

from baselines.cautious_bot import choose_action as cautious_bot
from baselines.forward_bot import choose_action as forward_bot
from baselines.wait_bot import choose_action as wait_bot
from local_arena.tournament import evaluate_bot
from student_bot.bot import choose_action as student_bot

OPPONENTS = {
    "wait": wait_bot,
    "forward": forward_bot,
    "cautious": cautious_bot,
}


def test_tournament_is_deterministic_and_covers_three_baselines() -> None:
    first = evaluate_bot(student_bot, OPPONENTS)
    second = evaluate_bot(student_bot, OPPONENTS)

    assert first == second
    assert [row["opponent"] for row in first] == ["wait", "forward", "cautious"]
    assert all(row["outcome"] in {"win", "draw", "loss"} for row in first)
