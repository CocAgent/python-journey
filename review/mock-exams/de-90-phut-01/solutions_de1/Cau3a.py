"""Cau3a — Reference cho bài ôn tập, chỉ mở sau khi tự giải."""

def count_even_before_zero(values: list[int]) -> int:
    if not isinstance(values, list):
        raise ValueError("Cần danh sách")
    count = 0
    for value in values:
        if type(value) is not int or value < 0:
            raise ValueError("Giá trị phải là số nguyên không âm")
        if value == 0:
            return count
        if value % 2 == 0:
            count += 1
    raise ValueError("Thiếu số 0 kết thúc")
