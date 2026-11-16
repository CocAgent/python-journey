"""Official solutions for guarded decisions."""


def withdraw_decision(balance: float, amount: float) -> str:
    if amount <= 0:
        return "Số tiền không hợp lệ"
    if amount > balance:
        return "Không đủ số dư"
    if amount % 50_000 != 0:
        return "Cần là bội số 50,000"
    return "Được phép rút"


def ticket_price(ticket_type: str, weekend: bool, age: int) -> int:
    price = 120_000 if ticket_type == "vip" else 80_000
    if weekend:
        price *= 1.3
    if age < 12 or age >= 65:
        price *= 0.5
    elif 18 <= age <= 25:
        price *= 0.8
    return int(price)
