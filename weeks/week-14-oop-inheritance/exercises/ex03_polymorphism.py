"""Bài 03: Đa hình và duck typing."""
import math

class HinhTron:
    def __init__(self, r):
        if r <= 0: raise ValueError("Bán kính phải > 0.")
        self.r = r
    def tinh_dien_tich(self): return math.pi * self.r ** 2
class HinhChuNhat:
    def __init__(self, dai, rong):
        if dai <= 0 or rong <= 0: raise ValueError("Kích thước phải > 0.")
        self.dai, self.rong = dai, rong
    def tinh_dien_tich(self): return self.dai * self.rong
class HinhTamGiac:
    def __init__(self, a, b, c):
        if min(a,b,c) <= 0 or a+b <= c or a+c <= b or b+c <= a: raise ValueError("Ba cạnh không tạo thành tam giác hợp lệ.")
        self.a, self.b, self.c = a,b,c
    def tinh_dien_tich(self):
        s=(self.a+self.b+self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

class ThanhToan:
    def phuong_thuc(self): raise NotImplementedError
    def xu_ly(self, so_tien): raise NotImplementedError
class TienMat(ThanhToan):
    def phuong_thuc(self): return "Tiền mặt"
    def xu_ly(self, so_tien): return f"Nhận {so_tien:,.0f} VNĐ bằng tiền mặt."
class TheNganHang(ThanhToan):
    def phuong_thuc(self): return "Thẻ ngân hàng"
    def xu_ly(self, so_tien): return f"Trừ thẻ {so_tien:,.0f} VNĐ."
class ViDienTu(ThanhToan):
    def phuong_thuc(self): return "Ví điện tử"
    def xu_ly(self, so_tien): return f"Thanh toán {so_tien:,.0f} VNĐ qua ví điện tử."
def thanh_toan(don_hang, phuong_thuc):
    if don_hang < 0: raise ValueError("Tổng đơn hàng không được âm.")
    return f"{phuong_thuc.phuong_thuc()}: {phuong_thuc.xu_ly(don_hang)}"

class Nguoi:
    def speak(self): return "Xin chào."
class ChoNoi:
    def speak(self): return "Gâu gâu."
def phat_bieu(obj):
    if not callable(getattr(obj, "speak", None)): raise TypeError("Đối tượng cần có method speak().")
    return obj.speak()

class NhanVien:
    def __init__(self, ten): self.ten=ten
    def tinh_luong(self): raise NotImplementedError
class FullTime(NhanVien):
    def __init__(self, ten, luong_thang): super().__init__(ten); self.luong_thang=luong_thang
    def tinh_luong(self): return self.luong_thang
class PartTime(NhanVien):
    def __init__(self, ten, gio, luong_gio): super().__init__(ten); self.gio=gio; self.luong_gio=luong_gio
    def tinh_luong(self): return self.gio*self.luong_gio
class Intern(NhanVien):
    def __init__(self, ten, tro_cap): super().__init__(ten); self.tro_cap=tro_cap
    def tinh_luong(self): return self.tro_cap
def tong_luong(danh_sach_nhan_vien): return sum(nv.tinh_luong() for nv in danh_sach_nhan_vien)

def main():
    for h in [HinhTron(5), HinhChuNhat(4,6), HinhTamGiac(3,4,5)]: print(type(h).__name__, round(h.tinh_dien_tich(),2))
    for p in [TienMat(), TheNganHang(), ViDienTu()]: print(thanh_toan(100_000,p))
    print(phat_bieu(Nguoi()), phat_bieu(ChoNoi()))
    staff=[FullTime("An",20_000_000),PartTime("Bình",80,50_000),Intern("Châu",3_000_000)]
    print("Tổng lương:",f"{tong_luong(staff):,.0f} VNĐ")

if __name__ == "__main__": main()
