"""
Bài tập 03: Tuple & Unpacking
==================================
Trình bày:
- Tuple giống như "HỘP NIÊM PHONG" - đã tạo ra là không thể thay đổi dữ liệu (immutable).
- Ưu điểm: An toàn tránh sửa nhầm, tốc độ chạy nhanh hơn list, làm khóa của dictionary được.
- Nhược điểm: Không thể thêm, xóa, sắp xếp trực tiếp; ít phương thức hỗ trợ.
"""

# TODO 1: Tạo tuple và thử nghiệm tính bất biến
# TRÌNH BÀY: Khởi tạo và dùng cơ chế Unpacking (mở hộp lấy dữ liệu đồng thời)
toa_do = (3, 7)          # Tạo tuple lưu tọa độ cố định
x, y = toa_do            # Unpacking: phân rã tuple gán thẳng cho x và y
print(f"Toa do: x = {x}, y = {y}")

# Thử sửa đổi giá trị trong tuple để kiểm chứng lỗi
try:
    toa_do[0] = 99       # Sẽ gây ra lỗi vì Tuple không cho phép gán lại phần tử
except TypeError as e:
    print(f"Loi khi sua tuple: {e}")
    print("  -> Bằng chứng Tuple là bất biến (immutable), không thể thay đổi sau khi tạo!")


# TODO 2: Hàm trả về nhiều giá trị qua tuple
# TRÌNH BÀY: Một trong những ứng dụng phổ biến nhất của Tuple trong thực tế
def tinh_thong_ke(numbers):
    """Tính toán và trả về cùng lúc 3 giá trị thông qua 1 tuple duy nhất."""
    # Python tự động đóng gói (packing) 3 giá trị này thành một tuple (min, max, trung_binh)
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


du_lieu = [5, 3, 9, 1, 7, 4, 8, 2, 6]
gia_tri_min, gia_tri_max, trung_binh = tinh_thong_ke(du_lieu)  # Unpacking nhận 3 giá trị trả về
print(f"\nThong ke {du_lieu}:")
print(f"  Min       : {gia_tri_min}")
print(f"  Max       : {gia_tri_max}")
print(f"  Trung binh: {trung_binh:.2f}")


# TODO 3: Thao tác trên danh sách chứa Tuple
# TRÌNH BÀY: Cách duyệt danh sách phức tạp và dùng lambda để so sánh, sắp xếp tuple
students = [("An", 8.5), ("Binh", 7.0), ("Chau", 9.2), ("Dung", 6.5)]

# a) Duyệt danh sách tuple kết hợp Unpacking trực tiếp trong vòng for
print("\nDanh sach sinh vien:")
for ten, diem in students:          # Tách thẳng mỗi tuple thành 2 biến: ten và diem
    print(f"  {ten}: {diem} diem")

# b) Tìm tuple có điểm cao nhất
# key=lambda sv: sv[1] nghĩa là so sánh dựa trên phần tử thứ 2 của tuple (tức là điểm số)
sv_gioi_nhat = max(students, key=lambda sv: sv[1])
print(f"\nSinh vien xuat sac nhat: {sv_gioi_nhat[0]} ({sv_gioi_nhat[1]} diem)")

# c) Sắp xếp danh sách tuple theo điểm giảm dần
# sorted() trả về một danh sách mới, không tác động đến danh sách gốc
xep_hang = sorted(students, key=lambda sv: sv[1], reverse=True)
print("\nXep hang theo diem giam dan:")
for hang, (ten, diem) in enumerate(xep_hang, start=1):  # Dùng enumerate để đánh số thứ tự từ 1
    print(f"  {hang}. {ten}: {diem} diem")


# TODO 4 (Thử thách): Kết hợp enumerate và zip
# TRÌNH BÀY: 
# - zip: Ghép đôi song song các phần tử tương ứng của 2 danh sách lại với nhau.
# - enumerate: Tự động đính kèm thêm số thứ tự tăng dần.
names = ["A", "B", "C"]
scores = [8, 9, 7]

print("\nKet hop enumerate + zip:")
# zip ghép thành: ("A", 8), ("B", 9), ("C", 7)
# enumerate thêm chỉ số: 1, 2, 3
for stt, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"  {stt}. {name} - {score} diem")
