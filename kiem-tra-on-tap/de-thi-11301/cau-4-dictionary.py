"""
CÂU 4 — DICTIONARY (2.0 điểm)

a) Nhập thông tin sách: mã sách, tên sách, tác giả, nhà xuất bản,
   năm xuất bản. Lưu thông tin vào từ điển.
b) Nhập mã sách cần xóa. Nếu có mã trong từ điển thì xóa,
   nếu không thì thông báo không tìm thấy.

Cách lưu:
tu_dien[ma_sach] = [ten_sach, tac_gia, nha_xuat_ban, nam_xuat_ban]

Gợi ý ôn tập:
- dictionary[key] = value: thêm/cập nhật phần tử.
- in dictionary: kiểm tra khóa có tồn tại không.
- del dictionary[key]: xóa phần tử theo khóa.
"""


from datetime import datetime


def nhap_sach():
    n = int(input("Nhập số lượng sách (n > 0): "))

    while n <= 0:
        n = int(input("Số lượng phải lớn hơn 0. Nhập lại: "))

    tu_dien = {}
    nam_hien_tai = datetime.now().year

    for i in range(n):
        print(f"\n--- Nhập sách thứ {i + 1} ---")

        ma_sach = input("Mã số sách: ")
        ten_sach = input("Tên sách: ")
        tac_gia = input("Tên tác giả: ")
        nha_xuat_ban = input("Nhà xuất bản: ")

        nam_xuat_ban = int(input("Năm xuất bản: "))
        while nam_xuat_ban > nam_hien_tai:
            nam_xuat_ban = int(
                input(f"Năm không hợp lệ. Nhập năm <= {nam_hien_tai}: ")
            )

        tu_dien[ma_sach] = [
            ten_sach,
            tac_gia,
            nha_xuat_ban,
            nam_xuat_ban,
        ]

    return tu_dien


def xoa_sach(tu_dien, ma_can_xoa):
    if ma_can_xoa in tu_dien:
        del tu_dien[ma_can_xoa]
        print(f"Cuốn sách có mã {ma_can_xoa} đã được xóa.")
    else:
        print("Không tìm thấy cuốn sách cần xóa.")


def main():
    tu_dien = nhap_sach()

    print("\nDanh sách sách:")
    print(tu_dien)

    ma_can_xoa = input("\nNhập mã số sách cần xóa: ")
    xoa_sach(tu_dien, ma_can_xoa)

    print("\nTừ điển sau khi xử lý:")
    print(tu_dien)


if __name__ == "__main__":
    main()
