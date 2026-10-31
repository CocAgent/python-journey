"""Lab 04 — Decision function: input -> validate -> action.

MÔ HÌNH GIẢNG DẠY, KHÔNG PHẢI VUACOC PRODUCTION CONTRACT.
minutes: int 0..60, confused: bool thật (không nhận chuỗi "False").
Action: stop nếu minutes=0; review nếu confused; còn lại practice.
"""


def choose_study_action(minutes: int, confused: bool) -> str:
    """Trả stop/review/practice ổn định; invalid input -> ValueError."""
    # TODO 1: kiểm type(minutes) is int, phạm vi 0..60;
    #         type(confused) is bool. Không tin chỉ vào type hints.
    # TODO 2: minutes == 0 => "stop" trước, kể cả confused=True.
    # TODO 3: confused => "review"; còn lại => "practice".
    raise NotImplementedError("Hoàn thành decision function")


if __name__ == "__main__":
    print("Thử input (0, True), (15, True), (15, False), (61, False).")
