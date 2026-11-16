"""Ôn tập 03 — Sửa lỗi logic và chỉ bắt exception dự kiến."""


def distance(start: int, end: int) -> int:
    """Khoảng cách tuyệt đối giữa hai ô nguyên từ 0 đến 10.

    Sai kiểu, bool hoặc ngoài phạm vi -> ValueError.
    """
    # TODO: kiểm cả hai phải là int thật (không bool), 0 <= value <= 10.
    # TODO: dùng abs(end - start), để hai chiều đều cho cùng khoảng cách.
    raise NotImplementedError("Hãy hoàn thành distance")


def parse_score(raw: str, audit: list[str]) -> int | None:
    """Chuyển điểm [0..10] và ghi lại từng lần thử.

    - text không phải số -> append 'invalid', trả None
    - số ngoài 0..10 -> append 'out_of_range', trả None
    - hợp lệ -> append 'accepted', trả int
    - finally luôn append f'attempt:{raw!r}'
    - input sai kiểu như None phải nổi TypeError, KHÔNG bị nuốt.
    """
    # TODO: try int(raw), except ValueError, else, finally.
    # TODO: không return trong finally; không dùng except Exception.
    raise NotImplementedError("Hãy hoàn thành parse_score")


if __name__ == "__main__":
    print("Tự viết hàm rồi thử input (4, 1), '8', 'abc', None.")
