"""Example 03 — prefer local data over mutable global state."""

GLOBAL_TOTAL = 0


def add_to_global(amount: int) -> int:
    """Show the global-state anti-pattern in a small isolated function."""
    global GLOBAL_TOTAL
    GLOBAL_TOTAL += amount
    return GLOBAL_TOTAL


def add_to_total(current_total: int, amount: int) -> int:
    """Return a new value without changing hidden state."""
    new_total = current_total + amount
    return new_total


def calculate_session_total(first: int, second: int) -> int:
    """Keep intermediate values local to this function."""
    subtotal = add_to_total(first, second)
    bonus = 5
    return add_to_total(subtotal, bonus)


def main() -> None:
    """Show that explicit input produces an easy-to-follow result."""
    starting_total = 10
    session_total = calculate_session_total(starting_total, 20)

    print(f"Giá trị ban đầu: {starting_total}")
    print(f"Kết quả local: {session_total}")
    print(f"Global chưa bị đổi: {GLOBAL_TOTAL}")
    print("add_to_global tồn tại để minh họa anti-pattern, không phải luồng chính.")


if __name__ == "__main__":
    main()
