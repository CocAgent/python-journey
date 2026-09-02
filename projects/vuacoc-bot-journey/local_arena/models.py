"""Small result models for the course-local Line Arena."""

from dataclasses import dataclass


@dataclass(frozen=True)
class TurnRecord:
    """One completed transition in a local match."""

    turn_number: int
    state_before: dict[str, int]
    bot_a_action: str
    bot_b_action: str
    state_after: dict[str, int]

    def to_dict(self) -> dict[str, object]:
        """Return JSON-compatible turn data."""
        return {
            "turn_number": self.turn_number,
            "state_before": self.state_before.copy(),
            "bot_a_action": self.bot_a_action,
            "bot_b_action": self.bot_b_action,
            "state_after": self.state_after.copy(),
        }


@dataclass(frozen=True)
class MatchResult:
    """Outcome and replay records from one local match."""

    status: str
    winner: str | None
    reason: str
    turns: list[TurnRecord]
    final_state: dict[str, int]
    max_turns: int

    def to_dict(self) -> dict[str, object]:
        """Return JSON-compatible match data."""
        return {
            "status": self.status,
            "winner": self.winner,
            "reason": self.reason,
            "turns": [turn.to_dict() for turn in self.turns],
            "final_state": self.final_state.copy(),
            "max_turns": self.max_turns,
        }
