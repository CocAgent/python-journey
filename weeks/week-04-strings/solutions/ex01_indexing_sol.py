"""Official solutions for indexing and slicing."""


def reverse_text(text: str) -> str:
    return text[::-1]


def is_palindrome(text: str) -> bool:
    normalized = "".join(text.lower().split())
    return normalized == normalized[::-1]


def identity_parts(identity: str) -> tuple[str, str, str]:
    return identity[:2], identity[2:3], identity[3:5]
