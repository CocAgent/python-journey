"""
Bài tập 03: Custom Exception 🏗️
==================================
Mục tiêu: Tạo exception riêng và raise
"""

# TODO 1: Tạo class InsufficientFundsError(Exception)
# Viết hàm rut_tien(so_du, so_tien)
# Raise InsufficientFundsError nếu rút quá số dư


# TODO 2: Tạo class InvalidAgeError(Exception)
# Viết hàm kiem_tra_tuoi(tuoi) raise nếu tuổi < 0 hoặc > 150


# TODO 3: Hệ thống đăng ký đơn giản
# Tạo: WeakPasswordError, DuplicateUserError
# Viết hàm dang_ky(username, password, existing_users)
# Raise lỗi phù hợp nếu mật khẩu yếu hoặc user đã tồn tại


# TODO 4 (Thử thách): Exception chain
# raise NewError("...") from original_error
