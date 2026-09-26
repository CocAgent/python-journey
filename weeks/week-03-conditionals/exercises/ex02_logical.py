"""
Bài tập 02: Toán tử logic 🧠
==============================
Mục tiêu: Kết hợp and, or, not trong điều kiện
"""

# =============================================================
# TODO 1: Kiểm tra đủ điều kiện lái xe
# Ý tưởng: Hỏi 3 thông tin, kiểm tra CẢ BA đều đạt thì mới được lái
# and = "VÀ" → tất cả điều kiện phải đúng mới là True
# =============================================================

tuoi = int(input("Tuổi: "))
co_bang_lai = input("Có bằng lái? (y/n): ").lower() == "y"
# .lower() → chuyển sang chữ thường (Y hoặc y đều được)
# == "y"   → so sánh, kết quả là True hoặc False
khong_say = input("Tỉnh táo? (y/n): ").lower() == "y"

if tuoi >= 18 and co_bang_lai and khong_say:
    # "and" = tất cả phải đúng — giống như ổ khóa cần đúng chìa khoá
    print("✅ Đủ điều kiện lái xe!")
else:
    # Nếu thiếu 1 trong 3, tìm hiểu lý do cụ thể để thông báo đúng chỗ
    if tuoi < 18:
        print("❌ Chưa đủ tuổi lái xe (cần >= 18 tuổi).")
    elif not co_bang_lai:       # "not" = đảo ngược: not True → False
        print("❌ Không có bằng lái xe.")
    else:
        print("❌ Không được lái xe khi say rượu/bia!")


# =============================================================
# TODO 2: Phân loại tam giác
# Ý tưởng:
#   Bước 1 — Kiểm tra 3 số có TẠO ĐƯỢC tam giác không
#             (quy tắc: tổng 2 cạnh bất kỳ phải LỚN HƠN cạnh còn lại)
#   Bước 2 — Nếu tạo được, phân loại: đều / cân / thường
# =============================================================

print("\n--- Phân loại tam giác ---")
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a + b > c and a + c > b and b + c > a:
    # Kiểm tra điều kiện tam giác hợp lệ cho cả 3 cặp cạnh
    if a == b == c:
        # Cả 3 cạnh bằng nhau → tam giác đều
        print("🔺 Tam giác đều")
    elif a == b or b == c or a == c:
        # Ít nhất 2 cạnh bằng nhau → tam giác cân
        print("🔺 Tam giác cân")
    else:
        # Không có cạnh nào bằng nhau → tam giác thường
        print("🔺 Tam giác thường")
else:
    print("❌ Ba cạnh này không tạo thành tam giác!")


# =============================================================
# TODO 3: Kiểm tra mật khẩu mạnh
# Ý tưởng: Mật khẩu đạt 4 tiêu chí: dài >= 8, có hoa, có thường, có số
# any(...) = "có ít nhất một" — như hỏi "trong hàng này, ai là sinh viên?"
# =============================================================

print("\n--- Kiểm tra mật khẩu ---")
pw = input("Nhập mật khẩu: ")

du_dai   = len(pw) >= 8                          # len() đếm số ký tự
co_hoa   = any(c.isupper() for c in pw)          # có ít nhất 1 ký tự IN HOA
co_thuong = any(c.islower() for c in pw)         # có ít nhất 1 ký tự thường
co_so    = any(c.isdigit() for c in pw)          # có ít nhất 1 chữ số (0-9)

if du_dai and co_hoa and co_thuong and co_so:
    print("✅ Mật khẩu mạnh!")
else:
    print("❌ Mật khẩu yếu! Cần:")
    if not du_dai:                # "not" đảo ngược: not True → False
        print("   - Ít nhất 8 ký tự")
    if not co_hoa:
        print("   - Có ít nhất 1 chữ HOA")
    if not co_thuong:
        print("   - Có ít nhất 1 chữ thường")
    if not co_so:
        print("   - Có ít nhất 1 chữ số")


# =============================================================
# TODO 4 (Thử thách): FizzBuzz
# Ý tưởng: Nhập số n, in "Fizz/Buzz/FizzBuzz" hoặc chính số đó
# Quan trọng: Kiểm tra chia hết cho 15 TRƯỚC (vì 15 = 3 × 5)
#             Nếu kiểm tra 3 trước → in "Fizz" mà quên "FizzBuzz"
# =============================================================

print("\n--- FizzBuzz ---")
n = int(input("Nhập số n: "))

if n % 3 == 0 and n % 5 == 0:  # Chia hết cho cả 3 lẫn 5 → kiểm tra trước!
    print("FizzBuzz")
elif n % 3 == 0:                # Chỉ chia hết cho 3
    print("Fizz")
elif n % 5 == 0:                # Chỉ chia hết cho 5
    print("Buzz")
else:                           # Không chia hết cho cái nào
    print(n)                    # In chính số đó
