"""Kiểm thử ví dụ thành tiền: trường hợp thường, biên và đầu vào sai."""

import pytest

from order_total import tinh_thanh_tien


@pytest.mark.parametrize(
    ("so_luong", "don_gia", "mong_doi"),
    [
        (2, 15_000, 30_000),  # Thông thường: mua hai sản phẩm.
        (0, 15_000, 0),  # Biên: chưa mua sản phẩm nào.
        (3, 0, 0),  # Biên: sản phẩm miễn phí.
    ],
)
def test_tinh_thanh_tien_hop_le(
    so_luong: int, don_gia: int, mong_doi: int
) -> None:
    # Mỗi hàng đầu vào là một lần kiểm thử độc lập.
    assert tinh_thanh_tien(so_luong, don_gia) == mong_doi


@pytest.mark.parametrize("so_luong,don_gia", [(-1, 10_000), (2, -100)])
def test_tu_choi_du_lieu_am(so_luong: int, don_gia: int) -> None:
    # Hàm phải báo ValueError; im lặng nhận giá trị âm là sai.
    with pytest.raises(ValueError, match="không được âm"):
        tinh_thanh_tien(so_luong, don_gia)
