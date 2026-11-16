"""Cau3b — LỜI GIẢI THAM KHẢO, chỉ mở sau khi tự làm.

Không sửa list nguồn. Sao chép, append("mango"), remove(3.14), reverse(); trả ba snapshot bằng keys after_append, after_remove, after_reverse. Thiếu 3.14 => ValueError.
"""


def inventory_steps(items: list[object]) -> dict[str, list[object]]:
    if not isinstance(items, list) or 3.14 not in items:
        raise ValueError("Dữ liệu thiếu phần tử 3.14 hoặc không phải list")
    working = items.copy()
    working.append("mango")
    after_append = working.copy()
    working.remove(3.14)
    after_remove = working.copy()
    working.reverse()
    return {"after_append": after_append, "after_remove": after_remove, "after_reverse": working}


if __name__ == "__main__":
    print("Chạy autograde_de1.py --reference để kiểm lời giải mẫu")
