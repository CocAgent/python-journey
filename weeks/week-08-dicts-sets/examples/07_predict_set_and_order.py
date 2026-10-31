"""Ví dụ 07 — set uniqueness và phép tập hợp; thứ tự là thuộc tính list."""


def unique_in_order(items: list[str]) -> list[str]:
    """Giữ thứ tự xuất hiện đầu tiên, set chỉ dùng cho membership."""
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def main() -> None:
    first = {"loop", "dict", "set"}
    second = {"dict", "function"}
    print(f"Union sorted: {sorted(first | second)}")
    print(f"Intersection sorted: {sorted(first & second)}")
    print(f"Only first sorted: {sorted(first - second)}")
    print(f"Empty set type: {type(set()).__name__}")
    print(f"Empty braces type: {type({}).__name__}")

    tags = ["python", "git", "python", "dict", "git"]
    print(f"Unique with order: {unique_in_order(tags)}")
    print(f"Raw list unchanged: {tags}")
    print(f"Length of set: {len(set(tags))}")
    print(f"Set cannot count repeats: {len(set('aab'))}")
    print("Một set KHÔNG cho biết số lần ký tự xuất hiện.")


if __name__ == "__main__":
    main()
