"""Lời giải 01 — kiểm input trước, xét ngưỡng từ cao xuống."""

score_text = input("Điểm: ").strip()
if not score_text.isdigit():
    print("Điểm không hợp lệ")
else:
    score = int(score_text)
    if score > 10:
        print("Điểm không hợp lệ")
    elif score >= 8:
        print("Giỏi")
    elif score >= 5:
        print("Đạt")
    else:
        print("Cần luyện tập")
