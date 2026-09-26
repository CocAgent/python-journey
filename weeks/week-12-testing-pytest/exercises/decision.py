"""Behavior under test in the Week 12 exercise."""

LOCAL_ACTIONS = {"left", "right", "wait"}


def choose_action(position: int, goal: int) -> str:
    if position == goal:
        return "wait"
    return "right" if position < goal else "left"


def validate_turn(turn: int) -> int:
    if turn < 1:
        raise ValueError("turn must be positive")
    return turn
