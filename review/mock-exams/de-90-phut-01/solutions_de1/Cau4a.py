"""Cau4a — Reference cho bài ôn tập, chỉ mở sau khi tự giải."""

def make_book(
    book_id: str, title: str, author: str, year: int, price: int
) -> dict[str, object]:
    if any(not isinstance(value, str) or not value.strip() for value in (book_id, title, author)):
        raise ValueError("Thông tin sách không hợp lệ")
    if type(year) is not int or not 1900 <= year <= 2100:
        raise ValueError("Năm xuất bản không hợp lệ")
    if type(price) is not int or price < 0:
        raise ValueError("Giá không hợp lệ")
    return {
        "id": book_id.strip(),
        "title": title.strip(),
        "author": author.strip(),
        "year": year,
        "price": price,
    }
