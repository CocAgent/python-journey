# Hints — Week 08

Chỉ mở tầng tiếp theo sau khi đã tự viết và chạy một phiên bản nhỏ.

## Exercise 01 — Dict lookup/update

### Hint 1

Copy dict trước khi cập nhật để caller vẫn giữ data ban đầu.

### Hint 2

`sum(scores.values()) / len(scores)` cần một nhánh riêng khi dict rỗng.

### Hint 3

Với frequency, giá trị mới bằng count hiện tại từ `.get()` cộng một.

## Exercise 02 — Nested data

### Hint 1

Đọc một tầng mỗi lần: student → `scores` → từng score.

### Hint 2

Duyệt `classroom.items()` để có cả name và student data.

### Hint 3

Tái sử dụng `diem_trung_binh()` thay vì viết lại phép tính.

## Exercise 03 — Sets

### Hint 1

Phần chung dùng `&`; tất cả dùng `|`; phần riêng dùng `-`.

### Hint 2

Để vừa loại trùng vừa giữ thứ tự, dùng một `set` theo dõi và một `list` kết quả.

### Hint 3

Anagram cần giữ số lần xuất hiện của mỗi ký tự; một set đơn lẻ chưa đủ.

## Exercise 04 — Bot heuristic

### Hint 1

Đọc `position`, `goal` và field tùy chọn trước khi viết rules.

### Hint 2

Xử lý boundary `position == goal` trước rule di chuyển.

### Hint 3

Nếu position nhỏ hơn goal thì đi `right`; nếu lớn hơn thì đi `left`.

## Mini-project — Decision Dashboard

### Hint 1

Viết model mẫu trước, rồi tách function validate, summarize và recommend.

### Hint 2

Set phù hợp cho tags và membership; dict phù hợp cho field có tên.

### Hint 3

Giải thích recommendation bằng chính field mà rule đã đọc.
