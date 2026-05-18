"""Lời giải Bài tập 02: Override & super()"""

class NhanVien:
    def __init__(self, ten, luong):
        self.ten = ten
        self.luong = luong

    def tinh_luong(self):
        return self.luong

    def __str__(self):
        return f"{self.ten} — Lương: {self.tinh_luong():,.0f}"

class QuanLy(NhanVien):
    def __init__(self, ten, luong, phong_ban):
        super().__init__(ten, luong)
        self.phong_ban = phong_ban

    def tinh_luong(self):
        return self.luong * 1.2

    def __str__(self):
        return f"{super().__str__()} (QL {self.phong_ban})"

class TapSu(NhanVien):
    def tinh_luong(self):
        return self.luong * 0.7

nv = NhanVien("An", 10000000)
ql = QuanLy("Bình", 15000000, "IT")
ts = TapSu("Châu", 8000000)

for person in [nv, ql, ts]:
    print(person)
