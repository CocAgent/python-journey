"""Lab 01 — Hàm RETURN giá trị, không chỉ print.

calculate_total(12_000, 2) == 24_000
calculate_total(12_000, 2, 5_000) == 29_000
price âm, quantity <=0, shipping âm, bool thay số -> ValueError.
Học theo PRACTICE/README.md trước khi mở solutions.
"""


def calculate_total(price: int, quantity: int, shipping: int = 0) -> int:
    """Trả về thành tiền (VND) khi dữ liệu hợp lệ; ngược lại raise ValueError."""
    # TODO: kiểm type(value) is int để bool không lọt qua;
    #       price >= 0, quantity > 0, shipping >= 0.
    # TODO: return price * quantity + shipping, KHÔNG print ở đây.
    raise NotImplementedError("Hoàn thành Lab 01")


if __name__ == "__main__":
    print("Tự làm TODO rồi thử calculate_total(12_000, 2).")
