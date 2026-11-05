"""Mini-project Tuần 14: Lớp Bot sử dụng Composition."""

from __future__ import annotations

from collections.abc import Callable

Strategy = Callable[[dict[str, int]], str]


class Bot:
    """Bot quản lý trạng thái và ủy nhiệm hành động cho Strategy đã chọn."""

    def __init__(self, strategy: Strategy, name: str = "MiniBot") -> None:
        self.strategy = strategy
        self.name = name

    def choose_action(self, state: dict[str, int]) -> str:
        """Thực thi chiến lược hiện tại mà không tự ý sửa state."""
        return self.strategy(state)

    def set_strategy(self, new_strategy: Strategy) -> None:
        """Thay đổi chiến lược linh hoạt lúc runtime."""
        self.strategy = new_strategy

    def __str__(self) -> str:
        strat_name = getattr(self.strategy, "__name__", str(self.strategy))
        return f"Bot(name={self.name}, strategy={strat_name})"
