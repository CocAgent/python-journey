# Week 14 — OOP essentials

## 1. Class, object và responsibility

Class mô tả cấu trúc; object là một instance. __init__ gán instance attributes,
method dùng self để làm việc với object hiện tại.

    class Progress:
        def __init__(self, completed: int, total: int):
            self.completed = completed
            self.total = total

        def percentage(self) -> float:
            return self.completed / self.total * 100

Progress chịu trách nhiệm cho dữ liệu và phép tính tiến độ liên quan.

## 2. Composition

Composition nghĩa là một object nhận hoặc chứa collaborator khác.

    class Bot:
        def __init__(self, strategy):
            self.strategy = strategy

        def choose_action(self, state):
            return self.strategy(state)

Thay strategy không cần sửa Bot hay arena. Đây là thiết kế chính cho milestone.

## 3. Strategy swap

defensive, balanced và aggressive đều tuân theo course-local action contract.
Chúng có thể là function nhỏ; không cần hierarchy.

## 4. Basic inheritance

Inheritance phù hợp khi quan hệ “is-a” rõ và thật sự giảm lặp:

    class Animal:
        def __init__(self, name):
            self.name = name

    class Dog(Animal):
        def speak(self):
            return f"{self.name}: woof"

Không dùng inheritance chỉ để chia sẻ vài dòng code. Tuần này không học multiple
inheritance, MRO, metaclass, descriptor hay abstract framework architecture.
