"""Exercise 03: one clear basic inheritance example."""


class Animal:
    def __init__(self, name: str):
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name}: woof"


def main() -> None:
    dog = Dog("Milo")

    print(dog.name)
    print(dog.speak())
    print(isinstance(dog, Animal))
    print("Dog is an Animal vì Dog kế thừa từ Animal và là một loại Animal.")


if __name__ == "__main__":
    main()
