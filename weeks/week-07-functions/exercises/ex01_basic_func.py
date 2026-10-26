"""Exercise 01 — Functions and return values.

Goal:
    Viết các hàm nhỏ và dùng ``return`` thay vì chỉ ``print``.

TODO:
    1. Hoàn thành ``chao``.
    2. Hoàn thành ``tinh_dien_tich_hinh_tron``.
    3. Hoàn thành ``la_so_chan``.

Examples:
    chao("An") == "Xin chào An!"
    tinh_dien_tich_hinh_tron(0) == 0.0
    la_so_chan(4) is True

Expected behavior:
    Mỗi hàm trả về dữ liệu để caller có thể dùng tiếp.

Basic boundary case:
    Bán kính bằng 0 có diện tích bằng 0.

Self-check command:
    python weeks/week-07-functions/exercises/ex01_basic_func.py
"""

import math


def chao(ten: str) -> str:
    """Trả về lời chào cho ``ten``."""
    # TODO: Trả về chuỗi "Xin chào <tên>!".
    return f"Xin chao {ten}!"
def tinh_dien_tich_hinh_tron(ban_kinh: float) -> float:
    """Trả về diện tích hình tròn."""
    # TODO: Dùng math.pi và lũy thừa bậc hai.
    return math.pi * ban_kinh ** 2


def la_so_chan(so: int) -> bool:
    """Trả về True khi ``so`` là số chẵn."""
    # TODO: Dùng phép chia lấy dư.
    return so % 2 == 0


if __name__ == "__main__":
    print(chao("Duc"))
    print(tinh_dien_tich_hinh_tron(0))
    print(la_so_chan(4))
    print(la_so_chan(5))
