"""Lời giải bài 3: kế thừa đơn giản Animal -> Dog."""


class Animal:
    def __init__(self, name: str) -> None:
        if not name.strip():
            raise ValueError("name không được để trống")
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name}: woof"
