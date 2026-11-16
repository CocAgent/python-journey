"""Lab 02 — Nested dict/list: dữ liệu bắt buộc và tùy chọn.

{"name":"An","scores":[8,9,7],"progress":{"week":8}}
-> "An: trung bình 8.0, tuần 8"
Thiếu progress -> "An: trung bình 8.0, tuần chưa rõ"
Thiếu name/scores, scores rỗng/sai kiểu -> "Dữ liệu không hợp lệ".
"""


def summarize_learner(learner: dict[str, object]) -> str:
    """Tạo báo cáo; không được sửa bất kỳ dữ liệu đầu vào nào."""
    # TODO 1: kiểm name là str không rỗng sau strip; scores là list không rỗng.
    # TODO 2: mọi điểm phải là int (không bool), từ 0 đến 10.
    # TODO 3: progress là optional; nếu có, yêu cầu dict và week int 1..15.
    #         progress không có week -> "tuần chưa rõ".
    # TODO 4: trung bình theo sum / len, f-string 1 chữ số thập phân.
    # TODO 5: thiếu hoặc sai field bắt buộc/field tùy chọn có mặt -> từ chối.
    raise NotImplementedError("Hoàn thành summarize_learner")


if __name__ == "__main__":
    print("Hoàn thiện TODO và thử normal/missing optional/invalid.")
