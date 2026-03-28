# Tuần 14 — OOP Phần 2 — Kế Thừa & Đa Hình

> **Python Journey** — Khóa học Python cơ bản cho người mới bắt đầu  
> Thời lượng: 2h lý thuyết + 2h thực hành

---

## 🎯 Mục Tiêu Tuần Này

Sau buổi học, bạn có thể:
- Dùng kế thừa để tái sử dụng code
- Ghi đè (override) phương thức từ class cha
- Gọi class cha với `super()`
- Hiểu đa hình và ứng dụng thực tế

---

## 1. Kế Thừa — Inheritance

```python
# Class cha (base class)
class DongVat:
    """Lớp cơ sở cho tất cả động vật."""
    
    def __init__(self, ten: str, tuoi: int):
        self.ten = ten
        self.tuoi = tuoi
    
    def an(self) -> str:
        return f"{self.ten} đang ăn"
    
    def ngu(self) -> str:
        return f"{self.ten} đang ngủ"
    
    def __str__(self) -> str:
        return f"{type(self).__name__}('{self.ten}', {self.tuoi} tuổi)"


# Class con (derived class) — kế thừa từ DongVat
class Cho(DongVat):
    """Lớp chó — kế thừa từ DongVat."""
    
    def __init__(self, ten: str, tuoi: int, giong: str):
        super().__init__(ten, tuoi)  # Gọi __init__ của class cha
        self.giong = giong
    
    # Override phương thức kêu
    def keu(self) -> str:
        return f"{self.ten}: Gâu gâu!"
    
    # Thêm phương thức riêng
    def lay(self, do_vat: str) -> str:
        return f"{self.ten} lấy {do_vat} về!"


class Meo(DongVat):
    def __init__(self, ten: str, tuoi: int, mau_long: str):
        super().__init__(ten, tuoi)
        self.mau_long = mau_long
    
    def keu(self) -> str:
        return f"{self.ten}: Meo meo!"
    
    def san_bat(self, con_moi: str) -> str:
        return f"{self.ten} đang săn {con_moi}"


# Dùng
cho1 = Cho("Rex", 3, "Golden Retriever")
meo1 = Meo("Mimi", 2, "trắng")

print(cho1)                    # Cho('Rex', 3 tuổi)
print(cho1.an())               # Rex đang ăn (kế thừa từ cha)
print(cho1.keu())              # Rex: Gâu gâu! (override)
print(cho1.lay("bóng"))       # Rex lấy bóng về!

print(meo1.keu())             # Mimi: Meo meo!
```

## 2. Đa Hình — Polymorphism

```python
# Đa hình: cùng phương thức, nhiều hành vi khác nhau
dong_vat = [
    Cho("Rex", 3, "Golden"),
    Meo("Mimi", 2, "trắng"),
    Cho("Buddy", 1, "Poodle"),
]

# Gọi keu() trên mỗi object — mỗi cái hành xử khác nhau
for dv in dong_vat:
    print(dv.keu())  # Python tự gọi đúng phiên bản keu()

# isinstance() kiểm tra kiểu
print(isinstance(cho1, Cho))      # True
print(isinstance(cho1, DongVat))  # True (kế thừa!)
print(isinstance(cho1, Meo))      # False
```

## 3. Abstract Class — Lớp Trừu Tượng

```python
from abc import ABC, abstractmethod

class HinhHoc(ABC):
    """Lớp trừu tượng — không thể tạo object trực tiếp."""
    
    @abstractmethod
    def tinh_dien_tich(self) -> float:
        """Tính diện tích — subclass PHẢI implement."""
        pass
    
    @abstractmethod
    def tinh_chu_vi(self) -> float:
        pass
    
    def mo_ta(self) -> str:
        return (f"{type(self).__name__}: "
                f"S={self.tinh_dien_tich():.2f}, "
                f"P={self.tinh_chu_vi():.2f}")


class HinhTron(HinhHoc):
    def __init__(self, ban_kinh: float):
        self.r = ban_kinh
    
    def tinh_dien_tich(self) -> float:
        import math
        return math.pi * self.r ** 2
    
    def tinh_chu_vi(self) -> float:
        import math
        return 2 * math.pi * self.r


class HinhChuNhat(HinhHoc):
    def __init__(self, dai: float, rong: float):
        self.dai = dai
        self.rong = rong
    
    def tinh_dien_tich(self) -> float:
        return self.dai * self.rong
    
    def tinh_chu_vi(self) -> float:
        return 2 * (self.dai + self.rong)


# Dùng
hinh1 = HinhTron(5)
hinh2 = HinhChuNhat(4, 6)
# hinh = HinhHoc()  # ❌ TypeError — không thể tạo ABC trực tiếp

for h in [hinh1, hinh2]:
    print(h.mo_ta())
```

## 4. Bài Tập

### Bài 1 — Thú cưng (Dễ)
Tạo hierarchy: DongVat → ThuCung → Cho/Meo/Ca. Mỗi class thêm thuộc tính và phương thức riêng.

### Bài 2 — Hình học (Trung bình)
Hierarchy HinhHoc → HinhTron/HinhChuNhat/HinhTamGiac. Dùng ABC và tính diện tích, chu vi.

### Bài 3 — Hệ thống nhân viên (Thử thách)
NhanVien → NhanVienToanThoiGian / NhanVienPartTime / NhanVienFreelance. Tính lương khác nhau cho từng loại.

---

## 🔑 Những Điều Quan Trọng Nhất Tuần Này

> 1. **`super().__init__()`** — phải gọi khi override `__init__` để khởi tạo đúng class cha
> 2. **Đa hình** = cùng tên phương thức, hành vi khác nhau — đây là sức mạnh của OOP
> 3. **Abstract class** tạo "hợp đồng" — subclass BẮT BUỘC implement các abstract methods
