class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    # Dog kế thừa Animal vì chó là một loại động vật (is-a relationship).
    def speak(self):
        return f"{self.name}: woof"
