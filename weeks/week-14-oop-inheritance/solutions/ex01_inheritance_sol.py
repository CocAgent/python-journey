"""Lời giải bài 01: Kế thừa cơ bản."""
import math

class DongVat:
    def __init__(self, ten, tuoi): self.ten, self.tuoi = ten, tuoi
    def an(self): return f"{self.ten} đang ăn."
    def ngu(self): return f"{self.ten} đang ngủ."
class Cho(DongVat):
    def __init__(self, ten, tuoi, giong): super().__init__(ten,tuoi); self.giong=giong
    def sua(self): return f"{self.ten}: Gâu gâu!"
class Meo(DongVat):
    def __init__(self, ten, tuoi, mau_long): super().__init__(ten,tuoi); self.mau_long=mau_long
    def keu(self): return f"{self.ten}: Meo meo!"
class HinhHoc:
    def tinh_dien_tich(self): raise NotImplementedError
    def tinh_chu_vi(self): raise NotImplementedError
class HinhTron(HinhHoc):
    def __init__(self,r):
        if r<=0: raise ValueError("Bán kính phải > 0.")
        self.r=r
    def tinh_dien_tich(self): return math.pi*self.r**2
    def tinh_chu_vi(self): return 2*math.pi*self.r
    def __str__(self): return f"Hình tròn r={self.r}: S={self.tinh_dien_tich():.2f}, C={self.tinh_chu_vi():.2f}"
class HinhChuNhat(HinhHoc):
    def __init__(self,dai,rong):
        if dai<=0 or rong<=0: raise ValueError("Kích thước phải > 0.")
        self.dai,self.rong=dai,rong
    def tinh_dien_tich(self): return self.dai*self.rong
    def tinh_chu_vi(self): return 2*(self.dai+self.rong)
    def __str__(self): return f"Hình chữ nhật {self.dai}x{self.rong}: S={self.tinh_dien_tich()}, C={self.tinh_chu_vi()}"
class Flyer:
    def fly(self): return "Đang bay."
class Swimmer:
    def swim(self): return "Đang bơi."
class Duck(Flyer,Swimmer): pass

def main():
    for animal in [Cho("Rex",3,"Husky"),Meo("Luna",2,"trắng")]: print(animal.an(),animal.ngu())
    for h in [HinhTron(5),HinhChuNhat(4,6)]: print(h,isinstance(h,HinhHoc))
    print("issubclass:",issubclass(HinhTron,HinhHoc)); d=Duck(); print(d.fly(),d.swim())
if __name__=="__main__": main()
