"""Deterministic course-local tournament helpers."""

from collections.abc import Callable

from local_arena.arena import run_match
from local_arena.models import MatchResult

Bot = Callable[[dict[str, int]], str]
TournamentRow = dict[str, str | int]


def _outcome(result: MatchResult, student_seat: str) -> str:
    if result.winner is None:
        return "draw"
    return "win" if result.winner == student_seat else "loss"


def _student_action_counts(
    result: MatchResult, student_seat: str
) -> tuple[int, int]:
    """Return legal and attempted student actions, including a failed turn."""
    legal = len(result.turns)
    attempts = len(result.turns)
    if result.status != "bot_failure":
        return legal, attempts

    failing_seat = "A" if result.winner == "B" else "B"
    if student_seat == failing_seat:
        return legal, attempts + 1
    if student_seat == "A" and failing_seat == "B":
        return legal + 1, attempts + 1
    return legal, attempts


def evaluate_bot(
    student_bot: Bot,
    opponents: dict[str, Bot],
) -> list[TournamentRow]:
    """Run the student in both seats against each named baseline."""
    standings: list[TournamentRow] = []
    for opponent_name, opponent in opponents.items():
        matches = (
            ("A", run_match(student_bot, opponent)),
            ("B", run_match(opponent, student_bot)),
        )
        for student_seat, result in matches:
            legal, attempts = _student_action_counts(result, student_seat)
            standings.append(
                {
                    "opponent": opponent_name,
                    "student_seat": student_seat,
                    "outcome": _outcome(result, student_seat),
                    "status": result.status,
                    "turns": len(result.turns),
                    "reason": result.reason,
                    "student_legal_actions": legal,
                    "student_action_attempts": attempts,
                }
            )
    return standings


def summarize_results(rows: list[TournamentRow]) -> dict[str, int | float]:
    """Summarize transparent course-local metrics without a rating score."""
    matches = len(rows)
    completed = sum(row["status"] == "completed" for row in rows)
    attempts = sum(int(row["student_action_attempts"]) for row in rows)
    legal = sum(int(row["student_legal_actions"]) for row in rows)
    return {
        "matches": matches,
        "wins": sum(row["outcome"] == "win" for row in rows),
        "draws": sum(row["outcome"] == "draw" for row in rows),
        "losses": sum(row["outcome"] == "loss" for row in rows),
        "match_completion_rate": completed / matches if matches else 0.0,
        "legal_action_rate": legal / attempts if attempts else 0.0,
        "known_failure_count": matches - completed,
    }
