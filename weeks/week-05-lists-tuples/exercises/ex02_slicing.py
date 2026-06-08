"""
Bài tập 02: Slicing & List Comprehension
=============================================
Trình bày: 
- Slicing: Cắt list ra thành các phần nhỏ.
- List Comprehension: Viết tắt vòng lặp trong ngoặc vuông [] để tạo nhanh list mới.
  Cấu trúc nhớ: [Lấy cái gì + Từ đâu + Điều kiện nào]
"""

# TODO 1: Slicing cơ bản
# TRÌNH BÀY: Cú pháp: list[start:stop:step] (bắt đầu : kết thúc : bước nhảy)
numbers = list(range(1, 21))         # Tạo danh sách từ 1 đến 20
print("Danh sach goc:", numbers)

nam_dau = numbers[:5]                # Chỉ định kết thúc là 5 -> Lấy 5 số đầu tiên (index 0 đến 4)
print("5 so dau       :", nam_dau)

nam_cuoi = numbers[-5:]              # Dùng chỉ số âm -> Lấy từ vị trí thứ 5 đếm ngược từ cuối đến hết
print("5 so cuoi      :", nam_cuoi)

vi_tri_chan = numbers[::2]           # Bước nhảy là 2 -> Lấy các phần tử ở vị trí index chẵn (0, 2, 4...)
print("So o vi tri chan (index chan):", vi_tri_chan)


# TODO 2: List comprehension cơ bản
# TRÌNH BÀY: Tạo nhanh danh sách chỉ trong 1 dòng code
# Cách nhớ: [Lấy cái gì + Từ đâu]
binh_phuong = [x ** 2 for x in range(1, 11)]          # Lấy x bình phương, với x chạy từ 1 đến 10
print("\nBinh phuong 1-10:", binh_phuong)

so_chan = [x for x in range(0, 21) if x % 2 == 0]     # Lấy x, với x chạy từ 0 đến 20, nếu x chia hết cho 2
print("So chan 0-20   :", so_chan)

words = ["hello", "world", "python"]
chu_hoa = [w.upper() for w in words]                  # Lấy w viết hoa, với w chạy trong danh sách words
print("Chu in hoa     :", chu_hoa)


# TODO 3: Lọc với comprehension
# TRÌNH BÀY: Kết hợp cả điều kiện lọc (if) và biểu thức gán nhãn (if/else)
# Cách nhớ: [Gán nhãn Đạt/Rớt + Từ đâu]
scores = [45, 78, 92, 56, 33, 88, 71, 95, 62, 50]

diem_dat = [s for s in scores if s >= 60]             # Lọc: Chỉ lấy điểm >= 60
diem_rot = [s for s in scores if s < 50]              # Lọc: Chỉ lấy điểm < 50
ket_qua = ["Dat" if s >= 60 else "Rot" for s in scores]  # Biểu thức inline: Gán nhãn tương ứng với mỗi điểm

print("\nDiem goc:", scores)
print("  Diem dat (>=60):", diem_dat)
print("  Diem rot (<50) :", diem_rot)
print("  Ket qua        :", ket_qua)


# TODO 4 (Thử thách): Ma trận chuyển vị
# TRÌNH BÀY: Dùng list comprehension lồng nhau để hoán đổi hàng và cột của ma trận
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Vòng lặp ngoài duyệt qua các cột c, vòng lặp trong lấy phần tử ở hàng r tương ứng
chuyen_vi = [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]

print("\nMa tran goc:")
for row in matrix:
    print(" ", row)

print("Ma tran chuyen vi:")
for row in chuyen_vi:
    print(" ", row)
