# Nhập thông tin sinh viên
ten = input("Nhập họ tên: ")
mssv = input("Nhập MSSV: ")
nghanh = input("Nhập ngành học: ")
namhoc = int(input("Nhập năm nhập học: "))

# Tính năm tốt nghiệp dự kiến
graduation_year = namhoc + 4

# Nội dung hiển thị
line1 = "THẺ SINH VIÊN"
line2 = f"Họ tên : {ten}"
line3 = f"MSSV   : {mssv}"
line4 = f"Ngành  : {nghanh}"
line6 = f"Khóa: {namhoc} - {graduation_year}"

# Tính độ rộng khung
width = max(
    len(line1),
    len(line2),
    len(line3),
    len(line4),
    len(line6)
) + 5

# In khung
print("╔" + "═" * width + "╗")
print(f"║{line1.center(width)}║")
print("╠" + "═" * width + "╣")
print(f"║ {line2.ljust(width - 2)} ║")
print(f"║ {line3.ljust(width - 2)} ║")
print(f"║ {line4.ljust(width - 2)} ║")
print(f"║ {line6.ljust(width - 2)} ║")
print("╚" + "═" * width + "╝")