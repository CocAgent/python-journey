"""Official Week 14 OOP essentials solutions."""

from collections.abc import Callable

Strategy = Callable[[dict[str, int]], str]


class Progress:
    def __init__(self, completed: int, total: int):
        if total < 1:
            raise ValueError("total must be positive")
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        return self.completed / self.total * 100


class Bot:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        return self.strategy(state)


def defensive(state: dict[str, int]) -> str:
    return "wait"


def balanced(state: dict[str, int]) -> str:
    return "right" if state["position"] < state["goal"] else "wait"


def aggressive(state: dict[str, int]) -> str:
    return "right"


class Animal:
    def __init__(self, name: str):
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name}: woof"
