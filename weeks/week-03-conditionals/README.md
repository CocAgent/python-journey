# Tuần 03 — Conditionals · Boolean · Input Validation

Tuần này bạn biến điều kiện thành decision rõ ràng và từ chối input không hợp
lệ trước khi xử lý.

## Outcomes

- dùng `if`, `elif`, `else` theo đúng thứ tự ưu tiên;
- kết hợp comparison với `and`, `or`, `not`;
- hiểu truthy/falsy ở mức nhập môn;
- dùng guard-style validation;
- tránh nested condition khi một nhánh return sớm rõ hơn.

## Learning path

```text
README → notes → examples → exercises → hints
       → machine check → mini-project → evidence
```

Đọc [`notes.md`](notes.md), chạy [`examples/`](examples/), làm
[`exercises/`](exercises/), dùng [`hints.md`](hints.md), chạy
[machine check](checks/README.md), rồi hoàn thành
[Decision Ticket](mini-project/README.md).

## Thực hành theo phương pháp dự đoán → chạy → giải thích

Hãy bắt đầu từ [**WORKED-EXAMPLES.md**](WORKED-EXAMPLES.md), gồm ba
ví dụ mới với bảng dự đoán kết quả, giải thích các nhánh và lỗi logic:

| File ví dụ | Nội dung | Tình huống tự thử |
|---|---|---|
| `04_predict_branch_order.py` | Thứ tự `if/elif/else` | điểm 4.9, 5, 8, 10, 11 |
| `05_boolean_reasoning.py` | `and/or/not`, truthy/falsy | vé `True/False`, cửa mở/đóng |
| `06_guard_before_decision.py` | Validate text → int → quyết định | tuổi 12, 65, 121, `abc` |

Từ gốc repository:

```bash
python weeks/week-03-conditionals/examples/04_predict_branch_order.py
python weeks/week-03-conditionals/examples/05_boolean_reasoning.py
python weeks/week-03-conditionals/examples/06_guard_before_decision.py
```

Sau đó làm [**3 bài tương tự có TODO**](practice/README.md):
xếp loại điểm, kiểm điều kiện vào cửa, tính phí giao hàng có ưu tiên.
Máy tự kiểm **thật sự chạy code trong `practice/starter/`**:

```bash
python weeks/week-03-conditionals/practice/checks/check_practice.py --starter
```

Starter chưa hoàn thiện → **FAIL có chủ đích**. `--solutions` chỉ kiểm
lời giải tham khảo; không thay thế bài do sinh viên tự viết.
Các nội dung này bổ sung, **không thay** bài tập/máy check/mini-project gốc
và không tạo rubric mới.

## Evidence

- output `Week 03 solution checks: PASS`;
- normal, boundary và invalid case;
- giải thích thứ tự của một chuỗi `if/elif/else`;
- commit và một bug logic đã sửa.
