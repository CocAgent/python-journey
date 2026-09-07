"""Complete these learner tests."""

from decision import LOCAL_ACTIONS, choose_action, validate_turn


def test_normal_case() -> None:
    # TODO: Arrange position/goal, Act, then Assert the expected action.
    assert choose_action(1, 4) in LOCAL_ACTIONS


def test_edge_case_at_goal() -> None:
    # TODO: assert the bot waits at its goal.
    assert choose_action(4, 4) in LOCAL_ACTIONS


def test_invalid_turn() -> None:
    # TODO: use pytest.raises(ValueError) for validate_turn(0).
    assert validate_turn(1) == 1


def test_regression_position_past_goal_moves_left() -> None:
    # Regression: an earlier version always returned "right".
    assert choose_action(4, 1) in LOCAL_ACTIONS
