# Week 07 — Bộ lab Functions tự viết, có kiểm hàm trực tiếp

**Bài thực hành bổ sung.** Sau khi xem [ba ví dụ có giải
thích](../WORKED-EXAMPLES.md), hãy làm bốn file trong `starter/`
với **hàm thực sự trả giá trị**, không chỉ in output đúng.
Bài tập gốc `exercises/` và mini-project vẫn giữ nguyên.

## Quy trình tự học

1. Dự đoán `return` của ba ví dụ mới (06–08) rồi chạy.
2. Đọc **signature, docstring, TODO, input/output/invalid** của từng lab.
3. Sửa `practice/starter/`, không mở đáp án ngay.
4. Gọi trực tiếp từng hàm với hai bộ tham số khác nhau.
5. Ghi một trường hợp biên và một trường hợp sai rồi chạy checker.
6. Nếu FAIL, xem tên Lab / thông báo `AssertionError`, sửa code.
7. Chỉ sau khi tự làm mới đối chiếu `practice/solutions/`.

## Lab 01 — Return, tham số mặc định và kiểm số lượng

File `starter/lab01_return_total.py`:

```python
def calculate_total(price: int, quantity: int, shipping: int = 0) -> int:
    # TODO: validate và return
    ...
```

| Input | Return mong đợi |
|---|---:|
| `(12_000, 2)` | `24000` |
| `(12_000, 2, 5_000)` | `29000` |
| `(0, 1)` | `0` |
| `(-1, 2)`, `(10, 0)`, phí âm | `ValueError` |
| `(True, 2)` | `ValueError` (bool không phải giá tiền) |

Hàm phải `return int` chứ **không print** để thay kết quả.

## Lab 02 — Validate → subtotal → discount

Ba hàm trong `starter/lab02_decomposition.py`:

`is_valid_order(price, quantity, percent)`,
`calculate_subtotal(price, quantity)`,
`calculate_final(price, quantity, percent=0)`.

Quy tắc **mô phỏng**: price nguyên không âm; quantity nguyên dương;
giảm giá nguyên 0..100%; tổng sau giảm làm tròn **xuống** đến
đồng VND (toán tử `//`).

| Input `calculate_final` | Return mong đợi |
|---|---:|
| `(25_000, 2)` | `50000` |
| `(25_000, 2, 10)` | `45000` |
| `(10_001, 1, 50)` | `5000` |
| `(0, 1, 100)` | `0` |
| quantity 0, percent -1/101, kiểu bool | `ValueError` |

`calculate_final` **phải gọi `calculate_subtotal`**, không
copy lại `price*quantity`; checker có kiểm hành vi tái sử dụng.

## Lab 03 — Scope và trạng thái thuộc về caller

File `starter/lab03_scope_notes.py`:

- `add_note(notes, text) -> bool`: `strip()`, từ chối chuỗi rỗng,
  thêm ghi chú vào list **được truyền tới**.
- `count_notes(notes) -> int`: chỉ đọc list.
- `search_notes(notes, keyword) -> list[str]`: tìm không phân biệt
  hoa/thường, trả **list kết quả mới**, không sửa danh sách nguồn.

Ví dụ: thêm `"  Học return  "` phải lưu `"Học return"`;
tìm `"RETURN"` thấy một ghi chú; tìm chuỗi chỉ có khoảng trắng
trả `[]`. Hai danh sách khác nhau không được tự chia sẻ dữ liệu.

## Lab 04 — Decision function có runtime validation

File `starter/lab04_decision_validation.py`, mô hình
học lập trình **không thuộc runtime VuaCóc**:

```python
choose_study_action(minutes: int, confused: bool) -> str
```

| Input | Return |
|---|---|
| `(0, True)` hoặc `(0, False)` | `"stop"` |
| `(15, True)` | `"review"` |
| `(15, False)` | `"practice"` |
| `(-1, False)`, `(61, False)` | `ValueError` |
| `(True, False)`, `(5, "False")` | `ValueError` |

Chặn dữ liệu **trước** khi ra quyết định. Type hints không
tự chặn runtime. Đầu vào giống nhau phải trả cùng một action.

## Lệnh tự kiểm từ repository root

```bash
# Chạy bài sinh viên để kiểm đúng hàm, không chỉ các dòng print
python weeks/week-07-functions/practice/checks/check_practice.py --starter

# Sau khi tự làm, đối chiếu lời giải tham khảo riêng
python weeks/week-07-functions/practice/checks/check_practice.py --solutions
```

**Trước khi làm TODO**, starter phải báo `FAIL (0/4)`.
Sau khi hoàn thiện:

```text
Lab 01: PASS
Lab 02: PASS
Lab 03: PASS
Lab 04: PASS
Week 07 student practice: PASS (4/4)
```

Checker chạy bằng **thư viện chuẩn Python**, không cần biết
`pytest` trước Week12. Nó kiểm trực tiếp function return
values, invalid inputs, mutation đúng contract và sự tái sử dụng
hàm con. **Không sửa checker để tạo PASS giả.**

## Ghi bằng chứng / bài mở rộng tự chọn

Sau khi làm, chọn một miền khác như hóa đơn sách, quản lý
nhiệm vụ hoặc chương trình chọn chiến thuật offline. Viết
signature, hai test thường, một test biên và một test dữ liệu
sai; chứng minh không lệ thuộc vào global state.

```text
Function:
Parameters:
Return:
Input thường -> expected -> actual:
Input sai -> expected -> actual:
Một lỗi đã sửa:
Giải thích vì sao return khác print:
Tôi đã tách chương trình thành những hàm nào?
```

Bộ này là **bài luyện thêm**, không tạo rubric mới, không đòi
framework, mạng hay agent thật. Lộ trình chính vẫn là
[Utility Toolkit](../mini-project/README.md).
