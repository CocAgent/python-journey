"""
Bài tập 01: Vòng lặp for 🔁
==============================
Mục tiêu: Dùng for duyệt list, range, string
"""

# TODO 1: In bảng cửu chương của số n (nhập từ người dùng)
n = int(input("Nhập số n: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# TODO 2: Duyệt list fruits và in kèm số thứ tự
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# Dùng enumerate()
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")


# TODO 3: Cho 2 list, ghép cặp và in
# names = ["An", "Bình", "Châu"]
# scores = [8, 9, 7]
# Dùng zip() → "An: 8 điểm", "Bình: 9 điểm", ...
names = ["An", "Bình", "Châu"]
scores = [8, 9, 7]
for name, score in zip(names, scores):
    print(f"{name}: {score} điểm")


# TODO 4: Tính tổng các số chẵn từ 1 đến 100 bằng for + range
total_even = 0
for i in range(2, 101, 2):
    total_even += i
print("Tổng các số chẵn từ 1 đến 100:", total_even)


# TODO 5 (Thử thách): Fibonacci
# In ra n số Fibonacci đầu tiên (n nhập từ người dùng)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
n_fib = int(input("Nhập n số Fibonacci cần in: "))
a, b = 0, 1
fib_sequence = []
for _ in range(n_fib):
    fib_sequence.append(str(a))
    a, b = b, a + b
print(", ".join(fib_sequence))


# TODO 6: List comprehension
# Tạo list bình phương các số chẵn từ 1 đến 10 bằng comprehension.
# In kết quả mong đợi: [4, 16, 36, 64, 100]
squares_of_evens = [x**2 for x in range(1, 11) if x % 2 == 0]
print(squares_of_evens)