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


class StudentWithCourses(Student):
    def __init__(self, name: str, age: int, score: float):
        super().__init__(name, age, score)
        self.courses: list[Course] = []

    def add_course(self, course: Course) -> None:
        self.courses.append(course)

    def total_credits(self) -> int:
        return sum(course.credits for course in self.courses)


class Person:
    def __init__(self, name: str):
        self.name = name

    def introduce(self) -> str:
        return f"Xin chào, tôi là {self.name}."


class Developer(Person):
    def introduce(self) -> str:
        return f"Xin chào, tôi là {self.name} và tôi là lập trình viên."


def exercise_1() -> None:
    student = Student("An", 20, 8.0)
    print("Bài 1:", student)
    print("Đậu:", student.is_passed())


def exercise_2() -> None:
    students = [
        Student("An", 20, 8.0),
        Student("Bình", 21, 4.5),
        Student("Chi", 19, 6.5),
    ]

    print("\nBài 2 - Sinh viên đậu:")
    for student in students:
        if student.is_passed():
            print(student)


def exercise_3() -> None:
    python = Course("Python", 3)
    database = Course("SQL Server", 4)
    student = StudentWithCourses("Đức", 20, 8.5)

    student.add_course(python)
    student.add_course(database)

    print("\nBài 3 - Composition:")
    print(student)
    for course in student.courses:
        print("-", course)
    print("Tổng tín chỉ:", student.total_credits())


def exercise_4() -> None:
    person = Person("Nam")
    developer = Developer("Đức")

    print("\nBài 4 - Inheritance:")
    print(person.introduce())
    print(developer.introduce())


def main() -> None:
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()


if __name__ == "__main__":
    main()
