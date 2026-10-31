"""Exercise 01: imports, modules and main guard."""

from bot_course.core import choose_action


def main() -> None:
    """Run a small example of the bot decision core."""
    position = 2
    goal = 5

    action = choose_action(position, goal)
    print(f"Position: {position}")
    print(f"Goal: {goal}")
    print(f"Suggested action: {action}")


if __name__ == "__main__":
    main()
