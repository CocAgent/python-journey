# Gợi ý — Week 06

- `range(1, 6)` tạo các số từ 1 đến 5.
- Dùng `enumerate(values, start=1)` khi số thứ tự hiển thị bắt đầu từ 1.
- Dùng `zip(left, right, strict=True)` khi hai danh sách phải dài bằng nhau.
- Cập nhật biến điều kiện của `while` trên mọi nhánh liên quan.
- Viết comprehension từ biểu thức output, sau đó tới mệnh đề `for`.

## Gợi ý cho 3 lab tự luyện

Đọc [ví dụ dự đoán kết quả](WORKED-EXAMPLES.md) và
[đề bài thực hành](practice/README.md) trước khi mở solutions.

- **Lab 01 — Báo cáo điểm:** `enumerate(zip(names, scores,
  strict=True), start=1)`. Dùng một vòng `for` khác để cộng
  tổng số điểm, không in list thô.
- **Lab 02 — Đếm ngược:** `raw = input(...).strip()`;
  kiểm `isdigit()` trước `int()`; nhận 0..5. Trong
  `while remaining > 0`, **phải có `remaining -= 1`**.
- **Lab 03 — Lọc số:** `continue` khi `number % 3 == 0`,
  `break` khi `number > 8`; comprehension bình phương
  các phần tử chẵn sau khi lọc.

Bài starter chưa hoàn thành cố ý FAIL; đừng sửa checker
để tạo PASS giả. Chỉ mở `practice/solutions/` sau khi tự thử.
