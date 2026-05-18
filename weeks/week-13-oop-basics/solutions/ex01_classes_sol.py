"""Lời giải Bài tập 01: Class đầu tiên"""

class HocSinh:
    dem = 0  # Class variable

    def __init__(self, ten, tuoi, diem):
        self.ten = ten
        self.tuoi = tuoi
        self.diem = diem
        HocSinh.dem += 1

    def tinh_xep_loai(self):
        if self.diem >= 9: return "Xuất sắc"
        if self.diem >= 8: return "Giỏi"
        if self.diem >= 6.5: return "Khá"
        if self.diem >= 5: return "Trung bình"
        return "Yếu"

    def __str__(self):
        return f"{self.ten} ({self.tuoi} tuổi) - Điểm: {self.diem} - {self.tinh_xep_loai()}"

    @classmethod
    def so_luong(cls):
        return cls.dem

hs1 = HocSinh("An", 20, 8.5)
hs2 = HocSinh("Bình", 21, 6.0)
hs3 = HocSinh("Châu", 20, 9.5)

for hs in [hs1, hs2, hs3]:
    print(hs)
print(f"Tổng: {HocSinh.so_luong()} học sinh")
