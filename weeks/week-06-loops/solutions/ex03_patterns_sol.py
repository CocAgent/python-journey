"""Official solution for readable comprehensions."""


def squares(numbers: list[int]) -> list[int]:
    return [number**2 for number in numbers]


def even_numbers(numbers: list[int]) -> list[int]:
    return [number for number in numbers if number % 2 == 0]
