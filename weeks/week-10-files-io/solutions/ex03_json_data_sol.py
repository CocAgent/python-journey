"""Lời giải Bài tập 03: JSON"""
import json
from datetime import datetime

# TODO 1
config = {"app_name": "MyApp", "version": "1.0", "debug": True}
with open("config.json", "w") as f:
    json.dump(config, f, indent=2)

# TODO 2
with open("config.json", "r") as f:
    data = json.load(f)
for k, v in data.items():
    print(f"{k}: {v}")

# TODO 3
products = [
    {"ten": "Laptop", "gia": 15000000, "so_luong": 10},
    {"ten": "Chuột", "gia": 200000, "so_luong": 50},
    {"ten": "Bàn phím", "gia": 500000, "so_luong": 30},
]
with open("products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

# TODO 4
FILE = "notes.json"
def load_notes():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2, ensure_ascii=False)

notes = load_notes()
notes.append({"noi_dung": "Học JSON!", "ngay": str(datetime.now())})
save_notes(notes)
print("Ghi chú đã lưu:")
for n in notes:
    print(f"  [{n['ngay']}] {n['noi_dung']}")
