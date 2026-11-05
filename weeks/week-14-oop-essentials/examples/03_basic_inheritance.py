"""Ví dụ 3: chỉ dùng kế thừa cho quan hệ 'là một' rõ ràng."""


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        """Dog thừa hưởng tên từ Animal và bổ sung hành vi riêng."""
        return f"{self.name}: woof"


if __name__ == "__main__":
    dog = Dog("Milo")
    print(dog.speak())
    print(isinstance(dog, Animal))  # True: Dog là một Animal
