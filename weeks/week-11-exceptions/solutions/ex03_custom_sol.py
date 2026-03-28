"""Lời giải Bài tập 03: Custom Exception"""

# TODO 1
class InsufficientFundsError(Exception):
    def __init__(self, so_du, so_tien):
        self.so_du = so_du
        self.so_tien = so_tien
        super().__init__(f"Không đủ tiền! Cần {so_tien:,}, có {so_du:,}")

def rut_tien(so_du, so_tien):
    if so_tien > so_du:
        raise InsufficientFundsError(so_du, so_tien)
    return so_du - so_tien

try:
    print(rut_tien(100000, 50000))   # 50000
    print(rut_tien(100000, 200000))  # Raise!
except InsufficientFundsError as e:
    print(e)

# TODO 2
class InvalidAgeError(Exception):
    pass

def kiem_tra_tuoi(tuoi):
    if not isinstance(tuoi, int):
        raise TypeError("Tuổi phải là số nguyên")
    if tuoi < 0 or tuoi > 150:
        raise InvalidAgeError(f"Tuổi {tuoi} không hợp lệ (0-150)")
    return True

# TODO 3
class WeakPasswordError(Exception):
    pass

class DuplicateUserError(Exception):
    pass

def dang_ky(username, password, existing_users):
    if username in existing_users:
        raise DuplicateUserError(f"User \"{username}\" đã tồn tại")
    if len(password) < 8:
        raise WeakPasswordError("Mật khẩu phải >= 8 ký tự")
    existing_users.add(username)
    print(f"Đăng ký thành công: {username}")

users = {"admin", "user1"}
try:
    dang_ky("newuser", "StrongP4ss", users)
    dang_ky("admin", "password", users)
except (WeakPasswordError, DuplicateUserError) as e:
    print(f"Lỗi: {e}")
