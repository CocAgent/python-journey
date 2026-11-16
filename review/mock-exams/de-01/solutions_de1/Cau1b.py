"""Cau1b — LỜI GIẢI THAM KHẢO, chỉ mở sau khi tự làm.

Chuẩn hóa tên bằng strip(), tuổi là int thật từ 0..120; trả "Xin chào An, bạn 20 tuổi.". Input sai => ValueError.
"""


def greet(name: str, age: int) -> str:
    if not isinstance(name, str) or not name.strip() or type(age) is not int or not 0 <= age <= 120:
        raise ValueError("Tên hoặc tuổi không hợp lệ")
    return f"Xin chào {name.strip()}, bạn {age} tuổi."


if __name__ == "__main__":
    print("Chạy autograde_de1.py --reference để kiểm lời giải mẫu")
