"""Exercise 04: structured course-local state → heuristic action."""

LOCAL_ACTIONS = {"left", "right", "wait"}


def choose_action(state: dict[str, int]) -> str:
    """Chọn một action local bằng 2–4 rules dễ giải thích."""
    # TODO 1: đọc position và goal; dùng .get() cho field tùy chọn.
    # TODO 2: nếu đã ở goal, trả "wait".
    # TODO 3: thêm một rule khi opponent ở gần nếu bạn thấy hữu ích.
    # TODO 4: đi "left" hoặc "right" về phía goal.
    return "wait"


def main() -> None:
    """Chạy một teaching state; không phải production contract."""
    state = {
        "turn": 1,
        "max_turns": 6,
        "position": 0,
        "opponent_position": 4,
        "goal": 4,
        "min_position": 0,
        "max_position": 4,
    }
    action = choose_action(state)
    print("COURSE TEACHING MODEL")
    print("NOT VUACOC PRODUCTION CONTRACT")
    print(f"action={action}, legal={action in LOCAL_ACTIONS}")


if __name__ == "__main__":
    main()
