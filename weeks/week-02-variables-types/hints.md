# Hints — Week 02

## Exercise 01

- Dùng bốn giá trị khác nhau rồi gọi `type(value)`.
- Python cho phép swap bằng `a, b = b, a`.

## Exercise 02

- `int()` bỏ phần thập phân của float, không làm tròn.
- Giá trị từ `input()` cần conversion trước phép tính.

## Exercise 03

- Tách từng input text, conversion và phép tính thành ba bước dễ quan sát.
- Trước phép chia, kiểm tra mẫu số hoặc tỷ giá khác 0.

## Mini-project

- `year_text.isdigit()` là validation preview đủ cho năm dương đơn giản.
- Dùng f-string để ghép năm bắt đầu và năm dự kiến tốt nghiệp.

## Ba bài tự luyện tương tự

Dùng [sổ tay dự đoán và chạy ví dụ](WORKED-EXAMPLES.md) trước khi
mở lời giải `practice/solutions/`.

- **Lab 01:** `age_text` là `str`; muốn cộng thêm 1 phải
  `age = int(age_text)`, sau đó dùng `type(age).__name__`.
- **Lab 02:** đổi hai chuỗi số sang `int`, tính `unit_price * quantity`.
  Dùng `f"{total:,}"` để trình bày có dấu phân cách.
- **Lab 03:** `input()` trả `str`. Dùng `.strip()`, `.isdigit()`,
  `int()` và kiểm số lượng > 0 trước khi in hóa đơn.

Máy kiểm `python weeks/week-02-variables-types/practice/checks/check_practice.py
--starter` có thể báo FAIL ban đầu: đó là bài cần em hoàn thiện, không
phải lỗi repository. `--solutions` chỉ dùng đối chiếu sau khi thử.
