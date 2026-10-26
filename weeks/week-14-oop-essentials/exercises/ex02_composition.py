"""Bài 2: thay chiến lược Bot bằng composition thay vì kế thừa."""


class Bot:
    def __init__(self, strategy) -> None:
        # TODO: lưu hàm chiến lược vào self.strategy.
        raise NotImplementedError("TODO: lưu strategy")

    def choose_action(self, state: dict[str, int]) -> str:
        # TODO: gọi chính strategy đã nhận, không cố định một hành động.
        raise NotImplementedError("TODO: ủy nhiệm choose_action")


def defensive(state: dict[str, int]) -> str:
    """Đứng yên khi đối thủ ở cách tối đa 1 ô; nếu không thì hướng tới đích."""
    # TODO: opponent_position có thể không tồn tại.
    raise NotImplementedError("TODO: chiến lược defensive")


def balanced(state: dict[str, int]) -> str:
    """Đi về goal ở cả hai chiều; tại goal thì đứng yên."""
    raise NotImplementedError("TODO: chiến lược balanced")


def aggressive(state: dict[str, int]) -> str:
    """Trong mô hình 1 chiều cơ bản, vẫn đi về đích như balanced."""
    # TODO: chưa cần tạo chiến thuật tấn công phức tạp hoặc luật arena.
    raise NotImplementedError("TODO: chiến lược aggressive")
