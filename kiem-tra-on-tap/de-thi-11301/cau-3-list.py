"""
CÂU 3 — DANH SÁCH LIST (2.0 điểm)

a) Nhập số nguyên vào danh sách, nhập 0 để kết thúc. In danh sách.
b) Tính tổng các số dương chẵn trong danh sách.
c) Đếm số lần xuất hiện của phần tử k.

Gợi ý ôn tập:
- append(): thêm phần tử vào cuối danh sách.
- break: kết thúc vòng lặp.
- i > 0 and i % 2 == 0: số dương chẵn.
- dem += 1: tăng biến đếm.
"""


def nhap_danh_sach():
    danh_sach = []

    while True:
        x = int(input("Nhập phần tử (0 để kết thúc): "))

        if x == 0:
            break

        danh_sach.append(x)

    return danh_sach


def tong_so_duong_chan(danh_sach):
    tong = 0

    for i in danh_sach:
        if i > 0 and i % 2 == 0:
            tong += i

    return tong


def dem_so_lan_xuat_hien(danh_sach, k):
    dem = 0

    for i in danh_sach:
        if i == k:
            dem += 1

    return dem


def main():
    danh_sach = nhap_danh_sach()
    print("Danh sách vừa nhập:", danh_sach)

    print("Tổng các số dương chẵn:", tong_so_duong_chan(danh_sach))

    k = int(input("Nhập phần tử k cần đếm: "))
    dem = dem_so_lan_xuat_hien(danh_sach, k)

    if dem == 0:
        print("Không có phần tử", k, "trong danh sách.")
    else:
        print("Số lần xuất hiện của", k, "là:", dem)


if __name__ == "__main__":
    main()
