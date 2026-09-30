"""Exercise 01 — Functions and return values.

Goal:
    Viết các hàm nhỏ và dùng ``return`` thay vì chỉ ``print``.
"""

import math


def chao(ten: str) -> str:
    """Trả về lời chào cho ``ten``."""
    return f"Xin chào {ten}!"


def tinh_dien_tich_hinh_tron(ban_kinh: float) -> float:
    """Trả về diện tích hình tròn."""
    return math.pi * ban_kinh**2


def la_so_chan(so: int) -> bool:
    """Trả về True khi ``so`` là số chẵn."""
    return so % 2 == 0


def main() -> None:
    """Chạy một vài ví dụ có output quan sát được."""
    print(chao("An"))
    print(f"Diện tích r=5: {tinh_dien_tich_hinh_tron(5):.2f}")
    print(f"4 là số chẵn: {la_so_chan(4)}")


if __name__ == "__main__":
    main()
