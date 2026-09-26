"""Reject invalid input before the main decision."""


def ticket_price(age: int) -> int | None:
    """Return a teaching price, or None for an invalid age."""
    if age < 0 or age > 120:
        return None
    if age < 12 or age >= 65:
        return 40_000
    return 80_000


for age in (-1, 10, 30, 70):
    print(f"age={age}, price={ticket_price(age)}")
