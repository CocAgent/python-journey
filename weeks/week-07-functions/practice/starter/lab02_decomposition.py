"""Lab 02 — Decomposition: validate -> subtotal -> discount.

Giữ số tiền bằng int VND; giảm giá làm tròn XUỐNG số nguyên đồng.
calculate_final(25_000, 2, 10) == 45_000.
calculate_final(25_000, 2) == 50_000.
"""


def is_valid_order(price: int, quantity: int, percent: int) -> bool:
    """True khi cả ba input là int (không phải bool) trong phạm vi."""
    # TODO: type(...) is int, price >= 0, quantity > 0, 0 <= percent <= 100.
    raise NotImplementedError("Hoàn thành bước validate")


def calculate_subtotal(price: int, quantity: int) -> int:
    """Tính tạm tính sau khi kiểm price và quantity."""
    # TODO: gọi is_valid_order(price, quantity, 0);
    #       invalid => raise ValueError; valid => return price * quantity.
    raise NotImplementedError("Hoàn thành bước subtotal")


def calculate_final(price: int, quantity: int, percent: int = 0) -> int:
    """Ghép các bước, trả tổng sau giảm, làm tròn xuống số nguyên VND."""
    # TODO: gọi is_valid_order(price, quantity, percent); invalid => ValueError.
    # TODO: amount = calculate_subtotal(price, quantity).
    # TODO: return amount * (100 - percent) // 100.
    raise NotImplementedError("Hoàn thành bước final")


if __name__ == "__main__":
    print("Tự hoàn thiện ba hàm rồi thử tính hóa đơn.")
