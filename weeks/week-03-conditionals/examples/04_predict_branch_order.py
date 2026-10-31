"""Ví dụ 04 — Đoán nhánh nào chạy trước, sau đó mới xem kết quả.

Chạy từ gốc repo: python weeks/week-03-conditionals/examples/04_predict_branch_order.py
"""


def classify_score(score: float) -> str:
    """Dùng ngưỡng giả lập để học if/elif/else, KHÔNG phải quy chế học tập."""
    if score < 0 or score > 10:
        return "Không hợp lệ"
    elif score >= 8:
        return "Giỏi"
    elif score >= 5:
        return "Đạt"
    else:
        return "Cần luyện tập"


# Dự đoán trên giấy trước khi chạy: Python xét từ trên xuống.
for score in (-1, 0, 4.9, 5, 7.9, 8, 10, 11):
    print(f"Điểm {score:g} -> {classify_score(score)}")

score = 9
# Sai ý định: >= 5 đứng trước >= 8 nên score=9 rơi vào nhánh đầu.
if score >= 5:
    wrong_result = "Đạt"
elif score >= 8:
    wrong_result = "Giỏi"
else:
    wrong_result = "Cần luyện tập"

print(f"Sai thứ tự, điểm 9 -> {wrong_result}")
print(f"Đúng thứ tự, điểm 9 -> {classify_score(score)}")
