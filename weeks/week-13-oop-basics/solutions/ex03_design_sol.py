"""Lời giải Bài tập 03: Thiết kế class"""

class Sach:
    def __init__(self, tua_de, tac_gia, so_trang):
        self.tua_de = tua_de
        self.tac_gia = tac_gia
        self.so_trang = so_trang
        self.da_doc = 0

    def doc(self, so_trang):
        self.da_doc = min(self.da_doc + so_trang, self.so_trang)

    def tien_do(self):
        return self.da_doc / self.so_trang * 100

    def __str__(self):
        return f"\"{self.tua_de}\" ({self.tac_gia}) - {self.tien_do():.0f}%"

s1 = Sach("Think Python", "Allen Downey", 300)
s1.doc(75)
print(s1)  # "Think Python" (Allen Downey) - 25%

s2 = Sach("Clean Code", "Robert Martin", 431)
s2.doc(200)
print(s2)
