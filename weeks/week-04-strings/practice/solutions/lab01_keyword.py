"""Lời giải Lab 01 — kiểm rỗng trước khi index."""

keyword = input("Từ khóa: ").strip()
if not keyword:
    print("Từ khóa không được rỗng")
else:
    print(f"Đầu: {keyword[0]}")
    print(f"Cuối: {keyword[-1]}")
    print(f"Đảo: {keyword[::-1]}")
    print(f"Độ dài: {len(keyword)}")
