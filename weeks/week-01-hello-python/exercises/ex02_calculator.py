"""
Bài tập 02: Máy tính Python 🧮
================================
Mục tiêu: Sử dụng các phép tính cơ bản trong Python
"""

# TODO 1: Tính và in ra kết quả của 2024 + 1000
print(2024 + 1000)

# TODO 2: Bạn có 150,000 VNĐ, mua 3 ly cà phê giá 35,000 VNĐ/ly.
# Tính và in ra số tiền còn lại.
a = 150000
b = 35000
print(a - 3 * b, "VNĐ")
# TODO 3: Tính diện tích hình tròn có bán kính = 7
# Gợi ý: Diện tích = 3.14159 * bán_kính ** 2
r = 7
print(3.14159 * r ** 2, "cm²")
# TODO 4: Bạn có 100 viên kẹo chia đều cho 7 người.
# In ra: mỗi người được bao nhiêu viên (chia nguyên)?
# In ra: còn dư bao nhiêu viên?
# Gợi ý: Dùng // và %
a = 100
n = 7
print("Mỗi người được:", a // n, "viên kẹo")
print("Còn dư:", a % n, "viên kẹo")
# TODO 5 (Thử thách): Chuyển đổi 37 độ C sang Fahrenheit
# Công thức: F = C * 9/5 + 32
# In ra kết quả dạng: "37°C = ???°F"
c = 37
f = c * 9 / 5 + 32
print(c, "°C =", f, "°F")