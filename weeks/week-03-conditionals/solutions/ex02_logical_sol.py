"""Official solutions for boolean logic."""


def can_drive(age: int, has_license: bool, is_alert: bool) -> bool:
    return age >= 18 and has_license and is_alert


def triangle_type(a: float, b: float, c: float) -> str:
    if min(a, b, c) <= 0 or a + b <= c or a + c <= b or b + c <= a:
        return "Không hợp lệ"
    if a == b == c:
        return "Đều"
    if a == b or b == c or a == c:
        return "Cân"
    return "Thường"


def strong_password(password: str) -> bool:
    return (
        len(password) >= 8
        and any(character.isupper() for character in password)
        and any(character.islower() for character in password)
        and any(character.isdigit() for character in password)
    )


def fizzbuzz(number: int) -> str:
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)
