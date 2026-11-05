"""Ví dụ test quyết định đi về mục tiêu bằng Arrange → Act → Assert."""

from decisions import choose_step


def test_choose_step_moves_toward_goal() -> None:
    # Arrange: chuẩn bị vị trí và mục tiêu.
    position, goal = 1, 4

    # Act: gọi hàm cần kiểm chứng.
    action = choose_step(position, goal)

    # Assert: so sánh với hành động phải xảy ra.
    assert action == "right"


def test_choose_step_waits_at_goal() -> None:
    # Biên: đã tới đích, bot phải đứng yên.
    assert choose_step(4, 4) == "wait"


def test_choose_step_moves_left_when_goal_is_smaller() -> None:
    # Hồi quy: cần bắt lỗi bot luôn đi "right".
    assert choose_step(4, 1) == "left"
