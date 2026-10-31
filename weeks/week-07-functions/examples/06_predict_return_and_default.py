"""Ví dụ 06 — Dự đoán hàm trả về gì và khi nào dùng default parameter.

Chạy: python weeks/week-07-functions/examples/06_predict_return_and_default.py
"""

def show_price(price: int, quantity: int) -> None:
    """In ra thông tin; không trả về con số để tính tiếp."""
    print(f"show_price in: {price * quantity:,} VND")


def calculate_price(price: int, quantity: int, fee: int = 0) -> int:
    """Trả về giá trị cho nơi gọi; fee mặc định bằng 0."""
    return price * quantity + fee


def first_positive(numbers: list[int]) -> int | None:
    """Dừng sớm khi gặp số dương đầu tiên; trả None nếu không có."""
    for number in numbers:
        if number > 0:
            return number
    return None


def main() -> None:
    printed_result = show_price(12_000, 2)
    print(f"Caller nhận từ show_price: {printed_result!r}")
    subtotal = calculate_price(12_000, 2)
    print(f"Caller nhận từ calculate_price: {subtotal:,} VND")
    print(f"Thêm phí 5,000: {calculate_price(12_000, 2, 5_000):,} VND")
    print(f"Số dương đầu tiên: {first_positive([-2, 0, 7, 9])}")
    print(f"Không có số dương: {first_positive([-2, 0])!r}")


if __name__ == "__main__":
    main()
