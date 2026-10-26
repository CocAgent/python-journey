"""Exercise 02 — Parameters, defaults and decomposition.

Goal:
    Dùng default parameter và ghép nhiều hàm nhỏ thành một luồng tính hóa đơn.

TODO:
    Hoàn thành bốn hàm bên dưới theo thứ tự.

Examples:
    gioi_thieu("An") == "Tôi là An, 18 tuổi."
    tinh_tam_tinh(25_000, 2) == 50_000
    ap_dung_giam_gia(100_000, 10) == 90_000

Expected behavior:
    ``tao_hoa_don`` dùng kết quả từ các hàm tính toán và định dạng.

Basic invalid case:
    Số lượng không dương tạo tạm tính bằng 0.

Self-check command:
    python weeks/week-07-functions/exercises/ex02_params.py
"""


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
    giam_gia = tam_tinh * (phan_tram / 100)
    return tam_tinh - giam_gia


def tao_hoa_don(gia: float, so_luong: int, phan_tram: float = 0) -> str:
    """Ghép các bước nhỏ và trả về dòng tổng tiền."""
    tam_tinh = tinh_tam_tinh(gia, so_luong)
    tong_tien = ap_dung_giam_gia(tam_tinh, phan_tram)
    return f"Tổng tiền: {tong_tien:,.0f} VNĐ"


if __name__ == "__main__":
    # Test thử các hàm
    print(gioi_thieu("An"))                     # Tôi là An, 18 tuổi.
    print(gioi_thieu("Bình", 20))               # Tôi là Bình, 20 tuổi.
    
    print(tinh_tam_tinh(25_000, 2))             # 50000.0
    print(tinh_tam_tinh(25_000, 0))             # 0.0 (Xử lý số lượng không dương)
    
    print(ap_dung_giam_gia(100_000, 10))        # 90000.0
    
    print(tao_hoa_don(25_000, 2, 10))           # Tổng tiền: 45,000 VNĐ