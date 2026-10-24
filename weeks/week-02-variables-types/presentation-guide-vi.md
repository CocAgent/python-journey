# Week 02 — Bản giải thích ngắn gọn để trình bày

## 1. Tuần này học gì?

Week 02 học cách lưu dữ liệu bằng biến, nhận biết kiểu dữ liệu, nhập dữ liệu từ người dùng, chuyển kiểu và hiển thị kết quả.

## 2. Các khái niệm chính

- **Biến (variable):** tên dùng để tham chiếu đến một giá trị, ví dụ `name = "An"`.
- **`int`:** số nguyên, ví dụ `18`.
- **`float`:** số thập phân, ví dụ `8.5`.
- **`str`:** chuỗi ký tự, ví dụ `"Python"`.
- **`bool`:** giá trị đúng hoặc sai, `True` hoặc `False`.
- **`input()`:** nhận dữ liệu người dùng nhập; kết quả luôn là chuỗi (`str`).
- **Chuyển kiểu:** dùng `int()`, `float()` để chuyển dữ liệu khi phù hợp.
- **f-string:** chèn biến vào chuỗi để in kết quả rõ ràng.

## 3. Ví dụ đơn giản

```python
name = input("Nhập tên: ")
age_text = input("Nhập tuổi: ")
age = int(age_text)

print(f"Xin chào {name}, bạn {age} tuổi.")
```

Ví dụ nhập tên `An` và tuổi `18`, chương trình sẽ in:

```text
Xin chào An, bạn 18 tuổi.
```

Lưu ý: nếu nhập chữ vào ô tuổi, `int(age_text)` có thể gây `ValueError`. Tuần 11 sẽ học cách xử lý lỗi này rõ ràng hơn.

## 4. Điểm dễ nhầm

`input()` trả về chuỗi, kể cả khi người dùng nhập `18`. Vì vậy cần dùng `int()` trước khi muốn tính toán số học.

Ví dụ:

```python
number = input("Nhập số: ")
print(number + "2")  # nối chuỗi
print(int(number) + 2)  # cộng số
```

Nếu nhập `3`, hai kết quả lần lượt là `32` và `5`.

## 5. Bài nói ngắn trước thầy

> Thưa thầy, Week 02 giúp em hiểu cách lưu dữ liệu bằng biến và phân biệt các kiểu như int, float, str, bool. Em học cách dùng input để nhận dữ liệu, chuyển kiểu bằng int hoặc float khi cần tính toán, và dùng f-string để hiển thị kết quả dễ đọc. Điểm quan trọng là input luôn trả về chuỗi nên em phải chuyển kiểu trước khi thực hiện phép tính số học.

## 6. Em cần nhớ

**Nhập dữ liệu → kiểm tra/chuyển kiểu → xử lý → in kết quả.**

Tài liệu này bổ sung phần giải thích bằng tiếng Việt; không thay thế bài học, bài tập hoặc file code gốc của Week 02.
