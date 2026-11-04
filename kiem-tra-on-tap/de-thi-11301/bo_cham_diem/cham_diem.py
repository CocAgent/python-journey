"""Chạy file này để test bài làm và tính điểm theo từng ý."""
import contextlib
import io
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import bai_lam as bai  # noqa: E402


def gan(a, b):
    return math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9)


def cham(ten, diem_toi_da, tests):
    dung = 0
    loi = []
    for mo_ta, ham in tests:
        try:
            if ham():
                dung += 1
            else:
                loi.append(mo_ta)
        except Exception as e:
            loi.append(f"{mo_ta} ({type(e).__name__}: {e})")
    return ten, diem_toi_da * dung / len(tests), diem_toi_da, loi


def test_dt_thuoc_tinh():
    dt = bai.DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    return (dt.MaMay, dt.TenMay, dt.HangSanXuat, dt.DungLuongPin, dt.GiaBan) == ("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)


def test_dt_hien_thi():
    dt = bai.DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        dt.thongtindienthoai()
    return all(x in out.getvalue() for x in ["DT01", "iPhone 15 Pro", "Apple", "3274", "28990000"])


def chay_cham():
    kq = []
    kq.append(cham("1a", .5, [("n=1 hợp lệ", lambda: bai.hop_le_n(1) is True), ("n=1500 hợp lệ", lambda: bai.hop_le_n(1500) is True), ("n=0 không hợp lệ", lambda: bai.hop_le_n(0) is False), ("n=1501 không hợp lệ", lambda: bai.hop_le_n(1501) is False)]))
    kq.append(cham("1b", .75, [("12345 có 3 chữ số lẻ", lambda: bai.dem_chu_so_le(12345) == 3), ("2468 có 0 chữ số lẻ", lambda: bai.dem_chu_so_le(2468) == 0), ("101 có 2 chữ số lẻ", lambda: bai.dem_chu_so_le(101) == 2)]))
    kq.append(cham("1c", .75, [("n=1", lambda: gan(bai.tinh_s(1), .5)), ("n=2", lambda: gan(bai.tinh_s(2), .75)), ("n=4", lambda: gan(bai.tinh_s(4), 1 + 1/24))]))
    kq.append(cham("2a", .67, [("AbC đếm được 2 chữ hoa", lambda: bai.dem_chu_hoa("AbC") == 2), ("python 123 có 0 chữ hoa", lambda: bai.dem_chu_hoa("python 123") == 0), ("ABC có 3 chữ hoa", lambda: bai.dem_chu_hoa("ABC") == 3)]))
    kq.append(cham("2b", .66, [("aba đối xứng", lambda: bai.la_chuoi_doi_xung("aba") is True), ("python không đối xứng", lambda: bai.la_chuoi_doi_xung("python") is False), ("chuỗi rỗng đối xứng", lambda: bai.la_chuoi_doi_xung("") is True)]))
    kq.append(cham("2c", .67, [("a1b2c3 tổng 6", lambda: bai.tinh_tong_chu_so("a1b2c3") == 6), ("abc tổng 0", lambda: bai.tinh_tong_chu_so("abc") == 0), ("908 tổng 17", lambda: bai.tinh_tong_chu_so("908") == 17)]))
    kq.append(cham("3a", .5, [("dừng tại 0", lambda: bai.tao_danh_sach([2, -1, 4, 0, 9]) == [2, -1, 4]), ("không có 0", lambda: bai.tao_danh_sach([1, 3]) == [1, 3]), ("0 đầu danh sách", lambda: bai.tao_danh_sach([0, 5]) == [])]))
    kq.append(cham("3b", .75, [("tổng số dương chẵn", lambda: bai.tong_so_duong_chan([-4, -2, 1, 2, 3, 6]) == 8), ("không có số dương chẵn", lambda: bai.tong_so_duong_chan([-2, -1, 1, 3]) == 0), ("danh sách rỗng", lambda: bai.tong_so_duong_chan([]) == 0)]))
    kq.append(cham("3c", .75, [("đếm nhiều lần", lambda: bai.dem_so_lan_xuat_hien([1, 2, 2, 3, 2], 2) == 3), ("không tìm thấy", lambda: bai.dem_so_lan_xuat_hien([1, 3], 2) == 0), ("danh sách rỗng", lambda: bai.dem_so_lan_xuat_hien([], 2) == 0)]))
    kq.append(cham("4a", 1, [("tạo dictionary", lambda: bai.tao_sach("S01", "Python", "An", "NXB A", 2020, 2026) == {"S01": ["Python", "An", "NXB A", 2020]}), ("từ chối năm tương lai", lambda: bai.tao_sach("S02", "AI", "Binh", "NXB B", 2027, 2026) is None), ("chấp nhận năm hiện tại", lambda: bai.tao_sach("S03", "Code", "Chi", "NXB C", 2026, 2026) is not None)]))
    kq.append(cham("4b", 1, [("xóa mã có tồn tại", lambda: (lambda d: bai.xoa_sach(d, "S01") is True and "S01" not in d)({"S01": ["Python"]})), ("mã không tồn tại", lambda: bai.xoa_sach({}, "S99") is False)]))
    kq.append(cham("5a", 1, [("khởi tạo đủ 5 thuộc tính", test_dt_thuoc_tinh), ("đối tượng thứ hai", lambda: (lambda d: d.TenMay == "Galaxy S24 Ultra" and d.GiaBan == 29990000)(bai.DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)))]))
    kq.append(cham("5b", 1, [("hiển thị đủ thông tin", test_dt_hien_thi)]))
    return kq


def main():
    print("=" * 54)
    print(" CHẤM ĐIỂM TỰ ĐỘNG — ĐỀ PYTHON 11301")
    print("=" * 54)
    tong = 0
    for ten, diem, toi_da, loi in chay_cham():
        tong += diem
        print(f"{ten:>3} | {diem:4.2f}/{toi_da:4.2f} | {'ĐẠT' if not loi else 'CẦN SỬA'}")
        for item in loi:
            print("     - " + item)
    print("-" * 54)
    print(f"TỔNG ĐIỂM: {tong:.2f}/10.00")
    print("Điểm dựa trên test mẫu, không thay thế hoàn toàn điểm giảng viên chấm.")
    print("Sửa bai_lam.py rồi chạy lại: py cham_diem.py")


if __name__ == "__main__":
    main()
