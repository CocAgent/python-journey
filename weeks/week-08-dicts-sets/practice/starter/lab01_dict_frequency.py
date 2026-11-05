"""Lab 01 — Dict word-frequency và copy-then-update.

count_words("Python python dict") -> {"python": 2, "dict": 1}
update_score({"dict": 7}, "dict", 9) -> {"dict": 9}
Điểm ngoài 0..10 hoặc kiểu bool -> ValueError. Không sửa dict đầu vào.
"""


def count_words(text: str) -> dict[str, int]:
    """Đếm các từ lowercase, tách bằng whitespace; text rỗng trả {}."""
    # TODO: loop text.lower().split(); dùng counts.get(word, 0) + 1.
    raise NotImplementedError("Hoàn thành count_words")


def update_score(scores: dict[str, int], topic: str, score: int) -> dict[str, int]:
    """Trả dict MỚI với điểm đã thay, không sửa scores của caller."""
    # TODO: kiểm type(score) is int và 0 <= score <= 10.
    # TODO: sai -> raise ValueError; đúng -> scores.copy(), cập nhật, return.
    raise NotImplementedError("Hoàn thành update_score")


if __name__ == "__main__":
    print("Tự làm hai TODO trước khi chạy các ví dụ.")
