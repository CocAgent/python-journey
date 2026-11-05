"""Bài 01 — tự hoàn thành import, main guard. Chạy với python -m."""

# TODO 1: import choose_action từ bot_course.core
from bot_course.core import choose_action

def main() -> None:
    """TODO 2: gọi choose_action(1, 4), in 'Hành động: right'."""
    a = choose_action(1,4)
    print(f"Hanh dong: {a} ")
   # print("TODO 01: import và gọi choose_action ở đây")


# TODO 3: chỉ gọi main() khi file được chạy, KHÔNG gọi khi import.
if __name__ =="__main__":
    main()
