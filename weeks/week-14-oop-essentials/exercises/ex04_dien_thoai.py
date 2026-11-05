"""Bài 4: tạo lớp DienThoai, hai đối tượng và hiển thị thông tin.

Không thay thế NotImplementedError bằng pass: bài chưa hoàn thành phải
được báo lỗi khi chạy kiểm thử.
"""


# Họ tên:
# MSSV:
# Lớp:

# Câu a: Tạo lớp DienThoai
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
        print("Giá bán:", format(self.GiaBan, ",").replace(",", "."), "VNĐ")


# Câu b: Tạo 2 đối tượng điện thoại
DT01 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
DT02 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)


# Gọi phương thức hiển thị thông tin
print("===== THÔNG TIN ĐIỆN THOẠI 1 =====")
DT01.thongtindienthoai()

print("\n===== THÔNG TIN ĐIỆN THOẠI 2 =====")
DT02.thongtindienthoai()
