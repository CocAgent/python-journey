"""
Bài tập 02: Máy tính Python 🧮
================================
Mục tiêu: Sử dụng các phép tính cơ bản trong Python
"""

# TODO 1: Tính và in ra kết quả của 2024 + 1000
print()
print("Tinh va in ra ket qua cua 2024 + 1000")
print("2024 + 1000 =", 2024 + 1000)
print()

# TODO 2: Bạn có 150,000 VNĐ, mua 3 ly cà phê giá 35,000 VNĐ/ly.
# Tính và in ra số tiền còn lại.
print("Ban co 150,000 VND, mua 3 ly ca phe gia 35,000 VND/ly.")
sotienhientai = 150000
print("So tien hien tai:",150000,"VND")
tongcaphe = 35000*3
print("Mua ba ly ca phe gia 35.000 VND:", tongcaphe)
print("So tien con lai:", sotienhientai-tongcaphe)
print()

# TODO 3: Tính diện tích hình tròn có bán kính = 7
# Gợi ý: Diện tích = 3.14159 * bán_kính ** 2
print("Cho hinh tron co ban kinh la 7, tinh dien tich")
bankinh = 7
dthinhtron = round(3.14159 * bankinh ** 2,2)
print("Dien tich hinh tron la:", dthinhtron)
print()

# TODO 4: Bạn có 100 viên kẹo chia đều cho 7 người.
# In ra: mỗi người được bao nhiêu viên (chia nguyên)?
# In ra: còn dư bao nhiêu viên?
# Gợi ý: Dùng // và %
print("Ban co 100 vien keo chia deu cho 7 nguoi")
duocvienkeo = 100 // 7
keodu = 100 % 7
print("Moi nguoi duoc",duocvienkeo,"vien keo")
print("Con du",keodu,"vien keo")
print()

# TODO 5 (Thử thách): Chuyển đổi 37 độ C sang Fahrenheit
# Công thức: F = C * 9/5 + 32
# In ra kết quả dạng: "37°C = ???°F"
print("chuyen doi 37 do C sang Fahrenheit")
C = 37
F = C * 9/5 + 32
print(C,"°C =",F,"°F")
