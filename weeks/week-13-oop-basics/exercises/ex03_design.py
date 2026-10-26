"""Bài tập 03: Thiết kế class cho bài toán."""


class Sach:
    def __init__(self, tua_de, tac_gia, so_trang):
        if so_trang <= 0:
            raise ValueError("Số trang phải lớn hơn 0.")
        self.tua_de = tua_de
        self.tac_gia = tac_gia
        self.so_trang = so_trang
        self.da_doc = 0

    def doc(self, so_trang):
        if so_trang < 0:
            raise ValueError("Số trang đọc thêm không được âm.")
        self.da_doc = min(self.da_doc + so_trang, self.so_trang)

    def tien_do(self):
        return self.da_doc / self.so_trang * 100

    def __str__(self):
        return (
            f'"{self.tua_de}" - {self.tac_gia}: '
            f"{self.da_doc}/{self.so_trang} trang ({self.tien_do():.1f}%)"
        )


class DanhBa:
    def __init__(self):
        self.danh_sach = []

    def them(self, ten, so_dien_thoai, email=""):
        if not ten.strip() or not so_dien_thoai.strip():
            return False
        if self.tim_theo_ten(ten):
            return False
        self.danh_sach.append({
            "ten": ten.strip(),
            "so_dien_thoai": so_dien_thoai.strip(),
            "email": email.strip(),
        })
        return True

    def tim_theo_ten(self, ten):
        tu_khoa = ten.strip().casefold()
        return [
            lien_he for lien_he in self.danh_sach
            if tu_khoa in lien_he["ten"].casefold()
        ]

    def xoa(self, ten):
        ket_qua = self.tim_theo_ten(ten)
        if not ket_qua:
            return False
        self.danh_sach.remove(ket_qua[0])
        return True

    def hien_thi(self):
        if not self.danh_sach:
            print("Danh bạ đang trống.")
            return
        for lien_he in self.danh_sach:
            print(
                f"{lien_he['ten']} | {lien_he['so_dien_thoai']} | "
                f"{lien_he['email'] or 'Chưa có email'}"
            )


class QuanLyCafe:
    def __init__(self):
        self.menu = {}
        self.don_hang = []

    def them_mon(self, ten, gia, danh_muc):
        if not ten.strip() or gia < 0:
            return False
        self.menu[ten.strip()] = {"gia": gia, "danh_muc": danh_muc}
        return True

    def tao_don_hang(self, ten_mon, so_luong):
        if ten_mon not in self.menu or so_luong <= 0:
            return False
        self.don_hang.append({"ten": ten_mon, "so_luong": so_luong})
        return True

    def tinh_tong_tien(self):
        return sum(
            self.menu[item["ten"]]["gia"] * item["so_luong"]
            for item in self.don_hang
        )

    def in_hoa_don(self):
        print("===== HOA DON CAFE =====")
        if not self.don_hang:
            print("Chưa có món nào.")
        for item in self.don_hang:
            mon = self.menu[item["ten"]]
            thanh_tien = mon["gia"] * item["so_luong"]
            print(
                f"{item['ten']} x {item['so_luong']}: "
                f"{thanh_tien:,.0f} VNĐ"
            )
        print(f"Tổng tiền: {self.tinh_tong_tien():,.0f} VNĐ")


def main():
    sach = Sach("Think Python", "Allen Downey", 300)
    sach.doc(75)
    print(sach)

    danh_ba = DanhBa()
    danh_ba.them("Nguyễn An", "0900000001", "an@example.com")
    danh_ba.them("Trần Bình", "0900000002")
    print("\nDanh bạ:")
    danh_ba.hien_thi()
    print("Tìm An:", danh_ba.tim_theo_ten("an"))

    cafe = QuanLyCafe()
    cafe.them_mon("Cà phê sữa", 25_000, "Cà phê")
    cafe.them_mon("Trà đào", 30_000, "Trà")
    cafe.tao_don_hang("Cà phê sữa", 2)
    cafe.tao_don_hang("Trà đào", 1)
    cafe.in_hoa_don()


if __name__ == "__main__":
    main()
