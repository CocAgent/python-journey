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
    raise NotImplementedError("Hoàn thành hàm them_ghi_chu")


def tim_ghi_chu(danh_sach: list[str], tu_khoa: str) -> list[str]:
    """Trả về các ghi chú chứa từ khóa, không phân biệt hoa thường."""
    # TODO: Tạo một result local rồi return result.
    raise NotImplementedError("Hoàn thành hàm tim_ghi_chu")


def dem_ghi_chu(danh_sach: list[str]) -> int:
    """Trả về số ghi chú trong list được truyền vào."""
    # TODO: Không đọc một biến global.
    raise NotImplementedError("Hoàn thành hàm dem_ghi_chu")


if __name__ == "__main__":
    print("Hoàn thành TODO và thử các hàm với một list local trong main.")
