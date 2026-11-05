"""Exercise 01: đọc, cập nhật và duyệt dictionary."""


def cap_nhat_diem(
    scores: dict[str, float], subject: str, score: float
) -> dict[str, float]:
    """Trả một dict mới có điểm được thêm hoặc cập nhật."""
    # TODO: copy scores, cập nhật subject rồi return bản mới.
    return scores.copy()


def diem_trung_binh(scores: dict[str, float]) -> float:
    """Trả điểm trung bình, hoặc 0.0 nếu dict rỗng."""
    # TODO: dùng values() và xử lý boundary case dict rỗng.
    return 0.0


def dem_tan_suat(text: str) -> dict[str, int]:
    """Đếm tần suất ký tự, bỏ qua khoảng trắng."""
    # TODO: dùng .get(character, 0) khi cập nhật count.
    return {}


def main() -> None:
    """Chạy starter với data mẫu."""
    scores = {"Toán": 8.0, "Văn": 7.0, "Anh": 9.0}
    print(cap_nhat_diem(scores, "Văn", 8.0))
    print(diem_trung_binh(scores))
    print(dem_tan_suat("hello"))


if __name__ == "__main__":
    main()
