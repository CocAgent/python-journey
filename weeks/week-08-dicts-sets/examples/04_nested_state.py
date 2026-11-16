"""Đọc structured state chứa dict và list lồng nhau."""


def summarize_state(state: dict[str, object]) -> str:
    """Tạo summary từ các nhóm dữ liệu có tên rõ ràng."""
    bot = state["bot"]
    match = state["match"]
    if not isinstance(bot, dict) or not isinstance(match, dict):
        return "State không hợp lệ"

    tags = state.get("tags", [])
    return (
        f"{bot['name']} ở vị trí {bot['position']}; "
        f"turn {match['turn']}/{match['max_turns']}; tags={tags}"
    )


def main() -> None:
    """Minh họa cách đọc nested data từ ngoài vào trong."""
    teaching_state = {
        "bot": {"name": "StudentBot", "position": 1, "goal": 4},
        "match": {"turn": 2, "max_turns": 6},
        "tags": ["course-local", "structured-state"],
    }

    print("COURSE TEACHING MODEL")
    print("NOT VUACOC PRODUCTION CONTRACT")
    print(summarize_state(teaching_state))

    bot_data = teaching_state["bot"]
    if isinstance(bot_data, dict):
        print(f"Goal: {bot_data['goal']}")


if __name__ == "__main__":
    main()
