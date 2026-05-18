"""Lời giải Bài tập 03: Set & Phép toán tập hợp"""
# TODO 1
hk1 = {"Toán", "Văn", "Anh", "Lý", "Hóa"}
hk2 = {"Toán", "Văn", "Anh", "Sinh", "Sử"}
print(f"Cả 2 kỳ: {hk1 & hk2}")
print(f"Chỉ kỳ 1: {hk1 - hk2}")
print(f"Chỉ kỳ 2: {hk2 - hk1}")
print(f"Tất cả: {hk1 | hk2}")

# TODO 2
words = ["apple", "banana", "apple", "cherry", "banana", "date"]
seen = set()
unique = []
for w in words:
    if w not in seen:
        seen.add(w)
        unique.append(w)
print(unique)

# TODO 3
s1 = set(input("Câu 1: ").lower().split())
s2 = set(input("Câu 2: ").lower().split())
print(f"Từ chung: {s1 & s2}")
print(f"Chỉ câu 1: {s1 - s2}")
print(f"Chỉ câu 2: {s2 - s1}")

# TODO 4
a = input("Chuỗi 1: ").lower().replace(" ", "")
b = input("Chuỗi 2: ").lower().replace(" ", "")
print("Anagram!" if sorted(a) == sorted(b) else "Không phải anagram")
