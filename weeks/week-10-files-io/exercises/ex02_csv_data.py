
import csv
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "match_summary.csv"

path.parent.mkdir(parents=True, exist_ok=True)


# Xem danh sach
def xem_du_lieu():
    if not path.exists() or path.stat().st_size == 0:
        print("\nChưa có dữ liệu!")
        return

    with path.open("r", newline="", encoding="utf-8-sig") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        print("\nDanh sách trống!")
        return

    print("\n========== DANH SÁCH NGƯỜI CHƠI ==========")
    print(f"{'STT':<5} {'Tên người chơi':<25} {'Trận thắng':>10}")
    print("-" * 45)

    for i, row in enumerate(rows, 1):
        print(f"{i:<5} {row['bot']:<25} {row['wins']:>10}")

    print(f"\nTổng số người chơi: {len(rows)}")


# Them nhieu nguoi choi
def them_du_lieu():
    while True:
        try:
            n = int(input("\nNhập số người chơi muốn thêm: "))
            if n <= 0:
                print("Số lượng phải lớn hơn 0!")
                continue
            break
        except ValueError:
            print("Vui lòng nhập số nguyên!")

    rows = []

    for i in range(n):
        print(f"\n--- Người chơi {i + 1}/{n} ---")

        while True:
            name = input("Nhập tên người chơi: ").strip()
            if name:
                break
            print("Tên không được để trống!")

        while True:
            try:
                wins = int(input("Nhập số trận thắng: "))
                if wins < 0:
                    print("Số trận thắng không được âm!")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập số nguyên!")

        rows.append({"bot": name, "wins": wins})

    # Kiem tra file moi
    file_moi = not path.exists() or path.stat().st_size == 0

    # Ghi them, khong ghi de
    with path.open("a", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=["bot", "wins"])

        if file_moi:
            writer.writeheader()

        writer.writerows(rows)

    print(f"\nĐã thêm thành công {len(rows)} người chơi!")


# Menu chinh
def main():
    while True:
        print("\n========== QUẢN LÝ NGƯỜI CHƠI ==========")
        print("1. Xem danh sách người chơi")
        print("2. Thêm nhiều người chơi")
        print("0. Thoát")
        print("========================================")

        choice = input("Chọn chức năng: ").strip()

        if choice == "1":
            xem_du_lieu()
        elif choice == "2":
            them_du_lieu()
        elif choice == "0":
            print("Đã thoát. Dữ liệu được giữ nguyên!")
            break
        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
