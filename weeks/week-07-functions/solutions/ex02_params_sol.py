"""Official solution for Exercise 02 — parameters and decomposition."""


def gioi_thieu(ten: str, tuoi: int = 18) -> str:
    """Trả về một câu giới thiệu ngắn."""
    return f"Tôi là {ten}, {tuoi} tuổi."


def tinh_tam_tinh(gia: float, so_luong: int) -> float:
    """Tính tạm tính; trả về 0 nếu số lượng không dương."""
    if so_luong <= 0:
        return 0.0
    return gia * so_luong


def ap_dung_giam_gia(tam_tinh: float, phan_tram: float = 0) -> float:
    """Trả về số tiền sau giảm giá."""
    tien_giam = tam_tinh * phan_tram / 100
    return tam_tinh - tien_giam


def tao_hoa_don(gia: float, so_luong: int, phan_tram: float = 0) -> str:
    """Ghép các bước tính và trả về dòng tổng tiền."""
    tam_tinh = tinh_tam_tinh(gia, so_luong)
    tong = ap_dung_giam_gia(tam_tinh, phan_tram)
    return f"Tổng: {tong:,.0f} đ"


def main() -> None:
    """Chạy ví dụ hóa đơn."""
    print(gioi_thieu("An"))
    print(tao_hoa_don(25_000, 2, 10))


if __name__ == "__main__":
    main()
