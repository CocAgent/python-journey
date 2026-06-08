"""
Bài tập 01: Tạo và thao tác List
=====================================
Trình bày: List giống như một "GIỎ HÀNG LINH HOẠT" - có thể bỏ thêm vào, 
lấy ra, sắp xếp lại tùy ý (mutable).
"""

# TODO 1: Tạo list 5 môn học yêu thích
# GIỚI THIỆU: Khởi tạo giỏ hàng ban đầu
mon_hoc = ["Toan", "Ly", "Hoa", "Van", "Anh"]  # Khởi tạo list 5 phần tử
print("Danh sach ban dau:", mon_hoc)

# THAO TÁC 1: append() - Thêm đồ vào cuối giỏ hàng
mon_hoc.append("Tin hoc")                        # Thêm phần tử vào cuối list
print("Sau khi append 'Tin hoc':", mon_hoc)

# THAO TÁC 2: insert() - Chèn đồ vào đúng vị trí mong muốn
mon_hoc.insert(2, "Sinh hoc")                    # Chèn "Sinh hoc" tại vị trí index 2 (vị trí thứ 3)
print("Sau khi insert 'Sinh hoc' vao vi tri 2:", mon_hoc)

# THAO TÁC 3: remove() - Lấy/xóa đồ ra khỏi giỏ theo tên
mon_hoc.remove("Hoa")                            # Xóa phần tử đầu tiên có giá trị "Hoa"
print("Sau khi remove 'Hoa':", mon_hoc)


# TODO 2: Thống kê danh sách điểm
# GIỚI THIỆU: Thao tác tính toán trên list điểm số
diem = [7, 9, 5, 8, 10, 6, 4, 9]               # List điểm ban đầu
print("\nDanh sach diem ban dau:", diem)

# THAO TÁC 4: sort() - Sắp xếp lại giỏ hàng tại chỗ
diem.sort()                                      # Sắp xếp tăng dần tại chỗ (sửa trực tiếp list gốc)
print("Sau khi sap xep tang dan:", diem)

# THỐNG KÊ: max(), min(), len(), sum() là các hàm hỗ trợ cực mạnh của list
cao_nhat = max(diem)                             # Lấy giá trị lớn nhất trong list
thap_nhat = min(diem)                            # Lấy giá trị nhỏ nhất trong list
trung_binh = sum(diem) / len(diem)               # Tổng các phần tử chia cho số lượng phần tử
print(f"Cao nhat: {cao_nhat} | Thap nhat: {thap_nhat} | Trung binh: {trung_binh:.2f}")

# LỌC NHANH: Đếm số điểm đạt
so_dat = len([d for d in diem if d >= 5])        # Đếm các phần tử thỏa mãn điều kiện >= 5
print(f"So diem dat (>=5): {so_dat}/{len(diem)}")


# TODO 3: Nhập n số từ người dùng rồi thống kê
# TRÌNH BÀY: Cách dùng vòng lặp để thu thập dữ liệu vào list
print("\nNhap danh sach so:")
n = int(input("Nhap n (so luong phan tu): "))   # Ép kiểu dữ liệu nhập vào thành số nguyên
so_nhap = []                                     # Chuẩn bị một list rỗng để chứa dữ liệu
for i in range(n):                               # Lặp n lần để nhận n số
    x = float(input(f"  Nhap so thu {i + 1}: "))  # Nhận số thực (float) từ bàn phím
    so_nhap.append(x)                            # Bỏ số vừa nhập vào cuối list

print(f"\nDanh sach vua nhap: {so_nhap}")
print(f"  Tong      : {sum(so_nhap)}")           # Tính tổng các số đã nhập
print(f"  Trung binh: {sum(so_nhap) / len(so_nhap):.2f}")
print(f"  Min       : {min(so_nhap)}")
print(f"  Max       : {max(so_nhap)}")


# TODO 4 (Thử thách): Xóa phần tử trùng lặp, giữ nguyên thứ tự
# TRÌNH BÀY: Logic loại bỏ trùng lặp thủ công (không dùng set)
nums = [1, 3, 2, 3, 1, 5, 2, 4]

seen = []    # List trung gian để đánh dấu những số đã từng gặp
unique = []  # List kết quả chứa các số không bị lặp

for num in nums:               # Duyệt qua từng số trong danh sách gốc
    if num not in seen:        # Nếu số này chưa từng gặp trước đây
        seen.append(num)       # Đánh dấu là đã gặp nó rồi
        unique.append(num)     # Thêm nó vào danh sách kết quả

print(f"\nXoa trung lap:")
print(f"  Truoc: {nums}")
print(f"  Sau  : {unique}")
