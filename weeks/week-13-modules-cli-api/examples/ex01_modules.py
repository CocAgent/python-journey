"""Ví dụ 1: import một hàm từ package do mình viết."""

from bot_course.core import choose_action


def main() -> None:
    """Không chạy ví dụ khi module được import bởi chương trình khác."""
    print("Đi từ 1 đến 4:", choose_action(1, 4))
    print("Đang ở đích:", choose_action(4, 4))


if __name__ == "__main__":
    main()
