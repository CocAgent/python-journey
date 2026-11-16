# Bài giảng Tuần 14 — Lập trình hướng đối tượng dễ hiểu

## 1. Khi nào nên dùng class?

Khi nhiều dữ liệu thuộc cùng một đối tượng, và có những thao tác liên quan,
`class` giúp gom chúng lại. Ví dụ tiến độ học: `completed`, `total` và
`percentage()`. Với hai giá trị đơn giản, một hàm cũng có thể đủ; **không nhất
thiết mọi bài toán đều cần class**.

| Khái niệm | Ví dụ | Ý nghĩa |
|---|---|---|
| Class (lớp) | `Progress` | Bản thiết kế |
| Object (đối tượng) | `Progress(3, 4)` | Một giá trị cụ thể |
| Attribute (thuộc tính) | `self.completed` | Dữ liệu thuộc đối tượng |
| Method (phương thức) | `percentage()` | Hành vi của đối tượng |
| `self` | `self.total` | Đối tượng đang gọi phương thức |
| `__init__` | `Progress(3, 4)` | Gán giá trị khi khởi tạo |

### Một ví dụ nhỏ

```python
class Progress:
    def __init__(self, completed: int, total: int):
        # Không cho tạo đối tượng có tổng số việc bằng 0 hoặc tiến độ vô lý.
        if total <= 0 or not 0 <= completed <= total:
            raise ValueError("Tiến độ không hợp lệ")
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        return self.completed / self.total * 100


a = Progress(3, 4)
b = Progress(0, 5)
print(a.percentage())  # 75.0
print(b.percentage())  # 0.0
```

`a` và `b` là **hai object độc lập**. Thay `a.completed` không tự làm thay đổi
`b.completed`.

## 2. Trả dữ liệu khác với in ra màn hình

Một phương thức dùng `return` có thể được dùng trong test, trên màn hình,
trong API hoặc khi ghi file. Dùng `print` ngay trong phương thức thì khó tái sử dụng:

```python
def __str__(self) -> str:
    # Python dùng chuỗi này khi chạy print(object).
    return f"Progress: {self.completed}/{self.total}"
```

`__str__` **trả chuỗi**. Bên ngoài có thể gọi `print(a)` để hiển thị. Không
đặt `print()` bên trong `__str__`.

## 3. Bài toán thực tế: quản lý điện thoại

Một `DienThoai` có năm thuộc tính:
`ma_may`, `ten_may`, `hang_san_xuat`, `dung_luong_pin`, `gia_ban`.

```python
iphone = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28_990_000)
samsung = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29_990_000)
print(iphone.thongtindienthoai())
print(samsung.thongtindienthoai())
```

Đây là ví dụ sử dụng class sau khi đã định nghĩa, xem [mã chạy được](examples/04_dien_thoai.py).

**Hỏi:** Vì sao `thongtindienthoai()` nên trả chuỗi thay vì tự in? Vì sao
phải từ chối dung lượng pin không dương và giá âm? Đó là cách suy nghĩ về
**trách nhiệm** và **điều kiện hợp lệ** của object.

## 4. Composition — Bot “có một” chiến lược

Một Bot cần chọn hành động, nhưng không cần tự quyết định mọi thuật toán.
Ta **truyền chiến lược vào Bot** (đây là composition đơn giản):

```python
class Bot:
    def __init__(self, strategy):
        self.strategy = strategy

    def choose_action(self, state):
        return self.strategy(state)


def di_ve_dich(state):
    if state["position"] < state["goal"]:
        return "right"
    if state["position"] > state["goal"]:
        return "left"
    return "wait"


bot = Bot(di_ve_dich)
print(bot.choose_action({"position": 4, "goal": 1}))  # left
```

Khi muốn thay hành vi, ta đổi `bot.strategy`, không cần sửa class `Bot`.

Bản tham chiếu có ba tên chiến lược:
- `defensive`: đứng yên nếu đối thủ ở gần (khoảng cách tối đa một ô);
- `balanced`: hướng về mục tiêu;
- `aggressive`: **trong mô hình một chiều của bài này cũng hướng về mục tiêu**.
  Tên gọi không chứng minh đã có chiến lược tấn công mạnh hơn.

Tất cả cần đúng khi `goal=0`, `goal=4` và khi đã đứng ở đích.
**Không hard-code `"right"`** cho mọi đầu vào.

## 5. Kế thừa — Dog “là một” Animal

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def speak(self):
        return f"{self.name}: woof"


dog = Dog("Milo")
assert isinstance(dog, Animal)
```

`Dog` kế thừa tên từ `Animal` và bổ sung hành vi `speak`.
Bot “có một strategy” **không có nghĩa** Bot “là một strategy”.
Vì vậy dùng composition tốt hơn trong ví dụ Bot.

**Không cần học:** multiple inheritance, MRO, design pattern, metaclass
hoặc cấu trúc OOP nhiều tầng.

## 6. Khi code có nhiều file

Tuần 13 đã học chia module. Xem [ví dụ Bot hai module](examples/oop_team/README.md)
để hiểu `bot.py` sử dụng chiến lược từ `strategies.py` mà không phải sao chép
mã hoặc sửa arena thật. Kiểm thử cần xác nhận **hành vi qua ranh giới module**,
không chỉ kiểm tra rằng một phương thức tồn tại.

## 7. Kiểm thử những gì?

| Trường hợp | Kết quả mong đợi |
|---|---|
| `Progress(3, 4)` | 75%, chuỗi dễ đọc |
| `Progress(0, 0)` | `ValueError` |
| `Progress(5, 4)` | `ValueError` |
| Bot ở vị trí 4, đích 1 | Đi `"left"` |
| Bot tại đích | `"wait"` |
| Defensive gặp đối thủ sát bên | `"wait"` |
| `Dog("Milo")` | `isinstance(dog, Animal)` là `True` |
| Điện thoại có pin 0 hoặc giá âm | `ValueError` |

Chạy [bài test sinh viên](checks/README.md) để biết code của **bạn** đã đúng
chưa. Kết quả của `solutions/` chỉ đánh giá tài liệu tham chiếu.

## 8. Tự học với AI

Thay vì hỏi “viết luôn cả class”, hãy thử:

> Tôi đang làm lớp DienThoai. Hãy gợi ý ba dữ liệu đầu vào dễ gây lỗi,
> giải thích vì sao cần test, nhưng đừng cung cấp toàn bộ lời giải.

Sau đó tự viết, tự chạy test và diễn giải vì sao một điều kiện kiểm tra tồn tại.
