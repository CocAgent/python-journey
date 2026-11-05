"""Bài 3: Animal và Dog minh họa quan hệ kế thừa đơn giản."""



class Animal:
    def __init__(self, name: str) -> None:
        # Lưu tên động vật
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        # Sử dụng thuộc tính name được kế thừa từ Animal
        return f"{self.name}: woof"


# Kiểm tra chương trình
dog = Dog("Milo")

print(dog.name)    # Milo
print(dog.speak()) # Milo: woof

