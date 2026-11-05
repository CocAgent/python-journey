"""Bài 3: Animal và Dog minh họa quan hệ kế thừa đơn giản."""


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name}: woof"


# Câu hỏi tự luận:
# 1. Vì sao Dog 'là một' Animal?
#    Dog mang bản chất và chia sẻ đầy đủ các đặc tính cơ bản của Animal (như tên gọi `name`),
#    đồng thời chuyên biệt hoá thêm hành vi riêng của loài chó (như tiếng sủa `speak`).
# 2. Khi nào việc kế thừa là không cần thiết?
#    - Khi mối quan hệ giữa hai đối tượng là "chứa/sở hữu" (HAS-A) thay vì "là một" (IS-A), ví dụ: Bot sở hữu Strategy (Composition).
#    - Khi chỉ muốn tái sử dụng mã mà không có mối quan hệ ngữ nghĩa thực tế.
#    - Khi các hành vi cần thay đổi linh hoạt tại thời điểm chạy (runtime), trong khi kế thừa tạo sự liên kết cứng (tight coupling) khó thay đổi.
