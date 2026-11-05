"""Bài 3: Animal và Dog minh họa quan hệ kế thừa đơn giản."""


class Animal:
    def __init__(self, name: str) -> None:
        # TODO: lưu tên đối tượng.
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        # TODO: dùng self.name được kế thừa; trả "Milo: woof".
        return f"{self.name}: woof"

if __name__ == "__main__":
    dog = Dog("Milo")
    print(dog.speak())
    print(isinstance(dog, Animal))

# Câu hỏi tự luận: vì sao Dog 'là một' Animal?
# => Dog là Animal vì class Dog kế thừa class Animal. Do đó, Dog có thể sử dụng lại các thuộc tính và phương thức của Animal.

# Khi nào việc kế thừa là không cần thiết?
# => Không cần sử dụng kế thừa khi hai class không có mối quan hệ cha – con rõ ràng, hoặc chỉ muốn dùng chung một vài chức 
#    năng nhỏ. Khi đó, ta có thể sử dụng class riêng biệt hoặc Composition.
