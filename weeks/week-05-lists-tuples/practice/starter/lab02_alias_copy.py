"""Lab 02 — Slice, alias, copy: dự đoán rồi tự kiểm.

Dữ liệu ban đầu là một list phẳng, chưa cần deepcopy.
"""

numbers = [10, 20, 30, 40, 50]

# TODO 1: first_two = numbers[:2] và last_two = numbers[-2:].
# TODO 2: alias = numbers; snapshot = numbers.copy().
# TODO 3: alias.append(60), sau đó numbers[0] = 99.
# TODO 4: in chính xác:
# Đầu: [10, 20]
# Cuối: [40, 50]
# Gốc: [99, 20, 30, 40, 50, 60]
# Alias: [99, 20, 30, 40, 50, 60]
# Copy: [10, 20, 30, 40, 50]
# Cùng đối tượng: True

print("TODO Lab 02: chưa hoàn thiện")
