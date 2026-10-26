# Week 14 — OOP Essentials · Composition · Basic Inheritance

## 1. Mục tiêu của Week 14

Week 14 tập trung vào nền tảng OOP (Object-Oriented Programming) trong Python:

- Class và Object.
- Constructor `__init__()`.
- Instance attributes và methods.
- `self`.
- Type hints cơ bản.
- `__str__()`.
- Kiểm tra dữ liệu và `raise ValueError`.
- Encapsulation theo trách nhiệm của object.
- Composition.
- Strategy Pattern đơn giản bằng function/object.
- Basic inheritance.
- Phân biệt quan hệ **has-a** và **is-a**.
- Biết khi nào nên dùng Composition và khi nào nên dùng Inheritance.

Thứ tự học:

```text
Class / Object
      ↓
__init__ / self / attributes / methods
      ↓
__str__ / validation
      ↓
Composition
      ↓
Strategy Composition
      ↓
Basic Inheritance
```

---

# 2. Class và Object

## Class là gì?

`class` là khuôn mẫu dùng để tạo ra các object.

```python
class Progress:
    pass
```

## Object là gì?

Object là một instance được tạo từ class.

```python
progress = Progress()
```

Có thể hình dung:

```text
Class:  Progress
   ↓
Object: progress
```

Một class có thể tạo ra nhiều object khác nhau:

```python
progress1 = Progress()
progress2 = Progress()
progress3 = Progress()
```

---

# 3. `__init__()` và `self`

`__init__()` là constructor, được gọi tự động khi tạo object.

```python
class Progress:
    def __init__(self, completed: int, total: int):
        self.completed = completed
        self.total = total
```

Tạo object:

```python
progress = Progress(3, 4)
```

Khi đó:

```text
progress.completed = 3
progress.total = 4
```

## `self` là gì?

`self` đại diện cho object hiện tại.

```python
self.completed = completed
```

Có thể hiểu là:

```text
object.completed = giá trị completed được truyền vào
```

`self` phải được đặt ở tham số đầu tiên của instance method.

---

# 4. Instance Attributes

Instance attribute là dữ liệu thuộc về từng object.

```python
class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
```

Ví dụ:

```python
student1 = Student("Duc", 20)
student2 = Student("An", 19)
```

Hai object có dữ liệu riêng:

```text
student1
├── name = "Duc"
└── age = 20

student2
├── name = "An"
└── age = 19
```

---

# 5. Methods

Method là function nằm bên trong class và thường thao tác với object thông qua `self`.

```python
class Progress:
    def __init__(self, completed: int, total: int):
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        return self.completed / self.total * 100
```

Gọi method:

```python
progress = Progress(3, 4)
print(progress.percentage())
```

Kết quả:

```text
75.0
```

---

# 6. Type Hints

Type hint giúp code dễ đọc và dễ kiểm tra hơn.

```python
def percentage(self) -> float:
```

`-> float` cho biết function dự kiến trả về `float`.

Ví dụ:

```python
completed: int
total: int
name: str
```

Type hint không tự động biến dữ liệu thành kiểu đó; nó chủ yếu mô tả kiểu dữ liệu dự kiến.

---

# 7. Validation và `raise ValueError`

Có thể kiểm tra dữ liệu ngay khi tạo object:

```python
class Progress:
    def __init__(self, completed: int, total: int):
        if total < 1:
            raise ValueError("total must be positive")

        self.completed = completed
        self.total = total
```

Nếu:

```python
Progress(3, 0)
```

chương trình sẽ báo:

```text
ValueError: total must be positive
```

Mục đích là ngăn object rơi vào trạng thái dữ liệu không hợp lệ.

---

# 8. `__str__()`

`__str__()` quyết định cách object được biểu diễn thành chuỗi khi dùng `print()`.

```python
class Progress:
    def __str__(self) -> str:
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.0f}%)"
```

Ví dụ:

```python
progress = Progress(3, 4)
print(progress)
```

Kết quả:

```text
Progress: 3/4 (75%)
```

Thay vì phải viết:

```python
print(progress.completed, progress.total)
```

object tự định nghĩa cách hiển thị của nó.

---

# 9. Encapsulation theo trách nhiệm

Trong Week 14, encapsulation được hiểu ở mức thiết kế: dữ liệu và hành vi liên quan nên được đặt cùng object.

Ví dụ `Progress` chịu trách nhiệm cho:

```text
completed
 total
 percentage()
 __str__()
```

Thay vì để nhiều function bên ngoài cùng xử lý dữ liệu tiến độ, object `Progress` tự quản lý những hành vi liên quan đến tiến độ.

Nguyên tắc đơn giản:

> Một object nên có trách nhiệm rõ ràng và dữ liệu liên quan đến trách nhiệm đó.

---

# 10. Composition

Composition là khi một object **có hoặc nhận một object/function khác để cộng tác**.

Có thể nhớ bằng quan hệ:

```text
has-a
```

Ví dụ:

```python
class Bot:
    def __init__(self, strategy):
        self.strategy = strategy

    def choose_action(self, state):
        return self.strategy(state)
```

`Bot` có một `strategy`.

```text
Bot
└── strategy
```

Đây là Composition.

---

# 11. Strategy Composition

Strategy là cách tách phần **quyết định hành động** ra khỏi class `Bot`.

Ví dụ:

```python
def defensive(state):
    ...


def balanced(state):
    ...


def aggressive(state):
    ...
```

Sau đó truyền strategy vào `Bot`:

```python
Bot(defensive)
Bot(balanced)
Bot(aggressive)
```

Class `Bot` không cần biết chi tiết strategy hoạt động như thế nào.

```python
class Bot:
    def __init__(self, strategy):
        self.strategy = strategy

    def choose_action(self, state):
        return self.strategy(state)
```

Khi gọi:

```python
bot.choose_action(state)
```

Bot sẽ gọi strategy đang được lưu trong `self.strategy`.

---

# 12. Strategy có thể thay đổi

Ví dụ:

```python
state = {
    "position": 1,
    "opponent_position": 4,
    "goal": 4,
}

bots = [
    Bot(defensive),
    Bot(balanced),
    Bot(aggressive),
]
```

Ta có thể thay strategy mà không cần sửa class `Bot`.

Đây là ưu điểm lớn của Composition:

```text
Bot + defensive
Bot + balanced
Bot + aggressive
```

cùng dùng một `Bot` nhưng có hành vi khác nhau.

---

# 13. Movement Strategy

Một strategy di chuyển về phía goal có thể viết:

```python
def move_toward_goal(state):
    if state["position"] < state["goal"]:
        return "right"
    if state["position"] > state["goal"]:
        return "left"
    return "wait"
```

Điểm quan trọng: không hard-code chỉ `"right"`.

Nếu:

```python
position = 1
goal = 4
```

→ `right`.

Nếu:

```python
position = 3
goal = 0
```

→ `left`.

Nếu:

```python
position = 4
goal = 4
```

→ `wait`.

---

# 14. Defensive / Balanced / Aggressive

Ba strategy trong Week 14 có thể là function nhỏ.

## Defensive

Defensive ưu tiên chờ nếu đối thủ ở rất gần:

```python
def defensive(state):
    opponent = state.get("opponent_position")

    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"

    return move_toward_goal(state)
```

## Balanced

Balanced đi về phía goal:

```python
def balanced(state):
    return move_toward_goal(state)
```

## Aggressive

Trong exercise của Week 14, aggressive cũng đi về phía goal:

```python
def aggressive(state):
    return move_toward_goal(state)
```

Điểm cần nhớ: Week 14 đang tập trung vào **cách truyền và thay strategy**, không phải xây dựng một AI chiến đấu phức tạp.

---

# 15. Kết quả Strategy Composition

State:

```python
state = {
    "position": 1,
    "opponent_position": 4,
    "goal": 4,
}
```

Kết quả:

```text
=== STRATEGY COMPOSITION ===
State: {'position': 1, 'opponent_position': 4, 'goal': 4}
Defensive: right
Balanced: right
Aggressive: right
```

Với state đảo chiều:

```python
reverse_state = {
    "position": 3,
    "opponent_position": 4,
    "goal": 0,
}
```

Kết quả:

```text
Reverse:
Defensive: wait
Balanced: left
Aggressive: left
```

Defensive trả về `wait` vì đối thủ cách bot 1 vị trí.

---

# 16. Basic Inheritance

Inheritance là cơ chế cho phép class con kế thừa từ class cha.

Quan hệ cần nhớ:

```text
is-a
```

Ví dụ:

```python
class Animal:
    def __init__(self, name: str):
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name}: woof"
```

Ở đây:

```text
Animal
   ↑
   │ kế thừa
   │
  Dog
```

Dog **is an Animal**.

---

# 17. Kế thừa constructor

`Dog` không khai báo `__init__()` riêng nên nó sử dụng `__init__()` của `Animal`.

```python
dog = Dog("Milo")
```

Sau đó:

```python
print(dog.name)
```

kết quả:

```text
Milo
```

`Dog` có thể sử dụng attribute `name` được tạo bởi class cha.

---

# 18. Method của class con

`Dog` có thêm method riêng:

```python
class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name}: woof"
```

Gọi:

```python
print(dog.speak())
```

Kết quả:

```text
Milo: woof
```

---

# 19. `isinstance()`

Dùng `isinstance()` để kiểm tra object có thuộc một class hoặc class cha hay không.

```python
print(isinstance(dog, Animal))
```

Kết quả:

```text
True
```

Vì:

```text
Dog kế thừa Animal
Dog là một loại Animal
```

Có thể nhớ:

```text
Dog → is-a → Animal
```

---

# 20. Composition vs Inheritance

## Composition — has-a

```python
class Bot:
    def __init__(self, strategy):
        self.strategy = strategy
```

Bot **has a strategy**.

```text
Bot
└── strategy
```

## Inheritance — is-a

```python
class Dog(Animal):
    pass
```

Dog **is an Animal**.

```text
Animal
   ↑
  Dog
```

### Nguyên tắc của Week 14

> Ưu tiên Composition khi object cần một behavior có thể thay thế.

> Dùng Inheritance khi quan hệ “is-a” rõ ràng và inheritance thực sự giúp mô hình đơn giản hơn.

Không nên dùng inheritance chỉ để chia sẻ vài dòng code.

---

# 21. Những thứ chưa học trong Week 14

Week 14 chỉ tập trung vào OOP cơ bản. Chưa cần học:

- Multiple inheritance.
- MRO (Method Resolution Order).
- Metaclass.
- Descriptor.
- Abstract framework architecture.
- Kiến trúc OOP phức tạp.

Các nội dung này có thể học ở giai đoạn nâng cao hơn.

---

# 22. Tổng hợp kiến thức bằng một ví dụ

```python
from collections.abc import Callable

State = dict[str, int]
Strategy = Callable[[State], str]


class Bot:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def choose_action(self, state: State) -> str:
        return self.strategy(state)


def move_toward_goal(state: State) -> str:
    if state["position"] < state["goal"]:
        return "right"
    if state["position"] > state["goal"]:
        return "left"
    return "wait"


def balanced(state: State) -> str:
    return move_toward_goal(state)


bot = Bot(balanced)

state = {
    "position": 1,
    "opponent_position": 4,
    "goal": 4,
}

print(bot.choose_action(state))
```

Luồng hoạt động:

```text
state
  ↓
Bot(balanced)
  ↓
self.strategy = balanced
  ↓
choose_action(state)
  ↓
balanced(state)
  ↓
move_toward_goal(state)
  ↓
"right"
```

---

# 23. Checklist sau khi hoàn thành Week 14

- [ ] Hiểu class là gì.
- [ ] Hiểu object là gì.
- [ ] Biết tạo `__init__()`.
- [ ] Hiểu `self`.
- [ ] Biết tạo instance attributes.
- [ ] Biết viết methods.
- [ ] Hiểu type hints cơ bản.
- [ ] Biết dùng `raise ValueError` để validation.
- [ ] Biết dùng `__str__()`.
- [ ] Hiểu responsibility của object.
- [ ] Hiểu Composition.
- [ ] Biết truyền function vào object.
- [ ] Biết thay strategy mà không sửa `Bot`.
- [ ] Hiểu `has-a`.
- [ ] Hiểu basic inheritance.
- [ ] Hiểu `is-a`.
- [ ] Biết dùng `isinstance()`.
- [ ] Biết khi nào nên ưu tiên Composition.
- [ ] Biết khi nào Inheritance phù hợp.

---

# 24. Bài tập tự luyện

### Bài 1 — Progress

Tạo class `Progress` có:

- `completed`.
- `total`.
- `percentage()`.
- `__str__()`.
- Kiểm tra `total > 0`.

### Bài 2 — Composition

Tạo class `Bot` nhận một strategy trong `__init__()`.

Tạo 3 strategy:

```text
defensive
balanced
aggressive
```

Sau đó thay đổi strategy mà không sửa class `Bot`.

### Bài 3 — Inheritance

Tạo:

```text
Animal
├── Dog
└── Cat
```

`Animal` chứa `name`.

`Dog` và `Cat` có method `speak()` riêng.

Kiểm tra bằng:

```python
isinstance(dog, Animal)
isinstance(cat, Animal)
```

### Bài 4 — Kết hợp

Tạo một `Bot` có strategy và thêm class `Progress` để theo dõi số lượt hoàn thành.

Mục tiêu là luyện đồng thời:

```text
Class
Object
Method
Composition
Inheritance
```

---

# 25. Cấu trúc Week 14 trong repository

```text
week-14-oop-essentials/
├── README.md
├── notes.md
├── examples/
├── exercises/
├── hints.md
├── checks/
├── solutions/
│   └── oop_models.py
└── mini-project/
    ├── README.md
    └── strategy_composition.py
```

Các phần chính:

- `notes.md`: lý thuyết ngắn gọn.
- `examples/`: ví dụ minh họa.
- `exercises/`: bài tập.
- `hints.md`: gợi ý.
- `checks/`: kiểm tra tự động.
- `solutions/`: lời giải chuẩn.
- `mini-project/`: bài project Strategy Composition.

---

# 26. Kết luận

Week 14 xây dựng nền tảng OOP quan trọng cho các Week tiếp theo.

Cần nhớ 4 ý chính:

```text
1. Class tạo Object.
2. Object gom dữ liệu + hành vi có cùng trách nhiệm.
3. Composition cho phép thay đổi behavior linh hoạt.
4. Inheritance dùng cho quan hệ is-a rõ ràng.
```

Đặc biệt:

```text
Composition → has-a → Bot có strategy
Inheritance → is-a  → Dog là Animal
```

Nếu nắm chắc hai ý này, bạn đã có nền tảng tốt để tiếp tục học OOP nâng cao.
