"""
Máy tính điểm GPA 📊
====================
Nhập điểm các môn → tính GPA → xếp loại → hiển thị kết quả.
"""

print("=" * 40)
print("       MÁY TÍNH ĐIỂM GPA")
print("=" * 40)

so_mon = int(input("Nhập số lượng môn học: "))

mon_hocs = []
tong_so_tc = 0
tong_diem_nhan_tc = 0.0

for i in range(so_mon):
    print(f"\n--- Môn {i + 1} ---")
    ten_mon = input("Tên môn: ")
    so_tc = int(input("Số tín chỉ: "))
    diem_10 = float(input("Điểm (0-10): "))

    # Chuyển điểm thang 10 → thang 4
    diem_4 = diem_10 * 4 / 10

    mon_hocs.append((ten_mon, so_tc, diem_10, diem_4))
    tong_so_tc += so_tc
    tong_diem_nhan_tc += diem_4 * so_tc

# Tính GPA
gpa = tong_diem_nhan_tc / tong_so_tc

# Xếp loại
if gpa >= 3.6:
    xep_loai = "Xuất sắc"
elif gpa >= 3.2:
    xep_loai = "Giỏi"
elif gpa >= 2.5:
    xep_loai = "Khá"
elif gpa >= 2.0:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"

# In bảng kết quả
print("\n" + "=" * 55)
print("              KẾT QUẢ HỌC TẬP")
print("=" * 55)
print(f"{'STT':<5} {'Tên môn':<15} {'TC':<5} {'Điểm 10':<10} {'Điểm 4':<8}")
print("-" * 55)
for idx, (ten, tc, d10, d4) in enumerate(mon_hocs, 1):
    print(f"{idx:<5} {ten:<15} {tc:<5} {d10:<10.1f} {d4:<8.2f}")
print("-" * 55)
print(f"GPA: {gpa:.2f} / 4.0  →  {xep_loai}")
print("=" * 55)
