"""Cau2b — LỜI GIẢI THAM KHẢO, chỉ mở sau khi tự làm.

Đếm ký tự chữ số ASCII 0–9 trong vị trí 1-based từ start đến end (bao gồm hai đầu). Phạm vi sai, chuỗi rỗng => ValueError.
"""


def count_digits_slice(text: str, start: int, end: int) -> int:
    if (not isinstance(text, str) or type(start) is not int or type(end) is not int
            or not 1 <= start <= end <= len(text)):
        raise ValueError("Vị trí hoặc chuỗi không hợp lệ")
    count = 0
    for character in text[start - 1:end]:
        if "0" <= character <= "9":
            count += 1
    return count


if __name__ == "__main__":
    print("Chạy autograde_de1.py --reference để kiểm lời giải mẫu")
