"""Exercise 01: đọc, cập nhật và duyệt dictionary."""


def cap_nhat_diem(
    scores: dict[str, float], subject: str, score: float
) -> dict[str, float]:
    """Trả một dict mới có điểm được thêm hoặc cập nhật."""
    new_scores = scores.copy()
    new_scores[subject] = score
    return new_scores


def diem_trung_binh(scores: dict[str, float]) -> float:
    """Trả điểm trung bình, hoặc 0.0 nếu dict rỗng."""
    if not scores:
        return 0.0

    return sum(scores.values()) / len(scores)


def dem_tan_suat(text: str) -> dict[str, int]:
    """Đếm tần suất ký tự, bỏ qua khoảng trắng."""
    counts = {}

    for character in text:
        if character != " ":
            counts[character] = counts.get(character, 0) + 1

    return counts


def main() -> None:
    """Chạy starter với data mẫu."""
    scores = {"Toán": 8.0, "Văn": 7.0, "Anh": 9.0}

    print(cap_nhat_diem(scores, "Văn", 8.0))
    print(diem_trung_binh(scores))
    print(dem_tan_suat("hello"))


if __name__ == "__main__":
    main()