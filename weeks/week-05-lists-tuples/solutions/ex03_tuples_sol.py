"""Official solution for tuple unpacking."""


def unpack_point(point: tuple[int, int]) -> str:
    x, y = point
    return f"x={x}, y={y}"


def unpack_profile(profile: tuple[str, int, str]) -> str:
    name, age, topic = profile
    return f"{name} · {age} · {topic}"


def swap(left: str, right: str) -> tuple[str, str]:
    left, right = right, left
    return left, right
