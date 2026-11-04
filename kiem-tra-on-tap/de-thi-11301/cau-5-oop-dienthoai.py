"""
CÂU 5 — LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG (2.0 điểm)

Tạo lớp DienThoai gồm các thuộc tính:
MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan.

Phương thức:
- __init__(): khởi tạo các thuộc tính.
- thongtindienthoai(): hiển thị thông tin điện thoại.

Tạo hai đối tượng DT01 và DT02 theo dữ liệu đề bài.

Gợi ý ôn tập:
- class: khai báo lớp.
- self: đại diện cho đối tượng hiện tại.
- self.ten_thuoc_tinh = tham_so: gán dữ liệu vào thuộc tính.
- doi_tuong.ten_phuong_thuc(): gọi phương thức.
"""


class DienThoai:
    def __init__(self, MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan):
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan

    def thongtindienthoai(self):
        print("Mã máy:", self.MaMay)
        print("Tên máy:", self.TenMay)
        print("Hãng sản xuất:", self.HangSanXuat)
        print("Dung lượng pin:", self.DungLuongPin)
        print("Giá bán:", self.GiaBan)


def main():
    DT01 = DienThoai(
        "DT01", "iPhone 15 Pro", "Apple", 3274, 28990000
    )

    DT02 = DienThoai(
        "DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000
    )

    print("--- Điện thoại 1 ---")
    DT01.thongtindienthoai()

    print("\n--- Điện thoại 2 ---")
    DT02.thongtindienthoai()


if __name__ == "__main__":
    main()
