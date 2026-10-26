"""Exercise 03: one clear basic inheritance example."""


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name}: woof"


def main() -> None:
    dog = Dog("Milo")
    print(dog.speak())
    # Dog is an Animal because Dog inherits from Animal.


if __name__ == "__main__":
    main()
