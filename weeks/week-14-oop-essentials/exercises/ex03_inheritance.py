"""Bài 3: kế thừa cơ bản qua quan hệ Dog là một Animal."""


class Animal:
    """Lớp cha lưu thông tin chung của động vật."""

    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):
    """Dog kế thừa thuộc tính name từ Animal."""

    def speak(self) -> str:
        return f"{self.name}: woof"


# Dog là một Animal vì mọi Dog đều có các đặc điểm cơ bản của Animal.
# Không nên dùng kế thừa nếu quan hệ giữa hai lớp không phải "là một".
