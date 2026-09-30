"""Exercise 04 — a deterministic decision function.

COURSE TEACHING MODEL
NOT VUACOC RUNTIME CONTRACT

Goal:
    Biến một state dạng chuỗi thành một action bằng function đơn giản.

TODO:
    Hoàn thành ``choose_action`` với tối đa ba rule dễ giải thích.

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
    # Xử lý an toàn: loại bỏ khoảng trắng thừa và chuyển về chữ thường (nếu cần)
    cleaned_state = state.strip().lower() if state else ""

    if cleaned_state == "danger":
        return "defend"
    elif cleaned_state == "opportunity":
        return "advance"
    else:
        return "wait"


if __name__ == "__main__":
    # Test thử các trường hợp
    print(choose_action("danger"))       # defend
    print(choose_action("opportunity"))  # advance
    print(choose_action("neutral"))      # wait
    print(choose_action(""))             # wait
    print(choose_action("unknown"))      # wait