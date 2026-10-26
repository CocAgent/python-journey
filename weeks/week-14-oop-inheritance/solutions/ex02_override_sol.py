"""Lời giải bài 02: Override và super()."""
class NhanVien:
    def __init__(self,ten,luong): self.ten,self.luong=ten,luong
    def tinh_luong(self): return self.luong
    def __str__(self): return f"{self.ten} — Lương: {self.tinh_luong():,.0f} VNĐ"
class QuanLy(NhanVien):
    def __init__(self,ten,luong,phong_ban): super().__init__(ten,luong); self.phong_ban=phong_ban
    def tinh_luong(self): return self.luong*1.2
    def __str__(self): return f"{super().__str__()} — Phòng ban: {self.phong_ban}"
class TapSu(NhanVien):
    def tinh_luong(self): return self.luong*0.7
class Vehicle:
    def __init__(self,name,speed): self.name,self.speed=name,speed
    def describe(self): return f"{self.name}, {self.speed} km/h"
class ElectricCar(Vehicle):
    def __init__(self,name,speed,battery):
        super().__init__(name,speed)
        if not 0<=battery<=100: raise ValueError("Pin phải từ 0 đến 100%.")
        self.battery=battery
    def describe(self): return f"{super().describe()}, pin {self.battery}%"
class Report:
    def header(self): return "BÁO CÁO"
    def body(self): raise NotImplementedError
    def footer(self): return "Kết thúc."
    def generate(self): return "\\n".join((self.header(),self.body(),self.footer()))
class HTMLReport(Report):
    def header(self): return "<h1>BÁO CÁO</h1>"
    def body(self): return "<p>Nội dung</p>"
    def footer(self): return "<footer>Kết thúc.</footer>"
class TextReport(Report):
    def body(self): return "Nội dung báo cáo dạng văn bản."
def main():
    for n in [NhanVien("An",10_000_000),QuanLy("Bình",15_000_000,"IT"),TapSu("Châu",8_000_000)]: print(n)
    print(ElectricCar("EV",160,85).describe()); print(HTMLReport().generate()); print(TextReport().generate())
if __name__=="__main__": main()
