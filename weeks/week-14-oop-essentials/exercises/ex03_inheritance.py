"""Bài 3: Animal và Dog minh họa quan hệ kế thừa đơn giản."""


class Animal:
    def __init__(self, name: str):
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name}: woof"


if __name__ == "__main__":
    dog = Dog("Milo")

    print(dog.speak())
    print(isinstance(dog, Animal))