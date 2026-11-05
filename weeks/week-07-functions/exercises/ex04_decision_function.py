"""Exercise 04 — a deterministic decision function.

COURSE TEACHING MODEL
NOT VUACOC RUNTIME CONTRACT

Goal:
    Biến một state dạng chuỗi thành một action bằng function đơn giản.

Covered function:
    Implemented ``choose_action`` với tối đa ba rule dễ giải thích.

Examples and expected behavior:
    "danger" -> "defend"
    "opportunity" -> "advance"
    "neutral" -> "wait"

Basic invalid case:
    State không biết hoặc chuỗi rỗng cũng trả về "wait".

Self-check command:
    python weeks/week-07-functions/exercises/ex04_decision_function.py
"""


def choose_action(state: str) -> str:
    """Return a deterministic teaching action for ``state``."""
    if state == "danger":
        return "defend"
    if state == "opportunity":
        return "advance"
    return "wait"


def main() -> None:
    """Print representative decisions."""
    for state in ("danger", "opportunity", "neutral", ""):
        print(f"{state!r} -> {choose_action(state)!r}")


if __name__ == "__main__":
    main()
