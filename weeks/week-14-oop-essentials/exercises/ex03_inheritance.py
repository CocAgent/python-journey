"""Bài 3: Animal và Dog minh họa quan hệ kế thừa đơn giản."""


class Animal:
    """Lớp cơ sở cho động vật có tên."""

    def __init__(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Tên động vật không được để trống")
        self.name = name

    def speak(self) -> str:
        """Hành vi chung mặc định của động vật."""
        return f"{self.name}: ..."


class Dog(Animal):
    """Dog là một Animal nên kế thừa thuộc tính name."""

    def speak(self) -> str:
        return f"{self.name}: woof"


# Dog là một Animal vì mọi Dog đều có thể được xem như một Animal.
# Không nên kế thừa nếu hai lớp không có quan hệ "là một";
# khi một đối tượng chỉ cần sử dụng đối tượng khác, composition phù hợp hơn.
