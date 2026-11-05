"""Bài 3: Animal và Dog minh họa quan hệ kế thừa đơn giản."""


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name}: woof"


# Câu hỏi tự luận: vì sao Dog 'là một' Animal?
# Trả lời: Dog là một Animal vì Dog chia sẻ các thuộc tính bản chất của động vật
# (như có tên) và mở rộng thêm hành vi đặc thù riêng (tiếng sủa).

# Khi nào việc kế thừa là không cần thiết?
# Trả lời: Kế thừa không cần thiết khi các đối tượng chỉ có mối quan hệ 'có một' (has-a)
# hoặc khi chỉ muốn tái sử dụng một hành vi có thể thay đổi độc lập (nên ưu tiên Composition).
