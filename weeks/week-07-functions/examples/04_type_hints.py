"""Example 04 — basic type hints communicate intent."""


def add(a: int, b: int) -> int:
    """Return the result of Python's ``+`` operation."""
    return a + b


def calculate_total(price: float, quantity: int) -> float:
    """Return a numeric total."""
    return price * quantity


def build_message(name: str, total: float) -> str:
    """Return a message ready for display."""
    return f"{name} cần thanh toán {total:,.0f} đ"


def main() -> None:
    """Run examples and explain the runtime distinction."""
    total = calculate_total(12_500, 3)
    print(build_message("An", total))
    print(f"add(2, 3) = {add(2, 3)}")

    # Annotations do not insert a runtime type check. Python evaluates the
    # operation normally; a separate checker could warn before runtime.
    joined_text = add("Py", "thon")  # type: ignore[arg-type]
    print(f"Python vẫn chạy add với chuỗi: {joined_text}")

    print("Type hints giúp người và công cụ hiểu ý định.")
    print("Python không tự enforce annotations tại runtime.")


if __name__ == "__main__":
    main()
