# Tuần 12 — Module và Package — Tái Sử Dụng Code

> **Python Journey** — Khóa học Python cơ bản cho người mới bắt đầu  
> Thời lượng: 2h lý thuyết + 2h thực hành

---

## 🎯 Mục Tiêu Tuần Này

Sau buổi học, bạn có thể:
- Import và dùng module chuẩn của Python
- Tạo module Python của riêng mình
- Dùng pip cài đặt thư viện bên ngoài
- Hiểu cấu trúc package

---

## 1. Module Chuẩn Python

```python
# math — toán học
import math

print(math.pi)              # 3.141592653589793
print(math.sqrt(16))        # 4.0
print(math.floor(3.7))      # 3
print(math.ceil(3.2))       # 4
print(math.pow(2, 10))      # 1024.0
print(math.log(100, 10))    # 2.0

# random — số ngẫu nhiên
import random

print(random.random())          # Float [0.0, 1.0)
print(random.randint(1, 100))   # Int [1, 100]
print(random.choice(["a","b","c"]))  # Chọn ngẫu nhiên
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)             # Trộn ngẫu nhiên tại chỗ
print(random.sample(lst, 3))    # Chọn 3 phần tử không trùng

# datetime — thời gian
from datetime import datetime, date, timedelta

now = datetime.now()
print(now.strftime("%d/%m/%Y %H:%M:%S"))  # 25/03/2025 14:30:00
today = date.today()
birthday = date(2000, 3, 15)
age_days = (today - birthday).days
print(f"Số ngày đã sống: {age_days:,}")

# os — hệ điều hành
import os

print(os.getcwd())              # Thư mục hiện tại
print(os.path.exists("file.txt"))
files = os.listdir(".")         # Danh sách file trong thư mục
```

## 2. Cách Import

```python
# Cách 1: Import toàn bộ module
import math
math.sqrt(16)

# Cách 2: Import chỉ những gì cần (khuyến nghị)
from math import sqrt, pi, floor
sqrt(16)  # Không cần viết math.

# Cách 3: Import với alias
import numpy as np      # Dùng alias np thay vì numpy

# ❌ Không nên
from math import *     # Import TẤT CẢ — gây xung đột tên
```

## 3. Tạo Module Của Riêng Mình

```python
# File: toan_hoc.py
"""Module các hàm toán học tùy chỉnh."""

PI = 3.14159

def tinh_chu_vi_duong_tron(r):
    """Tính chu vi đường tròn."""
    return 2 * PI * r

def tinh_dien_tich_duong_tron(r):
    """Tính diện tích đường tròn."""
    return PI * r ** 2

def so_nguyen_to(n):
    """Kiểm tra số nguyên tố."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

```python
# File: main.py — sử dụng module
import toan_hoc

r = 5
print(f"Chu vi: {toan_hoc.tinh_chu_vi_duong_tron(r):.2f}")
print(f"Diện tích: {toan_hoc.tinh_dien_tich_duong_tron(r):.2f}")

# Kiểm tra số nguyên tố
so_nt = [n for n in range(2, 50) if toan_hoc.so_nguyen_to(n)]
print(f"Số nguyên tố < 50: {so_nt}")
```

## 4. Cài Thư Viện Bên Ngoài — pip

```bash
# Cài thư viện
pip install requests       # HTTP requests
pip install rich           # In đẹp ra terminal

# Kiểm tra đã cài
pip list
pip show requests

# Tạo requirements.txt (lưu danh sách thư viện)
pip freeze > requirements.txt

# Cài từ requirements.txt (chia sẻ dự án)
pip install -r requirements.txt
```

```python
# Dùng requests
import requests

response = requests.get("https://api.github.com")
print(response.status_code)   # 200
data = response.json()
print(data.keys())
```

## 5. Bài Tập

### Bài 1 — Ứng dụng thời gian (Dễ)
Dùng datetime tính: tuổi, số ngày đến sinh nhật tiếp theo, ngày trong tuần.

### Bài 2 — Game đoán số nâng cao (Trung bình)
Dùng random: game đoán số với seed cố định, thống kê số lần đoán.

### Bài 3 — Module tiện ích (Thử thách)
Tạo module utils.py với 5 hàm hữu ích, import và dùng trong project.

---

## 🔑 Những Điều Quan Trọng Nhất Tuần Này

> 1. **from module import func** tốt hơn import * — rõ ràng những gì được dùng
> 2. **requirements.txt** là cách chia sẻ dependencies — luôn tạo cho project
> 3. **if __name__ == '__main__'** cho phép file vừa là module vừa là script chạy độc lập
