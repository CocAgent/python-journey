"""
╔══════════════════════════════════════════════════╗
║          🐍 PYTHON JOURNEY - BÀI 01             ║
║              📦 BIẾN TRONG PYTHON               ║
╚══════════════════════════════════════════════════╝

🎯 Mục tiêu:
   • Hiểu biến và kiểu dữ liệu
   • Hoán đổi giá trị biến
   • Augmented assignment
   • Multiple assignment
"""


# ╔════════════════════════════════════════════════╗
# ║                 🚀 BẮT ĐẦU                    ║
# ╚════════════════════════════════════════════════╝

print("\n" + "═" * 55)
print("🐍  PYTHON JOURNEY  |  BÀI TẬP 01: BIẾN")
print("═" * 55)


# ┌────────────────────────────────────────────────┐
# │ 📦 TODO 1: BIẾN VÀ KIỂU DỮ LIỆU                │
# └────────────────────────────────────────────────┘

ten = "Phat"
tuoi = 18
diem_tb = 5.5
dang_hoc = True

print("\n┌" + "─" * 53 + "┐")
print("│ 📦 TODO 1: BIẾN VÀ KIỂU DỮ LIỆU" + " " * 19 + "│")
print("└" + "─" * 53 + "┘")

print(f"  👤 Tên       : {ten}")
print(f"     └─ Kiểu   : {type(ten).__name__}")

print(f"  🎂 Tuổi      : {tuoi}")
print(f"     └─ Kiểu   : {type(tuoi).__name__}")

print(f"  📊 Điểm TB   : {diem_tb}")
print(f"     └─ Kiểu   : {type(diem_tb).__name__}")

print(f"  📚 Đang học  : {dang_hoc}")
print(f"     └─ Kiểu   : {type(dang_hoc).__name__}")


# ┌────────────────────────────────────────────────┐
# │ 🔄 TODO 2: HOÁN ĐỔI BIẾN                       │
# └────────────────────────────────────────────────┘

a = 10
b = 20

print("\n┌" + "─" * 53 + "┐")
print("│ 🔄 TODO 2: HOÁN ĐỔI BIẾN" + " " * 27 + "│")
print("└" + "─" * 53 + "┘")

print(f"  🔴 Trước khi đổi → a = {a}, b = {b}")

a, b = b, a

print(f"  🟢 Sau khi đổi   → a = {a}, b = {b}")


# ┌────────────────────────────────────────────────┐
# │ ➕ TODO 3: AUGMENTED ASSIGNMENT                 │
# └────────────────────────────────────────────────┘

x = 100

print("\n┌" + "─" * 53 + "┐")
print("│ ➕ TODO 3: AUGMENTED ASSIGNMENT" + " " * 20 + "│")
print("└" + "─" * 53 + "┘")

x += 20
print(f"  ➕ x += 20  → {x}")

x -= 10
print(f"  ➖ x -= 10  → {x}")

x *= 2
print(f"  ✖️ x *= 2   → {x}")

x //= 5
print(f"  ➗ x //= 5  → {x}")


# ┌────────────────────────────────────────────────┐
# │ 👤 TODO 4: MULTIPLE ASSIGNMENT                  │
# └────────────────────────────────────────────────┘

ho, ten, tuoi = "Lam", "Phat", 18

print("\n┌" + "─" * 53 + "┐")
print("│ 👤 TODO 4: MULTIPLE ASSIGNMENT" + " " * 21 + "│")
print("└" + "─" * 53 + "┘")

print(f"  📝 Họ tên: {ho} {ten}")
print(f"  🎂 Tuổi : {tuoi}")


# ╔════════════════════════════════════════════════╗
# ║                  🎉 TỔNG KẾT                   ║
# ╚════════════════════════════════════════════════╝

print("\n" + "═" * 55)
print("🎉  HOÀN THÀNH BÀI TẬP 01!")
print("═" * 55)

print("""
📚 Kiến thức đã học:

   ✅ Biến
   ✅ str      → chữ
   ✅ int      → số nguyên
   ✅ float    → số thập phân
   ✅ bool     → True / False
   ✅ type()   → kiểm tra kiểu dữ liệu

   🔄 a, b = b, a
      → Hoán đổi hai biến

   ➕ +=  -=  *=  //=
      → Tính toán và gán lại

   👤 Multiple assignment
      → Gán nhiều biến cùng lúc
""")

print("🐍 Keep learning Python!")
print("⭐ Python Journey - Week 02")
print("═" * 55)
