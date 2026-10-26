"""Starter for the Week 07 Personal Utility Toolkit."""


def calculate_subtotal(price: float, quantity: int) -> float:
    """Return price multiplied by quantity."""
    # TODO: Return 0 when quantity is not positive; otherwise calculate.
    if quantity <= 0:
        return 0.0
    return price * quantity


def calculate_discount(subtotal: float, percent: float = 0) -> float:
    """Return the discount amount, not the final total."""
    # TODO: Calculate a percentage of subtotal.
    return subtotal * percent / 100


def calculate_average(scores: list[float]) -> float:
    """Return the average, or 0 for an empty list."""
    # TODO: Handle the empty-list boundary before dividing.
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def classify_score(average: float) -> str:
    """Return a short classification for an average score."""
    # TODO: Define a few clear ranges such as excellent, passed and practice more.
    if average >= 8:
        return "Gioi"
    if average >= 6.5:
        return "Kha"
    if average >= 5:
        return "Trung binh"
    else:
        return "Chua dat"


def format_currency(amount: float) -> str:
    """Return an amount formatted in đồng."""
    # TODO: Use an f-string with thousands separators.
    return f"{amount:,.0f} VND"


def main() -> None:
    """Compose the toolkit functions into a visible program flow."""
    # TODO: Use outputs from calculation functions as later inputs.
    price = 25_000
    quantity = 2
    discount_percent = 10
    subtotal = calculate_subtotal(price, quantity)
    discount = calculate_discount(subtotal, discount_percent)
    final_total = subtotal - discount
    print("===HOA DON===")
    print(f"Don gia: {format_currency(price)}")
    print(f"So luong: {quantity}")
    print(f"Tam tinh: {format_currency(subtotal)}")
    print(f"Giam gia: {format_currency(discount)}")
    print(f"Tong tien: {format_currency(final_total)}")
    scores = [8, 7, 9, 8.5]
    average = calculate_average(scores)
    classification = classify_score(average)
    print("\n===KET QUA HOC TAP===")
    print(f"Diem: {scores}")
    print(f"Diem trung binh: {average:.2f}")
    print(f"Xep loai: {classification}")
    print("\n===KIEM TRA===")
    print(
        "quantity = 0:", 
        format_currency(calculate_subtotal(25_000, 0)),
    )
    print(
        "scores rong:",
        calculate_average([]),
    )


if __name__ == "__main__":
    main()
