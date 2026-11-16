"""Bài tập Tuần 12 — Sinh viên tự viết bốn phép kiểm thử.

Các phép kiểm tra ban đầu CỐ Ý FAIL để không tạo kết quả PASS giả.
Hãy thay mỗi pytest.fail(...) bằng câu lệnh tự viết.
"""

import pytest

from decision import choose_action, validate_turn


def test_normal_case() -> None:
    # TODO: Với position=1, goal=4, bot phải chọn một hành động CHÍNH XÁC.
    # Tự dùng Arrange → Act → Assert để kiểm tra kết quả mong đợi.
    pytest.fail("TODO 1: chưa kiểm tra bot đi về bên phải")


def test_edge_case_at_goal() -> None:
    # TODO: Khi position == goal, bot cần làm gì?
    # Test phải thất bại nếu bot vẫn di chuyển dù đã tới đích.
    pytest.fail("TODO 2: chưa kiểm tra hành động khi đã tới đích")


def test_invalid_turn() -> None:
    # TODO: validate_turn(0) phải báo lỗi ValueError.
    # Gợi ý: dùng with pytest.raises(ValueError): thay cho assert với lượt 1.
    pytest.fail("TODO 3: chưa kiểm tra lượt chơi không hợp lệ")


def test_regression_position_past_goal_moves_left() -> None:
    # TODO: Với position=4, goal=1, bot phải đi về bên nào?
    # Test cần phát hiện lỗi cũ "bot luôn đi phải".
    pytest.fail("TODO 4: chưa kiểm tra lỗi hồi quy đi sai hướng")
