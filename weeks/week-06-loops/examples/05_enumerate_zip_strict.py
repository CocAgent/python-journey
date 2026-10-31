"""Ví dụ 05 — enumerate + zip, ghép dữ liệu và phát hiện lệch cặp.

Chạy offline. ValueError do strict=True được bắt để sinh viên quan sát.
"""

names = ["An", "Bình", "Chi"]
scores = [8, 9, 7]

for position, (name, score) in enumerate(
    zip(names, scores, strict=True), start=1
):
    print(f"{position}. {name}: {score}")

print(f"Số bạn: {len(names)}")

# Không có strict=True: zip dừng ở list NGẮN HƠN, có thể làm mất điểm.
short_scores = [8, 9]
paired_default = list(zip(names, short_scores))
print(f"zip mặc định (mất Chi): {paired_default}")

# Lỗi chỉ xuất hiện khi zip được DUYỆT HẾT.
try:
    list(zip(names, short_scores, strict=True))
except ValueError:
    print("zip(strict=True): từ chối danh sách lệch độ dài")
