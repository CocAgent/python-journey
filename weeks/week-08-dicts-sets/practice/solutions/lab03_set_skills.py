"""Reference 03 — tập hợp dùng để so sánh; list giữ thứ tự."""


def compare_skills(first: set[str], second: set[str]) -> dict[str, set[str]]:
    """Trả bốn nhóm mà không chỉnh sửa input sets."""
    return {
        "common": first & second,
        "only_first": first - second,
        "only_second": second - first,
        "all": first | second,
    }


def unique_in_order(items: list[str]) -> list[str]:
    """Dùng seen set để kiểm nhanh nhưng kết quả giữ thứ tự list."""
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


if __name__ == "__main__":
    print(unique_in_order(["dict", "set", "dict"]))
