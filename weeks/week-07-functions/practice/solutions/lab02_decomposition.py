"""Lời giải 02 — Tách kiểm dữ liệu, tạm tính, giảm giá."""


def is_valid_order(price: int, quantity: int, percent: int) -> bool:
    """Kiểm dữ liệu runtime vì type hints không tự kiểm."""
    return (
        type(price) is int
        and type(quantity) is int
        and type(percent) is int
        and price >= 0
        and quantity > 0
        and 0 <= percent <= 100
    )


def calculate_subtotal(price: int, quantity: int) -> int:
    """Gọi validator rồi tính tạm tính."""
    if not is_valid_order(price, quantity, 0):
        raise ValueError("Đơn hàng không hợp lệ")
    return price * quantity


def calculate_final(price: int, quantity: int, percent: int = 0) -> int:
    """Dùng các hàm nhỏ; làm tròn xuống đến đồng nguyên."""
    if not is_valid_order(price, quantity, percent):
        raise ValueError("Đơn hàng không hợp lệ")
    amount = calculate_subtotal(price, quantity)
    return amount * (100 - percent) // 100


if __name__ == "__main__":
    print(f"Tổng: {calculate_final(25_000, 2, 10):,} VND")
