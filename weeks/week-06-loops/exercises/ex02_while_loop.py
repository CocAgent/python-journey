"""Exercise 02: while, break and continue."""

remaining = 5

# 1. Đếm ngược về 1 và cập nhật remaining qua từng vòng lặp
print("Đếm ngược:")
while remaining > 0:
    print(f"remaining = {remaining}")
    remaining -= 1

# 2. Lặp qua 1..10, bỏ qua bội số của 3 (continue) và dừng sau 8 (break)
print("\nLặp qua 1..10 (bỏ qua bội số của 3, dừng sau 8):")
for number in range(1, 11):
    if number % 3 == 0:
        continue
    if number > 8:
        break
    print(number)

print(f"\nGiá trị còn lại sau vòng lặp: remaining = {remaining}")
