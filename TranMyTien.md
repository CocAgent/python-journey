WEEK 2
Bài Tập Thực Hành
Bài 1: lí lịch cá nhân
ho_ten = "Trần Mỹ Tiên"  #string
tuoi = 20              #int
chieu_cao = 1.66         #float
thanh_pho = "Bến Tre"  #string
is_sinh_vien = True   #bool 
# in ra format đẹp
print(f"{'=== LÝ LỊCH CÁ NHÂN ===':^30}")
print("-" * 30)
print(f"Họ và tên: {ho_ten:<20}")
print(f"Tuổi:      {tuoi:<20}")
print(f"Chiều cao: {chieu_cao:.2f} m")         
print(f"Thành phố: {thanh_pho:<20}")
print(f"Sinh viên: {'Có' if is_sinh_vien else 'Không'}") 
print("-" * 30)

Bài 2: Đổi tiền tệ
ty_gia = 25000
nhap_usd = input("Nhập số tiền USD muốn đổi: ").strip()
if nhap_use:
  so_usd = float(usd_nhap)
  so_vnd = so_usd * ty_gia
  print(f"Số tiền VND tương đương: {so_vnd:,.0f} VND")
else:
  print("Bạn chưa nhập số tiền cần đổi!")
