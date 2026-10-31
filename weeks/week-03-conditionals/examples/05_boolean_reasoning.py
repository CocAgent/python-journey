"""Ví dụ 05 — and/or/not, ngoặc logic, truthy/falsy (offline).

Đủ 18 tuổi + có vé + cửa chưa đóng là quy tắc GIẢ LẬP để học boolean.
"""


age = 18
has_ticket = True
is_closed = False

age_ok = age >= 18
can_enter = age_ok and has_ticket and not is_closed
print(f"Đủ tuổi: {age_ok}")
print(f"Có thể vào: {can_enter}")

# Chỉ đổi 1 điều kiện để quan sát kết quả, không cần input().
is_closed = True
print(f"Cửa đã đóng: {age_ok and has_ticket and not is_closed}")

# Ngày đặc biệt: có vé hoặc thư mời, NHƯNG cửa không được đóng.
has_ticket = False
has_invitation = True
is_closed = False
allowed = (has_ticket or has_invitation) and not is_closed
print(f"Có giấy mời: {allowed}")

# "False" là chuỗi chứa 5 ký tự, KHÔNG phải boolean False.
print(f"bool('False'): {bool('False')}")
print(f"bool(''): {bool('')}")
print(f"bool('0'): {bool('0')}")
