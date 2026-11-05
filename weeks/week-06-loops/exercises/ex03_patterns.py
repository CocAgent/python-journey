"""Exercise 03: readable list comprehensions."""

numbers = range(1, 11)

# 1. Tạo squares cho tất cả các số bằng list comprehension
squares: list[int] = [number**2 for number in numbers]

# 2. Tạo even_numbers với bộ lọc (filter) điều kiện chẵn
even_numbers: list[int] = [number for number in numbers if number % 2 == 0]

# 3. Viết lại comprehension thành vòng lặp for thông thường để so sánh
squares_loop: list[int] = []
for number in numbers:
    squares_loop.append(number**2)

print("Squares (comprehension):", squares)
print("Even numbers (comprehension):", even_numbers)
print("Squares (for loop):", squares_loop)
print("Ket qua hai cach giong nhau:", squares == squares_loop)
