# Week 06 — Dự đoán vòng lặp → chạy → giải thích → sửa lỗi → tự làm

**Dành cho người mới học Python.** Bạn đã học biến, điều kiện, string,
list và tuple ở Week 02–05. Tuần này học cách **duyệt nhiều phần tử**
và biết chắc khi nào vòng lặp kết thúc.

**Không cần Internet, framework hay API key.** Chỉ cần Python >=3.12.

## 0. Bắt đầu

Chạy từ **thư mục gốc repository `python-journey`**:

```bash
python --version
python weeks/week-06-loops/examples/04_predict_range_break_continue.py
python weeks/week-06-loops/examples/05_enumerate_zip_strict.py
python weeks/week-06-loops/examples/06_comprehension_nested_loop.py
```

Trên Windows có thể dùng `py -3` thay cho `python`.

Với mỗi ví dụ: **che kết quả → ghi dự đoán → chạy → so sánh →
giải thích → đổi một giá trị → làm bài tương tự**. Hãy dùng Undo
để khôi phục ví dụ gốc sau khi thử.

## 1. Ví dụ 04 — `range`, `continue`, `break` và `while`

Đoán trước khi chạy:

| Biểu thức / tình huống | Dự đoán | Kết quả |
|---|---|---|
| `list(range(1, 6))` | … | `[1, 2, 3, 4, 5]` |
| `number % 3 == 0` | … | đúng ở 3, 6, 9… |
| Gặp `continue` | … | bỏ **lượt hiện tại**, xét số tiếp |
| Gặp `break` | … | kết thúc **toàn bộ vòng for hiện tại** |
| `while remaining > 0` với remaining=3 | … | in 3, 2, 1 |
| `while remaining > 0` với remaining=0 | … | không có lượt nào |

Code mô tả lựa chọn số:

```python
selected = []
for number in range(1, 11):
    if number % 3 == 0:
        continue
    if number > 8:
        break
    selected.append(number)
print(selected)  # [1, 2, 4, 5, 7, 8]
```

**Dấu vết (trace):** 1 và 2 được thêm; 3 bị `continue`;
4, 5 được thêm; 6 bị bỏ; 7, 8 được thêm; 9 bị `continue`;
10 gây `break`. Vì vậy kết quả không có 9 và 10.

**Chú ý:** với thứ tự điều kiện trên, `break` chỉ đến khi gặp 10.
Nếu bạn di chuyển `if number > 8: break` lên trước `continue`,
vòng sẽ dừng ở 9; output trong dữ liệu này vẫn giống nhưng **luồng
thực thi khác**. Khi debug, phải quan sát điều kiện được xét,
không chỉ nhìn output cuối.

```python
remaining = 3
while remaining > 0:
    print(remaining)
    remaining -= 1  # nếu quên, có nguy cơ vòng lặp vô hạn
```

Ở `while`, hãy luôn trả lời: “**điều gì sẽ làm điều kiện thành False?**”
Không xóa `remaining -= 1` rồi chạy thật; hãy vẽ trace trên giấy.

**Bài tương tự:** [Lab 02 — đếm ngược an toàn](practice/README.md)
nhận `0`, `3`, `5`, `abc`, `-1`, `6`.
[Lab 03](practice/README.md) dùng cả `break` và `continue`.

## 2. Ví dụ 05 — `enumerate` và `zip(..., strict=True)`

```python
names = ["An", "Bình", "Chi"]
scores = [8, 9, 7]
for position, (name, score) in enumerate(
    zip(names, scores, strict=True), start=1
):
    print(f"{position}. {name}: {score}")
```

Output dự kiến:

```text
1. An: 8
2. Bình: 9
3. Chi: 7
```

**Vì sao hai công cụ?** `zip` ghép hai danh sách theo vị trí;
`enumerate(start=1)` tạo số thứ tự trình bày.

Hãy đoán điều gì xảy ra nếu `scores=[8,9]` nhưng có 3 tên.

| Cách ghép | Hành vi |
|---|---|
| `list(zip(names, scores))` | chỉ có hai cặp, **bỏ mất Chi** |
| `list(zip(names, scores, strict=True))` | `ValueError` vì độ dài lệch |
| `zip(names, scores, strict=True)` (chưa duyệt) | chưa phát hiện lỗi; `zip` là iterator |

`strict=True` quan trọng khi **một điểm phải ứng với đúng một
học sinh**. Lỗi chỉ phát sinh khi iterator được duyệt đến phần
thiếu dữ liệu. File ví dụ **bắt có chủ đích** `ValueError` để
in lời giải thích, không báo ghép thành công.

**Tự thử:** đổi `start=1` thành `start=0`, rồi dự đoán
số thứ tự. Hãy thêm một score vào list ngắn và quan sát
`strict=True` không báo lỗi nữa.

**Bài tương tự:** [Lab 01 — báo cáo điểm có đánh số](practice/README.md).
Dùng `for` tính tổng, chưa cần hàm từ Week 07.

## 3. Ví dụ 06 — Vòng for thường, comprehension và vòng lặp lồng

```python
numbers = [1, 2, 3, 4, 5, 6]
evens_for = []
for number in numbers:
    if number % 2 == 0:
        evens_for.append(number**2)

evens_comprehension = [
    number**2 for number in numbers if number % 2 == 0
]
```

Cả hai cách trả `[4, 16, 36]`. Với phép lọc và biến đổi đơn
giản, comprehension ngắn và rõ. Nếu có nhiều nhánh điều kiện,
`break`, `continue`, hoặc cần giải thích từng bước, dùng
**vòng `for` thông thường** sẽ dễ đọc hơn.

Vòng lặp lồng khi thực sự cần ghép **mỗi hàng với mỗi cột**:

```python
cells = []
for row in range(1, 3):
    for col in range(1, 4):
        cells.append((row, col))
```

Kết quả là **6** tọa độ:
`[(1,1),(1,2),(1,3),(2,1),(2,2),(2,3)]`.
Vòng ngoài chạy 2 lần, vòng trong chạy 3 lần **cho mỗi lượt
ngoài**, nên 2 × 3 = 6. Nếu input là list rỗng, comprehension
trả `[]`, không tự gây lỗi.

**Bài tương tự:** [Lab 03 — lọc số và bình phương](practice/README.md).
Chỉ dùng comprehension ở bước cuối, không ép `break` vào
comprehension khó đọc.

## 4. Bảng lỗi cần biết

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| `range(1, 6)` không có 6 | `stop` là cận **không bao gồm** | dùng `range(1,7)` nếu cần 6 |
| `while` chạy mãi | quên cập nhật biến quyết định dừng | viết trace và bảo đảm có tiến triển |
| `continue` khiến dòng `append` không chạy | phần còn lại của lượt bị bỏ | đặt code đúng thứ tự |
| `break` bỏ cả các phần tử tiếp theo | `break` dừng loop | dùng `continue` nếu chỉ bỏ lượt |
| Tên và điểm thiếu một cặp | `zip` mặc định cắt theo list ngắn | `zip(..., strict=True)` khi cần đủ cặp |
| Lỗi `ValueError` chỉ xuất hiện khi duyệt `zip` | iterator tính dần | duyệt để phát hiện thiếu |
| Comprehension dài khó đọc | nhồi nhiều nhánh | chuyển về `for` có tên biến rõ |

## 5. Ba bài tự làm khác dữ liệu ví dụ

Mở [practice/README.md](practice/README.md) rồi sửa **chỉ**
`practice/starter/`:

- **Lab 01:** báo cáo học viên và điểm với `enumerate/zip`.
- **Lab 02:** `while` đếm ngược có kiểm input (0..5).
- **Lab 03:** `continue/break` và comprehension lấy bình phương chẵn.

Từ **gốc repo**:

```bash
python weeks/week-06-loops/practice/checks/check_practice.py --starter
```

Khi mới bắt đầu, `FAIL (0/3)` là **đúng** vì các TODO
chưa làm. Sau khi tự hoàn thiện, cần
`Week 06 student practice: PASS (3/3)`.

Đối chiếu đáp án **sau khi tự thử**:

```bash
python weeks/week-06-loops/practice/checks/check_practice.py --solutions
```

`--solutions` chỉ kiểm code mẫu, không chứng minh bài
của sinh viên đã hoàn thành.

## 6. Bài chuyển giao và ghi bằng chứng

Chọn **một** bài mới: đếm hàng còn trong kho, in lịch học có
số thứ tự, hoặc tạo bảng tọa độ trò chơi 2×3. Không sao chép
nguyên các dòng `print` trong solutions. Ghi lại:

```text
Input trước khi chạy:
Dự đoán số lượt lặp:
Điều kiện kết thúc:
Output dự đoán:
Output thực tế:
Một trường hợp biên / dữ liệu lỗi:
Em đã sửa bug nào và vì sao:
```

Sau đó quay về [Iteration Report](mini-project/README.md).
**Không thêm rubric, quota bài bắt buộc, hoặc framework mới.**
