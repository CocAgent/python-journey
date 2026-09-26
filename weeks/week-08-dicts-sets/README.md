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
2. Chạy lần lượt năm file trong [`examples/`](examples/).
3. Làm bốn bài trong [`exercises/`](exercises/).
4. Mở [`hints.md`](hints.md) theo từng tầng nếu bị kẹt.
5. Chạy [machine check](checks/README.md) cho official solutions.
6. Hoàn thành [Decision Dashboard](mini-project/README.md).
7. Commit kết quả và lưu bằng chứng.

## Learning path

```text
README → notes → examples → exercises → hints
       → machine checks → mini-project → evidence
```

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
