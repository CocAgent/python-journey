"""Official solution: arithmetic with Python."""

PI = 3.14159


def remaining_balance(budget: int, unit_price: int, quantity: int) -> int:
    """Return the money left after buying a quantity at a unit price."""
    return budget - unit_price * quantity


def circle_area(radius: float) -> float:
    """Return the area of a circle using a teaching value of pi."""
    if radius < 0:
        raise ValueError("radius cần >= 0")
    return PI * radius**2


def share_candy(total: int, people: int) -> tuple[int, int]:
    """Return candies per person and the remainder."""
    if people <= 0:
        raise ValueError("people cần > 0")
    return total // people, total % people


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


if __name__ == "__main__":
    print("2024 + 1000 =", 2024 + 1000)
    print(f"Số tiền còn lại: {remaining_balance(150_000, 35_000, 3):,} VNĐ")
    print(f"Diện tích hình tròn: {circle_area(7):.2f}")

    each, left = share_candy(100, 7)
    print(f"Mỗi người: {each} viên, dư: {left} viên")
    print(f"37°C = {celsius_to_fahrenheit(37)}°F")
