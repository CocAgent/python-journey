# Hai ví dụ hướng dẫn cách suy nghĩ — KHÔNG phải lời giải đề

## Ví dụ A: đếm chữ số chẵn trong số nguyên

Bài khác Câu 1a (bài chính đếm chữ số chia hết cho 3).

```python
def count_even_digits(n: int) -> int:
    if type(n) is not int or n < 0:
        raise ValueError("Cần số nguyên không âm")
    count = 0
    for char in str(n):
        if int(char) % 2 == 0:
            count += 1
    return count

print(count_even_digits(2045))  # 2 vì chữ số 2 và 0
```

**Tự đoán:** `count_even_digits(0)` → 1 vì `0`
là chữ số chẵn. Hãy tự đổi điều kiện thành chia hết
cho 3 trong đề chính, đồng thời chặn khoảng ngoài 1..1500.

## Ví dụ B: một class đơn giản khác lớp DienThoai

```python
class Sach:
    def __init__(self, ma: str, ten: str) -> None:
        if not ma.strip() or not ten.strip():
            raise ValueError("Thông tin sách thiếu")
        self.ma = ma.strip()
        self.ten = ten.strip()

    def thongtin(self) -> str:
        return f"{self.ma}: {self.ten}"

sach = Sach("S01", "Python")
print(sach.thongtin())  # S01: Python
```

**Giải thích:** `__init__` thiết lập trạng thái
đối tượng, `self` tham chiếu instance; `thongtin`
là method trả chuỗi để nơi gọi tự quyết định có in hay không.
Ở câu 5, cần nhiều trường hơn, validation riêng cho
pin và giá, sau đó tái sử dụng class ở file khác.

## Cách học

Che kết quả → dự đoán → chạy → giải thích → thử input
khác → tự làm starter → kiểm lại.
Đừng sao chép một ví dụ nguyên xi vào bài khác.
