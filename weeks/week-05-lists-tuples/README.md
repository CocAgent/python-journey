# Tuần 05 — Lists · Tuples · Mutability · Unpacking

Tuần này bạn chọn list cho collection có thể thay đổi và tuple cho một nhóm giá
trị cố định, đồng thời quan sát khác biệt giữa alias và copy.

## Outcomes

- tạo, đọc, cập nhật, thêm và xóa phần tử list;
- dùng indexing và slicing;
- tạo tuple, packing và unpacking;
- giải thích list mutable và tuple immutable;
- phân biệt hai tên cùng trỏ một list với shallow copy độc lập.

Comprehensions được học có hệ thống ở Week 06.

## Learning path

```text
README → notes → examples → exercises → hints
       → machine check → collection workflow → evidence
```

Đi theo [`notes.md`](notes.md), [`examples/`](examples/),
[`exercises/`](exercises/), [`hints.md`](hints.md),
[machine check](checks/README.md) và [mini-project](mini-project/README.md).

## Ba ví dụ dự đoán kết quả + bài tập tương tự

Học theo vòng **Dự đoán → Chạy → Giải thích → Thử lỗi → Tự viết → Kiểm chứng**
qua [**WORKED-EXAMPLES.md**](WORKED-EXAMPLES.md):

| Ví dụ mới | Sinh viên quan sát | Lỗi quan trọng |
|---|---|---|
| `04_predict_alias_and_copy.py` | Hai tên cùng trỏ một list và `.copy()` | Nhầm alias với bản sao; shallow copy list lồng nhau |
| `05_list_crud_and_slice.py` | CRUD, slicing, `sorted` và `sort` | `sort()` trả `None`; `remove` khi không tồn tại |
| `06_tuple_unpack_and_guard.py` | Tuple, unpack, swap, tuple một phần tử | Unpack sai số phần tử, gán lại tuple |

Từ **gốc repo**:

```bash
python weeks/week-05-lists-tuples/examples/04_predict_alias_and_copy.py
python weeks/week-05-lists-tuples/examples/05_list_crud_and_slice.py
python weeks/week-05-lists-tuples/examples/06_tuple_unpack_and_guard.py
```

Tiếp theo, mở [**3 bài tương tự**](practice/README.md) để tự
viết code trong `practice/starter/` (danh sách đồ dùng, snapshot
điểm số, tuple tọa độ/hồ sơ), có lời giải và máy kiểm độc lập:

```bash
python weeks/week-05-lists-tuples/practice/checks/check_practice.py --starter
```

**Starter chưa viết xong → FAIL có chủ đích**. `--solutions`
chỉ kiểm reference, không chứng minh đã hoàn thành bài.
Bộ thực hành mới là tùy chọn, không thay exercises/solutions gốc
hoặc mini-project.

## Evidence

- output `Week 05 solution checks: PASS`;
- một ví dụ alias thay đổi cùng list;
- một ví dụ copy không thay đổi source;
- tuple unpacking và một collection workflow đã chạy.
