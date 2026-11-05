"""Ranh giới dữ liệu course-local: kiểm input rồi gọi Bot Core.

Đây KHÔNG phải adapter cho VuaCóc production.
"""

from bot_course.core import choose_action

MIN_POSITION = 0
MAX_POSITION = 4


def validate_state(payload: dict[str, int]) -> tuple[int, int]:
    """Kiểm dữ liệu được cung cấp, thay vì tin rằng type hints tự kiểm."""
    if not isinstance(payload, dict):
        raise ValueError("state phải là dict")
    for key in ("position", "goal"):
        if key not in payload:
            raise ValueError(f"thiếu trường: {key}")
        value = payload[key]
        # bool là subclass của int, nhưng True không phải vị trí hợp lệ.
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{key} phải là số nguyên")
        if not MIN_POSITION <= value <= MAX_POSITION:
            raise ValueError(f"{key} phải từ {MIN_POSITION} đến {MAX_POSITION}")
    return payload["position"], payload["goal"]


def course_local_action(payload: dict[str, int]) -> dict[str, str]:
    """Chuyển trạng thái thành quyết định; ghi nhãn định dạng học tập."""
    position, goal = validate_state(payload)
    return {
        "format": "COURSE LOCAL FORMAT",
        "production_compatibility": "NOT VUACOC PRODUCTION FORMAT",
        "action": choose_action(position, goal),
    }
