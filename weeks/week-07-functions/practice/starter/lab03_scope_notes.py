"""Lab 03 — Scope: caller sở hữu list ghi chú, hàm nhận qua parameter.

Một hàm cố ý cập nhật list caller là add_note; hai hàm còn lại chỉ đọc.
Không dùng biến global để giữ danh sách.
"""


def add_note(notes: list[str], text: str) -> bool:
    """Strip và thêm nếu nội dung không rỗng; trả True nếu đã thêm."""
    # TODO: stripped = text.strip(), nếu rỗng trả False;
    #       notes.append(stripped), return True.
    raise NotImplementedError("Hoàn thành add_note")


def count_notes(notes: list[str]) -> int:
    """Đếm số ghi chú được caller truyền vào."""
    # TODO: return len(notes), không đọc global state.
    raise NotImplementedError("Hoàn thành count_notes")


def search_notes(notes: list[str], keyword: str) -> list[str]:
    """Tìm ghi chú chứa keyword (không phân biệt hoa/thường).

    Nếu keyword chỉ có khoảng trắng, trả [] và không sửa notes.
    """
    # TODO: dùng keyword.strip().lower() và loop for đơn giản;
    #       tạo result local rồi return result.
    raise NotImplementedError("Hoàn thành search_notes")


if __name__ == "__main__":
    print("Thử tạo list local rồi gọi lần lượt ba hàm.")
