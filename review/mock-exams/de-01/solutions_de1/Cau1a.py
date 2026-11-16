"""Cau1a — LỜI GIẢI THAM KHẢO, chỉ mở sau khi tự làm.

Kiểm tra số nguyên n, trả "Chan" nếu chia hết cho 2, ngược lại "Le". Ném ValueError nếu sai kiểu (kể cả bool).
"""


def parity(n: int) -> str:
    if type(n) is not int:
        raise ValueError("n phải là số nguyên")
    return "Chan" if n % 2 == 0 else "Le"


if __name__ == "__main__":
    print("Chạy autograde_de1.py --reference để kiểm lời giải mẫu")
