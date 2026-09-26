"""Example pytest cases using Arrange, Act, Assert."""

from decisions import choose_step


def test_choose_step_moves_toward_goal() -> None:
    # Arrange
    position, goal = 1, 4
    # Act
    action = choose_step(position, goal)
    # Assert
    assert action == "right"


def test_choose_step_waits_at_goal() -> None:
    assert choose_step(4, 4) == "wait"
