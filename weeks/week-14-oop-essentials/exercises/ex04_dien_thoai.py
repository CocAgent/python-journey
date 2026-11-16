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
        # TODO: lưu đủ năm thuộc tính với self.
        raise NotImplementedError("TODO: khởi tạo điện thoại")

    def thongtindienthoai(self) -> str:
        # TODO: trả chuỗi có đủ 5 trường; lệnh print nằm bên ngoài class.
        raise NotImplementedError("TODO: tạo chuỗi thông tin điện thoại")


if __name__ == "__main__":
    # TODO: tạo DT01 và DT02 theo đề bài rồi gọi print(...).
    raise NotImplementedError("TODO: tạo hai đối tượng DienThoai")
