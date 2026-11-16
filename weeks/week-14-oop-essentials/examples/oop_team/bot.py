"""Bot chỉ chịu trách nhiệm ủy nhiệm quyết định cho chiến lược."""

from collections.abc import Callable

Strategy = Callable[[dict[str, int]], str]


class Bot:
    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        # Không đặt thuật toán chiến lược vào trong class.
        return self.strategy(state)
