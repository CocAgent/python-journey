# Week 15 — Demo & defense 5–8 phút

Rubric duy nhất:
[FINAL_PROJECT.md](../../FINAL_PROJECT.md).

Tài liệu này là rehearsal guide, không thêm điểm hoặc tiêu chí chấm mới.

## Flow gợi ý

### 0:00–0:45 — Problem & scope

Nói:

- project giải quyết vấn đề gì;
- ai dùng;
- scope nào đã chủ động không làm.

### 0:45–3:00 — Demo một luồng chính

Chạy một flow đại diện end-to-end.

Không cần demo mọi menu/feature.

### 3:00–4:15 — Test & edge case

Cho thấy:

- test suite;
- một test có ý nghĩa;
- một edge/invalid case.

### 4:15–5:15 — Bug đã sửa

Trình bày:

```text
symptom → root cause → fix → regression test
```

### 5:15–6:15 — Design decision

Giải thích một lựa chọn:

- data structure;
- module boundary;
- class vs function;
- persistence;
- trade-off.

### 6:15–7:00 — Git / AI / limitation

Cho thấy một phần history, cách dùng AI nếu có và một known limitation.

### 7:00–8:00 — Q&A / live modification

Chuẩn bị sửa một yêu cầu nhỏ, ví dụ:

- thêm validation;
- đổi một rule;
- thêm một edge test;
- giải thích traceback.

## Câu hỏi tự luyện

- Vì sao bạn chọn cấu trúc dữ liệu này?
- Nếu file không tồn tại thì sao?
- Test nào có khả năng bắt bug thật?
- Bug khó nhất là gì?
- Phần nào AI hỗ trợ và bạn kiểm chứng thế nào?
- Nếu có thêm 2 giờ, bạn cải thiện gì trước?
- Có đoạn code nào bạn muốn refactor không?
- Nếu input thay đổi nhẹ, bạn sửa ở đâu?

## Tiêu chí tự kiểm cuối

Bạn nên trả lời “có” cho:

```text
Tôi chạy được project.
Tôi chạy được tests.
Tôi giải thích được core logic.
Tôi kể được một bug thật.
Tôi sửa được một yêu cầu nhỏ.
Tôi biết giới hạn hiện tại.
```
