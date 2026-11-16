"""Reference 01 — Kết hợp Week 02–08, không làm thay bài người học."""


def summarize_students(records: list[dict[str, object]]) -> dict[str, object]:
    """Tóm tắt điểm, bảo toàn nguồn và thứ tự học viên đạt."""
    if not isinstance(records, list):
        raise ValueError("Cần list bản ghi")
    seen: set[str] = set()
    passed: list[str] = []
    total = 0
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Mỗi bản ghi phải là dict")
        name = record.get("name")
        score = record.get("score")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Tên học viên không hợp lệ")
        if type(score) is not int or not 0 <= score <= 10:
            raise ValueError("Điểm học viên không hợp lệ")
        clean_name = name.strip()
        key = clean_name.casefold()
        if key in seen:
            raise ValueError("Tên học viên bị trùng")
        seen.add(key)
        total += score
        if score >= 5:
            passed.append(clean_name)
    count = len(records)
    average = total / count if count else None
    return {"count": count, "average": average, "passed": passed}


if __name__ == "__main__":
    print(summarize_students([{"name": "An", "score": 8}]))
