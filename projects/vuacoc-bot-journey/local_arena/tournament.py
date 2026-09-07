"""Deterministic course-local tournament helpers."""

from collections.abc import Callable

from local_arena.arena import run_match

Bot = Callable[[dict[str, int]], str]


def evaluate_bot(
    student_bot: Bot,
    opponents: dict[str, Bot],
) -> list[dict[str, str | int]]:
    """Run the student as bot A once against each named baseline."""
    standings = []
    for opponent_name, opponent in opponents.items():
        result = run_match(student_bot, opponent)
        outcome = "win" if result.winner == "A" else "loss"
        if result.winner is None:
            outcome = "draw"
        standings.append(
            {
                "opponent": opponent_name,
                "outcome": outcome,
                "turns": len(result.turns),
                "reason": result.reason,
            }
        )
    return standings
