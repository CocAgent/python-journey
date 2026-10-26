"""Mini-project — Personal Utility Toolkit."""


def calculate_subtotal(price: float, quantity: int) -> float:
    """Tính tạm tính; trả về 0.0 nếu số lượng không dương."""
    if quantity <= 0:
        return 0.0
    return price * quantity


def calculate_discount(subtotal: float, percent: float = 0.0) -> float:
    """Tính số tiền giảm từ tạm tính và phần trăm giảm giá."""
    if subtotal <= 0 or percent <= 0:
        return 0.0
    return subtotal * (percent / 100)


def calculate_average(scores: list[float]) -> float:
    """Tính điểm trung bình từ danh sách điểm; trả về 0.0 nếu danh sách rỗng."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def classify_score(average: float) -> str:
    """Phân loại học tập dựa trên điểm trung bình."""
    if average >= 8.5:
        return "Xuất sắc"
    elif average >= 7.0:
        return "Khá"
    elif average >= 5.0:
        return "Trung bình"
    else:
        return "Cần cố gắng"


def format_currency(amount: float) -> str:
    """Định dạng số tiền thành chuỗi tiền tệ VNĐ (ví dụ: 100,000 VNĐ)."""
    return f"{amount:,.0f} VNĐ"


def main() -> None:
    print("==========================================")
    print("      PERSONAL UTILITY TOOLKIT            ")
    print("==========================================")

    # --- PHẦN 1: TÍNH HÓA ĐƠN (Invoice Processing) ---
    print("\n1. XỬ LÝ HÓA ĐƠN")
    item_price = 150_000.0
    item_quantity = 3
    discount_percent = 10.0

    # Chạy luồng dữ liệu: price + quantity -> subtotal -> discount -> final total -> format
    subtotal = calculate_subtotal(item_price, item_quantity)
    discount_amount = calculate_discount(subtotal, discount_percent)
    final_total = subtotal - discount_amount

    print(f" - Đơn giá:           {format_currency(item_price)}")
    print(f" - Số lượng:          {item_quantity}")
    print(f" - Tạm tính:          {format_currency(subtotal)}")
    print(f" - Giảm giá ({discount_percent}%):    {format_currency(discount_amount)}")
    print(f" - Tổng thanh toán:   {format_currency(final_total)}")

    # Thử nghiệm trường hợp số lượng = 0
    zero_subtotal = calculate_subtotal(item_price, 0)
    print(f" - [Edge Case] Số lượng = 0 -> Tạm tính: {format_currency(zero_subtotal)}")

    # --- PHẦN 2: ĐÁNH GIÁ KẾT QUẢ HỌC TẬP (Academic Report) ---
    print("\n2. ĐÁNH GIÁ KẾT QUẢ HỌC TẬP")
    student_scores = [8.5, 9.0, 7.5, 8.0, 10.0]

    # Chạy luồng dữ liệu: scores -> average -> classification
    avg_score = calculate_average(student_scores)
    academic_rank = classify_score(avg_score)

    print(f" - Danh sách điểm:    {student_scores}")
    print(f" - Điểm trung bình:   {avg_score:.2f}")
    print(f" - Xếp loại:          {academic_rank}")

    # Thử nghiệm trường hợp danh sách điểm rỗng
    empty_scores: list[float] = []
    empty_avg = calculate_average(empty_scores)
    empty_rank = classify_score(empty_avg)
    print(f" - [Edge Case] Danh sách điểm rỗng -> ĐTB: {empty_avg:.1f} ({empty_rank})")


if __name__ == "__main__":
    main()