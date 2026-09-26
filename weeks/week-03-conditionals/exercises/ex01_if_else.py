"""
Bài tập 01: if/elif/else cơ bản 🔀
====================================
Mục tiêu: Viết câu lệnh điều kiện đúng cú pháp
"""

# =============================================================
# TODO 1: Phân nhóm tuổi
# Ý tưởng: Hỏi người dùng bao nhiêu tuổi, rồi in ra họ thuộc
#          nhóm nào (thiếu nhi, thiếu niên, người lớn, cao tuổi)
# =============================================================

tuoi = int(input("Nhập tuổi của bạn: "))
# int(...)  → chuyển chữ người dùng gõ thành số nguyên
# input(...)→ hiện câu hỏi lên màn hình và đợi người gõ

if tuoi < 13:              # Nếu tuổi nhỏ hơn 13
    print("Thiếu nhi")
elif tuoi <= 17:           # Nếu không phải trên, mà tuổi từ 13-17
    print("Thiếu niên")
elif tuoi <= 64:           # Nếu không phải trên, mà tuổi từ 18-64
    print("Người lớn")
else:                      # Còn lại (>= 65) — không cần kiểm tra thêm
    print("Người cao tuổi")


# =============================================================
# TODO 2: Xếp loại học lực theo điểm
# Ý tưởng: Hỏi điểm số, rồi in ra loại học lực tương ứng
# Python kiểm tra từ TRÊN XUỐNG — dừng ngay khi gặp điều kiện đúng
# =============================================================

diem = float(input("Nhập điểm (0-10): "))
# float(...) → chuyển thành số thập phân (để nhập 8.5, 7.25, v.v.)

if diem >= 9:              # Từ 9.0 trở lên
    print("Xếp loại: Xuất sắc")
elif diem >= 8:            # Từ 8.0 đến 8.9 (vì >= 9 đã bị chặn trên)
    print("Xếp loại: Giỏi")
elif diem >= 6.5:          # Từ 6.5 đến 7.9
    print("Xếp loại: Khá")
elif diem >= 5:            # Từ 5.0 đến 6.4
    print("Xếp loại: Trung bình")
else:                      # Dưới 5.0
    print("Xếp loại: Yếu")


# =============================================================
# TODO 3: Kiểm tra năm nhuận
# Quy tắc năm nhuận:
#   ✅ Chia hết cho 400     → năm nhuận (vd: 2000)
#   ✅ Chia hết cho 4       → năm nhuận (vd: 2024)
#   ❌ Chia hết cho 100     → KHÔNG nhuận (vd: 1900)
# =============================================================

nam = int(input("Nhập năm: "))
# Toán tử %  → lấy phần dư của phép chia
# vd: 2024 % 4 = 0  (chia hết, không dư)
#     2023 % 4 = 3  (còn dư 3, không chia hết)

if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
    # Điều kiện trên đọc thành tiếng Việt:
    # "Nếu chia hết cho 400" HOẶC "chia hết cho 4 VÀ không chia hết cho 100"
    print(f"{nam} là năm nhuận 🗓️")
else:
    print(f"{nam} không phải năm nhuận")


# =============================================================
# TODO 4 (Thử thách): Tìm số lớn nhất trong 3 số
# Ý tưởng: Hỏi 3 số, so sánh từng cặp để tìm ra số to nhất
# Quy tắc: KHÔNG dùng hàm max() — phải tự so sánh bằng if/elif/else
# =============================================================

a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))

if a >= b and a >= c:      # a lớn hơn hoặc bằng CẢ HAI b và c
    lon_nhat = a
elif b >= a and b >= c:    # b lớn hơn hoặc bằng cả a và c
    lon_nhat = b
else:                      # Còn lại → c là lớn nhất
    lon_nhat = c

print(f"Số lớn nhất là: {lon_nhat}")
