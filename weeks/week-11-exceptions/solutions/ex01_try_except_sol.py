"""Lời giải Bài tập 01: try/except cơ bản"""
# TODO 1
try:
    so = int(input("Nhập số: "))
    print(f"100 / {so} = {100 / so:.2f}")
except ValueError:
    print("Vui lòng nhập số nguyên!")
except ZeroDivisionError:
    print("Không thể chia cho 0!")

# TODO 2
fruits = ["apple", "banana", "cherry"]
try:
    idx = int(input("Nhập index: "))
    print(f"fruits[{idx}] = {fruits[idx]}")
except ValueError:
    print("Vui lòng nhập số!")
except IndexError:
    print(f"Index phải từ 0 đến {len(fruits) - 1}")

# TODO 3
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(safe_divide(10, 3))  # 3.33...
print(safe_divide(10, 0))  # None

# TODO 4
try:
    with open("khong_ton_tai.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File không tồn tại!")

# TODO 5
def safe_int(text, default=0):
    try:
        return int(text)
    except (ValueError, TypeError):
        return default

print(safe_int("42"))      # 42
print(safe_int("abc"))     # 0
print(safe_int("abc", -1)) # -1
