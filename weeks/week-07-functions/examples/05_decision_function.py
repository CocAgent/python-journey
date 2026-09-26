"""TEACHING MODEL — NOT VUACOC PRODUCTION CONTRACT.

This example introduces only: state → decision function → action.
"""

ALLOWED_ACTIONS = ("defend", "advance", "wait")


def choose_action(state: str) -> str:
    """Choose one deterministic action for a small teaching state."""
    if state == "danger":
        return "defend"
    if state == "opportunity":
        return "advance"
    return "wait"


def explain_decision(state: str) -> str:
    """Build a human-readable line from a state and its returned action."""
    action = choose_action(state)
    return f"state={state!r} → action={action!r}"


def main() -> None:
    """Show that the same input always produces the same output."""
    teaching_states = ("danger", "opportunity", "neutral", "unknown")
    for state in teaching_states:
        print(explain_decision(state))

    first = choose_action("danger")
    second = choose_action("danger")
    print(f"Deterministic: {first == second}")
    print(f"Action thuộc teaching set: {first in ALLOWED_ACTIONS}")


if __name__ == "__main__":
    main()
