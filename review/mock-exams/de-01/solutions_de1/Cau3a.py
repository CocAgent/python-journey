"""Cau3a — LỜI GIẢI THAM KHẢO, chỉ mở sau khi tự làm.

Lấy các phần tử có type là str từ list hỗn hợp, giữ thứ tự, không sửa list nguồn. Không phải list => ValueError.
"""


def only_strings(items: list[object]) -> list[str]:
    if not isinstance(items, list):
        raise ValueError("Cần list")
    result: list[str] = []
    for item in items:
        if isinstance(item, str):
            result.append(item)
    return result


if __name__ == "__main__":
    print("Chạy autograde_de1.py --reference để kiểm lời giải mẫu")
