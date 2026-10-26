s = input("Nhập chuỗi: ")
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
dem = 0
for i in range(x - 1, y):
    if s[i].isdigit():
        dem += 1
print("Số lượng ký tự chữ số:", dem)
