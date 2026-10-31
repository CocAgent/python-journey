"""Lời giải Lab 03: continue bỏ lượt, break dừng vòng for."""

selected: list[int] = []
for number in range(1, 11):
    if number % 3 == 0:
        continue
    if number > 8:
        break
    selected.append(number)

squares = [n**2 for n in selected if n % 2 == 0]
print(f"Đã chọn: {selected}")
print(f"Bình phương chẵn: {squares}")
