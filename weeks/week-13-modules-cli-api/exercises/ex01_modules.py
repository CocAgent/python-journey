"""Exercise 01: imports, modules and main guard."""

from bot_course.core import choose_action


def main() -> None:
    """Chọn hành động dựa vào vị trí hiện tại và mục tiêu."""
    position = 1
    goal = 4
    action = choose_action(position, goal)
    print(f"Vị trí: {position}, mục tiêu: {goal}")
    print(f"Hành động: {action}")


if __name__ == "__main__":
    main()
