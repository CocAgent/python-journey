"""Cau4a — LỜI GIẢI THAM KHẢO, chỉ mở sau khi tự làm.

Trả tuple gồm phần tử đầu, thứ ba và cuối. Tuple phải >=3 phần tử; sai => ValueError.
"""


def tuple_positions(items: tuple) -> tuple:
    if not isinstance(items, tuple) or len(items) < 3:
        raise ValueError("Cần tuple có ít nhất 3 phần tử")
    return items[0], items[2], items[-1]


if __name__ == "__main__":
    print("Chạy autograde_de1.py --reference để kiểm lời giải mẫu")
