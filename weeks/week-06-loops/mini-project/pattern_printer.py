"""
Mini-Project Week 06: Pattern Printer
========================================
In cac hoa van hinh hoc bang vong lap long.
"""


def in_tam_giac_vuong(n, ky_tu):
    """Tam giác vuông, tăng dần từ trái."""
    print(f"\nTam giac vuong (n={n}, ky tu='{ky_tu}'):")
    for i in range(1, n + 1):        # i = 1, 2, ..., n
        print(ky_tu * i)             # in i ký tự → bậc thang tăng dần


def in_tam_giac_can(n, ky_tu):
    """Tam giác cân, căn giữa."""
    print(f"\nTam giac can (n={n}, ky tu='{ky_tu}'):")
    for i in range(1, n + 1):
        so_ky_tu = 2 * i - 1         # số ký tự hàng i: 1, 3, 5, ...
        khoang = n - i               # khoảng trắng bên trái để căn giữa
        print(" " * khoang + ky_tu * so_ky_tu)


def in_kim_cuong(n, ky_tu):
    """Kim cương, n phải lẻ để cân đối."""
    if n % 2 == 0:                   # kiểm tra n lẻ, nếu chẵn tự tăng thêm 1
        n += 1
        print(f"  (n chan, tu dong dieu chinh thanh n={n})")
    print(f"\nKim cuong (n={n}, ky tu='{ky_tu}'):")
    nua = (n + 1) // 2              # số hàng của nửa trên kể cả đỉnh

    for i in range(1, nua + 1):     # nửa trên: số ký tự tăng dần
        so_ky_tu = 2 * i - 1
        khoang = nua - i
        print(" " * khoang + ky_tu * so_ky_tu)

    for i in range(nua - 1, 0, -1):  # nửa dưới: số ký tự giảm dần
        so_ky_tu = 2 * i - 1
        khoang = nua - i
        print(" " * khoang + ky_tu * so_ky_tu)


def in_cay_thong(n, ky_tu):
    """Cây thông gồm tán lá (tam giác cân) và thân."""
    print(f"\nCay thong (n={n}, ky tu='{ky_tu}'):")
    for i in range(1, n + 1):        # tán lá: n hàng tam giác cân
        so_ky_tu = 2 * i - 1
        khoang = n - i
        print(" " * khoang + ky_tu * so_ky_tu)
    # Thân cây: 3 ký tự căn giữa
    than = "|||"
    khoang_than = (2 * n - 1 - len(than)) // 2   # căn giữa so với chiều rộng tán
    print(" " * khoang_than + than)


def lay_ky_tu():
    """Hỏi người dùng chọn ký tự in, mặc định là '*'."""
    ky_tu = input("  Nhap ky tu in (Enter de dung '*'): ").strip()
    return ky_tu if ky_tu else "*"   # nếu bỏ trống → dùng '*'


def lay_kich_thuoc():
    """Hỏi kích thước n, lặp đến khi nhập số nguyên dương."""
    while True:
        try:
            n = int(input("  Nhap kich thuoc n (so nguyen duong): "))
            if n > 0:                # chỉ chấp nhận số nguyên dương
                return n
            print("  n phai lon hon 0!")
        except ValueError:
            print("  Vui long nhap so nguyen!")


def main():
    """Vòng lặp menu chính."""
    while True:
        print("\n=== PATTERN PRINTER ===")
        print("  1. Tam giac vuong")
        print("  2. Tam giac can")
        print("  3. Kim cuong")
        print("  4. Cay thong")
        print("  5. Thoat")

        chon = input("Chon hoa van (1-5): ").strip()

        if chon == "5":
            print("Tam biet!")
            break                    # thoát chương trình

        if chon not in ("1", "2", "3", "4"):
            print("  Lua chon khong hop le!")
            continue                 # quay lại menu

        n = lay_kich_thuoc()         # hỏi kích thước
        ky_tu = lay_ky_tu()          # hỏi ký tự

        if chon == "1":
            in_tam_giac_vuong(n, ky_tu)
        elif chon == "2":
            in_tam_giac_can(n, ky_tu)
        elif chon == "3":
            in_kim_cuong(n, ky_tu)
        elif chon == "4":
            in_cay_thong(n, ky_tu)


if __name__ == "__main__":
    main()
