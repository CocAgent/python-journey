"""
Bài tập 02: Vòng lặp while
==========================
Mục tiêu: Dùng while với điều kiện kiểm soát
"""

# TODO 1: Đếm ngược từ 10 đến 1, sau đó in lời báo phóng
countdown = 10
while countdown >= 1:
    print(countdown)
    countdown -= 1
print("Phóng! 🚀")

# TODO 2: Trò chơi đoán số
# Máy chọn số bí mật từ 1 đến 100. Đếm số lần đoán.
import random

secret = random.randint(1, 100)
attempts = 0
while True:
    guess_text = input("Đoán số (1-100): ")
    if not guess_text.isdigit():
        print("Vui lòng nhập một số nguyên từ 1 đến 100.")
        continue
    guess = int(guess_text)
    if not 1 <= guess <= 100:
        print("Số cần nằm trong khoảng 1 đến 100.")
        continue
    attempts += 1
    if guess < secret:
        print("Cao hơn!")
    elif guess > secret:
        print("Thấp hơn!")
    else:
        print(f"Chính xác! Bạn đoán {attempts} lần.")
        break

# TODO 3: Nhập tuổi hợp lệ từ 1 đến 120
while True:
    age_text = input("Nhập tuổi (1-120): ")
    if age_text.isdigit() and 1 <= int(age_text) <= 120:
        age = int(age_text)
        break
    print("Tuổi không hợp lệ, vui lòng thử lại.")
print(f"Tuổi: {age}")

# TODO 4 (Thử thách): Menu máy tính đơn giản
while True:
    print("\n1. Cộng  2. Trừ  3. Nhân  4. Thoát")
    choice = input("Chọn: ").strip()
    if choice == "4":
        print("Tạm biệt!")
        break
    if choice not in {"1", "2", "3"}:
        print("Lựa chọn không hợp lệ.")
        continue
    try:
        first = float(input("Số thứ nhất: "))
        second = float(input("Số thứ hai: "))
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")
        continue
    if choice == "1":
        print(f"{first} + {second} = {first + second}")
    elif choice == "2":
        print(f"{first} - {second} = {first - second}")
    else:
        print(f"{first} x {second} = {first * second}")
