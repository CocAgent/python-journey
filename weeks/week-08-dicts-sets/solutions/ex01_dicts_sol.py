"""Official solution 01: dictionary basics."""


def cap_nhat_diem(
    scores: dict[str, float], subject: str, score: float
) -> dict[str, float]:
    """Return a copied dictionary with one updated score."""
    updated = scores.copy()
    updated[subject] = score
    return updated


def diem_trung_binh(scores: dict[str, float]) -> float:
    """Return the average score, or zero for an empty dictionary."""
    if not scores:
        return 0.0
    return sum(scores.values()) / len(scores)


def dem_tan_suat(text: str) -> dict[str, int]:
    """Count non-space characters without changing their case."""
    frequency: dict[str, int] = {}
    for character in text:
        if not character.isspace():
            frequency[character] = frequency.get(character, 0) + 1
    return frequency


if __name__ == "__main__":
    sample = {"Toán": 8.0, "Văn": 7.0}
    print(cap_nhat_diem(sample, "Văn", 8.0))
    print(diem_trung_binh(sample))
    print(dem_tan_suat("hello"))
