"""
CÂU 1 — SỐ NGUYÊN (2.0 điểm)

a) Nhập số nguyên dương n trong đoạn [1, 1500]. Nếu sai thì nhập lại.
b) Viết hàm đếm số lượng chữ số lẻ của n.
c) Viết hàm tính S = 1/2 + 1/4 + ... + 1/(2*n).

Gợi ý ôn tập:
- while: kiểm tra dữ liệu nhập.
- % 10: lấy chữ số cuối.
- // 10: bỏ chữ số cuối.
- range(1, n + 1): lặp từ 1 đến n.
"""


def dem_chu_so_le(n):
    dem = 0

    while n != 0:
        chu_so = n % 10

        if chu_so % 2 != 0:
            dem += 1

        n //= 10

    return dem


def tinh_s(n):
    tong = 0

    for i in range(1, n + 1):
        tong += 1 / (2 * i)

    return tong


def main():
    n = int(input("Nhập số nguyên 1 <= n <= 1500: "))

    while n < 1 or n > 1500:
        n = int(input("Không hợp lệ. Nhập lại n (1..1500): "))

    print("Số lượng chữ số lẻ:", dem_chu_so_le(n))
    print("S =", tinh_s(n))


if __name__ == "__main__":
    main()
