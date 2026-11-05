# Bài 3: Inheritance - Kế thừa

class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def speak(self):
        return f"{self.name}: woof"


# Dog kế thừa thuộc tính name từ Animal
cho = Dog("Milo")
print(cho.speak())
print("Dog là Animal:", isinstance(cho, Animal))

# Dog là một Animal vì chó thuộc nhóm động vật.
