
"""Tests for Week 12 decision behavior."""
import pytest
from .decision import choose_action, validate_turn
# Test 01: Normal case
def test_move_right():
    assert choose_action(1, 4) == "right"
# Test 02: Edge case
def test_at_goal():
    assert choose_action(4, 4) == "wait"
# Test 03: Invalid case
def test_invalid_turn():
    with pytest.raises(ValueError):
        validate_turn(0)
# Test 04: Regression test
def test_move_left():
    assert choose_action(5, 2) == "left"