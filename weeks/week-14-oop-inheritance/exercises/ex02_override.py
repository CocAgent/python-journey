"""
Bài tập 02: Override & super() 🔄
===================================
Mục tiêu: Ghi đè phương thức, gọi class cha
"""

# TODO 1: Override __str__
# Class cha NhanVien: ten, luong, __str__()
# Class con QuanLy: thêm phong_ban, override __str__() thêm phòng ban
# Dùng super().__str__() + thông tin thêm


# TODO 2: Override method tính lương
# NhanVien.tinh_luong() → lương cơ bản
# QuanLy.tinh_luong() → lương + phụ cấp quản lý (20%)
# TapSu.tinh_luong() → lương × 0.7 (70%)


# TODO 3: super().__init__()
# Class cha: Vehicle(name, speed)
# Class con: ElectricCar(name, speed, battery)
# Dùng super().__init__(name, speed) trong __init__ của ElectricCar


# TODO 4 (Thử thách): Template method pattern
# Class cha Report: generate() gọi header(), body(), footer()
# Class con HTMLReport: override body() tạo HTML
# Class con TextReport: override body() tạo plain text
