ho_ten = input("Nhập họ tên: ")
mssv = input("Nhập MSSV: ")
nganh = input("Nhập ngành: ")
nam_nhap_hoc = int(input("Nhập năm nhập học: "))

nam_tot_nghiep = nam_nhap_hoc + 4

print()
print("╔══════════════════════════════════╗")
print("║          THẺ SINH VIÊN           ║")
print("║----------------------------------║")
print(f"║ Họ tên:  {ho_ten:<24}║")
print(f"║ MSSV:    {mssv:<24}║")
print(f"║ Ngành:   {nganh:<24}║")
print(f"║ Khóa:    {nam_nhap_hoc} - {nam_tot_nghiep:<13}║")
print("╚══════════════════════════════════╝")