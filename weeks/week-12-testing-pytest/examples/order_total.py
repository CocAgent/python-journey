"""Ví dụ: tính thành tiền với ràng buộc đầu vào rõ ràng."""


def tinh_thanh_tien(so_luong: int, don_gia: int) -> int:
    """Trả về thành tiền, báo lỗi nếu số lượng hoặc đơn giá âm."""
    # Giá trị âm không phù hợp với mô hình đơn hàng đơn giản của bài.
    if so_luong < 0 or don_gia < 0:
        raise ValueError("Số lượng và đơn giá không được âm")

    # Số lượng bằng 0 hợp lệ: chưa mua hàng thì thành tiền bằng 0.
    return so_luong * don_gia
