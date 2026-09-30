"""
Bài tập 01: Vòng lặp for 🔁
==============================
Mục tiêu: Dùng for duyệt list, range, string
"""

# TODO 1: In bảng cửu chương của số n (nhập từ người dùng)
n = int(input("Nhập số: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
# TODO 2: Duyệt list fruits và in kèm số thứ tự
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# Dùng enumerate()
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")

# TODO 3: Cho 2 list, ghép cặp và in
# names = ["An", "Bình", "Châu"]
# scores = [8, 9, 7]
# Dùng zip() → "An: 8 điểm", "Bình: 9 điểm", ...
names = ["An", "Bình", "Châu"]
scores = [8, 9, 7]
for name, score in zip(names, scores):
    print(f"{name}: {score} điểm")

# TODO 4: Tính tổng các số chẵn từ 1 đến 100 bằng for + range
tong = sum(x for x in range(1, 101) if x % 2 == 0)
print(f"Tổng số chẵn 1-100: {tong}")

# TODO 5 (Thử thách): Fibonacci
# In ra n số Fibonacci đầu tiên (n nhập từ người dùng)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
n = int(input("Số phần tử Fibonacci: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()