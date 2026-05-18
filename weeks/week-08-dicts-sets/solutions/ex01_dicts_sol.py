"""Lời giải Bài tập 01: Dictionary cơ bản"""
# TODO 1
sv = {"ten": "An", "tuoi": 20, "diem": 8.5, "lop": "12A1"}
for key in sv:
    print(f'{key}: {sv[key]} (get: {sv.get(key)})')

# TODO 2
diem = {"Toán": 8, "Văn": 7, "Anh": 9, "Lý": 6, "Hóa": 8}
diem["Sinh"] = 7
diem["Văn"] = 8
del diem["Hóa"]
for mon, d in diem.items():
    print(f"{mon}: {d}")
tb = sum(diem.values()) / len(diem)
print(f"TB: {tb:.1f}")

# TODO 3
squares = {i: i**2 for i in range(1, 11)}
evens = {k: v for k, v in squares.items() if k % 2 == 0}
print(squares)
print(evens)

# TODO 4
text = input("Nhập chuỗi: ")
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
