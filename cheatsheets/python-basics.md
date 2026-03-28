# Python Basics Cheat Sheet

## Kiểu dữ liệu
| Kiểu | Ví dụ | Mô tả |
|------|-------|-------|
| `int` | `42` | Số nguyên |
| `float` | `3.14` | Số thập phân |
| `str` | `"hello"` | Chuỗi |
| `bool` | `True` | Đúng/Sai |
| `list` | `[1,2,3]` | Danh sách |
| `dict` | `{"a":1}` | Từ điển |

## Input / Output
```python
name = input("Tên: ")
age = int(input("Tuổi: "))
print(f"Xin chào {name}, {age} tuổi!")
print(f"{3.14159:.2f}")       # 3.14
print(f"{1000000:,}")         # 1,000,000
```

## Toán tử: `+` `-` `*` `/` `//` `%` `**`
## So sánh: `==` `!=` `>` `<` `>=` `<=`
## Logic: `and` `or` `not`

## Điều kiện
```python
if x > 0:
    print("Dương")
elif x == 0:
    print("Zero")
else:
    print("Âm")
```

## Vòng lặp
```python
for i in range(5):        # 0..4
for item in my_list:      # duyệt list
while condition:          # lặp theo dk
```

## Hàm
```python
def greet(name, lang="vi"):
    return f"Xin chào {name}!"
```

## Try/Except
```python
try:
    risky_code()
except ValueError:
    handle_error()
```
