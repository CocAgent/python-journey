"""Lời giải Bài tập 03: Scope & Module hóa"""

# TODO 1
x = 10
def thay_doi():
    x = 20  # local x, không ảnh hưởng global x
    print(f"Trong hàm: x = {x}")  # 20

thay_doi()
print(f"Ngoài hàm: x = {x}")  # 10 — global x không đổi

# TODO 2
def them_ghi_chu(danh_sach, noi_dung):
    danh_sach.append(noi_dung)
    print(f"Đã thêm: {noi_dung}")

def xem_ghi_chu(danh_sach):
    if not danh_sach:
        print("Chưa có ghi chú nào.")
        return
    for i, gc in enumerate(danh_sach, 1):
        print(f"{i}. {gc}")

def tim_ghi_chu(danh_sach, tu_khoa):
    ket_qua = [gc for gc in danh_sach if tu_khoa.lower() in gc.lower()]
    if ket_qua:
        for gc in ket_qua:
            print(f"  - {gc}")
    else:
        print("Không tìm thấy.")

def menu():
    notes = []
    while True:
        print("\n1. Thêm  2. Xem  3. Tìm  4. Thoát")
        choice = input("Chọn: ")
        if choice == "1":
            them_ghi_chu(notes, input("Nội dung: "))
        elif choice == "2":
            xem_ghi_chu(notes)
        elif choice == "3":
            tim_ghi_chu(notes, input("Từ khóa: "))
        elif choice == "4":
            break

if __name__ == "__main__":
    menu()
