"""Lời giải Bài tập 01: Vòng lặp for"""
# TODO 1
n = int(input("Nhập số: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# TODO 2
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")

# TODO 3
names = ["An", "Bình", "Châu"]
scores = [8, 9, 7]
for name, score in zip(names, scores):
    print(f"{name}: {score} điểm")

# TODO 4
tong = sum(x for x in range(1, 101) if x % 2 == 0)
print(f"Tổng số chẵn 1-100: {tong}")

# TODO 5
n = int(input("Số phần tử Fibonacci: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
