"""Exercise 01: expected bad input."""

raw_turn= "buitrungson"
try:
    turn=int(raw_turn)
    print("S hop le:")
except ValueError:
    print("Du lieu nay khong pphia kieu so nguyen")
