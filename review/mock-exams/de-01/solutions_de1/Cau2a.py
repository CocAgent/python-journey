"""Cau2a — LỜI GIẢI THAM KHẢO, chỉ mở sau khi tự làm.

Tổng các số chẵn trong đoạn nguyên [start,end] bao gồm hai đầu; nếu start>end hoặc đầu vào sai => ValueError.
"""


def sum_even(start: int, end: int) -> int:
    if type(start) is not int or type(end) is not int or start > end:
        raise ValueError("Đoạn nguyên không hợp lệ")
    total = 0
    for number in range(start, end + 1):
        if number % 2 == 0:
            total += number
    return total


if __name__ == "__main__":
    print("Chạy autograde_de1.py --reference để kiểm lời giải mẫu")
