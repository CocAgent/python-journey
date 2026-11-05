"""Lời giải 01 — Return giá trị, không in trong logic."""


def calculate_total(price: int, quantity: int, shipping: int = 0) -> int:
    """Tính tổng tiền giả lập bằng số nguyên VND."""
    if (
        type(price) is not int
        or type(quantity) is not int
        or type(shipping) is not int
        or price < 0
        or quantity <= 0
        or shipping < 0
    ):
        raise ValueError("Giá, số lượng hoặc phí không hợp lệ")
    return price * quantity + shipping


if __name__ == "__main__":
    print(f"Thành tiền: {calculate_total(12_000, 2):,} VND")
