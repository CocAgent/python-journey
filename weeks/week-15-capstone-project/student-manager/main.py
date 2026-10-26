"""CLI for Week 15 Student Manager capstone."""

from pathlib import Path

from student_manager import (
    add_student,
    calculate_average,
    classify_student,
    find_student,
    load_students,
    save_students,
)

DATA_FILE = Path(__file__).resolve().parent / "data" / "students.json"


def show_students(students: list[dict]) -> None:
    if not students:
        print("No students.")
    for student in students:
        average = calculate_average(student["scores"])
        print(
            f'{student["id"]} | {student["name"]} | '
            f'{average:.2f} | {classify_student(average)}'
        )


def main() -> None:
    try:
        students = load_students(DATA_FILE)
    except ValueError as error:
        print(f"Cannot load data: {error}")
        return
    while True:
        print("\n1 Add  2 List  3 Find  4 Save  5 Exit")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                student_id = input("ID: ")
                name = input("Name: ")
                scores = [
                    float(x.strip())
                    for x in input("Scores, comma-separated: ").split(",")
                ]
                students = add_student(students, student_id, name, scores)
                print("Added.")
            elif choice == "2":
                show_students(students)
            elif choice == "3":
                student = find_student(students, input("Find ID: "))
                print(student if student else "Not found.")
            elif choice == "4":
                save_students(DATA_FILE, students)
                print("Saved.")
            elif choice == "5":
                print("Goodbye. Save changes using option 4 first.")
                return
            else:
                print("Invalid choice.")
        except (ValueError, OSError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
