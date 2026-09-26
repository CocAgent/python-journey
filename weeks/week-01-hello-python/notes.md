# Tuần 01 — Python fundamentals và chương trình đầu tiên

> **Python Journey** · Python >= 3.12 · Học qua chạy, quan sát và sửa lỗi

Phần cài đặt thuộc [`SETUP.md`](../../SETUP.md). Bản đồ công cụ thuộc
[`lesson-01-python-ecosystem-and-environment.md`](lesson-01-python-ecosystem-and-environment.md).

## Mục tiêu

Sau phần fundamentals, bạn có thể:

- dùng Python REPL để thử biểu thức;
- tạo và chạy file `.py` từ terminal;
- hiển thị dữ liệu bằng `print()`;
- dùng các phép toán số học cơ bản;
- viết comment có ích;
- phân biệt code, output và traceback;
- đọc ba lỗi đầu tiên: `SyntaxError`, `NameError` và `IndentationError`.

## 1. Code Python được chạy như thế nào?

File Python là source code dạng văn bản:

```python
print("Hello, Python Journey!")
```

Interpreter đọc file và thực hiện từng lệnh:

```text
source code
    ↓
Python interpreter
    ↓
output hoặc traceback
```

Trong Week 01, bạn làm việc theo vòng ngắn:

```text
Viết → Chạy → Quan sát → Sửa → Chạy lại
```

## 2. Python REPL

REPL là môi trường tương tác:

```text
Read → Eval → Print → Loop
```

Mở REPL bằng command Python hoạt động trên máy:

```bash
python
```

Trên Windows có thể là:

```powershell
py
```

Trên macOS/Linux thường là:

```bash
python3
```

Dấu nhắc `>>>` cho biết Python đang chờ một biểu thức hoặc lệnh:

```python
>>> 2 + 3
5
>>> 10 * 4
40
>>> "Py" + "thon"
'Python'
```

Thoát REPL:

```python
>>> exit()
```

### Khi nào dùng REPL?

Dùng REPL để:

- thử một biểu thức nhỏ;
- kiểm tra kết quả phép tính;
- quan sát kiểu hoặc giá trị;
- khám phá nhanh một hàm.

Dùng file `.py` khi muốn lưu, chạy lại, review và commit chương trình.

## 3. Chương trình đầu tiên

Tạo file `hello.py`:

```python
print("Xin chào thế giới!")
print("Tôi đang học Python.")
print("Week 01 — bắt đầu hành trình!")
```

Chạy từ terminal:

```bash
python hello.py
```

Dùng `py hello.py` trên Windows hoặc `python3 hello.py` trên macOS/Linux nếu
đó là command Python đã được bạn xác nhận trong setup.

Kết quả:

```text
Xin chào thế giới!
Tôi đang học Python.
Week 01 — bắt đầu hành trình!
```

Ba thành phần cần phân biệt:

- **code** nằm trong `hello.py`;
- **command** yêu cầu interpreter chạy file;
- **output** là nội dung chương trình hiển thị.

## 4. Hàm `print()`

`print()` yêu cầu Python hiển thị giá trị ra standard output.

### In văn bản và số

```python
print("Xin chào!")
print(42)
print(3.14)
```

Văn bản cần đặt trong dấu nháy. Số không cần dấu nháy.

### In nhiều giá trị

```python
name = "An"
age = 18

print("Tên:", name)
print("Tuổi:", age)
```

`print()` tự thêm khoảng trắng giữa các đối số.

### `sep` và `end`

```python
print("Python", "Journey", sep="-")
print("Dòng một", end=" | ")
print("vẫn cùng dòng")
```

Kết quả:

```text
Python-Journey
Dòng một | vẫn cùng dòng
```

### In dòng trống

```python
print("Phần 1")
print()
print("Phần 2")
```

## 5. Python như một máy tính

Các toán tử số học cơ bản:

| Toán tử | Ý nghĩa | Ví dụ | Kết quả |
|---|---|---|---|
| `+` | cộng | `2 + 3` | `5` |
| `-` | trừ | `10 - 4` | `6` |
| `*` | nhân | `3 * 7` | `21` |
| `/` | chia | `20 / 4` | `5.0` |
| `//` | chia lấy phần nguyên | `17 // 5` | `3` |
| `%` | chia lấy dư | `17 % 5` | `2` |
| `**` | lũy thừa | `2 ** 10` | `1024` |

Thứ tự ưu tiên giống toán học:

```python
print(2 + 3 * 4)      # 14
print((2 + 3) * 4)    # 20
```

Dùng ngoặc khi muốn ý định rõ ràng.

### Biểu thức và câu lệnh

Biểu thức tạo ra một giá trị:

```python
2 + 3
"Py" + "thon"
```

Lệnh yêu cầu Python làm một việc:

```python
print(2 + 3)
```

Trong REPL, giá trị biểu thức được hiển thị tự động. Trong file `.py`, hãy dùng
`print()` nếu muốn thấy giá trị.

## 6. Comment

Comment một dòng bắt đầu bằng `#`:

```python
# Tính diện tích sàn
length = 8
width = 5
print(length * width)  # đơn vị: mét vuông
```

Comment tốt giải thích ý định hoặc lý do. Không cần lặp lại điều code đã nói:

```python
# Không hữu ích: cộng 2 và 3
print(2 + 3)
```

Chuỗi ba dấu nháy là string literal, thường dùng cho docstring; nó không phải
cú pháp comment nhiều dòng:

```python
def greet():
    """Trả về lời chào mặc định."""
    return "Xin chào!"
```

Ở Week 01, ưu tiên comment `#` ngắn và rõ.

## 7. Đọc lỗi đầu tiên

Khi chương trình thất bại, Python thường cho biết:

1. file và dòng gây lỗi;
2. dòng code liên quan;
3. loại lỗi;
4. mô tả ngắn.

Đừng chỉ đọc dòng đầu. Hãy bắt đầu từ loại lỗi và dòng cuối của traceback.

### `SyntaxError` — code sai cú pháp

```python
print("Xin chào)
```

Dấu nháy chưa được đóng. Sửa:

```python
print("Xin chào")
```

### `NameError` — tên chưa tồn tại

```python
Print("Xin chào")
```

Python phân biệt chữ hoa và chữ thường. Tên đúng là:

```python
print("Xin chào")
```

### `IndentationError` — thụt lề không hợp lệ

```python
    print("Xin chào")
```

Ở cấp đầu file, bỏ phần thụt lề không có lý do:

```python
print("Xin chào")
```

### Vòng debug nhập môn

```text
Reproduce → Đọc lỗi → Xác định dòng → Sửa một việc → Chạy lại
```

Một lần chạy lỗi không phải thất bại học tập. Traceback là dữ liệu giúp bạn tìm
nguyên nhân.

## 8. Bài luyện tập ngắn

### Bài 1 — Tự giới thiệu

In bốn dòng:

```text
Tên: ...
Thành phố: ...
Mục tiêu học Python: ...
Công cụ đang dùng: ...
```

### Bài 2 — Tính toán

Tính và in:

- tổng của 123 và 456;
- tích của 17 và 38;
- 2 mũ 8;
- phần dư của 100 chia 7.

### Bài 3 — Hình chữ nhật

Một phòng dài 8 m, rộng 5 m, cao 3 m. Tính:

- diện tích sàn;
- chu vi sàn;
- diện tích bốn bức tường;
- thể tích phòng.

### Bài 4 — ASCII art

Dùng nhiều lệnh `print()` để vẽ một hình đơn giản:

```text
    *
   ***
  *****
 *******
   |||
   |||
```

## 9. Bài tập và mini-project của repository

Bài tập có starter:

- [`ex01_hello.py`](exercises/ex01_hello.py);
- [`ex02_calculator.py`](exercises/ex02_calculator.py);
- [`ex03_input.py`](exercises/ex03_input.py).

Hãy tự làm trước khi xem [`solutions/`](solutions/).

Mini-project:
[`ASCII Art Generator`](mini-project/README.md).

## 10. Tự kiểm tra

Trước khi kết thúc Week 01, hãy tự trả lời:

- REPL khác file `.py` như thế nào?
- `print()` nhận một hay nhiều giá trị?
- `/` khác `//` như thế nào?
- `%` trả về gì?
- Vì sao string cần dấu nháy?
- Comment tốt nên giải thích điều gì?
- Ba thông tin nào trong traceback giúp tìm lỗi?

## Điều quan trọng nhất

1. **Chạy code thường xuyên.** Đừng viết quá nhiều trước lần chạy đầu tiên.
2. **Quan sát output.** Kết quả là bằng chứng, không phải cảm giác.
3. **Đọc traceback.** Loại lỗi và dòng lỗi thường chỉ đường sửa.
4. **Giữ code đơn giản.** Week 01 ưu tiên hiểu rõ hơn kỹ thuật phức tạp.
5. **Commit tiến độ.** Git history ghi lại quá trình học, không chỉ kết quả cuối.
