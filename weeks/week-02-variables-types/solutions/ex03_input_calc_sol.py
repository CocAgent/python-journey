"""Official solution: calculations after input conversion."""


def calculate_total(first: float, second: float) -> float:
    """Return the sum of two converted numbers."""
    return first + second


def discounted_price(price: float, discount_percent: float) -> float:
    """Return a price after a percentage discount."""
    return price * (1 - discount_percent / 100)


def vnd_to_usd(amount: float, exchange_rate: float) -> float:
    """Convert VND using a caller-provided teaching exchange rate."""
    return amount / exchange_rate


if __name__ == "__main__":
    first = float(input("Số thứ nhất: "))
    second = float(input("Số thứ hai: "))
    print(f"Tổng: {calculate_total(first, second)}")
