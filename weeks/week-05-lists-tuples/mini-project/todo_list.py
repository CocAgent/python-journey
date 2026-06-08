"""
Mini-Project Week 05: Quan ly Todo List
=========================================
App todo terminal: them/xoa/danh dau hoan thanh/hien thi.
"""

# Mỗi task là một dict với 2 key: "ten" và "hoan_thanh"
todos = []  # list chứa tất cả các task


def hien_thi():
    """In toàn bộ danh sách todo ra màn hình."""
    print("\n=== TODO LIST ===")
    if not todos:                                      # kiểm tra list rỗng
        print("  (Chua co task nao)")
        return
    for i, task in enumerate(todos, start=1):          # enumerate đánh số từ 1
        trang_thai = "[X]" if task["hoan_thanh"] else "[ ]"  # X nếu đã xong
        print(f"  {i}. {trang_thai} {task['ten']}")


def them_task():
    """Thêm task mới vào cuối list."""
    ten = input("  Nhap ten task: ").strip()           # .strip() bỏ khoảng trắng thừa
    if not ten:                                        # không cho nhập rỗng
        print("  Ten task khong duoc de trong!")
        return
    todos.append({"ten": ten, "hoan_thanh": False})   # mặc định chưa hoàn thành
    print(f"  Da them: '{ten}'")


def danh_dau():
    """Đánh dấu hoàn thành một task theo số thứ tự."""
    hien_thi()
    try:
        so = int(input("  Nhap so thu tu task can danh dau: "))
        if 1 <= so <= len(todos):                      # kiểm tra chỉ số hợp lệ
            todos[so - 1]["hoan_thanh"] = True         # chuyển trạng thái thành True
            print(f"  Da hoan thanh: '{todos[so - 1]['ten']}'")
        else:
            print("  So thu tu khong hop le!")
    except ValueError:
        print("  Vui long nhap so nguyen!")            # bắt lỗi nhập sai kiểu


def xoa_task():
    """Xóa task khỏi list theo số thứ tự."""
    hien_thi()
    try:
        so = int(input("  Nhap so thu tu task can xoa: "))
        if 1 <= so <= len(todos):                      # kiểm tra chỉ số hợp lệ
            da_xoa = todos.pop(so - 1)                 # pop() xóa và trả về phần tử
            print(f"  Da xoa: '{da_xoa['ten']}'")
        else:
            print("  So thu tu khong hop le!")
    except ValueError:
        print("  Vui long nhap so nguyen!")


def main():
    """Vòng lặp menu chính của chương trình."""
    while True:                                        # chạy liên tục đến khi chọn Thoat
        print("\n--- MENU ---")
        print("  1. Them task")
        print("  2. Xem danh sach")
        print("  3. Danh dau hoan thanh")
        print("  4. Xoa task")
        print("  5. Thoat")

        chon = input("Chon chuc nang (1-5): ").strip()

        if chon == "1":
            them_task()
        elif chon == "2":
            hien_thi()
        elif chon == "3":
            danh_dau()
        elif chon == "4":
            xoa_task()
        elif chon == "5":
            print("Tam biet!")
            break                                      # thoát vòng lặp → kết thúc chương trình
        else:
            print("  Lua chon khong hop le, vui long thu lai!")


# Điểm vào chương trình: chỉ chạy khi file được chạy trực tiếp
if __name__ == "__main__":
    main()
