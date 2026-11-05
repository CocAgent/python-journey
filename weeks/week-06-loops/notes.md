# Week 06 — Iteration

## 1. `for` và `range`

```python
for number in range(1, 4):
    print(number)
```

`range(start, stop, step)` không gồm `stop`. Dùng `for` khi lặp qua một
iterable hoặc số lượt đã biết.

## 2. `while` và điều kiện dừng

```python
remaining = 3
while remaining > 0:
    print(remaining)
    remaining -= 1
```

Trước khi chạy, xác định biến nào làm điều kiện trở thành `False`.

## 3. `break` và `continue`

- `break` kết thúc loop hiện tại.
- `continue` bỏ qua phần còn lại của lượt hiện tại.

Giữ nhánh điều khiển ngắn để người đọc thấy luồng chạy.

## 4. `enumerate`

```python
topics = ["loops", "enumerate", "zip"]
for position, topic in enumerate(topics, start=1):
    print(position, topic)
```

Dùng `enumerate` khi cần cả vị trí và giá trị.

## 5. `zip`

```python
names = ["An", "Bình"]
scores = [8, 9]
for name, score in zip(names, scores, strict=True):
    print(name, score)
```

`strict=True` giúp phát hiện hai collection lệch độ dài trên Python 3.12+.

## 6. Comprehension đơn giản

```python
squares = [number**2 for number in range(1, 6)]
even_squares = [number**2 for number in range(1, 6) if number % 2 == 0]
```

Nếu cần nhiều nhánh, side effect hoặc comprehension lồng khó đọc, dùng loop
thường. Learner clarity quan trọng hơn việc rút ngắn code.

## 7. Quan sát vòng lặp qua ba ví dụ có giải thích

[WORKED-EXAMPLES.md](WORKED-EXAMPLES.md) có bảng dự đoán trước khi
chạy, trace các lượt lặp và trường hợp dữ liệu sai. Đặc biệt:

- `continue` chỉ bỏ lượt hiện tại; `break` kết thúc vòng lặp.
- Với `while`, cần biết rõ biến nào làm điều kiện dừng thay đổi.
- `zip(..., strict=True)` báo `ValueError` **khi iterator được
  duyệt tới phần không khớp**; không phải ngay lúc tạo `zip`.
- Comprehension dùng cho một phép biến đổi/lọc ngắn, không ép
  các nhánh phức tạp vào một dòng.

Sau khi xem ví dụ, làm [ba lab tương tự](practice/README.md)
và chạy `--starter` để kiểm code tự viết. `--solutions`
chỉ kiểm lời giải tham khảo.

Không dùng các bài này để yêu cầu học hàm (Week 07) hay
test pytest (Week 12) sớm.
