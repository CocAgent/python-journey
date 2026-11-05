"""Bài 3: Animal và Dog minh họa quan hệ kế thừa đơn giản."""


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name}: woof"


# Câu hỏi tự luận: vì sao Dog 'là một' Animal?
# Trả lời: Dog là một loại Animal, mọi Dog đều có name và đều là Animal,
# nên kế thừa mô tả đúng quan hệ này.
#
# Khi nào việc kế thừa là không cần thiết?
# Khi quan hệ chỉ là "có một" (ví dụ Bot có một strategy), hoặc khi
# chỉ cần tái sử dụng một hàm. Lúc đó nên dùng composition.