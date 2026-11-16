# Week 05 — Bài tương tự có TODO và máy tự kiểm riêng

**Chỉ bắt đầu sau khi chạy [ba ví dụ có giải thích](../WORKED-EXAMPLES.md).**
Ba lab bổ sung này **không thay** bài tập gốc ở `exercises/`,
lời giải gốc ở `solutions/` hoặc mini-project Collection Workflow.

## Cách học không sao chép

1. Che đáp án rồi dự đoán output trong `WORKED-EXAMPLES.md`.
2. Chạy ví dụ 04–06, đọc điểm khác với dự đoán.
3. Mở `practice/starter/`, đọc TODO và tự viết code.
4. Chạy chính file starter, so output với bảng yêu cầu.
5. Thử một lỗi hoặc thay một giá trị, giải thích kết quả.
6. Chạy máy kiểm `--starter`; nếu FAIL, sửa starter, **không sửa checker**.
7. Chỉ sau khi tự làm, mở `practice/solutions/` để đối chiếu.

Không cần vòng lặp/comprehension (Week 06), hàm (Week 07),
`pytest` (Week 12) hay thư viện bên ngoài.

## Lab 01 — CRUD danh sách đồ dùng

Mở `practice/starter/lab01_shopping_list.py`.

Dữ liệu đầu tiên: `["Sách", "Bút", "Tẩy"]`.

Thực hiện `append("Vở")`, `insert(1, "Thước")`,
thay item 0 bằng `"Sách Python"`, xóa `"Tẩy"`,
cuối cùng `removed = items.pop()`.

**Kết quả mong đợi:**

```text
Sau CRUD: ['Sách Python', 'Thước', 'Bút']
Đã lấy: Vở
Đầu: Sách Python
Cuối: Bút
```

**Tự hỏi:** `remove("Tẩy")` khác `pop()` ở đâu?
Nếu pop thêm khi list rỗng thì sao?

## Lab 02 — Slice, alias và snapshot

Mở `practice/starter/lab02_alias_copy.py`.

Dữ liệu: `[10,20,30,40,50]`. Lấy `first_two`, `last_two`;
tạo `alias = numbers` và `snapshot = numbers.copy()`,
sau đó thêm 60 qua alias và sửa giá trị đầu của numbers thành 99.

**Kết quả mong đợi:**

```text
Đầu: [10, 20]
Cuối: [40, 50]
Gốc: [99, 20, 30, 40, 50, 60]
Alias: [99, 20, 30, 40, 50, 60]
Copy: [10, 20, 30, 40, 50]
Cùng đối tượng: True
```

**Tự hỏi:** tại sao `Copy` không có 60? Với **list lồng nhau**
có list con, liệu `copy()` còn độc lập hoàn toàn không?

## Lab 03 — Tuple và unpacking

Mở `practice/starter/lab03_tuple.py`.

Dữ liệu: `coordinate=(3,7)`, `profile=("An",20,"Python")`,
`left="A"`, `right="B"`.

**Kết quả mong đợi:**

```text
Tọa độ: x=3, y=7
Học viên: An, 20 tuổi, học Python
Đổi chỗ: B, A
Tuple một phần tử: ('Cóc',)
Kiểu: tuple
```

**Tự hỏi:** vì sao `("Cóc")` không phải tuple? Điều gì xảy ra
nếu unpack `(3,)` thành hai biến?

## Lệnh chạy từ repository root

```bash
python weeks/week-05-lists-tuples/practice/starter/lab01_shopping_list.py
python weeks/week-05-lists-tuples/practice/starter/lab02_alias_copy.py
python weeks/week-05-lists-tuples/practice/starter/lab03_tuple.py

# Chấm chính code trong practice/starter (trước khi làm: FAIL)
python weeks/week-05-lists-tuples/practice/checks/check_practice.py --starter

# Kiểm lời giải tham khảo; không chấm code người học
python weeks/week-05-lists-tuples/practice/checks/check_practice.py --solutions
```

Khi hoàn thiện ba bài sẽ thấy:

```text
Lab 01: PASS
Lab 02: PASS
Lab 03: PASS
Week 05 student practice: PASS (3/3)
```

**Lưu ý:** máy kiểm này so output và được viết cho người học dễ nhận
lỗi. PASS **không phải bằng chứng tuyệt đối** về cách triển khai;
sinh viên cần giải thích từng thao tác và chứng minh khi thay dữ
liệu, code vẫn hợp lý.

## Một bài biến đổi tự chọn

Chọn **một** tình huống mới: danh sách sách mượn, list bài hát,
hoặc tuple tọa độ cửa hàng. Không chép trực tiếp câu in của
solutions. Ghi lại:

```text
Giả thuyết ban đầu:
Dữ liệu trước khi chạy:
Output dự đoán:
Output thực tế:
Vì sao thay đổi (hoặc không thay đổi):
Lỗi em đã phát hiện và cách sửa:
List hay tuple phù hợp hơn? Vì sao:
```

Không thay syllabus hoặc thang điểm của khóa học.
