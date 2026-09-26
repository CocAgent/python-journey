"""
Bài tập 01: Indexing & Slicing chuỗi 🔤
=========================================
Mục tiêu: Thành thạo truy cập và cắt chuỗi
"""

# =============================================================
# TODO 1: Truy cập từng ký tự của chuỗi
# Ý tưởng: Chuỗi giống như một hàng ghế đánh số — mỗi ký tự
#          có một số thứ tự gọi là "index" (bắt đầu từ 0)
#
#   s = "Python Journey"
#        P  y  t  h  o  n     J  o  u  r  n  e  y
#        0  1  2  3  4  5  6  7  8  9  10 11 12 13  (index dương, đếm từ trái)
#       -14-13-12-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1  (index âm, đếm từ phải)
# =============================================================

s = "Python Journey"

print(f"Ký tự đầu    : {s[0]}")    # s[0]  → ghế số 0 → 'P'
print(f"Ký tự cuối   : {s[-1]}")   # s[-1] → ghế cuối cùng từ phải → 'y'
print(f"5 ký tự đầu  : {s[:5]}")   # s[:5] → từ đầu đến ghế 4 (không lấy 5) → 'Pytho'


# =============================================================
# TODO 2: Slicing — cắt một đoạn của chuỗi
# Cú pháp: chuoi[bat_dau : ket_thuc : buoc]
#   - bat_dau: bắt đầu từ index nào (mặc định = 0)
#   - ket_thuc: dừng TRƯỚC index này (không lấy chính ký tự đó)
#   - buoc: nhảy bao nhiêu bước (mặc định = 1)
# =============================================================

print(f"a) Journey       : {s[7:]}")      # Từ index 7 đến hết → 'Journey'
print(f"b) Đảo ngược     : {s[::-1]}")    # Bước = -1 → đi từ phải sang trái → đảo chuỗi
print(f"c) Mỗi ký tự thứ 2: {s[::2]}")   # Bước = 2 → lấy ký tự 0, 2, 4, 6, ... (bỏ qua 1 ký tự)


# =============================================================
# TODO 3: Đọc thông tin từ số CCCD bằng slicing
# Ý tưởng: Số CCCD 12 chữ số được mã hóa có quy tắc:
#   - 3 số đầu: mã tỉnh/thành phố
#   - Số thứ 4 (index 3): mã giới tính và thế kỷ sinh
#   - 2 số tiếp (index 4-5): 2 chữ số cuối năm sinh
# =============================================================

cccd = input("\nNhập số CCCD (12 chữ số): ").strip()
# Dùng slicing để "cắt" từng phần của chuỗi số CCCD
print(f"Mã tỉnh    : {cccd[:3]}")    # 3 ký tự đầu tiên (index 0, 1, 2)
print(f"Giới tính  : {cccd[3]}")     # Ký tự thứ 4 (index 3)
print(f"Năm sinh   : {cccd[4:6]}")   # 2 ký tự tiếp theo (index 4, 5)


# =============================================================
# TODO 4 (Thử thách): Kiểm tra chuỗi đối xứng (palindrome)
# Định nghĩa: Palindrome là chuỗi đọc xuôi và đọc ngược đều giống nhau
#   Ví dụ: "racecar" → đảo ngược = "racecar" → GIỐNG → palindrome ✅
#           "hello"  → đảo ngược = "olleh"   → KHÁC  → không phải ❌
# Mẹo: dùng s[::-1] để đảo ngược rồi so sánh với s gốc
# =============================================================

chuoi = input("\nNhập chuỗi kiểm tra palindrome: ").strip().lower()
# .lower() → chuyển thường để "Racecar" và "racecar" được coi là như nhau

if chuoi == chuoi[::-1]:            # So sánh chuỗi gốc với bản đảo ngược
    print(f'"{chuoi}" là chuỗi đối xứng (palindrome) ✅')
else:
    print(f'"{chuoi}" KHÔNG phải chuỗi đối xứng ❌')
