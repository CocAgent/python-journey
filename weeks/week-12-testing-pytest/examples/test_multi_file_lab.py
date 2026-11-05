"""Ví dụ: kiểm tra lỗi ở nhiều tệp, từ hàm nhỏ đến luồng tích hợp."""

import pytest

from multi_file_lab.pricing import calculate_total
from multi_file_lab.service import create_order
from multi_file_lab.storage import load_order


def test_calculate_total_normal() -> None:
    # Kiểm tra giá trị cụ thể, không chỉ kiểm tra kiểu dữ liệu.
    assert calculate_total(2, 15_000) == 30_000


def test_calculate_total_zero_quantity() -> None:
    # Biên: không mua sản phẩm nào thì tổng bằng 0.
    assert calculate_total(0, 15_000) == 0


@pytest.mark.parametrize("quantity,unit_price", [(-1, 100), (1, -100)])
def test_calculate_total_rejects_negative(quantity: int, unit_price: int) -> None:
    with pytest.raises(ValueError, match="không được âm"):
        calculate_total(quantity, unit_price)


def test_create_order_persists_across_files(tmp_path) -> None:
    # Một thao tác đi qua service.py → pricing.py → storage.py.
    path = tmp_path / "order.json"
    order = create_order(2, 15_000, path)
    expected = {"quantity": 2, "unit_price": 15_000, "total": 30_000}
    assert order == expected
    assert path.is_file()
    assert load_order(path) == expected


def test_create_order_rejects_invalid_quantity_before_saving(tmp_path) -> None:
    # Khi dữ liệu sai, chương trình không được ghi đơn hàng không hợp lệ.
    path = tmp_path / "invalid.json"
    with pytest.raises(ValueError, match="không được âm"):
        create_order(-1, 15_000, path)
    assert not path.exists()


def test_load_order_rejects_broken_json(tmp_path) -> None:
    path = tmp_path / "broken.json"
    path.write_text("{invalid", encoding="utf-8")
    with pytest.raises(ValueError, match="JSON không hợp lệ"):
        load_order(path)


def test_load_order_missing_file(tmp_path) -> None:
    # Không che giấu lỗi tệp chưa tồn tại bằng cách trả về dict rỗng.
    with pytest.raises(FileNotFoundError):
        load_order(tmp_path / "not-found.json")
