"""Bài 04 — thực hành kiểm input trước khi gọi Bot Core."""

from bot_course.adapter import course_local_action


def main() -> None:
    """TODO: in hành động và thử trường hợp bị từ chối."""
    # TODO 1: gọi course_local_action({"position": 3, "goal": 1}) → left.
    # TODO 2: kiểm case {"position": True, "goal": 1} báo ValueError.
    print("TODO 04: học cách gọi adapter và bắt lỗi")
    # Đây chỉ là phần minh họa; em cần viết lời giải thật cho các TODO.
    assert course_local_action({"position": 3, "goal": 1})["action"] == "left"


if __name__ == "__main__":
    main()
