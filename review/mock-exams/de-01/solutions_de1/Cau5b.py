"""Cau5b — LỜI GIẢI THAM KHẢO, chỉ mở sau khi tự làm.

Trả list tên có điểm >= minimum, giữ thứ tự trong dict. Tên không rỗng; điểm/threshold là int thật 0..10; dữ liệu sai => ValueError. Không sửa dict nguồn.
"""


def high_scores(scores: dict[str, int], minimum: int) -> list[str]:
    if not isinstance(scores, dict) or type(minimum) is not int or not 0 <= minimum <= 10:
        raise ValueError("Bảng điểm hoặc ngưỡng không hợp lệ")
    for name, score in scores.items():
        if not isinstance(name, str) or not name.strip() or type(score) is not int or not 0 <= score <= 10:
            raise ValueError("Một bản ghi điểm không hợp lệ")
    return [name for name, score in scores.items() if score >= minimum]


if __name__ == "__main__":
    print("Chạy autograde_de1.py --reference để kiểm lời giải mẫu")
