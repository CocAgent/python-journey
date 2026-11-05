"""Cau4b — Reference cho bài ôn tập, chỉ mở sau khi tự giải."""

def remove_book(
    books: list[dict[str, object]], book_id: str
) -> list[dict[str, object]]:
    if not isinstance(books, list) or not isinstance(book_id, str) or not book_id.strip():
        raise ValueError("Input không hợp lệ")
    seen: set[str] = set()
    for book in books:
        if not isinstance(book, dict):
            raise ValueError("Mỗi sách phải là dict")
        identifier = book.get("id")
        if not isinstance(identifier, str) or not identifier.strip() or identifier in seen:
            raise ValueError("ID không hợp lệ hoặc bị trùng")
        seen.add(identifier)
    if book_id not in seen:
        raise ValueError("Không có sách với mã này")
    return [book.copy() for book in books if book["id"] != book_id]
