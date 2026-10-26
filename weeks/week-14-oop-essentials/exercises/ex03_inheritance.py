"""Exercise 03: one clear basic inheritance example."""


class Animal:
    """Base class for animals."""

    def __init__(self, name: str):
        self.name = name


class Dog(Animal):
    """A dog is an animal and can make a dog sound."""

    def speak(self) -> str:
        return f"{self.name}: woof"


if __name__ == "__main__":
    dog = Dog("Milo")
    print(dog.speak())
    # Dog is an Animal because Dog inherits the shared name attribute
    # and behavior of the Animal base class.
