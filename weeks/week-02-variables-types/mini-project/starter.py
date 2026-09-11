"""Starter for the Week 02 student card."""

name = input("Họ tên: ").strip()
student_id = input("Mã sinh viên: ").strip()
major = input("Ngành: ").strip()
start_year_text = input("Năm nhập học: ").strip()

if start_year_text.isdigit():
	start_year = int(start_year_text)
	graduation_year = start_year + 4
	print(f"{name} · {student_id} · {major}")
	print(f"Khóa: {start_year}–{graduation_year}")
else:
	print("Năm nhập học cần gồm các chữ số")


