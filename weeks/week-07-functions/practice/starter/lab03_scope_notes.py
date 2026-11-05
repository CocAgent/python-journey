"""Lời giải 03 — Truyền list qua parameter, không tạo global notebook."""


def add_note(notes: list[str], text: str) -> bool:
    """Mutate list mà caller cung cấp, không giữ một list ẩn."""
    clean = text.strip()
    if not clean:
        return False
    notes.append(clean)
    return True


def count_notes(notes: list[str]) -> int:
    """Chỉ đọc list từ parameter."""
    return len(notes)


def search_notes(notes: list[str], keyword: str) -> list[str]:
    """Tạo list kết quả mới, không sửa list nguồn."""
    search_text = keyword.strip().lower()
    if not search_text:
        return []
    found: list[str] = []
    for note in notes:
        if search_text in note.lower():
            found.append(note)
    return found


if __name__ == "__main__":
    notebook: list[str] = []
    add_note(notebook, "  Học return  ")
    print(f"Đang có {count_notes(notebook)} ghi chú")
