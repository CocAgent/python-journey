# Mini-project — Personal Utility Toolkit

Xây một chương trình nhỏ xử lý hóa đơn và đánh giá kết quả học tập. Mục tiêu
chính là luyện **decomposition**: mỗi bước của bài toán thuộc về một function
có contract rõ.

## Yêu cầu

Hoàn thành [`starter.py`](starter.py) theo năm function gợi ý sau:

1. `calculate_subtotal(price, quantity)` tính tạm tính;
2. `calculate_discount(subtotal, percent=0)` tính tiền giảm;
3. `calculate_average(scores)` tính điểm trung bình;
4. `classify_score(average)` phân loại kết quả;
5. `format_currency(amount)` định dạng số tiền.

Luồng `main()` phải dùng output của ít nhất một function làm input cho function
khác. Ví dụ:

```text
price + quantity → subtotal → discount → final total → formatted output
```

## Constraints

- Có ít nhất 4 functions nhỏ theo constraints hiện hành; starter đề xuất đủ 5 functions như danh sách trên.
- Có basic type hints cho parameters và return values.
- Không dùng global state không cần thiết.
- Mỗi function làm một việc.
- Có main flow rõ ràng và output quan sát được.
- Type hints mô tả ý định; chúng không tự validate input lúc runtime.

## Cách làm

1. Viết từng function và thử với một normal case.
2. Thử `quantity = 0` và một list điểm rỗng.
3. Ghép các function trong `main()`.
4. Chạy lại sau mỗi lần sửa.

```bash
python weeks/week-07-functions/mini-project/starter.py
```

Nếu bị kẹt, xem phần mini-project trong [`../hints.md`](../hints.md). Không có
full solution để bạn tự thiết kế luồng cuối cùng.

## Evidence

- Chụp hoặc lưu output của một lần chạy thành công.
- Ghi lại một bug và cách bạn tìm ra bước gây lỗi.
- Commit với message, ví dụ: `feat: complete week 07 utility toolkit`.

## Bài đệm trước khi tự thiết kế Toolkit

Nếu còn nhầm `return` với `print` hoặc chưa biết chia
hóa đơn thành nhiều hàm nhỏ, hãy làm
[Ví dụ 06–08](../WORKED-EXAMPLES.md) và
[Lab 01–04](../practice/README.md). Bộ lab tự kiểm
`return` và decomposition trực tiếp, không chỉ đọc
dòng kết quả in trên terminal.

Mốc 4 hàm trong constraints là mức tối thiểu hiện có;
5 hàm là phương án thiết kế gợi ý cho starter. Không
thay rubric hoặc tăng điều kiện hoàn thành dự án.
