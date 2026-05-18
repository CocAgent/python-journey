"""
Mini-Project: Thẻ sinh viên tự động 🪪
=====================================
Nhập thông tin sinh viên -> in thẻ với border và căn chỉnh đẹp.

Chạy: python student_card.py
"""

print("--- NHẬP THÔNG TIN SINH VIÊN ---")
ho_ten = input("Nhập họ tên: ").strip()
mssv = input("Nhập MSSV: ").strip()
nganh = input("Nhập chuyên ngành: ").strip()
nam_nhap_hoc = int(input("Nhập năm nhập học: "))

nam_tot_nghiep = nam_nhap_hoc + 4
khoa = f"{nam_nhap_hoc} - {nam_tot_nghiep}"

# Tính toán độ rộng khung thẻ
max_content_len = max(
    len(f" Họ tên:  {ho_ten}"),
    len(f" MSSV:    {mssv}"),
    len(f" Ngành:   {nganh}"),
    len(f" Khóa:    {khoa}"),
    len("    THẺ SINH VIÊN    ")
)
width = max_content_len + 4

print("\n" + "╔" + "═" * width + "╗")
print("║" + "THẺ SINH VIÊN".center(width) + "║")
print("║" + "-" * width + "║")
print("║" + f"  Họ tên:  {ho_ten}".ljust(width) + "║")
print("║" + f"  MSSV:    {mssv}".ljust(width) + "║")
print("║" + f"  Ngành:   {nganh}".ljust(width) + "║")
print("║" + f"  Khóa:    {khoa}".ljust(width) + "║")
print("╚" + "═" * width + "╝")
