"""
Bài tập 02: Máy tính Python 🧮
================================
Mục tiêu: Sử dụng các phép tính cơ bản trong Python
"""

print(2024 + 1000)


# TODO 2: Bạn có 150,000 VNĐ, mua 3 ly cà phê giá 35,000 VNĐ/ly.
# Tính và in ra số tiền còn lại.
price = 35000
cups = 3
budget = 150000
remaining = budget - price * cups
print(remaining)


# TODO 3: Tính diện tích hình tròn có bán kính = 7
radius = 7
area = 3.14159 * radius ** 2
print(area)
# Gợi ý: Diện tích = 3.14159 * bán_kính ** 2


# TODO 4: Bạn có 100 viên kẹo chia đều cho 7 người.
candies = 100
people = 7
each = candies // people
leftover = candies % people
print(f"Mỗi người được {each} viên kẹo")
print(f"Còn dư {leftover} viên kẹo")


# TODO 5 (Thử thách): Chuyển đổi 37 độ C sang Fahrenheit
celsius = 37
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}°C = {fahrenheit}°F")
