"""Example 01 — ``print`` displays; ``return`` gives data back."""


def show_total(price: float, quantity: int) -> None:
    """Display a total but give no value back to the caller."""
    total = price * quantity
    print(f"Hàm print-only hiển thị: {total:,.0f} đ")


def calculate_total(price: float, quantity: int) -> float:
    """Return a total so the caller can keep using it."""
    return price * quantity


def add_shipping(total: float, shipping_fee: float) -> float:
    """Return the total after adding a shipping fee."""
    return total + shipping_fee


def main() -> None:
    """Compare the two styles with visible output."""
    print("1. Function chỉ hiển thị:")
    print_only_result = show_total(25_000, 2)
    print(f"Giá trị caller nhận được: {print_only_result}")

    print("\n2. Function trả dữ liệu:")
    subtotal = calculate_total(25_000, 2)
    final_total = add_shipping(subtotal, 15_000)
    print(f"Tạm tính: {subtotal:,.0f} đ")
    print(f"Sau phí giao hàng: {final_total:,.0f} đ")


if __name__ == "__main__":
    main()
