"""Official solution for slicing, alias and copy."""


def slices(numbers: list[int]) -> tuple[list[int], list[int]]:
    return numbers[:3], numbers[-3:]


def alias_and_copy(numbers: list[int]) -> tuple[list[int], list[int], list[int]]:
    original = numbers.copy()
    alias = original
    copied = original.copy()
    alias.append(3)
    return original, alias, copied
