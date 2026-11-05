"""Module định nghĩa lớp Bot với kiến trúc Composition.

Bot không tự quyết định thuật toán chi tiết mà ủy nhiệm quyết định
cho một đối tượng chiến lược (Strategy) được truyền vào qua __init__.
"""

from collections.abc import Callable

Strategy = Callable[[dict[str, int]], str]


class Bot:
    """Lớp Bot đại diện cho tác tử trên sân đấu 1 chiều."""

    def __init__(self, strategy: Strategy) -> None:
        """Khởi tạo Bot với một chiến lược ban đầu.

        Args:
            strategy: Hàm nhận state và trả về hành động ("left", "right", "wait").
        """
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        """Chọn hành động bằng cách ủy quyền trực tiếp cho self.strategy.

        Args:
            state: Từ điển chứa trạng thái hiện tại (position, goal, v.v.).

        Returns:
            Hành động được chọn: "left", "right", hoặc "wait".
        """
        return self.strategy(state)
