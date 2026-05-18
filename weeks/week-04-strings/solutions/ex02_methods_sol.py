"""Lời giải Bài tập 02: Phương thức chuỗi"""

# TODO 1
email = "  User@Example.COM  "
email = email.strip().lower()
print(email)

# TODO 2
sentence = "hello world python programming"
print(sentence.title())
print(f"Số lần 'o': {sentence.count('o')}")
print(sentence.replace("python", "PYTHON"))

# TODO 3
ho_ten = input("Nhập họ tên đầy đủ: ")
parts = ho_ten.split()
ho = parts[0]
ten = parts[-1]
print(f"Họ: {ho}, Tên: {ten}")

# TODO 4
filename = input("Nhập tên file: ")
if filename.endswith((".py", ".txt", ".csv")):
    print("Tên file hợp lệ")
else:
    print("Không hỗ trợ định dạng này")

# TODO 5
text = input("Nhập chuỗi: ").lower()
shift = int(input("Bước dịch: "))
result = ""
for ch in text:
    if ch.isalpha():
        new_code = (ord(ch) - ord("a") + shift) % 26 + ord("a")
        result += chr(new_code)
    else:
        result += ch
print(f"Mã hóa: {result}")
