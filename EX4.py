import random


# ===== Bài 1: Xếp loại học sinh =====
def classify_score(score: float) -> str:
    if score < 0 or score > 10:
        return "Điểm không hợp lệ (phải từ 0 đến 10)"
    if score >= 9:
        return "Xuất sắc"
    elif score >= 8:
        return "Giỏi"
    elif score >= 6.5:
        return "Khá"
    elif score >= 5:
        return "Trung bình"
    else:
        return "Yếu"


# ===== Bài 2: Máy tính 4 phép =====
def calculate(a: float, b: float, op: str):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Lỗi: không thể chia cho 0"
        return a / b
    else:
        return "Lỗi: phép toán không hợp lệ"


# ===== Bài 3: Năm nhuận =====
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# ===== Bài 4: Game đoán số =====
def guessing_game():
    secret = random.randint(1, 100)
    attempts = 0
    print("Tôi đã nghĩ ra một số từ 1 đến 100. Hãy đoán xem!")

    while True:
        guess = int(input("Đoán số của bạn: "))
        attempts += 1
        if guess < secret:
            print("Thấp hơn rồi, thử lại nhé!")
        elif guess > secret:
            print("Cao hơn rồi, thử lại nhé!")
        else:
            print(f"Chính xác! Số đó là {secret}. Bạn đoán đúng sau {attempts} lần.")
            break


# ===== Chạy thử (menu chọn bài) =====
if __name__ == "__main__":
    print("1. Xếp loại học sinh")
    print("2. Máy tính")
    print("3. Kiểm tra năm nhuận")
    print("4. Game đoán số")
    choice = input("Chọn bài (1-4): ")

    if choice == "1":
        diem = float(input("Nhập điểm (0-10): "))
        print(classify_score(diem))
    elif choice == "2":
        a = float(input("Số thứ nhất: "))
        op = input("Phép toán (+, -, *, /): ")
        b = float(input("Số thứ hai: "))
        print("Kết quả:", calculate(a, b, op))
    elif choice == "3":
        year = int(input("Nhập năm: "))
        print(f"{year} là năm nhuận" if is_leap_year(year) else f"{year} không phải năm nhuận")
    elif choice == "4":
        guessing_game()
    else:
        print("Lựa chọn không hợp lệ")