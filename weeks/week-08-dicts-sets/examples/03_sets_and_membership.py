"""Dùng set cho uniqueness, membership và phép toán nhóm."""


def unique_in_order(items: list[str]) -> list[str]:
    """Loại trùng nhưng vẫn giữ thứ tự xuất hiện đầu tiên."""
    seen: set[str] = set()
    unique: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    return unique


def main() -> None:
    """So sánh hai nhóm kỹ năng và kiểm tra action local."""
    practiced = {"functions", "loops", "dicts"}
    target = {"dicts", "sets", "nested data"}

    print(f"Tất cả chủ đề: {sorted(practiced | target)}")
    print(f"Phần chung: {sorted(practiced & target)}")
    print(f"Cần luyện thêm: {sorted(target - practiced)}")

    local_actions = {"left", "right", "wait"}
    candidate = "right"
    print(f"Action hợp lệ: {candidate in local_actions}")

    attempts = ["wait", "right", "wait", "left", "right"]
    print(f"Action theo thứ tự đầu tiên: {unique_in_order(attempts)}")


if __name__ == "__main__":
    main()
