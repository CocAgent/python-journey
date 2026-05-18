"""Lời giải Bài tập 01: Kế thừa cơ bản"""
import math

class DongVat:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def an(self):
        return f"{self.ten} đang ăn"

    def ngu(self):
        return f"{self.ten} đang ngủ"

class Cho(DongVat):
    def __init__(self, ten, tuoi, giong):
        super().__init__(ten, tuoi)
        self.giong = giong

    def sua(self):
        return f"{self.ten} ({self.giong}): Gâu gâu!"

class Meo(DongVat):
    def __init__(self, ten, tuoi, mau_long):
        super().__init__(ten, tuoi)
        self.mau_long = mau_long

    def keu(self):
        return f"{self.ten} (lông {self.mau_long}): Meo meo!"

dog = Cho("Rex", 3, "Husky")
cat = Meo("Luna", 2, "trắng")
print(dog.an())
print(dog.sua())
print(cat.ngu())
print(cat.keu())

# TODO 2
class HinhHoc:
    def tinh_dien_tich(self):
        raise NotImplementedError

    def tinh_chu_vi(self):
        raise NotImplementedError

class HinhTron(HinhHoc):
    def __init__(self, r):
        self.r = r

    def tinh_dien_tich(self):
        return math.pi * self.r ** 2

    def tinh_chu_vi(self):
        return 2 * math.pi * self.r

    def __str__(self):
        return f"HinhTron(r={self.r}): S={self.tinh_dien_tich():.2f}, C={self.tinh_chu_vi():.2f}"

class HinhChuNhat(HinhHoc):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def tinh_dien_tich(self):
        return self.dai * self.rong

    def tinh_chu_vi(self):
        return 2 * (self.dai + self.rong)

    def __str__(self):
        return f"HCN({self.dai}x{self.rong}): S={self.tinh_dien_tich()}, C={self.tinh_chu_vi()}"

for h in [HinhTron(5), HinhChuNhat(4, 6)]:
    print(h)
    print(f"  isinstance HinhHoc: {isinstance(h, HinhHoc)}")
