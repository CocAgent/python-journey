# Hints — Week 01

## Exercise 01

- Mỗi lệnh `print()` tự xuống dòng, nên ba điều bạn thích cần ba lệnh hoặc một vòng lặp sau này.
- Hình chữ nhật rỗng gồm ba phần: dòng trên, các dòng giữa, dòng dưới.
- `"*" * 5` lặp ký tự mà không cần gõ tay từng dấu.

## Exercise 02

- `/` luôn trả về float, `//` trả về phần nguyên, `%` trả về phần dư.
- Phần nguyên và phần dư thường đi theo cặp khi chia đều một số lượng.
- Dùng `f"{value:,}"` để hiển thị số tiền có dấu phân cách nghìn.

## Exercise 03

- `input()` luôn trả về text, cần `int()` hoặc `float()` trước khi tính.
- Gọi `.strip()` để bỏ khoảng trắng thừa người dùng vô tình gõ.
- Nếu người dùng nhập chữ vào ô số, `int()` sẽ raise `ValueError` — Week 03 sẽ xử lý.

## Mini-project

- Vẽ hình ra giấy trước, đếm số ký tự mỗi dòng rồi mới viết `print()`.
- Ghép tên người dùng vào khung bằng f-string thay vì nối chuỗi thủ công.
