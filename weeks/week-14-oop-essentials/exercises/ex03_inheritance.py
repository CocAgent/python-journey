"""Exercise 03: one clear basic inheritance example."""


class Animal:
    """Base class for animals."""

    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):
    """A dog is an animal and inherits its name attribute."""

    def speak(self) -> str:
        return f"{self.name} says woof!"


def main() -> None:
    dog = Dog("Milo")
    print(dog.speak())
    print("Dog is an Animal because Dog inherits the shared animal attributes.")


if __name__ == "__main__":
    main()
