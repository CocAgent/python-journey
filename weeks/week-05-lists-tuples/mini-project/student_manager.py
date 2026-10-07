"""Hệ thống Quản lý Sinh viên — Week 05 mini-project.

Dùng list-of-lists để lưu danh sách sinh viên.
Mỗi sinh viên là một list: [mã_sv, họ_tên, tuổi, ngày_sinh, giới_tính, điểm_tb].

Chức năng: thêm, xem, cập nhật, xóa, tìm kiếm, sắp xếp, thống kê, xếp loại.
"""

import os

# ─── Cấu hình hiển thị ──────────────────────────────────────────────
# Độ rộng cột trong bảng hiển thị
DO_RONG_STT = 4
DO_RONG_MASV = 10
DO_RONG_HOTEN = 22
DO_RONG_TUOI = 6
DO_RONG_NGAYSINH = 14
DO_RONG_GIOITINH = 10
DO_RONG_DIEM = 8
DO_RONG_XEPLOAI = 12

TONG_DO_RONG = (
    DO_RONG_STT + DO_RONG_MASV + DO_RONG_HOTEN + DO_RONG_TUOI
    + DO_RONG_NGAYSINH + DO_RONG_GIOITINH + DO_RONG_DIEM + DO_RONG_XEPLOAI
    + 9  # 9 dấu phân cách │
)

# ─── Danh sách sinh viên ─────────────────────────────────────────────
danh_sach = []


# ═══════════════════════════════════════════════════════════════════════
#  PHẦN 1: HÀM TIỆN ÍCH
# ═══════════════════════════════════════════════════════════════════════

def xoa_man_hinh():
    """Xóa màn hình console."""
    os.system("cls" if os.name == "nt" else "clear")


def nhan_enter():
    """Dừng lại để người dùng đọc kết quả."""
    input("\n  ⏎  Nhấn Enter để tiếp tục...")


def duong_ke_ngang(kieu="giua"):
    """Vẽ đường kẻ ngang cho bảng.

    kieu: 'tren' (đầu bảng), 'giua' (ngăn cách), 'duoi' (cuối bảng).
    """
    goc_trai = {"tren": "┌", "giua": "├", "duoi": "└"}
    giao = {"tren": "┬", "giua": "┼", "duoi": "┴"}
    goc_phai = {"tren": "┐", "giua": "┤", "duoi": "┘"}

    cac_do_rong = [
        DO_RONG_STT, DO_RONG_MASV, DO_RONG_HOTEN, DO_RONG_TUOI,
        DO_RONG_NGAYSINH, DO_RONG_GIOITINH, DO_RONG_DIEM, DO_RONG_XEPLOAI,
    ]
    phan_than = []
    for w in cac_do_rong:
        phan_than.append("─" * w)
    return goc_trai[kieu] + giao[kieu].join(phan_than) + goc_phai[kieu]


def dong_du_lieu(stt, masv, hoten, tuoi, ngaysinh, gioitinh, diem, xeploai):
    """Tạo một dòng dữ liệu trong bảng với cột căn chỉnh."""
    stt_str = str(stt).center(DO_RONG_STT)
    masv_str = str(masv).center(DO_RONG_MASV)

    # Họ tên cần xử lý đặc biệt vì tiếng Việt có ký tự Unicode rộng
    hoten_str = str(hoten).ljust(DO_RONG_HOTEN)
    if len(hoten_str) > DO_RONG_HOTEN:
        hoten_str = hoten_str[:DO_RONG_HOTEN - 1] + "…"

    tuoi_str = str(tuoi).center(DO_RONG_TUOI)
    ngaysinh_str = str(ngaysinh).center(DO_RONG_NGAYSINH)
    gioitinh_str = str(gioitinh).center(DO_RONG_GIOITINH)
    diem_str = str(diem).center(DO_RONG_DIEM)
    xeploai_str = str(xeploai).center(DO_RONG_XEPLOAI)

    return (
        "│" + stt_str
        + "│" + masv_str
        + "│" + hoten_str
        + "│" + tuoi_str
        + "│" + ngaysinh_str
        + "│" + gioitinh_str
        + "│" + diem_str
        + "│" + xeploai_str
        + "│"
    )


def dong_tieu_de():
    """Tạo dòng tiêu đề của bảng."""
    return dong_du_lieu("STT", "Mã SV", "Họ tên", "Tuổi",
                        "Ngày sinh", "Giới tính", "Điểm", "Xếp loại")


def xep_loai_hoc_luc(diem):
    """Trả về xếp loại học lực dựa trên điểm trung bình.

    Quy tắc:
        >= 9.0 : Xuất sắc
        >= 8.0 : Giỏi
        >= 6.5 : Khá
        >= 5.0 : Trung bình
        >= 3.5 : Yếu
        <  3.5 : Kém
    """
    if diem >= 9.0:
        return "Xuất sắc"
    if diem >= 8.0:
        return "Giỏi"
    if diem >= 6.5:
        return "Khá"
    if diem >= 5.0:
        return "Trung bình"
    if diem >= 3.5:
        return "Yếu"
    return "Kém"


def tim_sinh_vien(masv):
    """Tìm sinh viên theo mã SV.

    Trả về index nếu tìm thấy, -1 nếu không.
    """
    for i in range(len(danh_sach)):
        if danh_sach[i][0].lower() == masv.lower():
            return i
    return -1


def nhap_diem():
    """Nhập và validate điểm trung bình (0.0 – 10.0)."""
    while True:
        diem_str = input("  Nhập điểm trung bình (0-10): ").strip()
        try:
            diem = float(diem_str)
            if 0.0 <= diem <= 10.0:
                return round(diem, 1)
            print("  ⚠ Điểm phải nằm trong khoảng 0 – 10.")
        except ValueError:
            print("  ⚠ Vui lòng nhập một số hợp lệ.")


def nhap_tuoi():
    """Nhập và validate tuổi (15 – 100)."""
    while True:
        tuoi_str = input("  Nhập tuổi (15-100): ").strip()
        if tuoi_str.isdigit():
            tuoi = int(tuoi_str)
            if 15 <= tuoi <= 100:
                return tuoi
            print("  ⚠ Tuổi phải từ 15 đến 100.")
        else:
            print("  ⚠ Vui lòng nhập một số nguyên.")


def nhap_gioi_tinh():
    """Nhập và validate giới tính."""
    gioi_tinh_hop_le = ("nam", "nữ", "nu", "khác", "khac")
    while True:
        gt = input("  Nhập giới tính (Nam/Nữ/Khác): ").strip()
        if gt.lower() in gioi_tinh_hop_le:
            # Chuẩn hóa về dạng viết hoa đầu
            if gt.lower() in ("nam",):
                return "Nam"
            if gt.lower() in ("nữ", "nu"):
                return "Nữ"
            return "Khác"
        print("  ⚠ Vui lòng nhập Nam, Nữ hoặc Khác.")


def nhap_thong_tin_sv():
    """Nhập thông tin đầy đủ một sinh viên.

    Trả về list [masv, hoten, tuoi, ngay_sinh, gioi_tinh, diem_tb].
    """
    while True:
        masv = input("  Mã sinh viên : ").strip()
        if masv:
            break
        print("  ⚠ Mã SV không được để trống.")

    while True:
        hoten = input("  Họ và tên    : ").strip()
        if hoten:
            break
        print("  ⚠ Họ tên không được để trống.")

    tuoi = nhap_tuoi()

    ngay_sinh = input("  Ngày sinh    : ").strip()
    if not ngay_sinh:
        ngay_sinh = "N/A"

    gioi_tinh = nhap_gioi_tinh()
    diem_tb = nhap_diem()

    return [masv, hoten, tuoi, ngay_sinh, gioi_tinh, diem_tb]


def in_bang(ds, tieu_de=""):
    """In danh sách sinh viên dưới dạng bảng chuyên nghiệp."""
    if not ds:
        print("\n  📋 Không có dữ liệu để hiển thị.")
        return

    if tieu_de:
        print(f"\n  {tieu_de}")

    print(duong_ke_ngang("tren"))
    print(dong_tieu_de())
    print(duong_ke_ngang("giua"))

    for i in range(len(ds)):
        masv, hoten, tuoi, ngaysinh, gioitinh, diem = ds[i]  # unpacking
        xeploai = xep_loai_hoc_luc(diem)
        print(dong_du_lieu(i + 1, masv, hoten, tuoi, ngaysinh,
                           gioitinh, diem, xeploai))

    print(duong_ke_ngang("duoi"))
    print(f"  Tổng: {len(ds)} sinh viên")


def hien_thi_chi_tiet(sv):
    """Hiển thị thông tin chi tiết một sinh viên theo dạng card."""
    masv, hoten, tuoi, ngaysinh, gioitinh, diem = sv  # tuple unpacking
    xeploai = xep_loai_hoc_luc(diem)

    print("  ┌─────────────────────────────────────┐")
    print(f"  │  🎓 {hoten:<33}│")
    print("  ├─────────────────────────────────────┤")
    print(f"  │  Mã SV      : {masv:<22}│")
    print(f"  │  Tuổi       : {tuoi:<22}│")
    print(f"  │  Ngày sinh  : {ngaysinh:<22}│")
    print(f"  │  Giới tính  : {gioitinh:<22}│")
    print(f"  │  Điểm TB    : {diem:<22}│")
    print(f"  │  Xếp loại   : {xeploai:<22}│")
    print("  └─────────────────────────────────────┘")


def hien_thi_menu():
    """Hiển thị menu chính."""
    print()
    print("  ╔═══════════════════════════════════════╗")
    print("  ║     🎓  HỆ THỐNG QUẢN LÝ SINH VIÊN   ║")
    print("  ╠═══════════════════════════════════════╣")
    print("  ║                                       ║")
    print("  ║   1.  📝  Thêm sinh viên              ║")
    print("  ║   2.  📋  Xem danh sách               ║")
    print("  ║   3.  🔍  Tìm kiếm sinh viên          ║")
    print("  ║   4.  ✏️   Cập nhật thông tin           ║")
    print("  ║   5.  🗑️   Xóa sinh viên               ║")
    print("  ║   6.  📊  Sắp xếp danh sách           ║")
    print("  ║   7.  📈  Thống kê & Xếp loại         ║")
    print("  ║   8.  📄  Xuất báo cáo                 ║")
    print("  ║   0.  🚪  Thoát                        ║")
    print("  ║                                       ║")
    print("  ╚═══════════════════════════════════════╝")
    so_sv = len(danh_sach)
    if so_sv > 0:
        print(f"  📌 Hiện có {so_sv} sinh viên trong hệ thống")
    print()


# ═══════════════════════════════════════════════════════════════════════
#  PHẦN 2: CÁC CHỨC NĂNG CHÍNH
# ═══════════════════════════════════════════════════════════════════════

def them_sinh_vien():
    """Thêm một hoặc nhiều sinh viên vào danh sách."""
    print("\n  ── THÊM SINH VIÊN ──")

    while True:
        so_luong_str = input("\n  Số lượng SV cần thêm (0 để hủy): ").strip()
        if so_luong_str == "0":
            print("  ↩ Đã hủy thao tác.")
            return
        if so_luong_str.isdigit() and int(so_luong_str) > 0:
            so_luong = int(so_luong_str)
            break
        print("  ⚠ Vui lòng nhập số nguyên dương.")

    dem_thanh_cong = 0
    for i in range(so_luong):
        print(f"\n  ╌╌╌ Sinh viên {i + 1}/{so_luong} ╌╌╌")
        sv = nhap_thong_tin_sv()

        # Kiểm tra mã SV trùng
        if tim_sinh_vien(sv[0]) != -1:
            print(f"  ⚠ Mã SV '{sv[0]}' đã tồn tại — bỏ qua.")
            continue

        danh_sach.append(sv)
        dem_thanh_cong = dem_thanh_cong + 1
        print(f"  ✅ Đã thêm '{sv[1]}' thành công.")

    print(f"\n  ── Kết quả: thêm {dem_thanh_cong}/{so_luong} sinh viên ──")


def xem_danh_sach():
    """Hiển thị toàn bộ danh sách sinh viên dưới dạng bảng."""
    print("\n  ── DANH SÁCH SINH VIÊN ──")

    if not danh_sach:
        print("  📋 Danh sách trống. Hãy thêm sinh viên trước.")
        return

    in_bang(danh_sach, "📋 BẢNG DANH SÁCH SINH VIÊN")


def tim_kiem_sinh_vien():
    """Tìm kiếm sinh viên theo nhiều tiêu chí."""
    print("\n  ── TÌM KIẾM SINH VIÊN ──")

    if not danh_sach:
        print("  📋 Danh sách trống.")
        return

    print("  Tìm kiếm theo:")
    print("    1. Mã sinh viên")
    print("    2. Họ tên")
    print("    3. Giới tính")
    print("    4. Xếp loại học lực")
    print("    0. Quay lại")

    lua_chon = input("  Chọn (0-4): ").strip()

    if lua_chon == "0":
        return

    if lua_chon == "1":
        masv = input("  Nhập mã SV: ").strip()
        vi_tri = tim_sinh_vien(masv)
        if vi_tri == -1:
            print(f"  ❌ Không tìm thấy SV có mã '{masv}'.")
        else:
            print()
            hien_thi_chi_tiet(danh_sach[vi_tri])

    elif lua_chon == "2":
        tu_khoa = input("  Nhập tên cần tìm: ").strip().lower()
        if not tu_khoa:
            print("  ⚠ Vui lòng nhập từ khóa.")
            return
        ket_qua = []
        for i in range(len(danh_sach)):
            if tu_khoa in danh_sach[i][1].lower():
                ket_qua.append(danh_sach[i])
        if not ket_qua:
            print(f"  ❌ Không tìm thấy SV có tên chứa '{tu_khoa}'.")
        else:
            in_bang(ket_qua, f"🔍 Kết quả tìm kiếm: '{tu_khoa}'")

    elif lua_chon == "3":
        gt = input("  Nhập giới tính (Nam/Nữ/Khác): ").strip()
        ket_qua = []
        for i in range(len(danh_sach)):
            if danh_sach[i][4].lower() == gt.lower():
                ket_qua.append(danh_sach[i])
        if not ket_qua:
            print(f"  ❌ Không tìm thấy SV giới tính '{gt}'.")
        else:
            in_bang(ket_qua, f"🔍 Sinh viên giới tính: {gt}")

    elif lua_chon == "4":
        print("  Xếp loại: Xuất sắc / Giỏi / Khá / Trung bình / Yếu / Kém")
        xl = input("  Nhập xếp loại: ").strip().lower()
        ket_qua = []
        for i in range(len(danh_sach)):
            if xep_loai_hoc_luc(danh_sach[i][5]).lower() == xl:
                ket_qua.append(danh_sach[i])
        if not ket_qua:
            print(f"  ❌ Không tìm thấy SV xếp loại '{xl}'.")
        else:
            in_bang(ket_qua, f"🔍 Sinh viên xếp loại: {xl.title()}")

    else:
        print("  ⚠ Lựa chọn không hợp lệ.")


def cap_nhat_sinh_vien():
    """Cập nhật thông tin sinh viên theo mã SV."""
    print("\n  ── CẬP NHẬT THÔNG TIN ──")

    if not danh_sach:
        print("  📋 Danh sách trống.")
        return

    masv = input("  Nhập mã SV cần cập nhật: ").strip()
    vi_tri = tim_sinh_vien(masv)

    if vi_tri == -1:
        print(f"  ❌ Không tìm thấy SV có mã '{masv}'.")
        return

    print("\n  Thông tin hiện tại:")
    hien_thi_chi_tiet(danh_sach[vi_tri])

    print("\n  Cập nhật:")
    print("    1. Cập nhật toàn bộ")
    print("    2. Chỉ cập nhật điểm")
    print("    3. Chỉ cập nhật họ tên")
    print("    0. Hủy")
    chon = input("  Chọn (0-3): ").strip()

    if chon == "0":
        print("  ↩ Đã hủy.")
        return

    if chon == "1":
        print("\n  📝 Nhập thông tin mới:")
        sv_moi = nhap_thong_tin_sv()
        # Nếu đổi mã SV, kiểm tra trùng
        if sv_moi[0].lower() != masv.lower() and tim_sinh_vien(sv_moi[0]) != -1:
            print(f"  ⚠ Mã SV '{sv_moi[0]}' đã tồn tại — hủy cập nhật.")
            return
        danh_sach[vi_tri] = sv_moi

    elif chon == "2":
        diem_moi = nhap_diem()
        danh_sach[vi_tri][5] = diem_moi

    elif chon == "3":
        while True:
            ten_moi = input("  Họ tên mới: ").strip()
            if ten_moi:
                break
            print("  ⚠ Họ tên không được để trống.")
        danh_sach[vi_tri][1] = ten_moi

    else:
        print("  ⚠ Lựa chọn không hợp lệ.")
        return

    print("  ✅ Cập nhật thành công!")
    print("\n  Thông tin sau cập nhật:")
    hien_thi_chi_tiet(danh_sach[vi_tri])


def xoa_sinh_vien():
    """Xóa sinh viên theo mã SV, có xác nhận."""
    print("\n  ── XÓA SINH VIÊN ──")

    if not danh_sach:
        print("  📋 Danh sách trống.")
        return

    masv = input("  Nhập mã SV cần xóa: ").strip()
    vi_tri = tim_sinh_vien(masv)

    if vi_tri == -1:
        print(f"  ❌ Không tìm thấy SV có mã '{masv}'.")
        return

    print("\n  Sinh viên sẽ bị xóa:")
    hien_thi_chi_tiet(danh_sach[vi_tri])

    xac_nhan = input("\n  ⚠ Bạn chắc chắn muốn xóa? (c/k): ").strip().lower()
    if xac_nhan == "c":
        sv_xoa = danh_sach.pop(vi_tri)
        print(f"  ✅ Đã xóa sinh viên '{sv_xoa[1]}' thành công.")
    else:
        print("  ↩ Đã hủy thao tác xóa.")


def sap_xep_danh_sach():
    """Sắp xếp danh sách sinh viên theo nhiều tiêu chí."""
    print("\n  ── SẮP XẾP DANH SÁCH ──")

    if not danh_sach:
        print("  📋 Danh sách trống.")
        return

    print("  Sắp xếp theo:")
    print("    1. Họ tên (A → Z)")
    print("    2. Họ tên (Z → A)")
    print("    3. Điểm TB (cao → thấp)")
    print("    4. Điểm TB (thấp → cao)")
    print("    5. Tuổi (tăng dần)")
    print("    6. Tuổi (giảm dần)")
    print("    7. Mã SV (tăng dần)")
    print("    0. Hủy")

    lua_chon = input("  Chọn (0-7): ").strip()

    if lua_chon == "0":
        return

    if lua_chon == "1":
        danh_sach.sort(key=lambda sv: sv[1].lower())
        mo_ta = "họ tên A → Z"
    elif lua_chon == "2":
        danh_sach.sort(key=lambda sv: sv[1].lower(), reverse=True)
        mo_ta = "họ tên Z → A"
    elif lua_chon == "3":
        danh_sach.sort(key=lambda sv: sv[5], reverse=True)
        mo_ta = "điểm TB cao → thấp"
    elif lua_chon == "4":
        danh_sach.sort(key=lambda sv: sv[5])
        mo_ta = "điểm TB thấp → cao"
    elif lua_chon == "5":
        danh_sach.sort(key=lambda sv: sv[2])
        mo_ta = "tuổi tăng dần"
    elif lua_chon == "6":
        danh_sach.sort(key=lambda sv: sv[2], reverse=True)
        mo_ta = "tuổi giảm dần"
    elif lua_chon == "7":
        danh_sach.sort(key=lambda sv: sv[0].lower())
        mo_ta = "mã SV tăng dần"
    else:
        print("  ⚠ Lựa chọn không hợp lệ.")
        return

    print(f"  ✅ Đã sắp xếp theo {mo_ta}.")
    in_bang(danh_sach)


def thong_ke():
    """Hiển thị thống kê tổng hợp và phân bổ xếp loại."""
    print("\n  ── THỐNG KÊ & XẾP LOẠI ──")

    if not danh_sach:
        print("  📋 Danh sách trống.")
        return

    tong = len(danh_sach)

    # Tính toán thống kê tuổi và điểm
    tong_tuoi = 0
    tong_diem = 0.0
    tuoi_min = danh_sach[0][2]
    tuoi_max = danh_sach[0][2]
    diem_min = danh_sach[0][5]
    diem_max = danh_sach[0][5]
    sv_diem_cao_nhat = danh_sach[0]
    sv_diem_thap_nhat = danh_sach[0]

    dem_nam = 0
    dem_nu = 0
    dem_khac = 0

    # Đếm theo xếp loại
    dem_xuat_sac = 0
    dem_gioi = 0
    dem_kha = 0
    dem_trung_binh = 0
    dem_yeu = 0
    dem_kem = 0

    for i in range(tong):
        sv = danh_sach[i]
        masv, hoten, tuoi, ngaysinh, gioitinh, diem = sv  # unpacking

        tong_tuoi = tong_tuoi + tuoi
        tong_diem = tong_diem + diem

        if tuoi < tuoi_min:
            tuoi_min = tuoi
        if tuoi > tuoi_max:
            tuoi_max = tuoi
        if diem > diem_max:
            diem_max = diem
            sv_diem_cao_nhat = sv
        if diem < diem_min:
            diem_min = diem
            sv_diem_thap_nhat = sv

        # Đếm giới tính
        if gioitinh == "Nam":
            dem_nam = dem_nam + 1
        elif gioitinh == "Nữ":
            dem_nu = dem_nu + 1
        else:
            dem_khac = dem_khac + 1

        # Đếm xếp loại
        xl = xep_loai_hoc_luc(diem)
        if xl == "Xuất sắc":
            dem_xuat_sac = dem_xuat_sac + 1
        elif xl == "Giỏi":
            dem_gioi = dem_gioi + 1
        elif xl == "Khá":
            dem_kha = dem_kha + 1
        elif xl == "Trung bình":
            dem_trung_binh = dem_trung_binh + 1
        elif xl == "Yếu":
            dem_yeu = dem_yeu + 1
        else:
            dem_kem = dem_kem + 1

    tuoi_tb = tong_tuoi / tong
    diem_tb = tong_diem / tong

    # Tính tỷ lệ đạt (>= 5.0)
    so_dat = dem_xuat_sac + dem_gioi + dem_kha + dem_trung_binh
    ty_le_dat = (so_dat / tong) * 100

    # Hiển thị
    print()
    print("  ╔═══════════════════════════════════════╗")
    print("  ║         📊  BÁO CÁO THỐNG KÊ         ║")
    print("  ╠═══════════════════════════════════════╣")
    print(f"  ║  Tổng số sinh viên : {tong:<17}║")
    print(f"  ║  Nam / Nữ / Khác   : {dem_nam} / {dem_nu} / {dem_khac:<10}║")
    print("  ╠═══════════════════════════════════════╣")
    print(f"  ║  Tuổi TB           : {tuoi_tb:<17.1f}║")
    print(f"  ║  Tuổi nhỏ nhất     : {tuoi_min:<17}║")
    print(f"  ║  Tuổi lớn nhất     : {tuoi_max:<17}║")
    print("  ╠═══════════════════════════════════════╣")
    print(f"  ║  Điểm TB chung     : {diem_tb:<17.2f}║")
    print(f"  ║  Điểm cao nhất     : {diem_max:<17}║")
    print(f"  ║  Điểm thấp nhất    : {diem_min:<17}║")
    print(f"  ║  Tỷ lệ đạt (≥5.0) : {ty_le_dat:<16.1f}%║")
    print("  ╠═══════════════════════════════════════╣")
    print("  ║       PHÂN BỔ XẾP LOẠI HỌC LỰC       ║")
    print("  ╠═══════════════════════════════════════╣")

    # Thanh tiến trình cho mỗi xếp loại
    cac_xep_loai = [
        ("Xuất sắc  ", dem_xuat_sac),
        ("Giỏi      ", dem_gioi),
        ("Khá       ", dem_kha),
        ("Trung bình", dem_trung_binh),
        ("Yếu       ", dem_yeu),
        ("Kém       ", dem_kem),
    ]
    for ten, so_luong in cac_xep_loai:  # tuple unpacking
        if tong > 0:
            ty_le = (so_luong / tong) * 100
            so_o = int(ty_le / 5)  # mỗi ô = 5%
            thanh = "█" * so_o + "░" * (20 - so_o)
            print(f"  ║  {ten}: {thanh} {so_luong:>2} ({ty_le:>5.1f}%)║")

    print("  ╚═══════════════════════════════════════╝")

    # Top sinh viên
    print(f"\n  🏆 Điểm cao nhất : {sv_diem_cao_nhat[1]} ({sv_diem_cao_nhat[5]})")
    print(f"  📉 Điểm thấp nhất: {sv_diem_thap_nhat[1]} ({sv_diem_thap_nhat[5]})")


def xuat_bao_cao():
    """Xuất báo cáo tổng hợp ra màn hình."""
    print("\n  ── XUẤT BÁO CÁO ──")

    if not danh_sach:
        print("  📋 Danh sách trống.")
        return

    xoa_man_hinh()
    print()
    print("  " + "=" * 50)
    print("       BÁO CÁO TỔNG HỢP DANH SÁCH SINH VIÊN")
    print("  " + "=" * 50)

    # Bảng danh sách đầy đủ
    in_bang(danh_sach)

    # Bảng tóm tắt theo xếp loại
    print("\n  ── TÓM TẮT THEO XẾP LOẠI ──")

    cac_loai = ["Xuất sắc", "Giỏi", "Khá", "Trung bình", "Yếu", "Kém"]
    for loai in cac_loai:
        nhom = []
        for i in range(len(danh_sach)):
            if xep_loai_hoc_luc(danh_sach[i][5]) == loai:
                nhom.append(danh_sach[i])
        if nhom:
            in_bang(nhom, f"📌 {loai} ({len(nhom)} SV)")

    print("\n  " + "=" * 50)
    print("       ── HẾT BÁO CÁO ──")
    print("  " + "=" * 50)


# ═══════════════════════════════════════════════════════════════════════
#  PHẦN 3: DỮ LIỆU MẪU (để demo nhanh)
# ═══════════════════════════════════════════════════════════════════════

def nap_du_lieu_mau():
    """Nạp dữ liệu mẫu để test nhanh các chức năng."""
    du_lieu_mau = [
        ["SV001", "Nguyễn Văn An", 20, "15/03/2006", "Nam", 8.5],
        ["SV002", "Trần Thị Bình", 21, "22/07/2005", "Nữ", 9.2],
        ["SV003", "Lê Hoàng Cường", 19, "10/11/2007", "Nam", 6.8],
        ["SV004", "Phạm Thị Dung", 20, "05/01/2006", "Nữ", 7.5],
        ["SV005", "Hoàng Minh Em", 22, "30/09/2004", "Nam", 4.2],
        ["SV006", "Võ Thị Phương", 20, "18/06/2006", "Nữ", 5.5],
        ["SV007", "Đặng Văn Giang", 21, "12/12/2005", "Nam", 9.8],
        ["SV008", "Bùi Thị Hạnh", 19, "25/04/2007", "Nữ", 3.0],
    ]
    for sv in du_lieu_mau:
        if tim_sinh_vien(sv[0]) == -1:
            danh_sach.append(sv)

    print(f"  ✅ Đã nạp {len(du_lieu_mau)} sinh viên mẫu.")


# ═══════════════════════════════════════════════════════════════════════
#  PHẦN 4: VÒNG LẶP CHÍNH
# ═══════════════════════════════════════════════════════════════════════

# Hỏi người dùng có muốn nạp dữ liệu mẫu không
print("\n  🎓 Chào mừng đến với Hệ thống Quản lý Sinh viên!")
nap_mau = input("  Nạp dữ liệu mẫu để thử nghiệm? (c/k): ").strip().lower()
if nap_mau == "c":
    nap_du_lieu_mau()

while True:
    hien_thi_menu()
    lua_chon = input("  👉 Chọn chức năng (0-8): ").strip()

    if lua_chon == "1":
        them_sinh_vien()
    elif lua_chon == "2":
        xem_danh_sach()
    elif lua_chon == "3":
        tim_kiem_sinh_vien()
    elif lua_chon == "4":
        cap_nhat_sinh_vien()
    elif lua_chon == "5":
        xoa_sinh_vien()
    elif lua_chon == "6":
        sap_xep_danh_sach()
    elif lua_chon == "7":
        thong_ke()
    elif lua_chon == "8":
        xuat_bao_cao()
    elif lua_chon == "0":
        print("\n  👋 Cảm ơn bạn đã sử dụng hệ thống. Tạm biệt!")
        print()
        break
    else:
        print("  ⚠ Lựa chọn không hợp lệ, vui lòng chọn 0-8.")

    if lua_chon != "0":
        nhan_enter()
