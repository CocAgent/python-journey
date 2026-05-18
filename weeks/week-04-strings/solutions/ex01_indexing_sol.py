"""Lời giải Bài tập 01: Indexing & Slicing"""
s = "Python Journey"

# TODO 1
print(f"Ký tự đầu: {s[0]}")
print(f"Ký tự cuối: {s[-1]}")
print(f"5 ký tự đầu: {s[:5]}")

# TODO 2
print(f"Journey: {s[7:]}")
print(f"Đảo ngược: {s[::-1]}")
print(f"Mỗi ký tự thứ 2: {s[::2]}")

# TODO 3
cccd = input("Nhập CCCD (12 số): ")
print(f"Mã tỉnh: {cccd[:2]}")
print(f"Giới tính: {cccd[2]}")
print(f"Năm sinh: {cccd[3:5]}")

# TODO 4
text = input("Nhập chuỗi: ").lower().replace(" ", "")
if text == text[::-1]:
    print("Palindrome!")
else:
    print("Không phải palindrome")
