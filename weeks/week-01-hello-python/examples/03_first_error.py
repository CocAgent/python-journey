"""Read the first traceback instead of skipping it."""

# Bỏ comment dòng dưới rồi chạy file để đọc traceback thật:
# print("Tổng: " + 5)

# Traceback cho biết ba thông tin quan trọng:
#   1. File và số dòng gây lỗi
#   2. Tên lỗi, ở đây là TypeError
#   3. Câu mô tả: can only concatenate str (not "int") to str
#
# Cách sửa: chuyển số thành text, hoặc để print() tự ngăn cách.
print("Tổng:", 5)
print("Tổng: " + str(5))
