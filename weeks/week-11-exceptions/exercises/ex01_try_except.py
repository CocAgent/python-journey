"""Exercise 01: expected bad input."""

raw_turn = "not-a-number"

try:
    turn = int(raw_turn)
    print(turn)
except ValueError:
    print(f"Lỗi: '{raw_turn}' không phải là một số hợp lệ. Vui lòng nhập một số nguyên.")

