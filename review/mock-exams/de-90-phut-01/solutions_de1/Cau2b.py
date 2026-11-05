"""Cau2b — Reference cho bài ôn tập, chỉ mở sau khi tự giải."""

def is_palindrome(text: str) -> bool:
    if not isinstance(text, str):
        raise ValueError("Cần chuỗi")
    normalized = "".join(char.casefold() for char in text if char.isalnum())
    return bool(normalized) and normalized == normalized[::-1]
