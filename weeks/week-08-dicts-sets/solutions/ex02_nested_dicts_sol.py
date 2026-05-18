"""Lời giải Bài tập 02: Dict lồng nhau"""
# TODO 1
lop = {
    "An":   {"tuoi": 20, "diem": [8, 9, 7]},
    "Bình": {"tuoi": 21, "diem": [7, 6, 8]},
    "Châu": {"tuoi": 20, "diem": [9, 9, 10]},
}
best_name, best_avg = "", 0
for ten, info in lop.items():
    avg = sum(info["diem"]) / len(info["diem"])
    print(f"{ten}: TB = {avg:.1f}")
    if avg > best_avg:
        best_name, best_avg = ten, avg
print(f"Cao nhất: {best_name} ({best_avg:.1f})")

lop["Dũng"] = {"tuoi": 22, "diem": [6, 7, 8]}

# TODO 2
products = {
    "p1": {"ten": "Laptop", "gia": 15000000, "so_luong": 10},
    "p2": {"ten": "Chuột", "gia": 200000, "so_luong": 50},
    "p3": {"ten": "Bàn phím", "gia": 500000, "so_luong": 30},
}
def tong_gia_tri_kho(products):
    return sum(p["gia"] * p["so_luong"] for p in products.values())

print(f"Tổng giá trị kho: {tong_gia_tri_kho(products):,} VNĐ")
