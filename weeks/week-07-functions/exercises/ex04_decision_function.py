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
    # TODO: danger -> defend, opportunity -> advance, còn lại -> wait.
    raise NotImplementedError("Hoàn thành hàm choose_action")


if __name__ == "__main__":
    print("Hoàn thành TODO rồi thử danger, opportunity, neutral và chuỗi rỗng.")
