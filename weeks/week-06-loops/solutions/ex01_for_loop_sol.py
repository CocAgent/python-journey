"""Official solution for for, range, enumerate and zip."""


def numbered_pairs(topics: list[str], scores: list[int]) -> list[str]:
    lines = []
    pairs = zip(topics, scores, strict=True)
    for position, (topic, score) in enumerate(pairs, start=1):
        lines.append(f"{position}. {topic}: {score}")
    return lines


def multiplication_table(number: int) -> list[str]:
    return [f"{number} x {factor} = {number * factor}" for factor in range(1, 11)]
