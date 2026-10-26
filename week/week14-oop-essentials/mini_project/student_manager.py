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
        if self.find_by_id(student.student_id) is not None:
            print("Mã sinh viên đã tồn tại.")
            return
        self.students.append(student)
        print("Đã thêm sinh viên.")

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


def read_positive_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Vui lòng nhập số nguyên dương.")
        except ValueError:
            print("Dữ liệu không hợp lệ.")


def create_sample_data(manager: StudentManager) -> None:
    student_1 = Student("SV001", "Nguyễn Như Đức", 20)
    student_1.add_course(Course("Python", 3))
    student_1.add_course(Course("Cơ sở dữ liệu", 4))

    student_2 = Student("SV002", "Nguyễn Văn A", 20)
    student_2.add_course(Course("C++", 3))

    manager.add_student(student_1)
    manager.add_student(student_2)


def add_course_to_student(manager: StudentManager) -> None:
    student_id = input("Mã sinh viên: ").strip()
    student = manager.find_by_id(student_id)

    if student is None:
        print("Không tìm thấy sinh viên.")
        return

    name = input("Tên môn học: ").strip()
    credits = read_positive_int("Số tín chỉ: ")
    student.add_course(Course(name, credits))
    print("Đã thêm môn học.")


def main() -> None:
    manager = StudentManager()
    create_sample_data(manager)

    while True:
        print("\n=== STUDENT MANAGEMENT OOP ===")
        print("1. Xem tất cả sinh viên")
        print("2. Tìm sinh viên theo mã")
        print("3. Thêm môn học cho sinh viên")
        print("0. Thoát")

        choice = input("Chọn: ").strip()

        if choice == "1":
            manager.show_all()
        elif choice == "2":
            student_id = input("Mã sinh viên: ").strip()
            student = manager.find_by_id(student_id)
            print(student if student else "Không tìm thấy sinh viên.")
        elif choice == "3":
            add_course_to_student(manager)
        elif choice == "0":
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()
