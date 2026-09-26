"""Starter for the Week 07 Personal Utility Toolkit."""


def calculate_subtotal(price: float, quantity: int) -> float:
    """Return price multiplied by quantity."""
    # TODO: Return 0 when quantity is not positive; otherwise calculate.
    raise NotImplementedError("Complete calculate_subtotal")


def calculate_discount(subtotal: float, percent: float = 0) -> float:
    """Return the discount amount, not the final total."""
    # TODO: Calculate a percentage of subtotal.
    raise NotImplementedError("Complete calculate_discount")


def calculate_average(scores: list[float]) -> float:
    """Return the average, or 0 for an empty list."""
    # TODO: Handle the empty-list boundary before dividing.
    raise NotImplementedError("Complete calculate_average")


def classify_score(average: float) -> str:
    """Return a short classification for an average score."""
    # TODO: Define a few clear ranges such as excellent, passed and practice more.
    raise NotImplementedError("Complete classify_score")


def format_currency(amount: float) -> str:
    """Return an amount formatted in đồng."""
    # TODO: Use an f-string with thousands separators.
    raise NotImplementedError("Complete format_currency")


def main() -> None:
    """Compose the toolkit functions into a visible program flow."""
    # TODO: Use outputs from calculation functions as later inputs.
    print("Complete the toolkit, then replace this message with useful output.")


if __name__ == "__main__":
    main()
