"""Duyệt keys, values và items theo câu hỏi cần trả lời."""


def print_topics(scores: dict[str, int]) -> None:
    """In tên từng chủ đề trong dictionary."""
    for topic in scores.keys():
        print(f"Chủ đề: {topic}")


def average_score(scores: dict[str, int]) -> float:
    """Tính điểm trung bình từ các values."""
    return sum(scores.values()) / len(scores)


def print_report(scores: dict[str, int]) -> None:
    """In từng cặp topic-score bằng items."""
    for topic, score in scores.items():
        status = "đạt" if score >= 7 else "cần luyện thêm"
        print(f"{topic}: {score} — {status}")


def main() -> None:
    """Chạy ba kiểu iteration trên cùng data."""
    scores = {"functions": 8, "scope": 6, "dicts": 9}

    print_topics(scores)
    print_report(scores)
    print(f"Điểm trung bình: {average_score(scores):.1f}")

    if "dicts" in scores:
        print("Đã có evidence cho dicts")


if __name__ == "__main__":
    main()
