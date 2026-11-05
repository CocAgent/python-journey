"""Bài 3: Animal và Dog minh họa quan hệ kế thừa đơn giản."""


class Animal:
<<<<<<< HEAD
    def __init__(self, name: str):
        self.name = name
=======
    def __init__(self, name: str) -> None:
        # TODO: lưu tên đối tượng.
        raise NotImplementedError("TODO: lưu tên động vật")
>>>>>>> dee0edc325298ea1e9c1e3b79a31da2a169d47d5


class Dog(Animal):
    def speak(self) -> str:
<<<<<<< HEAD
        return f"{self.name}: woof"


if __name__ == "__main__":
    dog = Dog("Milo")

    print(dog.speak())
    print(isinstance(dog, Animal))
=======
        # TODO: dùng self.name được kế thừa; trả "Milo: woof".
        raise NotImplementedError("TODO: tiếng sủa")


# Câu hỏi tự luận: vì sao Dog 'là một' Animal?
# Khi nào việc kế thừa là không cần thiết?
>>>>>>> dee0edc325298ea1e9c1e3b79a31da2a169d47d5
