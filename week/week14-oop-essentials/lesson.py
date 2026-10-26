class Student:
    def __init__(self, name: str, age: int, score: float):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self) -> str:
        return f"{self.name} - {self.age} tuổi - {self.score:.1f} điểm"

    def is_passed(self) -> bool:
        return self.score >= 5


class Course:
    def __init__(self, name: str, credits: int):
        self.name = name
        self.credits = credits

    def __str__(self) -> str:
        return f"{self.name} ({self.credits} tín chỉ)"


class UniversityStudent(Student):
    def __init__(self, name: str, age: int, score: float, major: str):
        super().__init__(name, age, score)
        self.major = major

    def __str__(self) -> str:
        return f"{self.name} - {self.major} - {self.score:.1f} điểm"


def main() -> None:
    student = Student("Nguyễn Như Đức", 20, 8.5)
    course = Course("Python", 3)
    university_student = UniversityStudent(
        "Nguyễn Văn A", 20, 7.8, "Công nghệ thông tin"
    )

    print("=== CLASS & OBJECT ===")
    print(student)
    print(f"Đậu: {student.is_passed()}")

    print("\n=== COMPOSITION IDEA ===")
    student.courses = [course]
    for item in student.courses:
        print(item)

    print("\n=== BASIC INHERITANCE ===")
    print(university_student)


if __name__ == "__main__":
    main()
