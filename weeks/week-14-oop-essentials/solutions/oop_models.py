"""Lời giải tham chiếu OOP Tuần 14: lớp, kết hợp và kế thừa."""

from collections.abc import Callable

Strategy = Callable[[dict[str, int]], str]


class Progress:
    """Theo dõi số việc đã hoàn thành trong một tổng số việc."""

    def __init__(self, completed: int, total: int) -> None:
        if total <= 0:
            raise ValueError("total must be positive")
        if not 0 <= completed <= total:
            raise ValueError("completed must be between 0 and total")
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        """Trả về phần trăm hoàn thành, không sửa dữ liệu của object."""
        return self.completed / self.total * 100

    def __str__(self) -> str:
        """Biểu diễn dễ đọc, không in hoặc thay đổi trạng thái."""
        return (
            f"Progress: {self.completed}/{self.total} "
            f"({self.percentage():.0f}%)"
        )


class Bot:
    """Một bot chứa chiến lược; không cần kế thừa để đổi chiến lược."""

    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        """Ủy nhiệm việc chọn hành động cho chiến lược hiện tại."""
        return self.strategy(state)


def move_toward_goal(state: dict[str, int]) -> str:
    """Chọn hướng tới mục tiêu kể cả khi mục tiêu nằm bên trái."""
    if state["position"] < state["goal"]:
        return "right"
    if state["position"] > state["goal"]:
        return "left"
    return "wait"


def defensive(state: dict[str, int]) -> str:
    """Ưu tiên đứng yên nếu đối thủ ở sát vị trí hiện tại."""
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state: dict[str, int]) -> str:
    """Di chuyển theo hướng tới mục tiêu."""
    return move_toward_goal(state)


def aggressive(state: dict[str, int]) -> str:
    """Ví dụ tối giản: tiến tới mục tiêu, chưa có quy tắc tấn công riêng."""
    return move_toward_goal(state)


class Animal:
    """Ví dụ lớp cha: mỗi động vật có tên."""

    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):
    """Dog là một Animal và có thêm hành vi sủa."""

    def speak(self) -> str:
        return f"{self.name}: woof"
