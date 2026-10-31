"""Ví dụ 5: nhìn dữ liệu đi qua JSON → adapter → Bot Core.

Tên file được giữ ổn định để dùng trong hướng dẫn, nhưng ví dụ minh họa
BOT COURSE-LOCAL; bài tương tự của sinh viên dùng dữ liệu Study Progress.

Chạy từ week root:
    python -m examples.ex05_trace_student_flow
Không mở mạng hoặc sửa file.
"""

from __future__ import annotations

import json

from bot_course.adapter import course_local_action


def build_action(raw_state: str) -> dict[str, str]:
    """Parse JSON rồi giao việc kiểm quy tắc cho adapter/course core."""
    try:
        state = json.loads(raw_state)
    except json.JSONDecodeError as error:
        raise ValueError("Bước JSON: cú pháp không hợp lệ") from error
    return course_local_action(state)


def main() -> None:
    print("Bước 1: nhận text JSON chứa position=1, goal=4")
    print("Bước 2: JSON → dict → adapter kiểm state → core quyết định")
    response = build_action('{"position": 1, "goal": 4}')
    print("Bước 3: action =", response["action"])

    print("Bước 4: thử position=99 (phải từ chối)")
    try:
        build_action('{"position": 99, "goal": 4}')
    except ValueError as error:
        print("Từ chối:", error)


if __name__ == "__main__":
    main()
