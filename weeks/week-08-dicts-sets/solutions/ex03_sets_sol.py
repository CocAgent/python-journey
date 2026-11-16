"""Official solution 03: sets and membership."""


def phan_tich_mon_hoc(
    semester_one: set[str], semester_two: set[str]
) -> dict[str, set[str]]:
    """Return four useful comparisons between two subject sets."""
    return {
        "common": semester_one & semester_two,
        "only_one": semester_one - semester_two,
        "only_two": semester_two - semester_one,
        "all": semester_one | semester_two,
    }


def loai_trung_giu_thu_tu(words: list[str]) -> list[str]:
    """Remove duplicates while preserving first-seen order."""
    seen: set[str] = set()
    unique: list[str] = []
    for word in words:
        if word not in seen:
            seen.add(word)
            unique.append(word)
    return unique


def tu_chung(first: str, second: str) -> set[str]:
    """Return lowercase words shared by both strings."""
    first_words = set(first.lower().split())
    second_words = set(second.lower().split())
    return first_words & second_words


def la_anagram(first: str, second: str) -> bool:
    """Compare normalized character sequences including duplicate counts."""
    normalized_first = first.lower().replace(" ", "")
    normalized_second = second.lower().replace(" ", "")
    return sorted(normalized_first) == sorted(normalized_second)


if __name__ == "__main__":
    print(loai_trung_giu_thu_tu(["dict", "set", "dict"]))
