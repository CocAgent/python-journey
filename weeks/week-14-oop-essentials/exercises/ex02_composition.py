"""Bài 2: thay chiến lược Bot bằng composition thay vì kế thừa."""


class Bot:
    def __init__(self, strategy) -> None:
        # TODO: lưu hàm chiến lược vào self.strategy.
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        # TODO: gọi chính strategy đã nhận, không cố định một hành động.
        return self.strategy(state)


def defensive(state: dict[str, int]) -> str:
    """Đứng yên khi đối thủ ở cách tối đa 1 ô; nếu không thì hướng tới đích."""
    # TODO: opponent_position có thể không tồn tại.
    opponent = state.get("opponent_position")

    if opponent is not None:
        if abs(opponent - state["position"]) <= 1:
            return "wait"

    return balanced(state)


def balanced(state: dict[str, int]) -> str:
    """Đi về goal ở cả hai chiều; tại goal thì đứng yên."""
    if state["position"] < state["goal"]:
        return "right"

    if state["position"] > state["goal"]:
        return "left"

    return "wait"


def aggressive(state: dict[str, int]) -> str:
    """Trong mô hình 1 chiều cơ bản, vẫn đi về đích như balanced."""
    # TODO: chưa cần tạo chiến thuật tấn công phức tạp hoặc luật arena.
    return balanced(state)


if __name__ == "__main__":
    state = {"position": 3, "goal": 0, "opponent_position": 4}
    bot = Bot(defensive)
    print(bot.choose_action(state))
    bot.strategy = balanced
    print(bot.choose_action(state))
