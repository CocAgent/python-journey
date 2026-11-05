"""Bài 2: thay chiến lược Bot bằng composition thay vì kế thừa."""


class Bot:
<<<<<<< HEAD
    def __init__(self, strategy):
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        return self.strategy(state)


# Hàm di chuyển về phía mục tiêu
def move_toward_goal(state: dict[str, int]) -> str:
    if state["position"] < state["goal"]:
        return "right"

    if state["position"] > state["goal"]:
        return "left"

    return "wait"


# Chiến lược phòng thủ
def defensive(state: dict[str, int]) -> str:
    opponent = state.get("opponent_position")

    if opponent is not None:
        if abs(opponent - state["position"]) <= 1:
            return "wait"

    return move_toward_goal(state)


# Chiến lược cân bằng
def balanced(state: dict[str, int]) -> str:
    return move_toward_goal(state)


# Chiến lược tấn công
def aggressive(state: dict[str, int]) -> str:
    return move_toward_goal(state)


if __name__ == "__main__":
    state = {
        "position": 3,
        "goal": 0,
        "opponent_position": 4
    }

    bot = Bot(defensive)

    print(bot.choose_action(state))

    # Thay đổi chiến lược
    bot.strategy = balanced

    print(bot.choose_action(state))
=======
    def __init__(self, strategy) -> None:
        # TODO: lưu hàm chiến lược vào self.strategy.
        raise NotImplementedError("TODO: lưu strategy")

    def choose_action(self, state: dict[str, int]) -> str:
        # TODO: gọi chính strategy đã nhận, không cố định một hành động.
        raise NotImplementedError("TODO: ủy nhiệm choose_action")


def defensive(state: dict[str, int]) -> str:
    """Đứng yên khi đối thủ ở cách tối đa 1 ô; nếu không thì hướng tới đích."""
    # TODO: opponent_position có thể không tồn tại.
    raise NotImplementedError("TODO: chiến lược defensive")


def balanced(state: dict[str, int]) -> str:
    """Đi về goal ở cả hai chiều; tại goal thì đứng yên."""
    raise NotImplementedError("TODO: chiến lược balanced")


def aggressive(state: dict[str, int]) -> str:
    """Trong mô hình 1 chiều cơ bản, vẫn đi về đích như balanced."""
    # TODO: chưa cần tạo chiến thuật tấn công phức tạp hoặc luật arena.
    raise NotImplementedError("TODO: chiến lược aggressive")
>>>>>>> dee0edc325298ea1e9c1e3b79a31da2a169d47d5
