"""Exercise 03 — Local scope and avoiding unnecessary global state.

Goal:
    Truyền dữ liệu qua parameter thay vì để hàm phụ thuộc vào biến global.

TODO:
    1. Hoàn thành ``them_ghi_chu``.
    2. Hoàn thành ``tim_ghi_chu``.
    3. Hoàn thành ``dem_ghi_chu``.

Examples:
    notes = []
    them_ghi_chu(notes, "Học return")
    dem_ghi_chu(notes) == 1

Expected behavior:
    Các hàm chỉ dùng list được caller truyền vào; không tạo global notebook.

Basic invalid case:
    Ghi chú chỉ chứa khoảng trắng không được thêm vào list.

Self-check command:
    python weeks/week-07-functions/exercises/ex03_scope.py
"""


def them_ghi_chu(danh_sach: list[str], noi_dung: str) -> bool:
    """Thêm ghi chú hợp lệ và báo thao tác có thành công hay không."""
    # TODO: Bỏ khoảng trắng hai đầu, từ chối nội dung rỗng, rồi append.
    noi_dung = noi_dung.strip()
    if not noi_dung:
        return False
    danh_sach.append(noi_dung)
    return True


def tim_ghi_chu(danh_sach: list[str], tu_khoa: str) -> list[str]:
    """Trả về các ghi chú chứa từ khóa, không phân biệt hoa thường."""
    # TODO: Tạo một result local rồi return result.
    tu_khoa = tu_khoa.strip().lower()
    result = []
    for ghi_chu in danh_sach:
        if tu_khoa in ghi_chu.lower():
            result.append(ghi_chu)
    return result


def dem_ghi_chu(danh_sach: list[str]) -> int:
    """Trả về số ghi chú trong list được truyền vào."""
    # TODO: Không đọc một biến global.
    return len(danh_sach)


if __name__ == "__main__":
    notes = []
    them_ghi_chu(notes, "Hoc return")
    them_ghi_chu(notes, "   Hoc parameter   ")
    them_ghi_chu(notes, "   ")
    print(notes)
    print(dem_ghi_chu(notes))
    print(tim_ghi_chu(notes, "RETURN"))