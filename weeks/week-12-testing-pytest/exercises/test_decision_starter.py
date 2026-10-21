"""Complete learner tests: normal, edge, invalid, regression."""

import pytest

try:
    from .decision import LOCAL_ACTIONS, choose_action, validate_turn
except ImportError:
    from decision import LOCAL_ACTIONS, choose_action, validate_turn


def test_normal_case() -> None:
    position, goal = 1, 4
    action = choose_action(position, goal)
    assert action == "right"
    assert action in LOCAL_ACTIONS


def test_edge_case_at_goal() -> None:
    assert choose_action(4, 4) == "wait"


def test_invalid_turn() -> None:
    with pytest.raises(ValueError, match="positive"):
        validate_turn(0)


def test_regression_position_past_goal_moves_left() -> None:
    assert choose_action(4, 1) == "left"
    assert choose_action(4, 1) in LOCAL_ACTIONS
