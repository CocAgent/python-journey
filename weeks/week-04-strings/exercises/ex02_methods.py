"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# =============================================================
# TODO 1: Chuẩn hóa email
# Ý tưởng: Người dùng hay gõ sai (thừa khoảng trắng, chữ hoa lẫn lộn)
#          Chuẩn hóa = dọn dẹp email về đúng định dạng
# .strip() → xóa khoảng trắng thừa ở đầu và cuối chuỗi
# .lower() → chuyển tất cả ký tự thành chữ thường
# Hai method nối nhau bằng dấu . → thực hiện lần lượt từ trái sang phải
# =============================================================

email = "  User@Example.COM  "

email_chuan = email.strip().lower()
# Bước 1: "  User@Example.COM  ".strip() → "User@Example.COM"
# Bước 2: "User@Example.COM".lower()     → "user@example.com"
print(f"Email chuẩn hóa: {email_chuan}")


# =============================================================
# TODO 2: Các thao tác phổ biến trên chuỗi
# .title()   → Viết hoa ký tự đầu mỗi từ (như tiêu đề)
# .count()   → Đếm số lần một ký tự/từ xuất hiện trong chuỗi
# .replace() → Tìm chuỗi A và thay bằng chuỗi B
# =============================================================

sentence = "hello world python programming"

print(f"a) Title Case    : {sentence.title()}")
# title() → "Hello World Python Programming"

print(f"b) Số lần 'o'    : {sentence.count('o')}")
# count('o') → đếm chữ 'o' trong chuỗi: hell[o] w[o]rld pyth[o]n pr[o]gramming → 4

print(f"c) Thay python   : {sentence.replace('python', 'PYTHON')}")
# replace('cũ', 'mới') → tìm 'python' và đổi thành 'PYTHON'


# =============================================================
# TODO 3: Tách họ và tên từ họ tên đầy đủ
# .split() → chặt chuỗi thành danh sách các từ (mặc định tách theo khoảng trắng)
#   "Nguyễn Văn An".split() → ["Nguyễn", "Văn", "An"]
# Sau đó dùng index để lấy phần tử:
#   [0]  → phần tử đầu tiên = "Nguyễn" (họ)
#   [-1] → phần tử cuối cùng = "An" (tên)
# =============================================================

ho_ten = input("\nNhập họ tên đầy đủ: ").strip()
phan = ho_ten.split()   # Tách thành danh sách: ["Nguyễn", "Văn", "An"]
ho   = phan[0]          # Lấy phần tử đầu tiên
ten  = phan[-1]         # Lấy phần tử cuối cùng (dù tên có mấy chữ lót)
print(f"Họ  : {ho}")
print(f"Tên : {ten}")


# =============================================================
# TODO 4: Kiểm tra đuôi file hợp lệ
# .endswith() → kiểm tra chuỗi có KẾT THÚC bằng một chuỗi nào đó không
# Có thể truyền vào một tuple (nhóm) để kiểm tra nhiều đuôi cùng lúc
# =============================================================

ten_file = input("\nNhập tên file: ").strip()
duoi_hop_le = (".py", ".txt", ".csv")
# Lưu ý: truyền vào tuple (nhóm) — endswith sẽ kiểm tra tất cả các đuôi

if ten_file.endswith(duoi_hop_le):
    print(f'✅ "{ten_file}" là file hợp lệ!')
else:
    print(f'❌ "{ten_file}" không hợp lệ (cần .py, .txt hoặc .csv)')


# =============================================================
# TODO 5 (Thử thách): Mã hóa Caesar
# Ý tưởng: Dịch chuyển mỗi chữ cái đi N bước trong bảng chữ cái
#   "abc" với shift=3 → "def"  (a→d, b→e, c→f)
#   "xyz" với shift=3 → "abc"  (quay vòng)
#
# Kỹ thuật: dùng số thứ tự ASCII của ký tự
#   ord('a') = 97, ord('z') = 122
#   chr(97)  = 'a'  (chuyển ngược lại từ số về ký tự)
# Công thức: ((vị_trí_hiện_tại + shift) % 26) + gốc
#   % 26 → đảm bảo quay vòng trong phạm vi 26 chữ cái
# =============================================================

print("\n--- Mã hóa Caesar ---")
van_ban = input("Nhập chuỗi cần mã hóa: ")
shift   = int(input("Số bước dịch (shift): "))

ket_qua = []    # Danh sách rỗng, sẽ gom kết quả từng ký tự vào đây
for ky_tu in van_ban:               # Lặp qua từng ký tự trong chuỗi
    if ky_tu.isalpha():             # Chỉ mã hóa chữ cái (bỏ qua số, dấu cách, ...)
        goc = ord('A') if ky_tu.isupper() else ord('a')
        # Nếu chữ HOA → gốc = 65 (ord của 'A')
        # Nếu chữ thường → gốc = 97 (ord của 'a')
        ma_hoa = chr((ord(ky_tu) - goc + shift) % 26 + goc)
        # ord(ky_tu) - goc   → vị trí trong bảng chữ cái (A=0, B=1, ...)
        # + shift             → dịch chuyển N bước
        # % 26                → quay vòng nếu vượt quá Z
        # + goc               → chuyển lại thành mã ASCII đúng
        # chr(...)            → chuyển mã ASCII về ký tự
        ket_qua.append(ma_hoa)     # Thêm ký tự đã mã hóa vào danh sách
    else:
        ket_qua.append(ky_tu)      # Giữ nguyên ký tự không phải chữ cái

print(f"Kết quả mã hóa: {''.join(ket_qua)}")
# ''.join(danh_sach) → ghép tất cả ký tự trong danh sách thành một chuỗi
