"""Kiem thu cac ham bang pytest."""

import pytest
from buggy_program import add_numbers, choose_action, validate_turn


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_at_goal_waits():
    assert choose_action(4, 4) == "wait"


def test_past_goal_moves_left():
    assert choose_action(5, 2) == "left"


def test_turn_zero_is_invalid():
    with pytest.raises(ValueError):
        validate_turn(0)