from unidecode import unidecode
fname=input("Họ Tên: ")
mssv=input("MSSV: ")
n=input("Ngành: ")
k=input("Khóa: ")
h="THẺ SINH VIÊN"
w=max(len(fname),len(n),len(k),len(h)) + 10

print("╔"+"═"*w+"╗")
print(f"║{h.center(w)}║")
print("║"+"-"*w+"║")
print(f"║{('Họ Tên: ' + fname).ljust(w)}║")
print(f"║{('MSSV: '+mssv).ljust(w)}║")
print(f"║{('Ngành: '+n).ljust(w)}║")
print(f"║{('Khóa: '+k).ljust(w)}║")
print("╚"+"═"*w+"╝")