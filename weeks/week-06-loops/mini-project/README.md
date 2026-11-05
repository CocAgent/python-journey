# Mini-project — Iteration Report

Tạo báo cáo đánh số cho các chủ đề và điểm tự đánh giá.

## Yêu cầu

- dùng `zip(..., strict=True)` để ghép hai list;
- dùng `enumerate(..., start=1)` để đánh số;
- dùng comprehension đơn giản để lấy các điểm đạt từ 8 trở lên;
- in output có thể dùng làm evidence.

```bash
python weeks/week-06-loops/mini-project/starter.py
```

## Bài đệm trước Iteration Report

Nếu khó kết hợp `enumerate(zip(...))`, thử
[Ví dụ 05 có bảng dự đoán](../WORKED-EXAMPLES.md)
và tự làm [Lab 01 — Báo cáo điểm](../practice/README.md)
trước khi quay lại mini-project.

Khi báo cáo đủ cặp dữ liệu, ưu tiên `strict=True`
để không âm thầm mất phần tử. Comprehension chỉ lọc
điểm `>=8` ở bước ngắn; nếu cần nhiều nhánh,
hãy dùng `for` rõ ràng.
