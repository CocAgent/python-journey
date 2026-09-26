"""Exercise 02: đọc và biến đổi nested data."""


def diem_trung_binh(student: dict[str, object]) -> float:
    """Tính trung bình list scores trong một student model."""
    # TODO: lấy scores, tính average và xử lý list rỗng.
    return 0.0


def hoc_sinh_tot_nhat(classroom: dict[str, dict[str, object]]) -> str:
    """Trả tên learner có điểm trung bình cao nhất."""
    # TODO: duyệt items() và tái sử dụng diem_trung_binh().
    return ""


def tong_gia_tri_kho(products: dict[str, dict[str, object]]) -> float:
    """Tính tổng price nhân quantity của mọi product."""
    # TODO: đọc từng product từ values().
    return 0.0


def main() -> None:
    """Chạy starter với một classroom nhỏ."""
    classroom = {
        "An": {"age": 20, "scores": [8, 9, 7]},
        "Bình": {"age": 21, "scores": [7, 6, 8]},
    }
    print(hoc_sinh_tot_nhat(classroom))


if __name__ == "__main__":
    main()
