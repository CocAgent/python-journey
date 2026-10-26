"""Lời giải bài 01: Class đầu tiên."""


class HocSinh:
    dem = 0

    def __init__(self, ten, tuoi, diem):
        if not ten.strip():
            raise ValueError("Tên học sinh không được để trống.")
        if tuoi <= 0:
            raise ValueError("Tuổi phải lớn hơn 0.")
        if not 0 <= diem <= 10:
            raise ValueError("Điểm phải từ 0 đến 10.")

        self.ten = ten
        self.tuoi = tuoi
        self.diem = diem
        type(self).dem += 1

    def tinh_xep_loai(self):
        if self.diem >= 9:
            return "Xuất sắc"
        if self.diem >= 8:
            return "Giỏi"
        if self.diem >= 6.5:
            return "Khá"
        if self.diem >= 5:
            return "Trung bình"
        return "Yếu"

    def __str__(self):
        return (
            f"{self.ten} ({self.tuoi} tuổi) - "
            f"Điểm: {self.diem:.1f} - {self.tinh_xep_loai()}"
        )

    @classmethod
    def so_luong(cls):
        return cls.dem


def main():
    danh_sach = [
        HocSinh("Nguyễn An", 20, 8.5),
        HocSinh("Trần Bình", 21, 6.0),
        HocSinh("Lê Châu", 19, 9.5),
    ]
    for hoc_sinh in danh_sach:
        print(hoc_sinh)
    print(f"Tổng: {HocSinh.so_luong()} học sinh")


if __name__ == "__main__":
    main()
