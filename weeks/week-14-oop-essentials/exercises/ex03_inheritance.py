"""Exercise 03: basic inheritance."""


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name}: woof"


# Dog is an Animal: a dog is a particular type of animal.
if __name__ == "__main__":
    dog = Dog("Milo")
    print(dog.speak())
    print(isinstance(dog, Animal))
