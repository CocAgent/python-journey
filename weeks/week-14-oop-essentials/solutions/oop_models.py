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

    def __str__(self) -> str:
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.0f}%)"


class Bot:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        return self.strategy(state)


def move_toward_goal(state: dict[str, int]) -> str:
    """Return one step toward either course-local goal."""
    if state["position"] < state["goal"]:
        return "right"
    if state["position"] > state["goal"]:
        return "left"
    return "wait"


def defensive(state: dict[str, int]) -> str:
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state: dict[str, int]) -> str:
    return move_toward_goal(state)


def aggressive(state: dict[str, int]) -> str:
    return move_toward_goal(state)


class Animal:
    def __init__(self, name: str):
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name}: woof"
