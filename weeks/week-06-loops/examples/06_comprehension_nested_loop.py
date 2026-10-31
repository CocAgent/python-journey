"""Ví dụ 06 — comprehension tương đương for, và nested loop đơn giản.

Không cần functions/class/ngoại lệ chuyên sâu.
"""

numbers = [1, 2, 3, 4, 5, 6]

evens_for = []
for number in numbers:
    if number % 2 == 0:
        evens_for.append(number**2)

evens_comprehension = [number**2 for number in numbers if number % 2 == 0]
print(f"for thường: {evens_for}")
print(f"comprehension: {evens_comprehension}")
print(f"Hai cách như nhau: {evens_for == evens_comprehension}")

# Loop lồng nhau khi thật sự cần các cặp hàng/cột.
cells = []
for row in range(1, 3):
    for col in range(1, 4):
        cells.append((row, col))
print(f"Ô lưới 2×3: {cells}")
print(f"Số ô: {len(cells)}")

empty_numbers = []
print(f"Không có số: {[n**2 for n in empty_numbers if n % 2 == 0]}")
