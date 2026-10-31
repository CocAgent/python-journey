"""Ví dụ 06 — dict membership, .get, frequency và copy.

Từ gốc repo: python weeks/week-08-dicts-sets/examples/06_predict_dict_get_copy.py
"""


def word_frequency(sentence: str) -> dict[str, int]:
    """Đếm từ tách bằng khoảng trắng, không phân tích dấu câu."""
    counts: dict[str, int] = {}
    for word in sentence.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def main() -> None:
    student = {"name": "An", "score": 8}
    print(f"Key 'name' tồn tại: {'name' in student}")
    print(f"Value 'An' là key: {'An' in student}")
    print(f"Optional level: {student.get('level', 'beginner')}")

    # .get() KHÔNG biến một key bắt buộc bị thiếu thành dữ liệu hợp lệ.
    if "id" not in student:
        print("Thiếu key bắt buộc: id")

    snapshot = student.copy()  # Bản sao nông; đủ với dict phẳng ở đây.
    student["score"] = 9
    print(f"Original score: {student['score']}")
    print(f"Snapshot score: {snapshot['score']}")

    print(f"Frequency: {word_frequency('Python python  dict')}")
    print(f"Empty frequency: {word_frequency('   ')}")


if __name__ == "__main__":
    main()
