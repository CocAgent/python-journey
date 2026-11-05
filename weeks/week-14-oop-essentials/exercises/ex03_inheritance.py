"""Bài 3: Animal và Dog minh họa quan hệ kế thừa đơn giản."""


class Animal:
    """Lớp cơ sở lưu những thông tin chung của động vật."""

    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):
    """Dog là một Animal nên kế thừa thuộc tính name."""

    def speak(self) -> str:
        return f"{self.name}: woof"


# Dog là một Animal (is-a): mọi Dog đều có thể được dùng như một Animal.
# Không nên kế thừa chỉ để tái sử dụng vài dòng code; khi quan hệ không phải
# "là một", hãy ưu tiên composition hoặc hàm dùng chung.
if __name__ == "__main__":
    dog = Dog("Milo")
    print(dog.speak())
