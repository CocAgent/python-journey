"""Ví dụ 08 — nested dict + optional field + guarded heuristic.

COURSE TEACHING MODEL — NOT VUACOC PRODUCTION CONTRACT.
Không gửi mạng, không động chạm runtime game.
"""


ACTIONS = {"left", "right", "wait"}


def valid_bot(bot: object) -> bool:
    """Các key bắt buộc phải có đúng kiểu và trong phạm vi giả lập 0..4."""
    if not isinstance(bot, dict):
        return False
    for key in ("position", "goal"):
        if key not in bot or type(bot[key]) is not int or not 0 <= bot[key] <= 4:
            return False
    if "opponent_position" not in bot:
        return True
    opponent = bot["opponent_position"]
    return type(opponent) is int and 0 <= opponent <= 4


def explain(state: dict[str, object]) -> str:
    """Không gọi thiếu/nhầm key là thành công, trả lý do rõ ràng."""
    bot = state.get("bot")
    if not valid_bot(bot):
        return "State không hợp lệ"
    assert isinstance(bot, dict)  # Chỉ giúp type narrowing sau valid_bot.

    position = bot["position"]
    goal = bot["goal"]
    opponent = bot.get("opponent_position")
    if position == goal or (opponent is not None and abs(position - opponent) <= 1):
        action = "wait"
    elif position < goal:
        action = "right"
    else:
        action = "left"
    return f"position={position}, goal={goal}, action={action}"


def main() -> None:
    print("COURSE TEACHING MODEL — NOT VUACOC PRODUCTION CONTRACT")
    for state in (
        {"bot": {"position": 1, "goal": 4, "opponent_position": 3}},
        {"bot": {"position": 4, "goal": 4}},
        {"bot": {"position": 3, "goal": 0}},
        {"bot": {"goal": 4}},
        {"bot": {"position": True, "goal": 4}},
    ):
        print(explain(state))


if __name__ == "__main__":
    main()
