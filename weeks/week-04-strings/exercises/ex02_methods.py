"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "

# .strip()  → xóa toàn bộ khoảng trắng ở đầu và cuối chuỗi
# .lower()  → chuyển tất cả ký tự thành chữ thường
# Hai method được nối chuỗi (method chaining): gọi liên tiếp trên cùng một dòng
email_chuan = email.strip().lower()
print(f"Email chuẩn hóa: {email_chuan}")   # in: "user@example.com"


# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"

print("\n=== TODO 2 ===")
# .title() → viết hoa chữ cái đầu của mỗi từ, các chữ còn lại thành chữ thường
print(f"a) Title Case : {sentence.title()}")

# .count('o') → đếm số lần chuỗi con 'o' xuất hiện trong sentence
print(f"b) Số lần 'o' : {sentence.count('o')}")

# .replace(old, new) → thay toàn bộ chuỗi con 'python' bằng 'PYTHON'
# Lưu ý: chuỗi gốc KHÔNG thay đổi — Python string là immutable (bất biến)
print(f"c) Thay python: {sentence.replace('python', 'PYTHON')}")


# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing

print("\n=== TODO 3 ===")
# .strip() → xóa khoảng trắng thừa ở đầu/cuối (phòng khi người dùng nhập thừa)
ho_ten = input("Nhập họ tên đầy đủ: ").strip()

# .split() → tách chuỗi thành list các từ, dùng khoảng trắng làm dấu phân cách
# "Nguyễn Văn An".split() → ['Nguyễn', 'Văn', 'An']
phan = ho_ten.split()

ho = phan[0]    # phần tử đầu tiên của list → họ
ten = phan[-1]  # phần tử cuối cùng (index âm -1) → tên, hoạt động dù tên có 1 hay nhiều phần
print(f"Họ  : {ho}")
print(f"Tên : {ten}")


# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()

print("\n=== TODO 4 ===")
ten_file = input("Nhập tên file: ").strip()

# Định nghĩa tuple chứa các đuôi file được chấp nhận
# Dùng tuple thay vì list vì endswith() nhận tuple để kiểm tra nhiều đuôi cùng lúc
duoi_hop_le = (".py", ".txt", ".csv")

# .endswith(tuple) → trả về True nếu chuỗi kết thúc bằng BẤT KỲ đuôi nào trong tuple
if ten_file.endswith(duoi_hop_le):
    print(f"✅ '{ten_file}' là file hợp lệ.")
else:
    print(f"❌ '{ten_file}' không hợp lệ. Chỉ chấp nhận: .py, .txt, .csv")


# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"

print("\n=== TODO 5 (Caesar Cipher) ===")
van_ban = input("Nhập chuỗi cần mã hóa: ")
shift = int(input("Nhập số bước dịch (shift): "))

ket_qua = []         # list rỗng để tích lũy từng ký tự sau khi mã hóa

for ch in van_ban:   # duyệt qua từng ký tự trong chuỗi gốc
    if ch.isalpha(): # .isAlpha() → True nếu ký tự là chữ cái (a-z hoặc A-Z)
        # ord(ch) → trả về mã ASCII của ký tự, ví dụ ord('a') = 97, ord('A') = 65
        # Cần điểm gốc (goc) để tính vị trí tương đối trong bảng chữ cái (0-25)
        goc = ord('a') if ch.islower() else ord('A')  # chữ thường dùng 'a', chữ hoa dùng 'A'

        # Công thức dịch Caesar với quay vòng:
        #   ord(ch) - goc        → vị trí hiện tại trong bảng (0=a, 1=b, ...)
        #   + shift              → dịch đi shift bước
        #   % 26                 → quay vòng: nếu vượt 'z'/'Z' thì về đầu bảng
        #   + goc                → chuyển lại thành mã ASCII
        #   chr(...)             → chuyển mã ASCII thành ký tự
        ky_tu_moi = chr((ord(ch) - goc + shift) % 26 + goc)
        ket_qua.append(ky_tu_moi)  # thêm ký tự đã mã hóa vào list
    else:
        # Ký tự không phải chữ cái (số, dấu câu, khoảng trắng) → giữ nguyên
        ket_qua.append(ch)

# ''.join(list) → nối tất cả ký tự trong list thành một chuỗi duy nhất
print(f"Kết quả mã hóa: {''.join(ket_qua)}")
