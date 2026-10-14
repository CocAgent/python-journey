"""
Bài tập 02: Máy tính Python 🧮
================================
Mục tiêu: Sử dụng các phép tính cơ bản trong Python
"""

# TODO 1: Tính và in ra kết quả của 2024 + 1000
print("2024 + 1000 =", 2024 + 1000)


# TODO 2: Bạn có 150,000 VNĐ, mua 3 ly cà phê giá 35,000 VNĐ/ly.
# Tính và in ra số tiền còn lại.
print("Số tiền còn lại:", 150000 - 3 * 35000, "VNĐ")


# TODO 3: Tính diện tích hình tròn có bán kính = 7
# Gợi ý: Diện tích = 3.14159 * bán_kính ** 2
bk = 7
dt = 3.14159 * bk ** 2
print(f"Diện tích hình tròn: {dt:.2f}")

# TODO 4: Bạn có 100 viên kẹo chia đều cho 7 người.
# In ra: mỗi người được bao nhiêu viên (chia nguyên)?
# In ra: còn dư bao nhiêu viên?
# Gợi ý: Dùng // và %
print("Mỗi người được:", 100 // 7, "viên")
print("Còn dư:", 100 % 7, "viên")

# TODO 5 (Thử thách): Chuyển đổi 37 độ C sang Fahrenheit
# Công thức: F = C * 9/5 + 32
# In ra kết quả dạng: "37°C = ???°F"
C = 37
F = C * 9/5 + 32
print(f"{C}°C = {F}°F")
