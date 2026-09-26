"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả
so_text = "42"                        # Tạo biến so_text chứa CHỮ "42" (có ngoặc kép → là chữ, không phải số)
so_nguyen = int(so_text) + 8          # int("42") chuyển chữ "42" thành số 42, rồi cộng thêm 8 → được 50
print("TODO 1:", so_nguyen)           # In ra: TODO 1: 50


# TODO 2: Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
pi = 3.14159                          # Tạo biến pi chứa số thực 3.14159
pi_nguyen = int(pi)                   # int(3.14159) CẮT BỎ phần thập phân → còn 3 (không làm tròn, int(3.9) cũng ra 3!)
print("TODO 2:", pi_nguyen)           # In ra: TODO 2: 3


# TODO 3: Kiểm tra bool() của các giá trị sau và in kết quả
# bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1,2])
print("TODO 3:")                           # In tiêu đề TODO 3
print("bool(0)      =", bool(0))           # bool(0)       → False  | số 0 = rỗng/không có gì → False
print("bool(1)      =", bool(1))           # bool(1)       → True   | số khác 0 → True
print('bool("")     =', bool(""))          # bool("")      → False  | chuỗi rỗng (không có chữ nào) → False
print('bool("hello")=', bool("hello"))     # bool("hello") → True   | chuỗi có chữ → True
print("bool([])     =", bool([]))          # bool([])      → False  | danh sách rỗng [] → False
print("bool([1,2])  =", bool([1, 2]))      # bool([1,2])   → True   | danh sách có phần tử → True
# 💡 Quy tắc: rỗng/bằng 0 → False | có nội dung/khác 0 → True


# TODO 4: Nhập chiều cao (m) và cân nặng (kg) từ người dùng
# Tính BMI = cân_nặng / (chiều_cao ** 2)
# In ra BMI với 1 chữ số thập phân
print("\nTODO 4:")                                        # \n = xuống dòng trống trước khi in tiêu đề
chieu_cao = float(input("Nhập chiều cao (m): "))         # input() hỏi người dùng gõ vào → float() chuyển chữ thành số thực
can_nang = float(input("Nhập cân nặng (kg): "))          # tương tự, nhập cân nặng và chuyển sang số thực
bmi = can_nang / (chieu_cao ** 2)                        # công thức BMI: cân nặng ÷ (chiều cao bình phương), ** là lũy thừa
print(f"BMI của bạn là: {bmi:.1f}")                      # :.1f = in BMI với đúng 1 chữ số thập phân, ví dụ: 22.9


# TODO 5 (Thử thách): Nhập số giây, chuyển sang giờ:phút:giây
# Ví dụ: 3661 giây → "1 giờ 1 phút 1 giây"
print("\nTODO 5:")                                        # \n = xuống dòng trống trước tiêu đề
tong_giay = int(input("Nhập số giây: "))                 # nhập tổng số giây (ví dụ: 3661), int() vì giây là số nguyên
gio = tong_giay // 3600                                  # // = chia lấy NGUYÊN | 1 giờ = 3600 giây | 3661 // 3600 = 1 giờ
phut = (tong_giay % 3600) // 60                          # % = lấy PHẦN DƯ | 3661 % 3600 = 61 giây dư → 61 // 60 = 1 phút
giay = tong_giay % 60                                    # 3661 % 60 = 1 → còn lại 1 giây
print(f"{gio} giờ {phut} phút {giay} giây")              # in kết quả: "1 giờ 1 phút 1 giây"
