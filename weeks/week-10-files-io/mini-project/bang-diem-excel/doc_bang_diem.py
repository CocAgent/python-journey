
from pathlib import Path
import csv
import json

# Đường dẫn thư mục chứa chương trình
THU_MUC = Path(__file__).resolve().parent


# ==========================================
# 1. ĐỌC FILE TXT, CSV, JSON
# ==========================================

def doc_file(loai):
    if loai == "1":
        path = THU_MUC / "bang_diem.txt"

        with path.open("r", encoding="utf-8-sig") as f:
            noi_dung = f.read().strip()

        if not noi_dung:
            return []

        # Hỗ trợ TXT dạng mỗi dòng là JSON
        if noi_dung.startswith("{"):
            return [
                json.loads(dong)
                for dong in noi_dung.splitlines()
                if dong.strip()
            ]

        # Hỗ trợ TXT cũ: MSSV | HoTen | Lop | DiemQT
        ds = []

        for dong in noi_dung.splitlines():
            cot = [x.strip() for x in dong.split("|")]

            if len(cot) == 4:
                ds.append({
                    "MSSV": cot[0],
                    "HoTen": cot[1],
                    "Lop": cot[2],
                    "DiemQT": cot[3],
                    "CacBuoi": []
                })

        return ds

    elif loai == "2":
        path = THU_MUC / "bang_diem.csv"

        with path.open(
            "r", encoding="utf-8-sig", newline=""
        ) as f:
            ds = list(csv.DictReader(f))

        for sv in ds:
            du_lieu = sv.get("CacBuoi", "")

            if du_lieu:
                sv["CacBuoi"] = json.loads(du_lieu)
            else:
                sv["CacBuoi"] = []

        return ds

    elif loai == "3":
        path = THU_MUC / "bang_diem.json"

        with path.open("r", encoding="utf-8-sig") as f:
            ds = json.load(f)

        for sv in ds:
            sv.setdefault("CacBuoi", [])

        return ds

    return []


# ==========================================
# 2. HIỂN THỊ THÔNG TIN SINH VIÊN
# ==========================================

def hien_thi(sv):
    print("-" * 40)
    print("MSSV:", sv["MSSV"])
    print("Họ tên:", sv["HoTen"])
    print("Lớp:", sv["Lop"])
    print("Điểm quá trình:", sv["DiemQT"])


# ==========================================
# 3. TÌM SINH VIÊN THEO MSSV
# ==========================================

def tim_sinh_vien(ds):
    mssv = input("Nhập MSSV: ").strip()

    for sv in ds:
        if str(sv["MSSV"]).strip() == mssv:
            return sv

    print("Không tìm thấy sinh viên!")
    return None


# ==========================================
# 4. LẤY DANH SÁCH ĐIỂM HỢP LỆ
# ==========================================

def lay_diem_hop_le(ds):
    ket_qua = []

    for sv in ds:
        try:
            diem = float(sv["DiemQT"])
            ket_qua.append((sv, diem))

        except (ValueError, TypeError):
            continue

    return ket_qua


# ==========================================
# 5. XEM SINH VIÊN Ở DÒNG BẤT KỲ
# ==========================================

def xem_dong(ds):
    try:
        dong = int(
            input(f"Nhập số dòng từ 1 đến {len(ds)}: ")
        )

        if 1 <= dong <= len(ds):
            print(f"\n===== SINH VIÊN DÒNG {dong} =====")
            hien_thi(ds[dong - 1])
        else:
            print("Số dòng không hợp lệ!")

    except ValueError:
        print("Vui lòng nhập số nguyên!")


# ==========================================
# 6. XEM N SINH VIÊN TỪ DÒNG BẤT KỲ
# ==========================================

def xem_n_sinh_vien(ds):
    try:
        bat_dau = int(input("Nhập dòng bắt đầu: "))
        so_luong = int(
            input("Nhập số sinh viên muốn xem: ")
        )

        if bat_dau < 1 or bat_dau > len(ds):
            print("Dòng bắt đầu không hợp lệ!")
            return

        if so_luong <= 0:
            print("Số lượng phải lớn hơn 0!")
            return

        ket_thuc = min(
            bat_dau - 1 + so_luong,
            len(ds)
        )

        print("\n===== DANH SÁCH SINH VIÊN =====")

        for i in range(bat_dau - 1, ket_thuc):
            print(f"\nSinh viên dòng {i + 1}")
            hien_thi(ds[i])

        print(
            f"\nĐã hiển thị {ket_thuc - bat_dau + 1} "
            "sinh viên."
        )

    except ValueError:
        print("Vui lòng nhập số nguyên!")


# ==========================================
# 7. XEM ĐIỂM MỘT BUỔI THEO MSSV
# ==========================================

def xem_diem_buoi(ds):
    sv = tim_sinh_vien(ds)

    if sv is None:
        return

    cac_buoi = sv.get("CacBuoi", [])

    if not cac_buoi:
        print("Chưa có dữ liệu điểm từng buổi.")
        print(
            "Cần chuyển lại file Excel để "
            "bổ sung dữ liệu CacBuoi."
        )
        return

    print("\n===== CÁC BUỔI HỌC =====")

    for buoi in cac_buoi:
        print(buoi.get("Bai", ""))

    ten = input(
        "\nNhập tên buổi học (VD: B3LT): "
    ).strip()

    ten = ten.replace(" ", "").upper()

    for buoi in cac_buoi:
        ten_bai = str(
            buoi.get("Bai", "")
        ).replace(" ", "").upper()

        if ten_bai == ten:
            print("\n===== KẾT QUẢ TRA CỨU =====")
            print("MSSV:", sv["MSSV"])
            print("Họ tên:", sv["HoTen"])
            print("Buổi học:", buoi.get("Bai"))
            print("Ngày:", buoi.get("Ngay"))

            diem = buoi.get("Diem")

            if diem is None or diem == "":
                print("Điểm: Chưa có điểm")
            else:
                print("Điểm:", diem)

            return

    print("Không tìm thấy buổi học!")


# ==========================================
# 8. XEM THỨ HẠNG CỦA MỘT SINH VIÊN
# ==========================================

def xem_thu_hang(ds):
    sv = tim_sinh_vien(ds)

    if sv is None:
        return

    hop_le = lay_diem_hop_le(ds)

    try:
        diem_ban = float(sv["DiemQT"])

    except (ValueError, TypeError):
        print("Sinh viên chưa có điểm hợp lệ.")
        return

    hang = 1 + sum(
        diem > diem_ban
        for _, diem in hop_le
    )

    print("\n===== THỨ HẠNG SINH VIÊN =====")

    hien_thi(sv)

    print(f"Thứ hạng: {hang}/{len(hop_le)}")


# ==========================================
# 9. XEM ĐIỂM CAO NHẤT VÀ THẤP NHẤT
# ==========================================

def xem_cao_thap(ds):
    hop_le = lay_diem_hop_le(ds)

    if not hop_le:
        print("Không có điểm hợp lệ.")
        return

    cao = max(diem for _, diem in hop_le)
    thap = min(diem for _, diem in hop_le)

    print("\n===== SINH VIÊN ĐIỂM CAO NHẤT =====")

    for sv, diem in hop_le:
        if diem == cao:
            hien_thi(sv)

    print("\n===== SINH VIÊN ĐIỂM THẤP NHẤT =====")

    for sv, diem in hop_le:
        if diem == thap:
            hien_thi(sv)


# ==========================================
# 10. ĐÁNH GIÁ NGUY CƠ RỚT MÔN
# ==========================================

def xem_nguy_co_rot(ds):
    print("\n===== ĐÁNH GIÁ NGUY CƠ RỚT MÔN =====")
    print("1. Nguy cơ cao: Điểm QT dưới 4")
    print("2. Nguy cơ trung bình: Từ 4 đến dưới 5")
    print("3. Xem tất cả sinh viên có điểm QT dưới 5")

    chon = input("Chọn mức nguy cơ: ").strip()

    if chon not in ("1", "2", "3"):
        print("Lựa chọn không hợp lệ!")
        return

    ket_qua = []

    for sv, diem in lay_diem_hop_le(ds):

        if diem < 4:
            muc_do = "Cao"

        elif diem < 5:
            muc_do = "Trung bình"

        else:
            continue

        if chon == "1" and diem >= 4:
            continue

        if chon == "2" and not (4 <= diem < 5):
            continue

        ket_qua.append((sv, diem, muc_do))

    # Sắp xếp từ điểm thấp đến cao
    ket_qua.sort(key=lambda x: x[1])

    if not ket_qua:
        print("Không có sinh viên thuộc nhóm này.")
        return

    print("\n===== DANH SÁCH CẢNH BÁO =====")

    for stt, (sv, diem, muc_do) in enumerate(
        ket_qua, start=1
    ):
        print(f"\n{stt}. {sv['HoTen']}")
        print("MSSV:", sv["MSSV"])
        print("Lớp:", sv["Lop"])
        print("Điểm quá trình:", diem)
        print("Mức nguy cơ:", muc_do)

    print("\nTổng số sinh viên:", len(ket_qua))

    print(
        "\nLưu ý: Đây là phân loại tham khảo "
        "theo điểm quá trình, không phải "
        "xác suất rớt môn thực tế."
    )


# ==========================================
# 11. MENU CHÍNH
# ==========================================

def main():
    print("\n========== QUẢN LÝ BẢNG ĐIỂM ==========")

    print("\nCHỌN ĐỊNH DẠNG FILE:")
    print("1. TXT")
    print("2. CSV")
    print("3. JSON")

    loai = input("Chọn định dạng: ").strip()

    if loai not in ("1", "2", "3"):
        print("Định dạng không hợp lệ!")
        return

    try:
        ds = doc_file(loai)

    except (
        FileNotFoundError,
        json.JSONDecodeError,
        UnicodeDecodeError,
        KeyError,
        TypeError
    ) as loi:
        print("Lỗi đọc file:", loi)
        return

    if not ds:
        print("Không có dữ liệu sinh viên!")
        return

    print(f"\nĐã đọc thành công {len(ds)} sinh viên.")

    while True:
        print("\n========== CHỨC NĂNG ==========")
        print("1. Xem sinh viên ở dòng bất kỳ")
        print("2. Xem N sinh viên")
        print("3. Tìm một sinh viên theo MSSV")
        print("4. Xem điểm một buổi theo MSSV")
        print("5. Xem thứ hạng của một sinh viên")
        print("6. Xem điểm cao nhất và thấp nhất")
        print("7. Xem sinh viên có nguy cơ rớt môn cao")
        print("0. Thoát")

        chon = input("\nChọn chức năng: ").strip()

        if chon == "1":
            xem_dong(ds)

        elif chon == "2":
            xem_n_sinh_vien(ds)

        elif chon == "3":
            sv = tim_sinh_vien(ds)

            if sv is not None:
                hien_thi(sv)

        elif chon == "4":
            xem_diem_buoi(ds)

        elif chon == "5":
            xem_thu_hang(ds)

        elif chon == "6":
            xem_cao_thap(ds)

        elif chon == "7":
            xem_nguy_co_rot(ds)

        elif chon == "0":
            print("\nĐã thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ!")


# ==========================================
# 12. CHẠY CHƯƠNG TRÌNH
# ==========================================

if __name__ == "__main__":
    main()
