"""Exercise 01: imports, modules and main guard."""

from bot_course.core import choose_action


def main() -> None:
    """Choose and display an action using the reusable bot core."""
    print(choose_action(position=1, goal=4))


if __name__ == "__main__":
    main()
