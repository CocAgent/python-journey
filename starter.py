# Mini-project — Thẻ sinh viên

ten = input("Nhập tên: ")
ma_sinh_vien = input("Nhập mã sinh viên: ")
nganh = input("Nhập ngành: ")

nam_nhap_hoc = input("Nhập năm nhập học: ")

# Kiểm tra năm chỉ gồm chữ số
if nam_nhap_hoc.isdigit():
    nam_nhap_hoc = int(nam_nhap_hoc)

    nam_tot_nghiep = nam_nhap_hoc + 4

    print("\n========== THẺ SINH VIÊN ==========")
    print(f"Họ tên: {ten}")
    print(f"Mã sinh viên: {ma_sinh_vien}")
    print(f"Ngành: {nganh}")
    print(f"Năm nhập học: {nam_nhap_hoc}")
    print(f"Năm dự kiến tốt nghiệp: {nam_tot_nghiep}")
    print("===================================")

else:
    print("Năm nhập học phải là số!")