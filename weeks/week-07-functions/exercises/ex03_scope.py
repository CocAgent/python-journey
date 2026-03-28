"""
Bài tập 03: Scope & Module hóa 🏗️
====================================
Mục tiêu: Hiểu local/global scope, tổ chức code
"""

# TODO 1: Đọc code sau và dự đoán output TRƯỚC KHI chạy
x = 10
def thay_doi():
    x = 20
    print(f"Trong hàm: x = {x}")

thay_doi()
print(f"Ngoài hàm: x = {x}")
# Dự đoán: ???


# TODO 2: Viết chương trình "Sổ tay đơn giản" gồm các hàm:
# - them_ghi_chu(danh_sach, noi_dung) → thêm vào list
# - xem_ghi_chu(danh_sach) → in tất cả
# - tim_ghi_chu(danh_sach, tu_khoa) → tìm theo từ khóa
# - menu() → hiển thị menu và gọi các hàm trên


# TODO 3 (Thử thách): Viết module my_math.py riêng
# Chứa các hàm: cong, tru, nhan, chia, luy_thua
# Import vào file này và sử dụng
