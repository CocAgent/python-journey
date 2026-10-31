# Tuần 06 — Loops · enumerate · zip · comprehensions

Tuần này bạn lặp qua dữ liệu rõ ràng, ghép các collection liên quan và dùng
comprehension khi biểu thức vẫn dễ đọc.

## Outcomes

- dùng `for`, `while` và `range` đúng tình huống;
- dùng `break` và `continue` có chủ đích;
- dùng `enumerate` thay cho index thủ công;
- dùng `zip` để ghép các collection song song;
- viết list comprehension đơn giản và chọn loop thường khi logic dài.

## Learning path

```text
README → notes → examples → exercises → hints
       → machine check → iteration report → evidence
```

Đi theo [`notes.md`](notes.md), [`examples/`](examples/),
[`exercises/`](exercises/), [`hints.md`](hints.md),
[machine check](checks/README.md) và [mini-project](mini-project/README.md).

## Ví dụ dự đoán kết quả và bài tương tự

Đọc [**WORKED-EXAMPLES.md**](WORKED-EXAMPLES.md) và thực hiện theo vòng:
**Dự đoán → Chạy → Giải thích → Thử lỗi → Tự làm → Kiểm chứng**.

| Ví dụ mới | Kiến thức | Lỗi cần nhận diện |
|---|---|---|
| `04_predict_range_break_continue.py` | `for/while/range/break/continue` | vòng while không dừng; break khác continue |
| `05_enumerate_zip_strict.py` | `enumerate`, `zip(strict=True)` | hai danh sách lệch độ dài làm mất dữ liệu |
| `06_comprehension_nested_loop.py` | comprehension vs for; nested loops | nhồi quá nhiều logic vào comprehension |

Chạy từ **gốc `python-journey/`**:

```bash
python weeks/week-06-loops/examples/04_predict_range_break_continue.py
python weeks/week-06-loops/examples/05_enumerate_zip_strict.py
python weeks/week-06-loops/examples/06_comprehension_nested_loop.py
```

Tiếp đó tự hoàn thiện [**3 bài tập tương tự**](practice/README.md):
báo cáo điểm, đếm ngược an toàn và lọc số/bình phương.
Có starter TODO, đáp án tách riêng và bộ kiểm trực tiếp bài sinh viên:

```bash
python weeks/week-06-loops/practice/checks/check_practice.py --starter
```

**Starter chưa làm xong → FAIL (0/3) là đúng thiết kế**.
`--solutions` chỉ kiểm đáp án tham khảo, không chấm bài sinh viên.
Giữ nguyên bộ exercises gốc và mini-project `Iteration Report`.

## Evidence

- output `Week 06 solution checks: PASS`;
- một loop có điều kiện dừng rõ ràng;
- output từ `enumerate`, `zip` và comprehension;
- báo cáo iteration đã chạy.
