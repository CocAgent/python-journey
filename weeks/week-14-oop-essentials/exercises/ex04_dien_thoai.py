"""Bài 4: tạo lớp DienThoai, hai đối tượng và hiển thị thông tin.

Không thay thế NotImplementedError bằng pass: bài chưa hoàn thành phải
được báo lỗi khi chạy kiểm thử.
"""


class DienThoai:
    def __init__(
        self,
        ma_may: str,
        ten_may: str,
        hang_san_xuat: str,
        dung_luong_pin: int,
        gia_ban: int,
    ) -> None:
        # TODO: từ chối mã/tên/hãng rỗng; dung_luong_pin <= 0; gia_ban < 0.
        if not ma_may.strip() or not ten_may.strip() or not hang_san_xuat.strip():
            raise ValueError ("Mã máy, tên máy hoặc hãng sản xuất không được rỗng")
        if dung_luong_pin <= 0:
            raise ValueError ("Dung lượng pin phải lớn hơn 0")
        if gia_ban < 0:
            raise ValueError ("Giá bán không được âm")
        # TODO: lưu đủ năm thuộc tính với self.
        self.ma_may = ma_may
        self.ten_may = ten_may
        self.hang_san_xuat = hang_san_xuat
        self.dung_luong_pin = dung_luong_pin
        self.gia_ban = gia_ban


    def thongtindienthoai(self) -> str:
        # TODO: trả chuỗi có đủ 5 trường; lệnh print nằm bên ngoài class.
        return (
            f"Mã máy: {self.ma_may}\n"
            f"Tên máy: {self.ten_may}\n"
            f"Hãng sản xuất: {self.hang_san_xuat}\n"
            f"Dung lượng pin: {self.dung_luong_pin} mAh\n"
            f"Giá bán: {self.gia_ban} VND\n"
        )
    


if __name__ == "__main__":
    # TODO: tạo DT01 và DT02 theo đề bài rồi gọi print(...).
    iphone = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28_990_000)
    samsung = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29_990_000)
    print(iphone.thongtindienthoai())
    print(samsung.thongtindienthoai())
