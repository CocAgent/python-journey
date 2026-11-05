"""Starter for the Week 07 Personal Utility Toolkit."""


def calculate_subtotal(price: float, quantity: int) -> float:
    """Return price multiplied by quantity."""
    if quantity <= 0:
        return 0.0
    return price * quantity


def calculate_discount(subtotal: float, percent: float = 0) -> float:
    """Return the discount amount, not the final total."""
    return subtotal * percent / 100


def calculate_average(scores: list[float]) -> float:
    """Return the average, or 0 for an empty list."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def classify_score(average: float) -> str:
    """Return a short classification for an average score."""
    if average >= 8:
        return "excellent"
    if average >= 5:
        return "passed"
    return "practice more"


def format_currency(amount: float) -> str:
    """Return an amount formatted in đồng."""
    return f"{amount:,.0f} đ"


def main() -> None:
    """Compose the toolkit functions into a visible program flow."""
    subtotal = calculate_subtotal(25_000, 2)
    discount = calculate_discount(subtotal, 10)
    total = subtotal - discount
    average = calculate_average([8.5, 7.0, 9.0])
    print(f"Subtotal: {format_currency(subtotal)}")
    print(f"Discount: {format_currency(discount)}")
    print(f"Total: {format_currency(total)}")
    print(f"Average: {average:.1f} — {classify_score(average)}")


if __name__ == "__main__":
    main()
