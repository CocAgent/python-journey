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
    # TODO: Dùng default ``tuoi`` khi caller không truyền argument thứ hai.
    raise NotImplementedError("Hoàn thành hàm gioi_thieu")


def tinh_tam_tinh(gia: float, so_luong: int) -> float:
    """Tính tạm tính; trả về 0 nếu số lượng không dương."""
    # TODO: Kiểm tra so_luong trước khi nhân.
    raise NotImplementedError("Hoàn thành hàm tinh_tam_tinh")


def ap_dung_giam_gia(tam_tinh: float, phan_tram: float = 0) -> float:
    """Trả về số tiền sau giảm giá."""
    # TODO: Tính phần trăm giảm từ ``tam_tinh``.
    raise NotImplementedError("Hoàn thành hàm ap_dung_giam_gia")


def tao_hoa_don(gia: float, so_luong: int, phan_tram: float = 0) -> str:
    """Ghép các bước nhỏ và trả về dòng tổng tiền."""
    # TODO: Gọi tinh_tam_tinh, sau đó gọi ap_dung_giam_gia.
    raise NotImplementedError("Hoàn thành hàm tao_hoa_don")


if __name__ == "__main__":
    print("Hoàn thành các TODO rồi thử tao_hoa_don(25_000, 2, 10).")
