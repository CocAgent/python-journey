"""Use inheritance for a clear is-a relationship."""


class Animal:
    def __init__(self, name: str):
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name}: woof"


print(Dog("Milo").speak())
