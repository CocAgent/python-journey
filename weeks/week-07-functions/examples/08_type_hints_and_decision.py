"""Ví dụ 08 — Annotation là chỉ dẫn, không tự xác thực runtime.

Decision function ở đây là mô hình học lập trình, KHÔNG là runtime VuaCóc.
"""

def repeat_text(text: str, times: int) -> str:
    """Hàm có type hints, nhưng Python vẫn thực hiện toán tử tại runtime."""
    return text * times


def is_valid_minutes(minutes: object) -> bool:
    """Runtime validation phải viết riêng khi dữ liệu cần tin cậy."""
    return isinstance(minutes, int) and not isinstance(minutes, bool) and 0 <= minutes <= 60


def decide_study_action(minutes: int, confused: bool) -> str:
    """Decision teaching model: stop nếu hết giờ, review nếu còn bối rối."""
    if minutes == 0:
        return "stop"
    if confused:
        return "review"
    return "practice"


def main() -> None:
    print(f"Lặp chuỗi đúng kiểu: {repeat_text('Py', 2)}")
    # str * True chạy được dù times khai báo int vì bool là subclass của int.
    print(f"Annotation không chặn bool: {repeat_text('Py', True)}")  # type: ignore[arg-type]
    print(f"Validator nhận 10: {is_valid_minutes(10)}")
    print(f"Validator từ chối True: {is_valid_minutes(True)}")
    print(f"Hết giờ, dù đang bối rối: {decide_study_action(0, True)}")
    print(f"Còn giờ và bối rối: {decide_study_action(15, True)}")
    print(f"Còn giờ và rõ bài: {decide_study_action(15, False)}")


if __name__ == "__main__":
    main()
