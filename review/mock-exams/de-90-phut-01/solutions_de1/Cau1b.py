"""Cau1b — Reference cho bài ôn tập, chỉ mở sau khi tự giải."""

def harmonic_sum(n: int) -> float:
    if type(n) is not int or not 1 <= n <= 1500:
        raise ValueError("n phải là số nguyên 1..1500")
    total = 0.0
    for index in range(1, n + 1):
        total += 1 / index
    return total
