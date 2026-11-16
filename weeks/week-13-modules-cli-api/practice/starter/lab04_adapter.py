"""Lab 4 — adapter chuyển form dict thành báo cáo.

Nhớ kiểm dict, student là chuỗi không rỗng và score thuộc 0..10.
"""


def make_student_report(payload: dict[str, object]) -> dict[str, object]:
    """TODO: validate và dùng hàm core; không copy quy tắc phân loại."""
    return {"todo": "Lab 4 chưa xử lý form"}


def main() -> None:
    print(make_student_report({"student": "  An  ", "score": 7.5}))


if __name__ == "__main__":
    main()
