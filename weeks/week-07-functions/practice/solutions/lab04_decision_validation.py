"""Lời giải 04 — Đơn giản, tất định, có runtime guard.

TEACHING MODEL ONLY — NOT VUACOC PRODUCTION CONTRACT.
"""


def choose_study_action(minutes: int, confused: bool) -> str:
    """Chặn input sai trước khi chọn một trong ba action."""
    if (
        type(minutes) is not int
        or not 0 <= minutes <= 60
        or type(confused) is not bool
    ):
        raise ValueError("Thời gian hoặc trạng thái không hợp lệ")
    if minutes == 0:
        return "stop"
    if confused:
        return "review"
    return "practice"


if __name__ == "__main__":
    print(choose_study_action(15, True))
