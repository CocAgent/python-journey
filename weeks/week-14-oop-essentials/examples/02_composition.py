"""Compose a bot with a replaceable strategy."""

from collections.abc import Callable

Strategy = Callable[[dict[str, int]], str]


class Bot:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        return self.strategy(state)


def defensive(state: dict[str, int]) -> str:
    return "wait"


print(Bot(defensive).choose_action({"turn": 1}))
