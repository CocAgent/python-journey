class Student:
    def __init__(self, name: str, score: float):
        self.name = name
        self.score = score

    def __str__(self) -> str:
        return f"{self.name} - {self.score:.1f}"

    def is_passed(self) -> bool:
        return self.score >= 5


def exercise_1() -> None:
    student = Student("An", 8.0)
    print(student)
    print(student.is_passed())


def exercise_2() -> None:
    students = [
        Student("An", 8.0),
        Student("Bình", 4.5),
        Student("Chi", 9.0),
    ]

    for student in students:
        if student.is_passed():
            print(student)


def exercise_3() -> None:
    class Course:
        def __init__(self, name: str, credits: int):
            self.name = name
            self.credits = credits

        def __str__(self) -> str:
            return f"{self.name} - {self.credits} tín chỉ"

    class StudentWithCourses(Student):
        def __init__(self, name: str, score: float):
            super().__init__(name, score)
            self.courses = []

        def add_course(self, course: Course) -> None:
            self.courses.append(course)

    student = StudentWithCourses("Đức", 8.5)
    student.add_course(Course("Python", 3))
    student.add_course(Course("C++", 3))

    print(student)
    for course in student.courses:
        print(course)


def exercise_4() -> None:
    class Person:
        def __init__(self, name: str):
            self.name = name

        def introduce(self) -> str:
            return f"Tôi là {self.name}."

    class Developer(Person):
        def __init__(self, name: str, language: str):
            super().__init__(name)
            self.language = language

        def introduce(self) -> str:
            return f"Tôi là {self.name}, tôi học {self.language}."

    developer = Developer("Đức", "Python")
    print(developer.introduce())


if __name__ == "__main__":
    print("=== Bài 1 ===")
    exercise_1()

    print("\n=== Bài 2 ===")
    exercise_2()

    print("\n=== Bài 3 ===")
    exercise_3()

    print("\n=== Bài 4 ===")
    exercise_4()
