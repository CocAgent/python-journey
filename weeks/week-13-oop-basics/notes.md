# Tuần 13 — Lập Trình Hướng Đối Tượng (OOP) — Phần 1

> **Python Journey** — Khóa học Python cơ bản cho người mới bắt đầu  
> Thời lượng: 2h lý thuyết + 2h thực hành

---

## 🎯 Mục Tiêu Tuần Này

Sau buổi học, bạn có thể:
- Giải thích OOP là gì và tại sao dùng
- Định nghĩa class và tạo object
- Viết `__init__`, instance methods, `__str__`
- Phân biệt instance variable và class variable

---

## 1. Tại Sao Cần OOP?

```python
# Không dùng OOP — quản lý nhiều học sinh phức tạp
ten1 = "An";    tuoi1 = 20;    diem1 = 8.5
ten2 = "Bình";  tuoi2 = 21;    diem2 = 7.0
# ... 30 học sinh → 90 biến riêng lẻ → hỗn loạn!

# Dùng OOP — gọn gàng, mở rộng được
class HocSinh:
    pass

hs1 = HocSinh()
hs2 = HocSinh()
# Mỗi object có dữ liệu riêng, cùng cấu trúc
```

## 2. Định Nghĩa Class và Tạo Object

```python
class HocSinh:
    """Đại diện cho một học sinh."""
    
    # Class variable — dùng chung cho tất cả objects
    truong = "THPT Nguyễn Trãi"
    tong_so_hs = 0
    
    def __init__(self, ten: str, tuoi: int, diem: float):
        """Khởi tạo học sinh mới."""
        # Instance variables — riêng của mỗi object
        self.ten = ten
        self.tuoi = tuoi
        self.diem = diem
        HocSinh.tong_so_hs += 1
    
    def xep_loai(self) -> str:
        """Trả về xếp loại học lực."""
        if self.diem >= 9:
            return "Xuất sắc"
        elif self.diem >= 8:
            return "Giỏi"
        elif self.diem >= 6.5:
            return "Khá"
        elif self.diem >= 5:
            return "Trung bình"
        return "Yếu"
    
    def hoc(self, mon: str) -> None:
        """Học sinh học một môn."""
        print(f"{self.ten} đang học {mon}")
    
    def __str__(self) -> str:
        """Biểu diễn chuỗi của object — dùng với print()."""
        return (f"HocSinh(ten='{self.ten}', tuoi={self.tuoi}, "
                f"diem={self.diem}, loai='{self.xep_loai()}')")
    
    def __repr__(self) -> str:
        """Biểu diễn kỹ thuật — dùng trong debug."""
        return f"HocSinh('{self.ten}', {self.tuoi}, {self.diem})"


# Tạo objects
hs1 = HocSinh("Nguyễn An", 20, 8.5)
hs2 = HocSinh("Trần Bình", 21, 7.0)
hs3 = HocSinh("Lê Châu", 19, 9.5)

# Dùng object
print(hs1)                          # Dùng __str__
print(hs1.ten)                      # Nguyễn An
print(hs1.xep_loai())              # Giỏi
hs1.hoc("Toán")                    # Nguyễn An đang học Toán

# Class variable — truy cập qua class hoặc object
print(HocSinh.tong_so_hs)          # 3
print(hs1.truong)                   # THPT Nguyễn Trãi
```

## 3. Class Methods và Static Methods

```python
class HocSinh:
    tong_so = 0
    
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem
        HocSinh.tong_so += 1
    
    # Instance method — truy cập self
    def xep_loai(self):
        return "Giỏi" if self.diem >= 8 else "Khá"
    
    # Class method — truy cập class, không phải instance
    @classmethod
    def get_tong_so(cls):
        return cls.tong_so
    
    # Static method — không truy cập class hay instance
    @staticmethod
    def diem_hop_le(diem):
        return 0 <= diem <= 10


# Gọi
hs = HocSinh("An", 8.5)
print(HocSinh.get_tong_so())       # 1
print(HocSinh.diem_hop_le(11))    # False
print(hs.diem_hop_le(8.5))        # True
```

## 4. Bài Tập

### Bài 1 — Class BankAccount (Dễ)
```python
class BankAccount:
    # so_tai_khoan, chu_so_huu, so_du
    # deposit(so_tien), withdraw(so_tien), get_balance()
    pass
```

### Bài 2 — Class Circle (Trung bình)
Class vòng tròn với bán kính, tính chu vi/diện tích, so sánh hai vòng tròn.

### Bài 3 — Thư viện sách (Thử thách)
Class Book (tieu_de, tac_gia, nam, so_trang) và Library quản lý danh sách sách.

---

## 🔑 Những Điều Quan Trọng Nhất Tuần Này

> 1. **`self`** là tham chiếu đến object hiện tại — mọi instance method đều cần nó làm tham số đầu tiên
> 2. **`__init__`** không phải constructor — Python đã tạo object rồi, `__init__` chỉ khởi tạo
> 3. **`__str__`** quyết định output của `print(object)` — luôn định nghĩa để debug dễ hơn
