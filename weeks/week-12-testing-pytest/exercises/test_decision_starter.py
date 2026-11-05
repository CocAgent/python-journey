"""Learner tests using Arrange → Act → Assert."""

import pytest

from decision import choose_action, validate_turn


def test_normal_case() -> None:
    position = 1
    goal = 4
    action = choose_action(position, goal)
    assert action == "right"


def test_edge_case_at_goal() -> None:
    action = choose_action(4, 4)
    assert action == "wait"


def test_invalid_turn() -> None:
    with pytest.raises(ValueError, match="turn must be positive"):
        validate_turn(0)


def test_regression_position_past_goal_moves_left() -> None:
    assert choose_action(4, 1) == "left"
