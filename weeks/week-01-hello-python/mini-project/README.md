# Mini-project Tuần 01 — Khung ASCII

## Mức A: Tuần 01 bắt buộc

Dùng các lệnh `print()` tạo một khung và lời chào **tĩnh**, không cần
`input()`, `if`, vòng lặp hoặc hàm. Ví dụ:

```text
+--------------+
| Xin chào An! |
+--------------+
```

Độ dài viền trên/dưới bằng nhau, `|` của dòng giữa thẳng hàng.
Bắt đầu với [`starter_basic.py`](starter_basic.py), tự viết TODO.

## Mức B: chuẩn bị Tuần 02 (tự chọn)

Hỏi tên bằng `input()` rồi căn khung theo tên:

```text
Tên của bạn: An
+--------------+
| Xin chào An! |
+--------------+
```

Bắt đầu từ [`starter.py`](starter.py); chỉ sau khi tự làm hãy xem
[`reference.py`](reference.py). Mức này sử dụng biến, `len()` và
`input()`, vì thế không phải yêu cầu Tuần 01. Với emoji và dấu kết hợp,
độ rộng hiển thị trong terminal có thể khác `len()`; không cần giải quyết
vấn đề Unicode nâng cao.

## Tự chấm mini-project cùng hai bài cốt lõi

AutoGrade kiểm `starter_basic.py` ở **mức A** (1 điểm) khi em chạy máy chấm Week 01. Xem [hướng dẫn tự đánh giá](../assessment/STUDENT-GUIDE.md); `starter.py` mức B không được tính trong điểm Week 01.

## Minh chứng

Ghi lệnh chạy, output, một lỗi/sửa lỗi, branch và commit SHA vào
[phiếu minh chứng](../evidence-template.md). Bộ test tham chiếu không
chấm code student starter.
