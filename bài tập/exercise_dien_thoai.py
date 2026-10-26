"""Bài tập làm thêm: Lớp DienThoai theo đề Câu 5."""


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
        print("Dung lượng pin:", self.DungLuongPin, "mAh")
        print("Giá bán:", f"{self.GiaBan:,}", "VNĐ")


def main():
    dt01 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    dt02 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

    print("===== THÔNG TIN ĐIỆN THOẠI 1 =====")
    dt01.thongtindienthoai()

    print("\n===== THÔNG TIN ĐIỆN THOẠI 2 =====")
    dt02.thongtindienthoai()


if __name__ == "__main__":
    main()
