"""Exercise 01: imports, modules and main guard."""

from bot_course.core import choose_action


def main() -> None:
    """Call the reusable decision function and display its action."""
    action = choose_action(position=1, goal=4)
    print(action)


if __name__ == "__main__":
    main()
