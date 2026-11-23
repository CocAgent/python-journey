"""Mini-project Tuần 02 — Thẻ sinh viên (Student Card)."""

print("==========================================")
print("      CHƯƠNG TRÌNH TẠO THẺ SINH VIÊN      ")
print("==========================================")

# 1. Nhập dữ liệu từ người dùng
name = input("Nhập họ và tên       : ").strip()
student_id = input("Nhập mã sinh viên    : ").strip()
major = input("Nhập ngành học       : ").strip()
start_year_text = input("Nhập năm nhập học    : ").strip()
class_name = input("Nhập lớp (tùy chọn)  : ").strip()

# 2. Kiểm tra dữ liệu và xử lý
if not name or not student_id or not major:
    print("\n[!] Lỗi: Họ tên, mã sinh viên và ngành học không được để trống.")
elif not start_year_text.isdigit():
    print("\n[!] Lỗi: Năm nhập học cần gồm các chữ số (ví dụ: 2024).")
else:
    start_year = int(start_year_text)
    graduation_year = start_year + 4
    display_class = class_name if class_name else "Chưa cập nhật"

    # 3. In thẻ sinh viên với khung đẹp mắt bằng f-string
    width = 48
    border_top = "╔" + "═" * width + "╗"
    border_mid = "╠" + "═" * width + "╣"
    border_bot = "╚" + "═" * width + "╝"

    print()
    print(border_top)
    print(f"║{'THẺ SINH VIÊN · STUDENT CARD':^{width}}║")
    print(border_mid)
    print(f"║  {'Họ và tên':<14}: {name:<30}║")
    print(f"║  {'Mã sinh viên':<14}: {student_id:<30}║")
    print(f"║  {'Ngành học':<14}: {major:<30}║")
    print(f"║  {'Lớp':<14}: {display_class:<30}║")
    print(f"║  {'Niên khóa':<14}: {f'{start_year} - {graduation_year}':<30}║")
    print(f"║  {'Dự kiến TN':<14}: {f'Năm {graduation_year}':<30}║")
    print(border_bot)
