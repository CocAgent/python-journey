"""Cau1a — Reference cho bài ôn tập, chỉ mở sau khi tự giải."""

def count_divisible_by_three_digits(n: int) -> int:
    if type(n) is not int or not 1 <= n <= 1500:
        raise ValueError("n phải là số nguyên 1..1500")
    return sum(char in "0369" for char in str(n))
