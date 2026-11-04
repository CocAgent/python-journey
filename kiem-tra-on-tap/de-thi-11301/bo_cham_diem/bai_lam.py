"""FILE ĐIỀN ĐÁP ÁN — sửa các hàm bên dưới, không sửa cham_diem.py."""

# CÂU 1 — SỐ NGUYÊN
def hop_le_n(n):
    """1a. True nếu n là số nguyên trong [1, 1500]."""
    raise NotImplementedError("Làm câu 1a")

def dem_chu_so_le(n):
    """1b. Đếm chữ số lẻ của n."""
    raise NotImplementedError("Làm câu 1b")

def tinh_s(n):
    """1c. Tính 1/2 + 1/4 + ... + 1/(2*n)."""
    raise NotImplementedError("Làm câu 1c")

# CÂU 2 — CHUỖI
def dem_chu_hoa(s):
    """2a. Đếm ký tự chữ hoa."""
    raise NotImplementedError("Làm câu 2a")

def la_chuoi_doi_xung(s):
    """2b. Kiểm tra chuỗi đối xứng."""
    raise NotImplementedError("Làm câu 2b")

def tinh_tong_chu_so(s):
    """2c. Tính tổng các chữ số trong chuỗi."""
    raise NotImplementedError("Làm câu 2c")

# CÂU 3 — LIST
def tao_danh_sach(ds_nhap):
    """3a. Trả về các phần tử trước số 0 kết thúc."""
    raise NotImplementedError("Làm câu 3a")

def tong_so_duong_chan(danh_sach):
    """3b. Tính tổng các số dương chẵn."""
    raise NotImplementedError("Làm câu 3b")

def dem_so_lan_xuat_hien(danh_sach, k):
    """3c. Đếm số lần k xuất hiện."""
    raise NotImplementedError("Làm câu 3c")

# CÂU 4 — DICTIONARY
def tao_sach(ma_sach, ten_sach, tac_gia, nha_xuat_ban, nam_xuat_ban, nam_hien_tai):
    """4a. Trả dictionary {ma: [tên, tác giả, NXB, năm]}, None nếu năm tương lai."""
    raise NotImplementedError("Làm câu 4a")

def xoa_sach(tu_dien, ma_can_xoa):
    """4b. Xóa mã sách; True nếu xóa được, False nếu không có."""
    raise NotImplementedError("Làm câu 4b")

# CÂU 5 — OOP
class DienThoai:
    """5a/5b. Class điện thoại có đủ thuộc tính và phương thức hiển thị."""
    def __init__(self, MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan):
        raise NotImplementedError("Làm __init__ câu 5")

    def thongtindienthoai(self):
        raise NotImplementedError("Làm phương thức câu 5")
