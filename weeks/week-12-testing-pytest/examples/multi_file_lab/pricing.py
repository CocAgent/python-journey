"""Tính thành tiền và kiểm tra dữ liệu đầu vào."""


def calculate_total(quantity: int, unit_price: int) -> int:
    """Tính thành tiền; không chấp nhận số lượng hoặc đơn giá âm."""
    # Giá trị âm làm sai ý nghĩa đơn hàng, nên kiểm tra trước khi tính.
    if quantity < 0 or unit_price < 0:
        raise ValueError("Số lượng và đơn giá không được âm")
    return quantity * unit_price
