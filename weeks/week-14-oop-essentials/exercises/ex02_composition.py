"""Bài 2: thay chiến lược Bot bằng composition thay vì kế thừa."""


class Bot:
    def __init__(self, strategy) -> None:
        # TODO: lưu hàm chiến lược vào self.strategy.
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        # TODO: gọi chính strategy đã nhận, không cố định một hành động.
        return self.strategy(state)


def _move_toward_goal(state: dict[str, int]) -> str:
    position = state["position"]
    goal = state["goal"]

    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def defensive(state: dict[str, int]) -> str:
    """Đứng yên khi đối thủ ở cách tối đa 1 ô; nếu không thì hướng tới đích."""
    # TODO: opponent_position có thể không tồn tại.
    opponent_position = state.get("opponent_position")
    if (
        opponent_position is not None
        and abs(opponent_position - state["position"]) <= 1
    ):
        return "wait"
    return _move_toward_goal(state)


def balanced(state: dict[str, int]) -> str:
    """Đi về goal ở cả hai chiều; tại goal thì đứng yên."""
    return _move_toward_goal(state)


def aggressive(state: dict[str, int]) -> str:
    """Trong mô hình 1 chiều cơ bản, vẫn đi về đích như balanced."""
    # TODO: chưa cần tạo chiến thuật tấn công phức tạp hoặc luật arena.
    return _move_toward_goal(state)


if __name__ == "__main__":
    state = {"position": 1, "opponent_position": 4, "goal": 4}

    for name, strategy in (
        ("Defensive", defensive),
        ("Balanced", balanced),
        ("Aggressive", aggressive),
    ):
        bot = Bot(strategy)
        print(f"{name}: {bot.choose_action(state)}")

    reverse_state = {"position": 3, "goal": 0}
    print("Balanced toward goal 0:", Bot(balanced).choose_action(reverse_state))
