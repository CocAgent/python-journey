"""Exercise 03: uniqueness, membership và set operations."""


def phan_tich_mon_hoc(
    semester_one: set[str], semester_two: set[str]
) -> dict[str, set[str]]:
    """Trả các nhóm common, only_one, only_two và all."""
    # TODO: dùng intersection, difference và union.
    return {}


def loai_trung_giu_thu_tu(words: list[str]) -> list[str]:
    """Loại từ trùng nhưng giữ thứ tự xuất hiện đầu tiên."""
    # TODO: dùng một set seen và một list result.
    return []


def tu_chung(first: str, second: str) -> set[str]:
    """Trả các từ lowercase xuất hiện trong cả hai câu."""
    # TODO: biến mỗi câu thành set rồi lấy phần giao.
    return set()


def la_anagram(first: str, second: str) -> bool:
    """Kiểm tra hai chuỗi có cùng ký tự và số lần xuất hiện."""
    # TODO: normalize khoảng trắng và chữ hoa trước khi so sánh.
    return False


if __name__ == "__main__":
    print(loai_trung_giu_thu_tu(["dict", "set", "dict"]))
