# Week 05 — Dự đoán · Chạy · Giải thích · Thử lỗi · Tự viết

**Python Journey · List, tuple, slicing, alias/copy và unpacking.**

Đây là sổ tay thực hành cho người mới học, **không cần Internet, thư viện
ngoài, lớp, hàm phức tạp hoặc vòng lặp**. Những nội dung nâng cao của
Week 06 (loop/comprehension) và Week 07 (functions) vẫn để đúng tuần.

## 0. Cách bắt đầu

Mở terminal tại **thư mục gốc repo `python-journey/`**:

```bash
python --version
python weeks/week-05-lists-tuples/examples/04_predict_alias_and_copy.py
python weeks/week-05-lists-tuples/examples/05_list_crud_and_slice.py
python weeks/week-05-lists-tuples/examples/06_tuple_unpack_and_guard.py
```

Nếu Windows không nhận `python`, có thể dùng `py -3`.

**Mỗi bài thực hiện 6 bước:** (1) che đáp án, đoán output;
(2) chạy chương trình; (3) so kết quả; (4) giải thích dòng làm
thay đổi dữ liệu; (5) thay một giá trị rồi tự thử; (6) giải bài
tương tự trong `practice/starter/`.

## Ví dụ 04 — Một list, hai tên: alias khác copy thế nào?

Đọc code trước khi chạy:

```python
books = ["Toán", "Văn"]
alias = books
snapshot = books.copy()
alias.append("Anh")
books[0] = "Tin"
```

Hãy đoán `books`, `alias`, `snapshot` trước khi xem đáp án:

| Biến | Dự đoán của em | Kết quả |
|---|---|---|
| `books` | … | `["Tin", "Văn", "Anh"]` |
| `alias` | … | `["Tin", "Văn", "Anh"]` |
| `snapshot` | … | `["Toán", "Văn"]` |
| `alias is books` | … | `True` |
| `snapshot is books` | … | `False` |

**Vì sao?** `alias = books` không tạo list mới. Hai tên cùng
tham chiếu một list. `books.copy()` tạo **list mới** nên sửa
các phần tử ở danh sách gốc không làm thay đổi bản sao (với list
phẳng chứa chuỗi/số trong bài này).

<escape>**Cẩn thận với list lồng nhau:**</escape> `copy()` chỉ sao chép
**một lớp (shallow copy)**. Đoạn cuối ví dụ dùng
`nested = [["A"], ["B"]]`: sau khi thêm `"C"` vào list con
`nested[0]`, bản sao cũng nhìn thấy `["A", "C"]`.
Điều này không mâu thuẫn với ví dụ list phẳng.

**Tự thử:** đổi `alias.append("Anh")` thành
`snapshot.append("Anh")`, dự đoán hai list nào thay đổi.
Sau khi thử, dùng Undo/Restore để đưa ví dụ về trạng thái ban đầu.

**Bài tương tự:** [Lab 02 — điểm số, alias và copy](practice/README.md).
Không copy nguyên code `books` vào bài `numbers`: hãy tự suy luận.

## Ví dụ 05 — CRUD, slice, `sorted` và `sort`

Nhìn chuỗi thao tác trên dữ liệu:

```text
["An", "Bình", "Chi"]
     ↓ append("Dũng")
["An", "Bình", "Chi", "Dũng"]
     ↓ insert(1, "Lan")
["An", "Lan", "Bình", "Chi", "Dũng"]
     ↓ names[0] = "Mai"
     ↓ remove("Chi")
     ↓ last = pop()
["Mai", "Lan", "Bình"]; last = "Dũng"
```

Sau khi chạy `05_list_crud_and_slice.py`, tự trả lời:

| Câu hỏi | Đáp án cần kiểm chứng |
|---|---|
| `names[:2]` | `["Mai", "Lan"]` |
| `names[::-1]` | `["Bình", "Lan", "Mai"]` |
| `names[:99]` | trả phần list hiện có, **không lỗi** |
| `names[99]` nếu gọi | `IndexError` (không gọi trong demo) |
| `names.remove("Nam")` nếu không có | `ValueError` (demo kiểm `in` trước) |
| `sorted([7, 4, 9])` | list mới `[4, 7, 9]`, không sửa list cũ |
| `scores.sort()` | sửa list cũ **tại chỗ**, trả `None` |

Phân biệt `remove(value)` (**xóa theo giá trị**),
`pop(index)` (**xóa theo vị trí và trả phần tử**), `append`
(**thêm cuối**), `insert` (**chèn trước vị trí**).

**Lỗi dễ mắc:** `scores = scores.sort()` khiến `scores`
trở thành `None`. Muốn có list mới dùng `sorted(scores)`;
muốn sửa list tại chỗ chỉ gọi `scores.sort()`.

**Tự thử:** thêm `"Nam"` trước khi kiểm `"Nam" in names`,
rồi quan sát kết quả remove. Đổi `names[:2]` thành
`names[1:3]` và dự đoán khác biệt. Slice **không gồm chỉ số cuối**.

**Bài tương tự:** [Lab 01 — danh sách đồ dùng học tập](practice/README.md)
gồm thêm, chèn, sửa và xóa; không cần vòng lặp.

## Ví dụ 06 — Tuple, unpacking, hoán đổi và tuple một phần tử

```python
position = (3, 7)
x, y = position
profile = ("An", 20, "Python")
name, age, topic = profile
left, right = "A", "B"
left, right = right, left
```

Dự đoán `x=3`, `y=7`, sau đó `left="B"`, `right="A"`.

Tuple có thứ tự, cho đọc theo index và unpack; **không hỗ trợ
gán lại phần tử** như `position[0] = 9` (gây `TypeError`).
`("Cóc",)` là tuple một phần tử nhờ **dấu phẩy**,
còn `("Cóc")` chỉ là string trong ngoặc.

Nếu có `candidate=(8,)` mà viết `x,y=candidate`,
chương trình báo `ValueError` vì thiếu phần tử. Ví dụ dùng
`len(candidate) == 2` trước khi unpack.

**Giới hạn cần hiểu:** tuple không cho thay phần tử, nhưng nếu
tuple chứa một list thì **list bên trong vẫn có thể thay đổi**.
Vì vậy “tuple immutable” không đồng nghĩa mọi object bên trong
đều bất biến.

**Bài tương tự:** [Lab 03 — tọa độ và hồ sơ](practice/README.md).

## Khi lỗi — đừng chỉ đoán cách sửa

| Tình huống | Loại lỗi / kết quả | Cách hiểu |
|---|---|---|
| `items[99]` | `IndexError` | index đơn vượt phạm vi |
| `items[:99]` | không lỗi | slice bị giới hạn bởi độ dài |
| `items.remove("Khác")` | `ValueError` | giá trị chưa tồn tại |
| `items.pop()` khi rỗng | `IndexError` | cần kiểm có phần tử |
| `items = items.sort()` | `items` thành `None` | `sort` sửa tại chỗ và không trả list |
| `x, y = (8,)` | `ValueError` | số giá trị unpack không khớp |
| `point[0] = 9` | `TypeError` | tuple không cho sửa phần tử |
| `a = b` với list | **không tạo copy** | hai biến trỏ cùng đối tượng |

**Không bắt buộc dùng `try/except` ở Week 05:** kiểm dữ liệu
trước khi gọi thao tác có thể lỗi; Week 11 học exceptions chi tiết.

## Ba bài tương tự để tự làm

Hãy hoàn thành theo thứ tự:
[Lab 01 — CRUD](practice/README.md),
[Lab 02 — slice/alias/copy](practice/README.md),
[Lab 03 — tuple/unpack](practice/README.md).

Mỗi lab có starter TODO, lời giải riêng và máy tự kiểm.
Từ **gốc repo**:

```bash
python weeks/week-05-lists-tuples/practice/checks/check_practice.py --starter
```

Trước khi sửa TODO: **FAIL (0/3) là đúng**; sau khi làm xong
cần `Week 05 student practice: PASS (3/3)`.

Chỉ sau khi đã tự thử, dùng:

```bash
python weeks/week-05-lists-tuples/practice/checks/check_practice.py --solutions
```

**PASS reference không chứng minh starter của bạn đã hoàn thành.**

## Bài nâng cao tự chọn — chuyển sang một bài toán khác

Chọn một trong các hướng sau (không phải bài bắt buộc mới):

- **Giỏ hàng nhỏ:** list tên sản phẩm; thêm/sửa/xóa 1 item,
  tạo snapshot trước khi sửa giỏ.
- **Vị trí trò chơi:** tuple `(row, col)`, unpack và đổi hai vị
  trí; thử tuple thiếu dữ liệu.
- **Bảng công việc:** list các tuple `(title, status)`;
  cập nhật **bằng cách thay tuple trong list** thay vì sửa một
  phần tử tuple. Tham khảo [Collection Workflow](mini-project/README.md).

Nêu một input thường, một giá trị biên, một lỗi đã sửa,
và giải thích **vì sao chọn list hay tuple**. Vòng học:
**Dự đoán → Chạy → Giải thích → Sửa → Kiểm chứng**.
