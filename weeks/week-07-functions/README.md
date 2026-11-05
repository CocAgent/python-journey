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

Story mở đầu tùy chọn: [Cóc, bác Rùa và những chiếc Hàm](../../assets/Story-07-%20Hàm.md).

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

## Xem ví dụ → dự đoán return → tự viết function

Đọc [**WORKED-EXAMPLES.md**](WORKED-EXAMPLES.md) để luyện
**Dự đoán → Chạy → Giải thích → Thử lỗi → Chuyển bài toán → Kiểm chứng**:

| Ví dụ mới | Kỹ năng | Sai lầm cần phát hiện |
|---|---|---|
| `06_predict_return_and_default.py` | `return` vs `print`, default, early return | Caller nhận `None` dù terminal đã in đúng |
| `07_scope_and_decomposition_trace.py` | validate → calculate → format, local scope | Copy logic và phụ thuộc global state |
| `08_type_hints_and_decision.py` | type hints vs runtime guard, decision function | Nhầm `int` annotation với xác thực input |

Chạy từ thư mục gốc repository:

```bash
python weeks/week-07-functions/examples/06_predict_return_and_default.py
python weeks/week-07-functions/examples/07_scope_and_decomposition_trace.py
python weeks/week-07-functions/examples/08_type_hints_and_decision.py
```

Tiếp đó tự làm [**4 bài tương tự**](practice/README.md):
tính tiền bằng `return`, phân rã hóa đơn, quản lý ghi chú qua
parameter và decision function được kiểm dữ liệu trước.
`practice/starter/` chứa TODO; `practice/solutions/`
chỉ mở để đối chiếu sau khi đã tự làm.

```bash
# Kiểm TRỰC TIẾP giá trị hàm trong code người học
python weeks/week-07-functions/practice/checks/check_practice.py --starter

# Chỉ kiểm lời giải mẫu, không thay kết quả code của sinh viên
python weeks/week-07-functions/practice/checks/check_practice.py --solutions
```

**Starter chưa hoàn thiện phải FAIL (0/4)**. Checker mới kiểm
giá trị `return`, input hợp lệ/không hợp lệ, local state và
việc hàm lớn **gọi lại hàm nhỏ**; chỉ in sẵn một dòng kết quả
không đủ để PASS. Bộ này tự chọn và không thay 4 bài
trong `exercises/`, Utility Toolkit hay rubric gốc.

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
