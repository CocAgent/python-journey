"""Mini-project mức A: vẽ thẻ ASCII tĩnh bằng print()."""

# Dùng cùng độ rộng cho cả ba dòng để viền trái/phải thẳng hàng.
width = 24
border = "+" + "-" * (width - 2) + "+"
message = "|" + "Hello, Python!".center(width - 2) + "|"
print(border)
print(message)
print(border)

# Thử thách: thay lời chào hoặc thêm một dòng trang trí có cùng độ rộng.
