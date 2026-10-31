"""Bộ kiểm thử tham chiếu của giảng viên, không phải bài sinh viên."""

import pytest

from exercises.decision import LOCAL_ACTIONS, choose_action, validate_turn


@pytest.mark.parametrize(
    ("position", "goal", "expected"),
    [
        (1, 4, "right"),  # Thông thường: đích bên phải.
        (4, 1, "left"),  # Hồi quy: đích bên trái.
        (4, 4, "wait"),  # Biên: đang ở đúng vị trí đích.
        (0, 0, "wait"),  # Biên khác: đích tại vị trí 0.
    ],
)
def test_choose_action_exact_result(
    position: int, goal: int, expected: str
) -> None:
    # Kiểm tra hành động CỤ THỂ; membership một mình không phát hiện sai hướng.
    action = choose_action(position, goal)
    assert action == expected
    assert action in LOCAL_ACTIONS


@pytest.mark.parametrize("turn", [1, 2, 10])
def test_validate_turn_accepts_positive_values(turn: int) -> None:
    assert validate_turn(turn) == turn


@pytest.mark.parametrize("turn", [0, -1, -5])
def test_validate_turn_rejects_invalid_values(turn: int) -> None:
    # Đầu vào không hợp lệ phải báo exception, không được trả kết quả bình thường.
    with pytest.raises(ValueError, match="positive"):
        validate_turn(turn)
