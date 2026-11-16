"""Ví dụ 07 — Chuyển dữ liệu qua hàm, tránh biến global ẩn.

Dữ liệu đơn hàng là giả lập, VND dùng số nguyên, không gọi mạng.
"""

def validate_order(price: int, quantity: int) -> bool:
    """Kiểm quy tắc đơn giản của bài học trước khi tính."""
    return price >= 0 and quantity > 0


def subtotal(price: int, quantity: int) -> int:
    """Phép tính không in, không sửa global state."""
    return price * quantity


def with_shipping(amount: int, shipping: int = 0) -> int:
    """Trả số tiền mới, không thay đổi amount ở caller."""
    return amount + shipping


def build_receipt(price: int, quantity: int, shipping: int = 0) -> str:
    """Kết hợp kiểm → tính → thêm phí → định dạng."""
    if not validate_order(price, quantity) or shipping < 0:
        return "Đơn hàng không hợp lệ"
    amount = subtotal(price, quantity)  # local
    final = with_shipping(amount, shipping)  # local
    return f"Thanh toán: {final:,} VND"


def main() -> None:
    input_price = 20_000
    print(f"Giá ở caller trước: {input_price}")
    print(build_receipt(input_price, 2, 5_000))
    print(f"Giá ở caller sau: {input_price}")
    print(build_receipt(20_000, 0))
    print(build_receipt(20_000, 2, -1))


if __name__ == "__main__":
    main()
