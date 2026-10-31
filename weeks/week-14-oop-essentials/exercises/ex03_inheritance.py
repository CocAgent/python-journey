"""Bài 3: Animal và Dog minh họa quan hệ kế thừa đơn giản."""


class Animal:
    def __init__(self, name: str) -> None:
        # TODO: lưu tên đối tượng.
        raise NotImplementedError("TODO: lưu tên động vật")


class Dog(Animal):
    def speak(self) -> str:
        # TODO: dùng self.name được kế thừa; trả "Milo: woof".
        raise NotImplementedError("TODO: tiếng sủa")


# Câu hỏi tự luận: vì sao Dog 'là một' Animal?
# Khi nào việc kế thừa là không cần thiết?
