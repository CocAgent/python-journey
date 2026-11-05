"""Official solution: first output with print()."""


def greeting(name: str) -> str:
    """Return a greeting line for a name."""
    return f"Hello, {name}!"


def favourite_lines(items: list[str]) -> list[str]:
    """Return one sentence per favourite thing."""
    return [f"Tôi thích {item}" for item in items]


def rectangle(width: int, height: int) -> list[str]:
    """Return a hollow rectangle drawn with asterisks."""
    if width < 2 or height < 2:
        raise ValueError("width và height cần >= 2")
    top = "*" * width
    middle = "*" + " " * (width - 2) + "*"
    return [top, *[middle] * (height - 2), top]


if __name__ == "__main__":
    print("Hello, World!")
    print(greeting("Nguyễn Văn Minh"))

    for line in favourite_lines(["ăn phở", "nghe nhạc", "code Python"]):
        print(line)

    for line in rectangle(5, 4):
        print(line)
