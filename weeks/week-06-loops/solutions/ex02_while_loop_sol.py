"""Lời giải Bài tập 02: Vòng lặp while"""
import random

# TODO 1
i = 10
while i >= 1:
    print(i)
    i -= 1
print("Phóng! 🚀")

# TODO 2
secret = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Đoán số (1-100): "))
    attempts += 1
    if guess < secret:
        print("Cao hơn!")
    elif guess > secret:
        print("Thấp hơn!")
    else:
        print(f"Đúng rồi! Bạn đoán {attempts} lần.")
        break

# TODO 3
while True:
    tuoi_str = input("Nhập tuổi (1-120): ")
    if tuoi_str.isdigit() and 1 <= int(tuoi_str) <= 120:
        tuoi = int(tuoi_str)
        break
    print("Tuổi không hợp lệ, thử lại!")
print(f"Tuổi: {tuoi}")

# TODO 4
while True:
    print("\n1. Cộng  2. Trừ  3. Nhân  4. Thoát")
    choice = input("Chọn: ")
    if choice == "4":
        print("Tạm biệt!")
        break
    a = float(input("Số a: "))
    b = float(input("Số b: "))
    if choice == "1":
        print(f"{a} + {b} = {a + b}")
    elif choice == "2":
        print(f"{a} - {b} = {a - b}")
    elif choice == "3":
        print(f"{a} * {b} = {a * b}")
