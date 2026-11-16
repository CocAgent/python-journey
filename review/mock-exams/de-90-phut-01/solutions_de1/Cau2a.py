"""Cau2a — Reference cho bài ôn tập, chỉ mở sau khi tự giải."""

def count_uppercase(text: str) -> int:
    if not isinstance(text, str):
        raise ValueError("Cần chuỗi")
    return sum(1 for char in text if char.isupper())
