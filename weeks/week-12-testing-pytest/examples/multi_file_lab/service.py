"""Ghép phần tính toán và lưu trữ thành một chức năng."""

from pathlib import Path

from .pricing import calculate_total
from .storage import save_order


def create_order(quantity: int, unit_price: int, path: Path) -> dict[str, int]:
    """Tạo đơn hàng, tính tổng chính xác và lưu vào tệp."""
    total = calculate_total(quantity, unit_price)
    order = {"quantity": quantity, "unit_price": unit_price, "total": total}
    # Dữ liệu đã tính phải được lưu để lần đọc sau khôi phục đúng.
    save_order(path, order)
    return order
