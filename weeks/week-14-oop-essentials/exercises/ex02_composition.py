"""Bài 2: thay chiến lược Bot bằng composition thay vì kế thừa."""


class Bot:
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