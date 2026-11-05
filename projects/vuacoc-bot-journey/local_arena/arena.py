"""Deterministic engine for the course-local Line Arena."""

from local_arena.models import MatchResult, TurnRecord

MIN_POSITION = 0
MAX_POSITION = 4
DEFAULT_MAX_TURNS = 6
LOCAL_ACTIONS = ("left", "right", "wait")


def initial_state() -> dict[str, int]:
    """Return a fresh match state."""
    return {
        "bot_a_position": MIN_POSITION,
        "bot_b_position": MAX_POSITION,
    }


def bot_view(
    state: dict[str, int], bot_name: str, turn: int, max_turns: int
) -> dict[str, int]:
    """Build a course-local state from one bot's perspective."""
    if bot_name == "A":
        position = state["bot_a_position"]
        opponent_position = state["bot_b_position"]
        goal = MAX_POSITION
    else:
        position = state["bot_b_position"]
        opponent_position = state["bot_a_position"]
        goal = MIN_POSITION

    return {
        "turn": turn,
        "max_turns": max_turns,
        "position": position,
        "opponent_position": opponent_position,
        "goal": goal,
        "min_position": MIN_POSITION,
        "max_position": MAX_POSITION,
    }


def transition(position: int, action: str) -> int:
    """Apply one validated local action to one position."""
    if action == "left":
        return max(MIN_POSITION, position - 1)
    if action == "right":
        return min(MAX_POSITION, position + 1)
    return position


def failure_result(
    failing_bot: str,
    reason: str,
    state: dict[str, int],
    turns: list[TurnRecord],
    max_turns: int,
) -> MatchResult:
    """Return a deterministic fail-closed result."""
    winner = "B" if failing_bot == "A" else "A"
    return MatchResult(
        status="bot_failure",
        winner=winner,
        reason=reason,
        turns=turns,
        final_state=state.copy(),
        max_turns=max_turns,
    )


def call_bot(bot, view: dict[str, int], bot_name: str) -> tuple[str | None, str | None]:
    """Call a bot and return either its action or an explicit error."""
    try:
        action = bot(view.copy())
    except Exception as error:  # The arena boundary records learner bot failures.
        message = f"bot {bot_name} exception: {type(error).__name__}: {error}"
        return None, message
    return action, None


def run_match(bot_a, bot_b, max_turns: int = DEFAULT_MAX_TURNS) -> MatchResult:
    """Run one bounded deterministic course-local match."""
    if max_turns < 1:
        raise ValueError("max_turns must be at least 1")

    state = initial_state()
    turns: list[TurnRecord] = []

    for turn_number in range(1, max_turns + 1):
        state_before = state.copy()
        action_a, error_a = call_bot(
            bot_a,
            bot_view(state_before, "A", turn_number, max_turns),
            "A",
        )
        if error_a is not None:
            return failure_result("A", error_a, state, turns, max_turns)

        action_b, error_b = call_bot(
            bot_b,
            bot_view(state_before, "B", turn_number, max_turns),
            "B",
        )
        if error_b is not None:
            return failure_result("B", error_b, state, turns, max_turns)

        if action_a not in LOCAL_ACTIONS:
            reason = f"bot A returned illegal local action: {action_a!r}"
            return failure_result("A", reason, state, turns, max_turns)
        if action_b not in LOCAL_ACTIONS:
            reason = f"bot B returned illegal local action: {action_b!r}"
            return failure_result("B", reason, state, turns, max_turns)

        state = {
            "bot_a_position": transition(state_before["bot_a_position"], action_a),
            "bot_b_position": transition(state_before["bot_b_position"], action_b),
        }
        turns.append(
            TurnRecord(
                turn_number=turn_number,
                state_before=state_before,
                bot_a_action=action_a,
                bot_b_action=action_b,
                state_after=state.copy(),
            )
        )

        bot_a_reached_goal = state["bot_a_position"] == MAX_POSITION
        bot_b_reached_goal = state["bot_b_position"] == MIN_POSITION
        if bot_a_reached_goal and bot_b_reached_goal:
            return MatchResult(
                "completed", None, "both_reached_goal", turns, state, max_turns
            )
        if bot_a_reached_goal:
            return MatchResult(
                "completed", "A", "bot_a_reached_goal", turns, state, max_turns
            )
        if bot_b_reached_goal:
            return MatchResult(
                "completed", "B", "bot_b_reached_goal", turns, state, max_turns
            )

    return MatchResult("completed", None, "max_turns_reached", turns, state, max_turns)
