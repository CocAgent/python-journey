# Hints — Week 05

- `append` thêm cuối; `insert(index, value)` thêm tại vị trí.
- Slice không gồm end index.
- `alias = original` không tạo list mới.
- `copied = original.copy()` tạo shallow copy.
- Unpack coordinate bằng `x, y = coordinate`.
- Swap hai giá trị bằng `left, right = right, left`.

## Ba lab tự luyện theo phương pháp dự đoán

Đọc [WORKED-EXAMPLES.md](WORKED-EXAMPLES.md) và
[practice/README.md](practice/README.md) trước.

- **Lab 01 — Shopping list:** theo thứ tự `append`, `insert`,
  cập nhật `items[0]`, `remove("Tẩy")`, `pop()`. Đọc
  lại list ở **cuối** rồi mới in đầu/cuối.
- **Lab 02 — Alias/copy:** lấy hai slice **trước khi sửa**.
  `alias = numbers` và `snapshot = numbers.copy()`
  không giống nhau. Dùng `alias is numbers` để kiểm cùng object.
- **Lab 03 — Tuple:** `x, y = coordinate` và
  `name, age, topic = profile`; swap bằng
  `left, right = right, left`. Tuple một phần tử cần dấu phẩy:
  `("Cóc",)`.

`--starter` FAIL trước khi làm là đúng thiết kế. Chỉ sau khi
tự sửa xong mới xem `practice/solutions/`.
