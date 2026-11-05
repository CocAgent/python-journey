"""Show that input is text before explicit conversion."""

age_text = input("Tuổi của bạn: ").strip()
print(f"Kiểu trước conversion: {type(age_text).__name__}")

if age_text.isdigit():
    age = int(age_text)
    print(f"Năm sau bạn {age + 1} tuổi")
else:
    print("Tuổi cần gồm các chữ số")
