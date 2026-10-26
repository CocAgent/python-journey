"""Ví dụ tuần 12: kiểm tra nhiều trường hợp bằng pytest."""

import pytest

from order_total import tinh_thanh_tien


@pytest.mark.parametrize(
    ("so_luong", "don_gia", "ket_qua"),
    [
        (2, 15_000, 30_000),  # Trường hợp thông thường.
        (0, 15_000, 0),  # Biên: chưa mua món nào.
        (3, 0, 0),  # Biên: món hàng miễn phí.
    ],
)
def test_tinh_thanh_tien_hop_le(
    so_luong: int, don_gia: int, ket_qua: int
) -> None:
    # Cùng một phép kiểm tra chạy trên nhiều bộ dữ liệu để tránh lặp code.
    assert tinh_thanh_tien(so_luong, don_gia) == ket_qua


@pytest.mark.parametrize("so_luong,don_gia", [(-1, 10_000), (2, -100)])
def test_tu_choi_gia_tri_am(so_luong: int, don_gia: int) -> None:
    # Test phải xác nhận hàm từ chối dữ liệu sai, không chỉ kiểm tra giá trị trả về.
    with pytest.raises(ValueError, match="không được âm"):
        tinh_thanh_tien(so_luong, don_gia)
