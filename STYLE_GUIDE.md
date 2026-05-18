# Style Guide — Python Journey

> Quy tắc viết code trong khóa học này, dựa trên PEP 8.

## Đặt tên

```python
# Biến và hàm: snake_case
ten_hoc_sinh = "An"
so_luong_san_pham = 42

def tinh_dien_tich(dai, rong):
    return dai * rong

# Class: PascalCase
class HocSinh:
    pass

class TaiKhoanNganHang:
    pass

# Hằng số: UPPER_SNAKE_CASE
MAX_RETRY = 3
PI = 3.14159
DATABASE_URL = "sqlite:///db.sqlite3"
```

## Khoảng trắng

```python
# ✅ Đúng
x = 10
y = x + 5
result = func(a, b)
my_list = [1, 2, 3]

# ❌ Sai
x=10
y = x+5
result = func( a , b )
my_list = [1,2,3]
```

## Docstring

```python
def tinh_bmi(can_nang: float, chieu_cao: float) -> float:
    """Tính chỉ số BMI.

    Args:
        can_nang: Cân nặng tính bằng kg.
        chieu_cao: Chiều cao tính bằng mét.

    Returns:
        Chỉ số BMI (float).

    Raises:
        ValueError: Nếu chiều cao <= 0.
    """
    if chieu_cao <= 0:
        raise ValueError("Chiều cao phải > 0")
    return can_nang / (chieu_cao ** 2)
```

## Import

```python
# ✅ Mỗi module một dòng, nhóm theo thứ tự
import os
import sys

import requests

from my_module import my_function
```

## Độ dài dòng

Tối đa **88 ký tự** mỗi dòng. Nếu dài hơn, xuống dòng:

```python
# Dùng ngoặc
result = (first_value
          + second_value
          - third_value)

# Dùng \ (ít dùng hơn)
total = first_long_variable + \
        second_long_variable
```

## Quy tắc khóa này

1. **Luôn dùng f-string** thay `format()` hay `%`
2. **Luôn dùng `with`** khi mở file
3. **Không bare `except:`** — luôn chỉ rõ loại exception
4. **Comment giải thích *tại sao***, không giải thích *cái gì*
5. **Mỗi hàm làm MỘT việc** — nếu quá 20 dòng, tách ra
