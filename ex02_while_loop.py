"""
Bài tập 02: Vòng lặp while ⏳
================================
Mục tiêu: Dùng while với điều kiện kiểm soát
"""

# TODO 1: Đếm ngược từ 10 → 1, in "Phóng! 🚀"
count = 10
while count > 0:
    print(count)
    count -= 1
print("Phóng! 🚀")


# TODO 2: Trò chơi đoán số
# Máy chọn số bí mật (random.randint(1, 100))
# Người dùng đoán, máy gợi ý "Cao hơn!" hoặc "Thấp hơn!"
# Đếm số lần đoán
import random

secret_number = random.randint(1, 100)
attempts = 0
guess = 0

while guess != secret_number:
    guess = int(input("Đoán một số (1-100): "))
    attempts += 1
    if guess < secret_number:
        print("Cao hơn!")
    elif guess > secret_number:
        print("Thấp hơn!")

print(f"Chính xác! Bạn đã đoán đúng sau {attempts} lần.")


# TODO 3: Nhập liệu an toàn
# Hỏi nhập tuổi, lặp lại cho đến khi người dùng nhập số hợp lệ (1-120)
# Dùng while True + break
while True:
    input_age = input("Nhập tuổi của bạn (1-120): ")
    if input_age.isdigit():
        age = int(input_age)
        if 1 <= age <= 120:
            print(f"Tuổi hợp lệ: {age}")
            break
    print("Mức tuổi không hợp lệ, vui lòng nhập lại!")


# TODO 4 (Thử thách): Menu chương trình
# Hiển thị menu: 1. Cộng, 2. Trừ, 3. Nhân, 4. Thoát
# Lặp lại đến khi người dùng chọn 4
while True:
    print("\n--- MENU ---")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Thoát")
    
    choice = input("Chọn chức năng (1-4): ")
    
    if choice == '4':
        print("Đã thoát chương trình.")
        break
    elif choice in ['1', '2', '3']:
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))
        
        if choice == '1':
            print(f"Kết quả: {a} + {b} = {a + b}")
        elif choice == '2':
            print(f"Kết quả: {a} - {b} = {a - b}")
        elif choice == '3':
            print(f"Kết quả: {a} * {b} = {a * b}")
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại!")