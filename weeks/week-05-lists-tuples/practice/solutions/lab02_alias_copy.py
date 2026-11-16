"""Lời giải tham khảo Lab 02: alias là cùng list, copy là list khác."""

numbers = [10, 20, 30, 40, 50]
first_two = numbers[:2]
last_two = numbers[-2:]
alias = numbers
snapshot = numbers.copy()
alias.append(60)
numbers[0] = 99

print(f"Đầu: {first_two}")
print(f"Cuối: {last_two}")
print(f"Gốc: {numbers}")
print(f"Alias: {alias}")
print(f"Copy: {snapshot}")
print(f"Cùng đối tượng: {alias is numbers}")
