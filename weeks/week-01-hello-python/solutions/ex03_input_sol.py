"""Official solution: talking to the user with input()."""


def birth_year(current_year: int, age: int) -> int:
    """Return an approximate birth year from a current age."""
    if age < 0:
        raise ValueError("age cần >= 0")
    return current_year - age


def total_of(first: float, second: float) -> float:
    """Return the sum of two numbers."""
    return first + second


def mad_lib(name: str, adjective: str, animal: str, number: str) -> list[str]:
    """Return a two-line story built from user words."""
    return [
        f"{name} có một con {animal} rất {adjective}.",
        f"Mỗi ngày nó ăn {number} bát cơm!",
    ]


if __name__ == "__main__":
    name = input("Bạn tên là gì? ").strip()
    print(f"Xin chào, {name}!")

    age = int(input("Bạn bao nhiêu tuổi? "))
    print(f"Bạn sinh năm {birth_year(2026, age)}")

    first = float(input("Nhập số thứ nhất: "))
    second = float(input("Nhập số thứ hai: "))
    print(f"Tổng: {first} + {second} = {total_of(first, second)}")

    for line in mad_lib(
        input("Nhập tên: ").strip(),
        input("Nhập tính từ: ").strip(),
        input("Nhập con vật: ").strip(),
        input("Nhập một số: ").strip(),
    ):
        print(line)
