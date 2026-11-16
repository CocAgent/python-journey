"""Behavior tests for the course-local Week 15 tournament."""

from baselines.cautious_bot import choose_action as cautious_bot
from baselines.forward_bot import choose_action as forward_bot
from baselines.wait_bot import choose_action as wait_bot
from local_arena.tournament import evaluate_bot, summarize_results
from student_bot.bot import choose_action as student_bot

OPPONENTS = {
    "wait": wait_bot,
    "forward": forward_bot,
    "cautious": cautious_bot,
}


def illegal_bot(state: dict[str, int]) -> str:
    """Return an illegal action for summary negative control."""
    return "teleport"


def test_tournament_is_deterministic_and_covers_three_baselines() -> None:
    first = evaluate_bot(student_bot, OPPONENTS)
    second = evaluate_bot(student_bot, OPPONENTS)

    assert first == second
    assert [row["opponent"] for row in first] == [
        "wait",
        "wait",
        "forward",
        "forward",
        "cautious",
        "cautious",
    ]
    assert [row["student_seat"] for row in first] == ["A", "B"] * 3
    assert all(row["outcome"] in {"win", "draw", "loss"} for row in first)


def test_tournament_summary_reports_course_local_metrics() -> None:
    rows = evaluate_bot(student_bot, OPPONENTS)
    summary = summarize_results(rows)

    assert summary["matches"] == 6
    assert summary["wins"] + summary["draws"] + summary["losses"] == 6
    assert summary["match_completion_rate"] == 1.0
    assert summary["legal_action_rate"] == 1.0
    assert summary["known_failure_count"] == 0


def test_tournament_summary_counts_student_contract_failures() -> None:
    rows = evaluate_bot(illegal_bot, {"wait": wait_bot})
    summary = summarize_results(rows)

    assert summary["matches"] == 2
    assert summary["match_completion_rate"] == 0.0
    assert summary["legal_action_rate"] == 0.0
    assert summary["known_failure_count"] == 2
