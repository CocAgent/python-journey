"""Ví dụ tuần 12: tách phép tính khỏi việc nhập và in dữ liệu."""


def tinh_thanh_tien(so_luong: int, don_gia: int) -> int:
    """Trả về thành tiền; từ chối số lượng hoặc đơn giá âm."""
    # Nếu đầu vào âm, báo lỗi ngay để tránh tạo ra hóa đơn không hợp lệ.
    if so_luong < 0 or don_gia < 0:
        raise ValueError("Số lượng và đơn giá không được âm")

    # Trường hợp số lượng bằng 0 vẫn hợp lệ và cho thành tiền bằng 0.
    return so_luong * don_gia
