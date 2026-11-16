"""Cau5a — LỜI GIẢI THAM KHẢO, chỉ mở sau khi tự làm.

Đếm tần suất từng ký tự trong chuỗi (bao gồm khoảng trắng, có phân biệt hoa/thường). Text rỗng => {}. Sai kiểu => ValueError.
"""


def char_frequency(text: str) -> dict[str, int]:
    if not isinstance(text, str):
        raise ValueError("Cần chuỗi")
    counts: dict[str, int] = {}
    for character in text:
        counts[character] = counts.get(character, 0) + 1
    return counts


if __name__ == "__main__":
    print("Chạy autograde_de1.py --reference để kiểm lời giải mẫu")
