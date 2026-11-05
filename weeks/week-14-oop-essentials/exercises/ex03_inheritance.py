"""Bài 3 — Lời giải: Animal và Dog."""


class Animal:
    def __init__(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Tên động vật không được để trống")
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name}: woof"


# Dog là một Animal nên có thể kế thừa thuộc tính name từ Animal.
# Không nên kế thừa nếu quan hệ giữa hai lớp chỉ là "có một".
