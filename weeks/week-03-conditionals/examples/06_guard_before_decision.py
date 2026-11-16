"""Ví dụ 06 — kiểm dữ liệu đầu vào trước khi ra quyết định.

Tất cả là chuỗi nhập mô phỏng (không hỏi bàn phím, không gọi mạng).
"""


def ticket_message(age_text: str) -> str:
    """Trả message dễ kiểm; không để int() gặp text sai."""
    clean = age_text.strip()
    if not clean.isdigit():
        return "Lỗi: tuổi phải là số nguyên không âm"

    age = int(clean)
    if age > 120:
        return "Lỗi: tuổi phải từ 0 đến 120"

    if age < 12:
        return "Vé trẻ em"
    elif age >= 65:
        return "Vé người cao tuổi"
    else:
        return "Vé tiêu chuẩn"


for text in (" 10 ", "12", "64", "65", "120", "121", "abc", "-1", ""):
    print(f"Input {text!r} -> {ticket_message(text)}")

# Dùng giá vé chỉ để minh họa điều kiện; không phải bảng giá thực.
