class Course:
    def __init__(self, name: str, credits: int):
        self.name = name
        self.credits = credits

    def __str__(self) -> str:
        return f"{self.name} ({self.credits} tín chỉ)"


class Student:
    def __init__(self, student_id: str, name: str, age: int):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses: list[Course] = []

    def add_course(self, course: Course) -> None:
        self.courses.append(course)

    def total_credits(self) -> int:
        return sum(course.credits for course in self.courses)

    def __str__(self) -> str:
        return (
            f"{self.student_id} | {self.name} | {self.age} tuổi | "
            f"{self.total_credits()} tín chỉ"
        )


class StudentManager:
    def __init__(self):
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def find_by_id(self, student_id: str) -> Student | None:
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def show_all(self) -> None:
        if not self.students:
            print("Chưa có sinh viên.")
            return

        for student in self.students:
            print(student)
            if student.courses:
                for course in student.courses:
                    print(f"  - {course}")


def create_sample_data(manager: StudentManager) -> None:
    python = Course("Python", 3)
    sql = Course("SQL Server", 3)
    cpp = Course("C++", 4)

    duc = Student("SV001", "Nguyễn Như Đức", 20)
    duc.add_course(python)
    duc.add_course(sql)

    an = Student("SV002", "Nguyễn Văn An", 20)
    an.add_course(cpp)

    manager.add_student(duc)
    manager.add_student(an)


def main() -> None:
    manager = StudentManager()
    create_sample_data(manager)

    while True:
        print("\n=== STUDENT MANAGER OOP ===")
        print("1. Hiển thị sinh viên")
        print("2. Tìm sinh viên")
        print("3. Thêm môn học")
        print("0. Thoát")

        choice = input("Chọn: ").strip()

        if choice == "1":
            manager.show_all()

        elif choice == "2":
            student_id = input("Mã sinh viên: ").strip()
            student = manager.find_by_id(student_id)
            print(student if student else "Không tìm thấy sinh viên.")

        elif choice == "3":
            student_id = input("Mã sinh viên: ").strip()
            student = manager.find_by_id(student_id)

            if student is None:
                print("Không tìm thấy sinh viên.")
                continue

            name = input("Tên môn học: ").strip()
            credits_text = input("Số tín chỉ: ").strip()

            try:
                credits = int(credits_text)
                if credits <= 0:
                    raise ValueError
            except ValueError:
                print("Số tín chỉ phải là số nguyên dương.")
                continue

            student.add_course(Course(name, credits))
            print("Đã thêm môn học.")

        elif choice == "0":
            print("Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()
