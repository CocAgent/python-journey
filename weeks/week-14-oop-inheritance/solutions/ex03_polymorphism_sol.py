"""Lời giải Bài tập 03: Đa hình"""
import math

class HinhTron:
    def __init__(self, r):
        self.r = r
    def tinh_dien_tich(self):
        return math.pi * self.r ** 2

class HinhChuNhat:
    def __init__(self, dai, rong):
        self.dai, self.rong = dai, rong
    def tinh_dien_tich(self):
        return self.dai * self.rong

class HinhTamGiac:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def tinh_dien_tich(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))

# TODO 1 — Đa hình: cùng method name, kết quả khác nhau
shapes = [HinhTron(5), HinhChuNhat(4, 6), HinhTamGiac(3, 4, 5)]
for shape in shapes:
    print(f"{type(shape).__name__}: S = {shape.tinh_dien_tich():.2f}")

# TODO 2
class ThanhToan:
    def xu_ly(self, so_tien):
        raise NotImplementedError

class TienMat(ThanhToan):
    def xu_ly(self, so_tien):
        print(f"Nhận {so_tien:,} tiền mặt")

class TheNganHang(ThanhToan):
    def xu_ly(self, so_tien):
        print(f"Trừ thẻ {so_tien:,}")

class ViDienTu(ThanhToan):
    def xu_ly(self, so_tien):
        print(f"Chuyển {so_tien:,} qua ví điện tử")

def thanh_toan(so_tien, phuong_thuc):
    phuong_thuc.xu_ly(so_tien)

for pt in [TienMat(), TheNganHang(), ViDienTu()]:
    thanh_toan(100000, pt)
