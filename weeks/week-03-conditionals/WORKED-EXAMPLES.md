# Week 03 — Dự đoán nhánh chạy · giải thích logic · kiểm lỗi đầu vào

**Dành cho sinh viên mới học Python.** Dựa trên [Week 03 README](README.md) và
[notes](notes.md). Chỉ dùng `if`, `elif`, `else`, so sánh, `and/or/not`,
`input()`, `isdigit()`, `int()` và `f-string`. Không cần Internet, thư viện
ngoài hay tài khoản AI.

## Chuẩn bị và cách học

Chạy từ **gốc repo `python-journey`**:

```bash
python --version
python weeks/week-03-conditionals/examples/04_predict_branch_order.py
python weeks/week-03-conditionals/examples/05_boolean_reasoning.py
python weeks/week-03-conditionals/examples/06_guard_before_decision.py
```

Nếu Windows không nhận `python`, có thể thử `py -3`. Hãy **che cột đáp án**
và ghi dự đoán trước khi chạy. Sau khi chạy, chọn một giá trị để thay đổi,
đoán kết quả mới, rồi mới thử. Mỗi ví dụ đều có nhánh đúng, điều kiện biên
và một lỗi dễ mắc.

## Ví dụ 04 — Vì sao thứ tự `if/elif` quyết định kết quả?

`if/elif/else` xét từ **trên xuống**, nhánh đầu tiên đúng sẽ chạy; các
nhánh sau không chạy. Quy tắc điểm trong ví dụ chỉ để học câu lệnh điều kiện,
không phải quy chế học tập thực tế.

```python
if score < 0 or score > 10:
    result = "Không hợp lệ"
elif score >= 8:
    result = "Giỏi"
elif score >= 5:
    result = "Đạt"
else:
    result = "Cần luyện tập"
```

Dự đoán rồi chạy:

| Điểm | Dự đoán của em | Đáp án giải thích |
|---:|---|---|
| -1 | ... | Không hợp lệ (ngoài 0..10) |
| 4.9 | ... | Cần luyện tập |
| 5 | ... | Đạt (bằng ngưỡng 5) |
| 7.9 | ... | Đạt |
| 8 | ... | Giỏi (bằng ngưỡng 8) |
| 10 | ... | Giỏi |
| 11 | ... | Không hợp lệ |

**Lỗi phổ biến:** nếu đặt `score >= 5` trước `score >= 8`, điểm 9 được
xếp `"Đạt"` thay vì `"Giỏi"` vì nhánh đầu đã đúng. Trong file ví dụ có
hai dòng so sánh **Sai thứ tự** và **Đúng thứ tự**. Đó là lỗi logic:
chương trình vẫn chạy nhưng kết quả không đúng ý định.

**Tự thử:** sửa score trong đoạn cuối từ 9 thành 8, rồi thành 4;
giải thích vì sao hai thứ tự có thể cho kết quả giống nhau ở score=4.
Đừng sửa `solutions/` để thử.

**Bài tương tự:** viết lại ý tưởng này trong [Lab 01 — xếp loại điểm](practice/README.md).
Lần này input đến từ `input()`, phải từ chối `"abc"` và `"11"` trước
khi xếp loại.

## Ví dụ 05 — `and`, `or`, `not`, ngoặc và truthy/falsy

Ví dụ **giả lập** luật vào phòng hội thảo: người tham gia được vào khi
đủ 18 tuổi **và** có vé **và** cửa chưa đóng.

```python
age_ok = age >= 18
can_enter = age_ok and has_ticket and not is_closed
```

| `age_ok` | `has_ticket` | `is_closed` | Dự đoán được vào? |
|---|---|---|---|
| True | True | False | **True** |
| False | True | False | False |
| True | False | False | False |
| True | True | True | False |

Trong một sự kiện giả lập khác, giấy mời **hoặc** vé có thể thay thế
cho nhau nhưng cửa vẫn phải mở:

```python
allowed = (has_ticket or has_invitation) and not is_closed
```

Dùng ngoặc để người đọc hiểu nhóm điều kiện. So sánh hai biểu thức:

```python
(False or True) and not False  # True
(False or True) and not True   # False
```

**Bẫy truthy/falsy:** `bool("False")` trả `True` vì đây là một
**chuỗi có ký tự**, còn `bool("")` trả `False`. Khi nhận
`"y"`/`"n"` từ `input()`, hãy so sánh `answer == "y"`,
**không** dùng `bool(answer)` để suy ra người dùng chọn có/không.

**Tự thử:** thay `has_invitation=True` thành `False` hoặc đổi
`is_closed` thành `True`, dự đoán kết quả trước khi chạy.

**Bài tương tự:** [Lab 02 — kiểm điều kiện vào cửa](practice/README.md)
sẽ thêm input thật; cần từ chối `"x"`, tuổi 121 và tuổi `"abc"`.

## Ví dụ 06 — Kiểm dữ liệu (guard) trước khi quyết định

Chương trình nhận tuổi dạng **text**, vì `input()` luôn trả `str`.
Nó phải kiểm text trước khi gọi `int()`.

```text
age_text = " 10 " (str)
       ↓ .strip() → "10"
       ↓ .isdigit() → True
       ↓ int() → 10 (int)
       ↓ 0..120 hợp lệ?
       ↓ dưới 12?
"Vé trẻ em"
```

Đoạn code quan trọng:

```python
clean = age_text.strip()
if not clean.isdigit():
    return "Lỗi: tuổi phải là số nguyên không âm"
age = int(clean)
if age > 120:
    return "Lỗi: tuổi phải từ 0 đến 120"
```

`return` ở đây thuộc **hàm minh họa**, đã giới thiệu hàm ở
Week 02/07 theo lộ trình học; sinh viên có thể viết **`if/else` trực tiếp**
ở các bài W03, không bắt buộc viết hàm.

| Input mô phỏng | Dự đoán | Kết quả |
|---|---|---|
| `" 10 "` | ... | Vé trẻ em |
| `"12"` | ... | Vé tiêu chuẩn |
| `"64"` | ... | Vé tiêu chuẩn |
| `"65"` | ... | Vé người cao tuổi |
| `"120"` | ... | Vé người cao tuổi |
| `"121"` | ... | Lỗi ngoài 0..120 |
| `"abc"` | ... | Lỗi text không phải số |
| `"-1"` | ... | Lỗi text không phải số |
| `""` | ... | Lỗi rỗng |

**Tại sao kiểm trước?** `int("abc")` trực tiếp gây `ValueError`.
Ví dụ này không cần `try/except`, chỉ dùng `if` để từ chối dữ
liệu không hợp lệ. Học exception chuyên sâu ở Week 11.

**Giới hạn:** `isdigit()` là kiểm tra đơn giản cho bài nhập môn,
không thay validation toàn diện (âm, dấu thập phân, Unicode khác,
trường hợp đặc biệt). Ví dụ chỉ giả định tuổi nguyên không âm.

**Bài tương tự:** [Lab 03 — phí giao hàng](practice/README.md) là bài
khác miền dữ liệu, cần kiểm số tiền, y/n và thứ tự ưu tiên miễn phí
trước giao nhanh.

## Bài chuyển giao — tự thiết kế, không chép ví dụ

Sau khi hoàn tất ba lab, chọn một dự án khác:

- **Giá vé xe:** dưới 6 tuổi miễn phí, từ 6–17 giảm giá, còn lại giá
  thường; từ chối tuổi vượt 120.
- **Mở khóa màn chơi:** `level >= 3` **và** `has_key` **và** `not is_locked`.
- **Ưu đãi cửa hàng:** thành viên có hóa đơn ít nhất 100.000đ
  **hoặc** tổng hóa đơn từ 200.000đ miễn phí giao hàng;
  nếu không thì tính phí.
- **Đăng ký sự kiện:** chỉ chấp nhận số lượng nguyên dương và còn chỗ.

Tự viết **bảng quyết định** (input, điều kiện, kết quả), một case bình
thường, hai giá trị biên và một case không hợp lệ. Chương trình phải
không in thành công khi input sai.

## Khi sai, kiểm theo thứ tự này

| Hiện tượng | Nguyên nhân thường gặp | Cách kiểm |
|---|---|---|
| Điểm 9 thành “Đạt” | ngưỡng >=5 đứng trước >=8 | xét ngưỡng từ cao xuống |
| `"n"` lại là True | `bool("n")` là True | dùng `answer == "y"` |
| `int("abc")` crash | đổi kiểu trước kiểm input | `strip()` / `isdigit()` trước |
| Tuổi 121 vẫn có vé | thiếu guard phạm vi | kiểm 0..120 trước nhánh vé |
| Đơn 200.000 vẫn tính phí | ưu tiên giao nhanh trước miễn phí | đổi thứ tự `if/elif` |
| Code chạy nhưng ra sai | lỗi logic, không phải SyntaxError | thử bảng test biên |

**Tiếp tục:** [3 lab tự làm](practice/README.md), [hints](hints.md),
[mini-project Decision Ticket](mini-project/README.md).
Không thêm điểm bắt buộc hoặc rubric mới.
