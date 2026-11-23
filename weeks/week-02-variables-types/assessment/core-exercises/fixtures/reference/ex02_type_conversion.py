"""Trusted checker fixture; not a student submission."""

# TODO 1: Chuyển chuỗi 42, cộng 8
so_text = "42"
so = int(so_text)
print(so + 8)

# TODO 2: int của pi
pi = 3.14159
print(int(pi))

# TODO 3: bool()
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("hello"))
print(bool([]))
print(bool([1, 2]))

# TODO 4: BMI
chieu_cao = float(input())
can_nang = float(input())
bmi = can_nang / (chieu_cao ** 2)
print(f"BMI: {bmi:.1f}")

# TODO 5 (Thử thách): không yêu cầu làm
