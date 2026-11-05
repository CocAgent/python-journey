"""Bài 3: Animal và Dog minh họa quan hệ kế thừa đơn giản."""


class Animal:
    def __init__(self, name: str) -> None:
        # TODO: lưu tên đối tượng.
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        # TODO: dùng self.name được kế thừa; trả "Milo: woof".
        return f"{self.name}: woof"


# Câu hỏi tự luận: vì sao Dog 'là một' Animal?
# Khi nào việc kế thừa là không cần thiết?
# Dog là một Animal vì Dog là một loại động vật cụ thể và kế thừa đặc điểm của Animal.
# Không cần kế thừa khi các lớp không có quan hệ "là một"; khi đó composition thường phù hợp hơn.


if __name__ == "__main__":
    dog = Dog("Milo")
    print(dog.speak())
