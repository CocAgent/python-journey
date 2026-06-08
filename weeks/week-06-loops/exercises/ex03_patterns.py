"""
Bài tập 03: In hoa văn bằng vòng lặp lồng
===============================================
Trình bày: 
- Vòng lặp lồng nhau (Nested loops): Vòng lặp này nằm trong vòng lặp khác.
- Nguyên lý in hình học: 
  + Vòng lặp NGOÀI kiểm soát số dòng (Hàng dọc).
  + Vòng lặp TRONG kiểm soát số ký tự/khoảng trắng in ra trên mỗi dòng (Hàng ngang).
"""

n = 5  # Kích thước chung của các hoa văn hình học

# TODO 1: In tam giác vuông
# TRÌNH BÀY: Dòng thứ i sẽ có đúng i dấu sao
print("TODO 1 - Tam giac vuong:")
for i in range(1, n + 1):       # Chạy từ dòng 1 đến dòng n
    print("*" * i)               # Nhân bản ký tự '*' theo số dòng hiện tại và in ra


# TODO 2: In tam giác cân (căn giữa)
# TRÌNH BÀY: Công thức: Hàng thứ i có (n - i) khoảng trắng và (2*i - 1) dấu sao
print("\nTODO 2 - Tam giac can:")
for i in range(1, n + 1):
    so_sao = 2 * i - 1           # Số lượng sao tăng dần theo hàng lẻ: 1, 3, 5, 7, 9
    khoang_cach = n - i          # Số lượng khoảng trống giảm dần để đẩy hình vào giữa
    print(" " * khoang_cach + "*" * so_sao)


# TODO 3: In hình kim cương (n lẻ)
# TRÌNH BÀY: Chia làm 2 phần: Nửa trên phình to ra, nửa dưới thu nhỏ lại
print("\nTODO 3 - Kim cuong (n=5):")
nua_tren = (n + 1) // 2         # Xác định dòng chính giữa kim cương

# Vẽ nửa trên (tính cả dòng giữa): tăng dần số lượng sao
for i in range(1, nua_tren + 1):
    so_sao = 2 * i - 1
    khoang_cach = nua_tren - i
    print(" " * khoang_cach + "*" * so_sao)

# Vẽ nửa dưới: Giảm dần số lượng sao (chạy ngược chỉ số i từ (nửa trên - 1) về 1)
for i in range(nua_tren - 1, 0, -1):
    so_sao = 2 * i - 1
    khoang_cach = nua_tren - i
    print(" " * khoang_cach + "*" * so_sao)


# TODO 4 (Thử thách): In bàn cờ n x n
# TRÌNH BÀY: Ô chẵn (tổng chỉ số hàng + cột chia hết cho 2) in 'O', ô lẻ in 'X'
print("\nTODO 4 - Ban co (n=4):")
n_co = 4
for r in range(n_co):           # Vòng lặp ngoài kiểm soát dòng thứ r
    dong = ""                   # Chuỗi tích lũy các ô trên một dòng
    for c in range(n_co):       # Vòng lặp trong kiểm soát cột thứ c trên dòng đó
        if (r + c) % 2 == 0:   # Nếu tổng chỉ số hàng và cột chẵn
            dong += "O "       # Vẽ ô sáng
        else:                   # Nếu tổng chỉ số lẻ
            dong += "X "       # Vẽ ô tối
    print(dong.rstrip())        # In dòng đó ra và xóa khoảng trắng thừa cuối dòng
