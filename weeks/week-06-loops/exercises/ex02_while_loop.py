"""
Bài tập 02: Vòng lặp while
================================
Trình bày:
- Vòng lặp while: Dùng khi CHƯA BIẾT TRƯỚC số lần lặp, chạy liên tục dựa trên điều kiện kiểm soát.
- Vòng lặp vô hạn (while True): Chạy mãi mãi, thường kết hợp với 'break' để thoát khi đạt điều kiện.
- continue: Bỏ qua các lệnh phía sau ở vòng lặp hiện tại, lập tức quay lại đầu vòng lặp.
"""

# TODO 1: Đếm ngược từ 10 → 1
# TRÌNH BÀY: Vòng lặp while cơ bản với một biến điều kiện giảm dần
dem = 10                      # Khởi tạo giá trị bắt đầu là 10
while dem >= 1:               # Tiếp tục chạy khi biến đếm còn lớn hơn hoặc bằng 1
    print(dem)
    dem -= 1                  # Rất quan trọng: Giảm biến đếm để tránh vòng lặp vô hạn
print("Phong!")               # In sau khi kết thúc vòng lặp


# TODO 2: Trò chơi đoán số
# TRÌNH BÀY: Ứng dụng while True để lặp lại hành động đoán của người dùng đến khi đúng mới dừng
import random

bi_mat = random.randint(1, 100)  # Máy chọn ngẫu nhiên một số bí mật từ 1 đến 100
so_lan = 0                        # Biến đếm số lần người dùng đoán

print("\nTro choi doan so (1 - 100):")
while True:                       # Lặp vô hạn cho đến khi người dùng đoán trúng (gặp lệnh break)
    try:
        doan = int(input("  Nhap du doan cua ban: "))  # Lấy dữ liệu và ép kiểu về số nguyên
    except ValueError:
        print("  Vui long nhap mot so nguyen!")        # Bắt lỗi nếu người dùng nhập chữ hoặc ký tự lạ
        continue                                        # Lập tức quay lại dòng nhập, bỏ qua đoạn code dưới

    so_lan += 1                   # Tăng số lần đoán sau khi nhập số hợp lệ

    if doan < bi_mat:
        print("  Cao hon!")       # Gợi ý số bí mật lớn hơn số vừa đoán
    elif doan > bi_mat:
        print("  Thap hon!")      # Gợi ý số bí mật nhỏ hơn số vừa đoán
    else:
        print(f"  Chinh xac! So bi mat la {bi_mat}. Ban doan {so_lan} lan.")
        break                     # Đoán đúng -> Thoát vòng lặp lập tức


# TODO 3: Nhập tuổi hợp lệ (Nhập liệu an toàn)
# TRÌNH BÀY: Ép buộc người dùng nhập đúng chuẩn, nếu sai bắt nhập lại
print()
while True:
    try:
        tuoi = int(input("Nhap tuoi cua ban (1 - 120): "))
        if 1 <= tuoi <= 120:      # Kiểm tra tuổi nằm trong giới hạn thực tế
            print(f"  Tuoi hop le: {tuoi}")
            break                 # Hợp lệ thì dừng vòng lặp
        else:
            print("  Tuoi phai nam trong khoang 1 den 120, thu lai!")
    except ValueError:
        print("  Vui long nhap mot so nguyen hop le!")


# TODO 4 (Thử thách): Menu chương trình lặp lại
# TRÌNH BÀY: Vòng lặp giữ cho chương trình terminal hoạt động liên tục cho tới khi chọn Thoát
print()
while True:
    print("=== Menu ===")
    print("  1. Cong")
    print("  2. Tru")
    print("  3. Nhan")
    print("  4. Thoat")

    lua_chon = input("Chon phep tinh (1-4): ").strip()  # Cắt bỏ khoảng trắng thừa đầu và cuối

    if lua_chon == "4":           # Người dùng chọn thoát
        print("Tam biet!")
        break                     # Kết thúc chương trình
    elif lua_chon in ("1", "2", "3"):
        try:
            a = float(input("  Nhap so a: "))   # Nhập số thực thứ nhất
            b = float(input("  Nhap so b: "))   # Nhập số thực thứ hai
        except ValueError:
            print("  Gia tri khong hop le!\n")
            continue              # Nhập sai thì quay về menu ban đầu

        if lua_chon == "1":
            print(f"  {a} + {b} = {a + b}\n")
        elif lua_chon == "2":
            print(f"  {a} - {b} = {a - b}\n")
        elif lua_chon == "3":
            print(f"  {a} x {b} = {a * b}\n")
    else:
        print("  Lua chon khong hop le, thu lai!\n")
