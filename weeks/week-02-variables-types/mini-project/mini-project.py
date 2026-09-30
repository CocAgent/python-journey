ho_ten = input("Nhập họ tên: ")
mssv = input("Nhập MSSV: ")
nganh = input("Nhập ngành: ")
nam_nhap_hoc = int(input("Nhập năm nhập học: "))

nam_tot_nghiep = nam_nhap_hoc + 4
khoa = f"{nam_nhap_hoc} - {nam_tot_nghiep}"

print("╔════════════════════════════╗")
print("║    THẺ SINH VIÊN           ║")
print("║----------------------------║")
print(f"║ Họ tên:  {ho_ten:<17} ║")
print(f"║ MSSV:    {mssv:<17} ║")
print(f"║ Ngành:   {nganh:<17} ║")
print(f"║ Khóa:    {khoa:<17} ║")
print("╚════════════════════════════╝")