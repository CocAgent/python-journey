# Hints — Week 03

## Exercise 01

- Kiểm tra range không hợp lệ trước khi xếp loại.
- Với năm nhuận, dùng ngoặc để làm rõ kết hợp `and` và `or`.

## Exercise 02

- Viết từng boolean có tên trước khi ghép chúng.
- FizzBuzz cần kiểm tra chia hết cả 3 và 5 trước hai case riêng.

## Exercise 03

- Guard invalid amount trước balance và denomination.
- Chỉ nested khi quyết định thứ hai thật sự phụ thuộc quyết định thứ nhất.

## Mini-project

- Validate text rỗng và tuổi chỉ gồm chữ số trước conversion.
- Tách validation khỏi decision để output lỗi cụ thể.

## Ba bài tập tương tự có máy tự kiểm (Week 03)

Tham khảo [WORKED-EXAMPLES.md](WORKED-EXAMPLES.md) rồi xem đề
[practice/README.md](practice/README.md). Gợi ý theo ba bước:

- **Lab 01 — Điểm:** kiểm `score_text.isdigit()`; nếu sai hoặc
  `score > 10`, in `Điểm không hợp lệ`. Sắp `>=8` **trước**
  `>=5`. Thử đúng mốc 5, 8 và 10.
- **Lab 02 — Vào cửa:** kiểm input có chỉ chứa `y/n`, rồi tính
  `age_ok = age >= 18`, `has_ticket = ticket_text == "y"`,
  `is_closed = closed_text == "y"`. Kết hợp bằng `and ... not`.
  Không dùng `bool("n")`.
- **Lab 03 — Giao hàng:** kiểm số tiền **nguyên không âm**;
  tạo `free_shipping = (amount >= 200_000) or
  (is_member and amount >= 100_000)`. Phải kiểm miễn phí trước
  phí giao nhanh để không tính phí nhầm.

Chạy `python weeks/week-03-conditionals/practice/checks/check_practice.py
--starter` từ gốc repo; nếu FAIL, đọc input test của từng lab.
**Đừng sửa máy check cho PASS giả.** Sau khi thử xong, mới đối chiếu
`practice/solutions/`.
