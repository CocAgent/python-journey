"""
CÂU 2 — XỬ LÝ CHUỖI (2.0 điểm)

Nhập chuỗi s và thực hiện:
a) Đếm ký tự chữ hoa.
b) Kiểm tra chuỗi có đối xứng hay không.
c) Tính tổng các chữ số xuất hiện trong chuỗi.

Gợi ý ôn tập:
- isupper(): kiểm tra chữ hoa.
- s[::-1]: đảo ngược chuỗi.
- isdigit(): kiểm tra ký tự là chữ số.
- int(): đổi ký tự số thành số nguyên.
"""


def dem_chu_hoa(s):
    dem = 0

    for ky_tu in s:
        if ky_tu.isupper():
            dem += 1

    return dem


def la_chuoi_doi_xung(s):
    return s == s[::-1]


def tinh_tong_chu_so(s):
    tong = 0

    for ky_tu in s:
        if ky_tu.isdigit():
            tong += int(ky_tu)

    return tong


def main():
    s = input("Nhập chuỗi s: ")

    print("Số ký tự chữ hoa:", dem_chu_hoa(s))

    if la_chuoi_doi_xung(s):
        print("Chuỗi đối xứng.")
    else:
        print("Chuỗi không đối xứng.")

    print("Tổng các chữ số trong chuỗi:", tinh_tong_chu_so(s))


if __name__ == "__main__":
    main()
