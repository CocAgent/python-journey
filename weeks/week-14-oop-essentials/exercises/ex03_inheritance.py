"""Bài 3: Animal và Dog minh họa quan hệ kế thừa đơn giản."""


class Animal:
    """Lớp cha đại diện cho động vật có thuộc tính tên."""

    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):
    """Dog là một Animal (kế thừa) và có thêm hành vi sủa speak()."""

    def speak(self) -> str:
        return f"{self.name}: woof"


# Câu hỏi tự luận:
# 1. Vì sao Dog 'là một' Animal?
# -> Dog "là một" (IS-A) Animal vì chó là một loài động vật cụ thể, kế thừa tự nhiên
#    các đặc tính cơ bản của Animal (như có tên `name`) và mở rộng thêm hành vi riêng (sủa `speak()`).
#
# 2. Khi nào việc kế thừa là không cần thiết?
# -> Kế thừa không cần thiết khi hai đối tượng chỉ có quan hệ "sở hữu / chứa đựng" (HAS-A)
#    thay vì "là một" (IS-A), hoặc khi chỉ muốn tái sử dụng thuật toán/hành vi có thể thay đổi
#    linh hoạt trong thời gian chạy (runtime) — lúc đó nên dùng Composition (kết hợp) thay vì Inheritance.


if __name__ == "__main__":
    dog = Dog("Milo")
    print(dog.name)
    print(dog.speak())
