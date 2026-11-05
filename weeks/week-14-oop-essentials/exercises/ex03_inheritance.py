"""Bài 3: Animal và Dog minh họa quan hệ kế thừa đơn giản."""


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        # Dog kế thừa thuộc tính name từ Animal.
        return f"{self.name}: woof"


# Dog là một Animal vì chó là một loại động vật.
# Kế thừa không cần thiết khi hai lớp không có quan hệ "là một"
# hoặc khi chỉ muốn tái sử dụng một vài hành vi không cùng bản chất.
