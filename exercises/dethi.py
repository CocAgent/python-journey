class DienThoai:
    def __init__(self, MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan):
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan 
    
    def thongtindienthoai(self):
        print("Ma may:", self.MaMay)
        print("Ten may:", self.TenMay)
        print("Hang san xuat:", self.HangSanXuat)
        print("Dung luong pin:", self.DungLuongPin)
        print("Gia ban:", self.GiaBan)
        print("-" * 30)
        
DT01 = DienThoai("DT01", "Iphone 15 Pro", "Apple", 3274, 28990000)
DT02 = DienThoai("DT02", "Galaxy S24 Ultra", "SamSung", 5000, 29990000)

DT01.thongtindienthoai()
DT02.thongtindienthoai()
