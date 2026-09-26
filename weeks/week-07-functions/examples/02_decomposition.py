"""Example 02 — split one problem into validate, calculate and format."""


def is_valid_order(price: float, quantity: int) -> bool:
    """Return whether the basic order values can be calculated."""
    return price >= 0 and quantity > 0


def calculate_subtotal(price: float, quantity: int) -> float:
    """Return the subtotal for one item."""
    return price * quantity


def apply_discount(subtotal: float, percent: float = 0) -> float:
    """Return the subtotal after a percentage discount."""
    discount = subtotal * percent / 100
    return subtotal - discount


def format_currency(amount: float) -> str:
    """Format an amount for display."""
    return f"{amount:,.0f} đ"


def build_total_line(price: float, quantity: int, percent: float = 0) -> str:
    """Compose the small steps into one result."""
    if not is_valid_order(price, quantity):
        return "Đơn hàng không hợp lệ"

    subtotal = calculate_subtotal(price, quantity)
    final_total = apply_discount(subtotal, percent)
    return f"Thành tiền: {format_currency(final_total)}"


def main() -> None:
    """Run normal and invalid examples."""
    print(build_total_line(40_000, 3, 10))
    print(build_total_line(40_000, 0))


if __name__ == "__main__":
    main()
