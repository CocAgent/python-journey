"""Exercise 03: uniqueness, membership và set operations."""


def phan_tich_mon_hoc(
    semester_one: set[str], semester_two: set[str]
) -> dict[str, set[str]]:
    """Trả các nhóm common, only_one, only_two và all."""
    return {
        "common": semester_one & semester_two,
        "only_one": semester_one - semester_two,
        "only_two": semester_two - semester_one,
        "all": semester_one | semester_two,
    }


def loai_trung_giu_thu_tu(words: list[str]) -> list[str]:
    """Loại từ trùng nhưng giữ thứ tự xuất hiện đầu tiên."""
    seen = set()
    result = []

    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)

    return result


def tu_chung(first: str, second: str) -> set[str]:
    """Trả các từ lowercase xuất hiện trong cả hai câu."""
    first_words = set(first.lower().split())
    second_words = set(second.lower().split())

    return first_words & second_words


def la_anagram(first: str, second: str) -> bool:
    """Kiểm tra hai chuỗi có cùng ký tự và số lần xuất hiện."""
    first = first.replace(" ", "").lower()
    second = second.replace(" ", "").lower()

    return sorted(first) == sorted(second)


if __name__ == "__main__":
    print(loai_trung_giu_thu_tu(["dict", "set", "dict"]))