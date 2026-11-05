# Hints — Week 07

Chỉ mở tầng tiếp theo sau khi bạn đã thử viết và chạy code. Các hints định
hướng cách nghĩ nhưng không chứa full answer.

## Exercise 01 — Functions và `return`

### Hint 1 — hướng suy nghĩ

Mỗi function cần tạo một giá trị để caller nhận lại. Hãy bắt đầu bằng ví dụ nhỏ
nhất trong docstring.

### Hint 2 — cấu trúc

Dùng f-string cho lời chào, `math.pi` cho diện tích và phép chia lấy dư `%` để
nhận biết số chẵn.

### Hint 3 — gần pseudocode

```text
greeting = ghép "Xin chào", tên và "!"
area = pi nhân radius mũ 2
is_even = phần dư khi chia 2 bằng 0
```

## Exercise 02 — Parameters và decomposition

### Hint 1 — hướng suy nghĩ

Hoàn thành từng phép tính nhỏ trước, rồi mới ghép chúng trong `tao_hoa_don`.

### Hint 2 — cấu trúc

Kiểm tra `so_luong` trước khi nhân. Tiền giảm bằng tạm tính nhân phần trăm chia
100.

### Hint 3 — gần pseudocode

```text
subtotal = gọi hàm tính tạm tính
total = gọi hàm giảm giá với subtotal
return chuỗi định dạng total
```

## Exercise 03 — Scope

### Hint 1 — hướng suy nghĩ

List ghi chú thuộc về caller. Function nhận list đó qua parameter và không cần
tìm một biến global.

### Hint 2 — cấu trúc

Dùng `strip()` để tạo nội dung local. Với tìm kiếm, tạo `ket_qua` local và thêm
các ghi chú phù hợp vào đó.

### Hint 3 — gần pseudocode

```text
cleaned = nội dung đã strip
nếu cleaned rỗng: báo False
nếu hợp lệ: append vào list được truyền vào, báo True
```

## Exercise 04 — Decision function

### Hint 1 — hướng suy nghĩ

Đọc state theo thứ tự và trả action ngay khi một rule khớp.

### Hint 2 — cấu trúc

Dùng hai nhánh `if` cho `danger` và `opportunity`. Một `return` cuối xử lý mọi
state còn lại.

### Hint 3 — gần pseudocode

```text
nếu nguy hiểm: phòng thủ
nếu có cơ hội: tiến lên
còn lại: chờ
```

## Mini-project — Personal Utility Toolkit

### Hint 1 — hướng suy nghĩ

Vẽ luồng dữ liệu trước khi code. Đánh dấu output của function nào trở thành
input cho function tiếp theo.

### Hint 2 — cấu trúc

Hoàn thành các function tính toán trước, function định dạng sau, rồi ghép tất
cả trong `main()`.

### Hint 3 — gần pseudocode

```text
subtotal = price × quantity
discount = subtotal × percent / 100
final_total = subtotal - discount
display = format final_total
```
