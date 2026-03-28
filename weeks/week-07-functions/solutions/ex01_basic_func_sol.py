"""Lời giải Bài tập 01: Hàm cơ bản"""
import math

# TODO 1
def chao(ten):
    print(f"Xin chào, {ten}!")

chao("An"); chao("Bình"); chao("Châu")

# TODO 2
def tinh_dien_tich_hinh_tron(ban_kinh):
    return math.pi * ban_kinh ** 2

for r in [5, 7, 10]:
    print(f"r={r}: S={tinh_dien_tich_hinh_tron(r):.2f}")

# TODO 3
def la_so_chan(n):
    return n % 2 == 0

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for n in [2, 3, 4, 7, 10, 13]:
    print(f"{n}: chẵn={la_so_chan(n)}, nguyên tố={la_so_nguyen_to(n)}")

# TODO 4
def tinh_thong_ke(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers), sum(numbers)

mi, ma, tb, tg = tinh_thong_ke([7, 9, 5, 8, 10])
print(f"Min={mi}, Max={ma}, TB={tb:.1f}, Tổng={tg}")

# TODO 5
def tinh_giai_thua(n):
    if n <= 1:
        return 1
    return n * tinh_giai_thua(n - 1)

print(f"5! = {tinh_giai_thua(5)}")
