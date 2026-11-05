"""Ôn tập 01 — Kết hợp list, dict, set, điều kiện, vòng lặp và hàm.

Ví dụ: [{"name": " An ", "score": 8}, {"name": "Bình", "score": 4}]
-> {"count": 2, "average": 6.0, "passed": ["An"]}

Đọc review/practice/README.md trước khi sửa TODO.
"""


def summarize_students(records: list[dict[str, object]]) -> dict[str, object]:
    """Tóm tắt điểm, không thay đổi list/dict do caller truyền vào.

    - name: str không rỗng sau strip()
    - score: int thực (không bool), trong [0, 10]
    - tên trùng sau strip().casefold() -> ValueError
    - pass khi score >= 5, giữ thứ tự nguồn
    - list rỗng -> {"count": 0, "average": None, "passed": []}
    """
    # TODO: kiểm records là list; mỗi record là dict có name và score.
    # TODO: dùng seen=set() phát hiện trùng tên; raise ValueError khi sai.
    # TODO: vòng for tính tổng và xây passed; dùng return thay print.
    # TODO: chống chia cho 0 khi danh sách rỗng.
    raise NotImplementedError("Hãy hoàn thành Lab 01")


if __name__ == "__main__":
    print("Hãy hoàn thiện TODO rồi chạy review/practice/checks/check_review.py --starter")
