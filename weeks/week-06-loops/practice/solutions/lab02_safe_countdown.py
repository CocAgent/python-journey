"""Lời giải Lab 02: kiểm input rồi mới chạy while, cập nhật biến dừng."""

raw = input("Bắt đầu (0..5): ").strip()
if not raw.isdigit():
    print("Dữ liệu không hợp lệ")
else:
    remaining = int(raw)
    if remaining > 5:
        print("Dữ liệu không hợp lệ")
    else:
        while remaining > 0:
            print(f"Còn: {remaining}")
            remaining -= 1
        print("Kết thúc")
