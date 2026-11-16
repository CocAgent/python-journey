"""Cau4b — LỜI GIẢI THAM KHẢO, chỉ mở sau khi tự làm.

Trả tuple (first + second, first * 3). Hai đầu vào phải là tuple, không sửa dữ liệu nguồn.
"""


def tuple_combine(first: tuple, second: tuple) -> tuple:
    if not isinstance(first, tuple) or not isinstance(second, tuple):
        raise ValueError("Cần hai tuple")
    return first + second, first * 3


if __name__ == "__main__":
    print("Chạy autograde_de1.py --reference để kiểm lời giải mẫu")
