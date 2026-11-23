"""
Bài tập 02: Máy tính Python 🧮
================================
Mục tiêu: Sử dụng các phép tính cơ bản trong Python
"""

# TODO 1: Tính và in ra kết quả của 2024 + 1000
result1 = 2024 + 1000
print("TODO 1:", result1)

# TODO 2: Bạn có 150,000 VNĐ, mua 3 ly cà phê giá 35,000 VNĐ/ly.
# Tính và in ra số tiền còn lại.
money = 150000
coffee_price = 35000
remaining = money - coffee_price * 3
print("TODO 2: Số tiền còn lại:", remaining, "VNĐ")

# TODO 3: Tính diện tích hình tròn có bán kính = 7
# Gợi ý: Diện tích = 3.14159 * bán_kính ** 2
radius = 7
area = 3.14159 * radius ** 2
print("TODO 3: Diện tích hình tròn:", round(area, 2))

# TODO 4: Bạn có 100 viên kẹo chia đều cho 7 người.
# In ra: mỗi người được bao nhiêu viên (chia nguyên)?
# In ra: còn dư bao nhiêu viên?
# Gợi ý: Dùng // và %
candies = 100
people = 7

each_person = candies // people
leftover = candies % people

print("TODO 4: Mỗi người được:", each_person, "viên kẹo")
print("TODO 4: Số kẹo còn dư:", leftover, "viên")

# TODO 5 (Thử thách): Chuyển đổi 37 độ C sang Fahrenheit
# Công thức: F = C * 9/5 + 32
# In ra kết quả dạng: "37°C = ???°F"
celsius = 37
fahrenheit = celsius * 9 / 5 + 32

print("TODO 5:", celsius, "°C =", fahrenheit, "°F")
