"""Tuần 12 — Tự viết kiểm thử cho chương trình ra quyết định.

Bài tập: sửa từng hàm test theo mô hình Chuẩn bị → Thực hiện → Kiểm tra.
Ban đầu các test CỐ Ý báo chưa hoàn thành, để tránh PASS giả.
"""

import pytest

from decision import choose_action, validate_turn


def test_normal_case() -> None:
    # TODO: Cho position=1, goal=4. Hãy dự đoán hành động chính xác.
    # Sau đó dùng assert so sánh kết quả thực tế với kết quả dự đoán.
    raise NotImplementedError("Hãy tự viết assert cho trường hợp thông thường")


def test_edge_case_at_goal() -> None:
    # TODO: Khi position bằng goal, bot nên thực hiện hành động nào?
    # Dùng phép so sánh chính xác, không chỉ kiểm tra action thuộc tập hợp.
    raise NotImplementedError("Hãy tự viết assert cho trường hợp biên")


def test_invalid_turn() -> None:
    # TODO: Dùng with pytest.raises(ValueError) để kiểm tra validate_turn(0).
    # Trường hợp này phải ném lỗi; không được chỉ kiểm tra validate_turn(1).
    raise NotImplementedError("Hãy tự kiểm chứng đầu vào không hợp lệ")


def test_regression_position_past_goal_moves_left() -> None:
    # TODO: Với position=4, goal=1, kiểm tra hướng đi CHÍNH XÁC.
    # Mục tiêu: phát hiện lỗi bot luôn trả về cùng một hướng.
    raise NotImplementedError("Hãy bổ sung bài kiểm thử hồi quy")
