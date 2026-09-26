"""Exercise 04: a small regular-expression lab."""

# =============================================================
# Regex (Regular Expression) là gì?
# → Một "mô tả hình dạng" của chuỗi bạn cần tìm
# → Thay vì tìm từ cụ thể, bạn mô tả "kiểu dạng" của nó
#
# Ví dụ pattern r"PJ-\d{3}":
#   PJ-    → ký tự cố định "PJ-"
#   \d     → một chữ số bất kỳ (0-9)
#   {3}    → lặp lại đúng 3 lần
#   → Tìm bất kỳ chuỗi nào dạng: PJ-xxx (xxx là 3 chữ số)
#
# Chữ "r" trước chuỗi (r"...") → "raw string":
#   → Dấu \ không bị Python hiểu nhầm là ký tự đặc biệt
#   → Cần thiết khi viết pattern regex có dấu \
# =============================================================

import re  # noqa: F401 — learner uses this import to complete the TODOs.
# "import re" → nạp thư viện regex của Python vào chương trình

text = "Tickets PJ-101 and PJ-205 are open; XX-999 is unrelated."

# =============================================================
# TODO 1: Tìm TẤT CẢ chuỗi khớp với pattern trong văn bản
# re.findall(pattern, chuỗi) → trả về DANH SÁCH tất cả kết quả tìm thấy
#   Ví dụ: tìm tất cả mã khoá học dạng PJ-xxx
# =============================================================

codes: list[str] = re.findall(r"PJ-\d{3}", text)
# Kết quả: ['PJ-101', 'PJ-205']  (XX-999 không khớp vì không bắt đầu bằng PJ-)

# =============================================================
# TODO 2: Tìm KHỚP ĐẦU TIÊN trong chuỗi
# re.search(pattern, chuỗi) → trả về kết quả khớp ĐẦU TIÊN tìm thấy
#   .group() → lấy nội dung chuỗi khớp ra
# r"\d+" → \d là chữ số, + là "1 hoặc nhiều hơn"
#         → Tìm dãy số đầu tiên xuất hiện trong text
# =============================================================

match = re.search(r"\d+", text)
# Tìm dãy số đầu tiên: "101" (trong "PJ-101")
first_number = match.group() if match else None
# "if match else None" → phòng trường hợp không tìm thấy, tránh lỗi crash

# =============================================================
# TODO 3: Kiểm tra TOÀN BỘ chuỗi có khớp pattern không
# re.fullmatch(pattern, chuỗi) → khớp TOÀN BỘ chuỗi (không chỉ một phần)
# r"W\d{2}" → W + đúng 2 chữ số
#   "W04"  → W + 04 → khớp ✅
#   "W4"   → W + 1 chữ số → không khớp ❌
#   "WK04" → K không phải số → không khớp ❌
# bool(...) → chuyển kết quả thành True/False
# =============================================================

candidate    = "W04"
is_week_code = bool(re.fullmatch(r"W\d{2}", candidate))
# fullmatch trả về "Match object" nếu khớp, None nếu không
# bool(None) = False,  bool(Match) = True

print(codes)         # ['PJ-101', 'PJ-205']
print(first_number)  # '101'
print(is_week_code)  # True
