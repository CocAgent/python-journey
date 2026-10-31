"""Các chiến lược độc lập để có thể đổi mà không sửa Bot."""


def toward_goal(state: dict[str, int]) -> str:
    if state["position"] < state["goal"]:
        return "right"
    if state["position"] > state["goal"]:
        return "left"
    return "wait"


def defensive(state: dict[str, int]) -> str:
    # Dùng get vì dữ liệu đối thủ không phải lúc nào cũng có.
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return toward_goal(state)


def balanced(state: dict[str, int]) -> str:
    return toward_goal(state)
