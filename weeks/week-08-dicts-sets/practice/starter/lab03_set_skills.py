"""Lab 03 — Set operations và unique-in-order.

compare_skills({"dict","set"}, {"set","loop"}) trả 4 nhóm dạng set.
unique_in_order(["a","b","a"]) -> ["a","b"].
Không sửa list/set nguồn; empty input cũng phải chạy.
"""


def compare_skills(first: set[str], second: set[str]) -> dict[str, set[str]]:
    """Trả common, only_first, only_second, all dưới dạng set."""
    # TODO: dùng &, -, | rồi return dict đủ bốn key.
    raise NotImplementedError("Hoàn thành compare_skills")


def unique_in_order(items: list[str]) -> list[str]:
    """Loại trùng nhưng giữ thứ tự xuất hiện đầu tiên."""
    # TODO: một set seen và một list result; duyệt từng item.
    # Không dùng list(set(items)): thứ tự không được bảo đảm.
    raise NotImplementedError("Hoàn thành unique_in_order")


if __name__ == "__main__":
    print("Hoàn thành hai TODO, chạy thử trường hợp list rỗng.")
