"""Passing reference tests for Week 12 learner behavior."""

import pytest
from exercises.decision import LOCAL_ACTIONS, choose_action, validate_turn


def test_normal_case_moves_toward_goal() -> None:
    # Arrange
    position, goal = 1, 4
    # Act
    action = choose_action(position, goal)
    # Assert
    assert action == "right"
    assert action in LOCAL_ACTIONS


def test_edge_case_waits_at_goal() -> None:
    assert choose_action(4, 4) == "wait"


def test_invalid_turn_is_rejected() -> None:
    with pytest.raises(ValueError, match="positive"):
        validate_turn(0)


def test_regression_position_past_goal_moves_left() -> None:
    assert choose_action(4, 1) == "left"
