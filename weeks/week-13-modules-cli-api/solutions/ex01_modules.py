"""Lời giải 01 — import + main guard."""

from bot_course.core import choose_action


def main() -> None:
    print("Hành động:", choose_action(1, 4))


if __name__ == "__main__":
    main()
