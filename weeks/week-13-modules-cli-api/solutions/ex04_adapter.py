"""Lời giải 04 — biến state dict thành hành động qua adapter."""

from bot_course.adapter import course_local_action


def main() -> None:
    result = course_local_action({"position": 3, "goal": 1})
    print("Hành động:", result["action"])
    try:
        course_local_action({"position": True, "goal": 1})
    except ValueError as error:
        print("Từ chối:", error)


if __name__ == "__main__":
    main()
