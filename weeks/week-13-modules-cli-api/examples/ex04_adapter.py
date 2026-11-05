"""Ví dụ 4: Bot core không biết adapter; adapter kiểm input rồi mới gọi core."""

from bot_course.adapter import course_local_action


def main() -> None:
    print("Case đúng:", course_local_action({"position": 2, "goal": 4}))
    try:
        course_local_action({"position": 99, "goal": 4})
    except ValueError as error:
        print("Case sai:", error)


if __name__ == "__main__":
    main()
