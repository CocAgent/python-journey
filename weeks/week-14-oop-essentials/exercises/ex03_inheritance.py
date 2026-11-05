"""Bài 3: Animal và Dog minh họa quan hệ kế thừa đơn giản."""


class Animal:
    """Lớp cha đại diện cho động vật có tên."""

    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):
    """Dog là một Animal và có thêm hành vi sủa speak()."""

    def speak(self) -> str:
        return f"{self.name}: woof"


# Câu hỏi tự luận:
# 1. Vì sao Dog 'là một' Animal?
# -> Dog là một Animal vì Dog chia sẻ bản chất và các thuộc tính/hành vi chung của động vật
#    (ví dụ có tên, có sự sống). Quan hệ "is-a" ở đây tự nhiên, logic và giúp tái sử dụng mã nguồn.
#
# 2. Khi nào việc kế thừa là không cần thiết (hoặc nên tránh)?
# -> Khi hai thực thể chỉ có quan hệ "có một" (has-a) thay vì "là một" (is-a), ví dụ: Bot "có"
#    một chiến lược (Strategy), chứ Bot không "là một" chiến lược. Khi đó dùng Composition
#    (chứa đối tượng khác hoặc truyền hàm) sẽ linh hoạt hơn, dễ hoán đổi runtime và tránh
#    làm cây phân cấp kế thừa bị cứng nhắc, phức tạp không cần thiết.

