# Tuần 08 — Dict · Set · Nested Data · Data Modeling

Tuần này bạn dùng cấu trúc dữ liệu để mô tả một trạng thái nhỏ, sau đó biến
trạng thái đó thành một quyết định có thể giải thích. Learning loop tiếp tục:

```text
Learn → Build → Test → Debug → Improve → Commit → Prove
```

## Mục tiêu

Sau Week 08, bạn có thể:

- tạo, đọc và cập nhật giá trị trong `dict`;
- duyệt `keys()`, `values()` và `items()`;
- dùng membership để kiểm tra key hoặc phần tử;
- dùng `set` để loại trùng và thực hiện phép hợp, giao, hiệu đơn giản;
- đọc dữ liệu lồng nhau gồm `dict` và `list`;
- chọn cấu trúc dữ liệu phù hợp cho một state nhỏ;
- phân biệt data model với behavior xử lý data;
- dùng `.get()` khi key có thể thiếu;
- biến structured state thành một heuristic decision;
- mở rộng decision function Week 07 sang course-local bot state.

## Prerequisites

Bạn nên hoàn thành Week 01–07, đặc biệt là loop, function, `return`, scope và
decision function.

## Thứ tự học

1. Đọc [`notes.md`](notes.md).
2. Chạy lần lượt năm file gốc trong [`examples/`](examples/), sau đó xem [3 ví dụ bổ sung](WORKED-EXAMPLES.md).
3. Làm bốn bài trong [`exercises/`](exercises/) và tùy chọn [4 lab tự luyện](practice/README.md).
4. Mở [`hints.md`](hints.md) theo từng tầng nếu bị kẹt.
5. Chạy [machine check](checks/README.md) cho official solutions.
6. Hoàn thành [Decision Dashboard](mini-project/README.md).
7. Commit kết quả và lưu bằng chứng.

## Learning path

```text
README → notes → examples → exercises → hints
       → machine checks → mini-project → evidence
```

## Dự đoán trước khi chạy — sổ tay và bốn lab tự luyện

Bắt đầu từ [**WORKED-EXAMPLES.md**](WORKED-EXAMPLES.md) để thực hiện
**Dự đoán → Chạy → Giải thích → Thử lỗi → Viết bài tương tự → Kiểm chứng**.

| Ví dụ mới | Trọng tâm | Lỗi dễ mắc |
|---|---|---|
| `06_predict_dict_get_copy.py` | dict key, `.get`, frequency, `.copy()` | dùng default để che key bắt buộc thiếu |
| `07_predict_set_and_order.py` | phép set, uniqueness và list order | `list(set(...))` làm mất thứ tự, set không đếm tần suất |
| `08_nested_state_validated.py` | nested data + validation + heuristic | xem bool như int hoặc field sai là hợp lệ |

Chạy từ **gốc repo `python-journey/`**:

```bash
python weeks/week-08-dicts-sets/examples/06_predict_dict_get_copy.py
python weeks/week-08-dicts-sets/examples/07_predict_set_and_order.py
python weeks/week-08-dicts-sets/examples/08_nested_state_validated.py
```

Tiếp theo, tự làm [**4 lab độc lập với bài gốc**](practice/README.md):
đếm từ và cập nhật dict copy; xử lý nested learner; phép set và
thứ tự; state → validate → action → explanation.

```bash
# Máy kiểm GỌI TRỰC TIẾP các hàm sinh viên tự viết
python weeks/week-08-dicts-sets/practice/checks/check_practice.py --starter

# Chỉ kiểm đáp án mẫu sau khi tự làm
python weeks/week-08-dicts-sets/practice/checks/check_practice.py --solutions
```

**Starter ban đầu FAIL (0/4) là đúng thiết kế.** `--solutions`
PASS không chứng minh sinh viên đã làm xong starter.
Bộ bổ sung không thay bốn exercises, Decision Dashboard hay rubric.

## Checklist

- [ ] Tôi đọc và cập nhật được một `dict`.
- [ ] Tôi duyệt được key, value và cặp key-value.
- [ ] Tôi dùng `set` cho uniqueness và membership.
- [ ] Tôi đọc được nested data.
- [ ] Tôi giải thích được data model mình chọn.
- [ ] Tôi viết được heuristic từ structured state.
- [ ] Tôi chạy machine check.
- [ ] Tôi hoàn thành mini-project.
- [ ] Tôi commit kết quả.

## Evidence

Lưu lại:

- output `Week 08 solution checks: PASS`;
- output của một normal state và một boundary state;
- output khi chạy mini-project;
- commit chứa bài làm;
- một ghi chú về data-modeling decision và một lỗi bạn đã sửa.

## VuaCóc Bot Journey

Week 08 milestone: [State + Heuristic](../../projects/vuacoc-bot-journey/milestones/w08-state-and-heuristic.md).

```text
COURSE TEACHING MODEL
NOT VUACOC PRODUCTION CONTRACT
```
