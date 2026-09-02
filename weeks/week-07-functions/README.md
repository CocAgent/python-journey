# Tuần 07 — Functions · Decomposition · Scope · Type hints

Tuần này dùng hàm để chia một vấn đề thành những phần nhỏ, nhận input và trả
output rõ ràng. Đây là tuần thí điểm cho learning loop:

```text
Learn → Build → Test → Debug → Improve → Commit → Prove
```

## Mục tiêu

Sau Week 07, bạn có thể:

- viết và gọi hàm với `def`;
- phân biệt parameter và argument;
- dùng `return` để đưa dữ liệu về nơi gọi hàm;
- dùng default parameter ở mức cơ bản;
- giải thích local scope và tránh lạm dụng global state;
- phân rã một bài toán thành các hàm nhỏ;
- viết docstring ngắn và type hints cơ bản;
- giải thích vì sao type hints không tự kiểm tra kiểu khi chương trình chạy;
- viết một decision function đơn giản, xác định được từ input đến output.

## Prerequisites

Bạn nên hoàn thành Week 01–06 và đã quen với biến, kiểu dữ liệu, điều kiện,
chuỗi, list và loop.

## Thứ tự học

1. Đọc [`notes.md`](notes.md).
2. Chạy lần lượt các file trong [`examples/`](examples/).
3. Làm bốn bài trong [`exercises/`](exercises/).
4. Mở [`hints.md`](hints.md) theo từng tầng nếu bị kẹt.
5. Chạy [machine check](checks/README.md) cho official solutions.
6. Hoàn thành [Personal Utility Toolkit](mini-project/README.md).
7. Commit kết quả và lưu bằng chứng.

## Learning path

```text
README → notes → examples → exercises → hints
       → machine checks → mini-project → evidence
```

## Checklist

- [ ] Tôi dùng `return` đúng.
- [ ] Tôi chia được bài toán thành nhiều hàm.
- [ ] Tôi giải thích được local scope.
- [ ] Tôi viết được type hints cơ bản.
- [ ] Tôi biết type hints không validate runtime.
- [ ] Tôi hoàn thành decision function.
- [ ] Tôi chạy machine check.
- [ ] Tôi hoàn thành mini-project.
- [ ] Tôi commit kết quả.

## Evidence

Lưu lại:

- output `Week 07 solution checks: PASS`;
- output khi chạy mini-project;
- commit chứa bài làm với message có ý nghĩa;
- một ghi chú ngắn về lỗi bạn đã gặp và cách bạn sửa lỗi.

## VuaCóc Bot Journey

Week 07 milestone: [Function Bot](../../projects/vuacoc-bot-journey/milestones/w07-function-bot.md).
