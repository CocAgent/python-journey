"""Cau3b — Reference cho bài ôn tập, chỉ mở sau khi tự giải."""

def count_value_before_zero(values: list[int], target: int) -> int:
    if not isinstance(values, list) or type(target) is not int or target <= 0:
        raise ValueError("Đầu vào không hợp lệ")
    count = 0
    for value in values:
        if type(value) is not int or value < 0:
            raise ValueError("Danh sách không hợp lệ")
        if value == 0:
            return count
        if value == target:
            count += 1
    raise ValueError("Thiếu số 0 kết thúc")
