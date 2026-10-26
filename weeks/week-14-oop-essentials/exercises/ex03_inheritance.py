"""Exercise 03: demonstrate a simple and meaningful inheritance relationship."""


class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def speak(self):
        return f"{self.name}: woof"


if __name__ == "__main__":
    dog = Dog("Milo")
    print(dog.speak())
    # Dog is an Animal: it inherits the name attribute from Animal.
    print("Dog is an Animal:", isinstance(dog, Animal))
