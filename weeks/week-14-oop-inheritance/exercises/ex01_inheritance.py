"""Bài 01: Kế thừa cơ bản."""
import math

class DongVat:
    def __init__(self, ten, tuoi):
        self.ten, self.tuoi = ten, tuoi
    def an(self): return f"{self.ten} đang ăn."
    def ngu(self): return f"{self.ten} đang ngủ."

class Cho(DongVat):
    def __init__(self, ten, tuoi, giong):
        super().__init__(ten, tuoi); self.giong = giong
    def sua(self): return f"{self.ten}: Gâu gâu!"

class Meo(DongVat):
    def __init__(self, ten, tuoi, mau_long):
        super().__init__(ten, tuoi); self.mau_long = mau_long
    def keu(self): return f"{self.ten}: Meo meo!"

class HinhHoc:
    def tinh_dien_tich(self): raise NotImplementedError
    def tinh_chu_vi(self): raise NotImplementedError

class HinhTron(HinhHoc):
    def __init__(self, ban_kinh):
        if ban_kinh <= 0: raise ValueError("Bán kính phải > 0.")
        self.ban_kinh = ban_kinh
    def tinh_dien_tich(self): return math.pi * self.ban_kinh ** 2
    def tinh_chu_vi(self): return 2 * math.pi * self.ban_kinh
    def __str__(self): return f"Hình tròn r={self.ban_kinh}: S={self.tinh_dien_tich():.2f}, C={self.tinh_chu_vi():.2f}"

class HinhChuNhat(HinhHoc):
    def __init__(self, dai, rong):
        if dai <= 0 or rong <= 0: raise ValueError("Chiều dài/rộng phải > 0.")
        self.dai, self.rong = dai, rong
    def tinh_dien_tich(self): return self.dai * self.rong
    def tinh_chu_vi(self): return 2 * (self.dai + self.rong)
    def __str__(self): return f"Hình chữ nhật {self.dai}x{self.rong}: S={self.tinh_dien_tich()}, C={self.tinh_chu_vi()}"

class Flyer:
    def fly(self): return "Đang bay."
class Swimmer:
    def swim(self): return "Đang bơi."
class Duck(Flyer, Swimmer): pass

def main():
    cho, meo = Cho("Rex", 3, "Husky"), Meo("Luna", 2, "trắng")
    print(cho.an(), cho.sua()); print(meo.ngu(), meo.keu())
    for hinh in [HinhTron(5), HinhChuNhat(4, 6)]:
        print(hinh, "| là HinhHoc:", isinstance(hinh, HinhHoc))
    print("HinhTron kế thừa HinhHoc:", issubclass(HinhTron, HinhHoc))
    vit = Duck(); print(vit.fly(), vit.swim())

if __name__ == "__main__": main()
