"""Mini-project: Bot class sử dụng composition để quản lý chiến lược di chuyển."""

from collections.abc import Callable

Strategy = Callable[[dict[str, int]], str]


class Bot:
    """Lớp Bot ủy quyền hành vi quyết định hành động cho một chiến lược độc lập."""

    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        """Thực thi chiến lược hiện tại với trạng thái môi trường."""
        return self.strategy(state)

