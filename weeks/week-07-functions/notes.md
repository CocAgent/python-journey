# Week 07 — Functions

Functions không chỉ là cú pháp `def`. Một function đặt tên cho một công việc,
nhận input và tạo output để ta có thể hiểu, dùng lại và kiểm tra từng phần của
chương trình.

## 1. Vì sao cần function?

Code lặp lại khó sửa vì một thay đổi phải được thực hiện ở nhiều nơi:

```python
print("Xin chào An")
print("Xin chào Bình")
```

Đưa logic lặp vào function giúp ta chỉ cần định nghĩa hành vi một lần:

```python
def greet(name: str) -> str:
    return f"Xin chào {name}"


print(greet("An"))
print(greet("Bình"))
```

## 2. Định nghĩa và gọi function

```python
def greet(name: str) -> str:
    """Tạo lời chào cho một người."""
    return f"Xin chào {name}"


message = greet("An")
```

- `name` trong phần định nghĩa là **parameter**.
- `"An"` trong lời gọi là **argument**.
- Docstring ngắn mô tả contract khi tên hàm chưa nói đủ ý.

## 3. `return` khác `print`

```text
print  = hiển thị dữ liệu cho người dùng
return = trả dữ liệu về caller
```

Một hàm chỉ `print` kết quả khó ghép vào bước tiếp theo:

```python
def show_total(price: float, quantity: int) -> None:
    print(price * quantity)
```

Một hàm `return` kết quả cho phép caller tiếp tục tính toán hoặc kiểm tra:

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


total = calculate_total(25_000, 2)
print(f"Tổng: {total:,.0f} đ")
```

## 4. Parameter, argument và default parameter

```python
def build_greeting(name: str, prefix: str = "Xin chào") -> str:
    return f"{prefix} {name}"


print(build_greeting("An"))
print(build_greeting("Bình", "Chào buổi sáng"))
```

Default parameter phù hợp khi có một lựa chọn phổ biến và rõ nghĩa. Đừng thêm
quá nhiều default chỉ để tránh suy nghĩ về contract của hàm.

## 5. Decomposition — chia bài toán thành các bước nhỏ

Một chương trình tính hóa đơn có thể được chia theo luồng:

```text
input → validate → calculate → format → output
```

```python
def is_valid_quantity(quantity: int) -> bool:
    return quantity > 0


def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


def format_total(total: float) -> str:
    return f"{total:,.0f} đ"
```

Mỗi hàm có một trách nhiệm. Khi kết quả sai, ta có thể kiểm tra từng bước thay
vì đoán lỗi trong một khối code lớn.

## 6. Scope

Biến được tạo trong hàm có **local scope** và chỉ tồn tại trong hàm đó:

```python
def add_tax(subtotal: float) -> float:
    tax = subtotal * 0.1
    return subtotal + tax
```

`tax` là biến local. Caller chỉ nhận giá trị được `return`.

Global state có thể khiến kết quả phụ thuộc vào thứ tự chạy và khó debug. Thay
vì sửa một biến global, hãy truyền dữ liệu qua parameter và nhận kết quả qua
`return`.

## 7. Type hints cơ bản

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
```

Type hints giúp người đọc và công cụ hiểu **ý định** của hàm. Chúng cũng đóng
vai trò như một phần của contract và tài liệu.

> Type hints help humans and tools understand intent. Python does not
> automatically enforce these annotations at runtime.

Python vẫn là ngôn ngữ dynamic: annotation không tự ép kiểu và không tự
validate input. Nếu chương trình cần validation, ta phải viết logic validation
riêng.

## 8. Decision function — cây cầu nhỏ tới agent

Một agent đơn giản có thể được nhìn như một decision function:

```text
state → choose_action(state) → action
```

```python
def choose_action(state: str) -> str:
    if state == "danger":
        return "defend"
    if state == "opportunity":
        return "advance"
    return "wait"
```

```text
TEACHING MODEL
NOT VUACOC PRODUCTION CONTRACT
```

Ví dụ chỉ minh họa input → decision → output. Nó không mô tả state, action,
API hay runtime chính thức của VuaCóc.

## 9. Cách luyện tập

Với mỗi bài:

1. đọc contract và ví dụ;
2. viết phiên bản nhỏ nhất chạy được;
3. thử normal case và boundary case;
4. đọc lỗi, xác định bước sai và sửa;
5. chạy lại rồi commit bằng chứng.
