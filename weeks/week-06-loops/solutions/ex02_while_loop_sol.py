"""Official solution for while, break and continue."""


def countdown(start: int) -> list[int]:
    values = []
    remaining = start
    while remaining > 0:
        values.append(remaining)
        remaining -= 1
    return values


def selected_numbers() -> list[int]:
    values = []
    for number in range(1, 11):
        if number % 3 == 0:
            continue
        if number > 8:
            break
        values.append(number)
    return values
