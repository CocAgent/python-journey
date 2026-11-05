"""Reference 01 — word-frequency và cập nhật dict bất biến với caller."""


def count_words(text: str) -> dict[str, int]:
    """Đếm từ theo whitespace (không phải tokenizer tiếng Việt hoàn chỉnh)."""
    counts: dict[str, int] = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def update_score(scores: dict[str, int], topic: str, score: int) -> dict[str, int]:
    """Tạo bản sao dict phẳng trước khi cập nhật."""
    if type(score) is not int or not 0 <= score <= 10:
        raise ValueError("Điểm không hợp lệ")
    result = scores.copy()
    result[topic] = score
    return result


if __name__ == "__main__":
    print(count_words("Python python dict"))
