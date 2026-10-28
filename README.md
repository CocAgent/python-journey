# 🐍 Python Journey

> Hành trình học Python từ cơ bản đến nâng cao — học lý thuyết, làm bài tập và xây dựng project.

---

## 👨‍💻 Thông tin

- **Tên:** Bùi Trung Sơn
- **Ngôn ngữ:** Python
- **Mục tiêu:** Học và thực hành Python từ cơ bản đến nâng cao
- **GitHub:** buitrungson09-maker

---

## 📚 Lộ trình học — cập nhật 28/10/2026

| Tuần | Chủ đề | Trạng thái |
|---|---|---|
| Week 01 | Hello Python | ✅ Đã thực hành |
| Week 02 | Variables & Data Types | ✅ Đã thực hành |
| Week 03 | Conditionals | ✅ Đã thực hành |
| Week 04 | Strings | ✅ Đã thực hành |
| Week 05 | Lists & Tuples | ✅ Đã thực hành |
| Week 06 | Loops | ✅ Đã thực hành |
| Week 07 | Functions | ✅ Đã thực hành |
| Week 08 | Dictionaries & Sets | ✅ Đã thực hành |
| Week 09 | Midterm Project / Student Manager | ✅ Đã thực hành |
| Week 10 | Files I/O | ✅ Đã thực hành |
| Week 11 | Exceptions | ✅ Đã thực hành |
| Week 12 | Testing with Pytest | ✅ Đã thực hành (4 test đã pass) |
| Week 13 | Modules & CLI API | ⏳ Kế tiếp |
| Week 14 | OOP Essentials | ⏳ Chưa xác nhận hoàn thành |
| Week 15 | Capstone Project | ⏳ Chưa xác nhận hoàn thành |

> Các dấu ✅ ghi nhận nội dung đã thực hành; không đồng nghĩa mọi bài tập trong tuần đã được kiểm tra đầy đủ.
---

## 📁 Cấu trúc thư mục

```text
python-journey/
│
├── weeks/
│   ├── week-01-hello-python/
│   │
│   ├── week-02-variables-types/
│   │   ├── checks/
│   │   ├── examples/
│   │   ├── exercises/
│   │   │   ├── ex01_variables.py
│   │   │   ├── ex02_type_conversion.py
│   │   │   └── ex03_input_calc.py
│   │   ├── mini-project/
│   │   ├── solutions/
│   │   ├── hints.md
│   │   ├── notes.md
│   │   └── README.md
│   │
│   ├── week-03-conditionals/
│   ├── week-04-strings/
│   ├── week-05-lists-tuples/
│   ├── week-06-loops/
│   ├── week-07-functions/
│   ├── week-08-dicts-sets/
│   ├── week-09-midterm-project/
│   ├── week-10-files-io/
│   ├── week-11-exceptions/
│   ├── week-12-testing-pytest/
│   ├── week-13-modules-cli-api/
│   ├── week-14-oop-essentials/
│   └── week-15-capstone-project/
│
├── projects/
├── scripts/
├── tests/
└── README.md
```

---

## 🚀 Week 02 — Variables & Data Types

### 📝 Bài tập

- `ex01_variables.py` — Biến trong Python
- `ex02_type_conversion.py` — Chuyển đổi kiểu dữ liệu
- `ex03_input_calc.py` — Nhập dữ liệu và tính toán

### 🧠 Kiến thức đã học

- Khai báo và sử dụng biến
- Kiểu dữ liệu `str`, `int`, `float`, `bool`
- Kiểm tra kiểu dữ liệu bằng `type()`
- Chuyển đổi kiểu bằng `int()`, `float()`, `str()`, `bool()`
- Nhập dữ liệu bằng `input()`
- Multiple Assignment
- Hoán đổi giá trị hai biến
- Augmented Assignment: `+=`, `-=`, `*=`, `//=`
- F-string
- Tính BMI
- Chuyển đổi giây sang giờ, phút, giây

---

## 💻 Ví dụ Python

```python
ten = "Son"
tuoi = 18
diem_tb = 8.5
dang_hoc = True

print(ten, type(ten))
print(tuoi, type(tuoi))
print(diem_tb, type(diem_tb))
print(dang_hoc, type(dang_hoc))
```

---

## 🔄 Hoán đổi biến

```python
a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)
```

**Kết quả:**

```text
a = 20
b = 10
```

---

## 🧮 Augmented Assignment

```python
x = 100

x += 20
x -= 10
x *= 2
x //= 5

print(x)
```

**Kết quả:**

```text
44
```

---

## 🛠️ Công nghệ sử dụng

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-Version_Control-orange?logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)
![VS Code](https://img.shields.io/badge/VS_Code-Editor-blue?logo=visualstudiocode&logoColor=white)

---

## 🎯 Mục tiêu

- ✅ Làm quen với Python và môi trường lập trình
- 🔄 Nắm chắc Python cơ bản
- 🔄 Hoàn thành bài tập theo từng tuần
- 🔄 Thành thạo Git và GitHub
- ⏳ Hoàn thành Mini Project
- ⏳ Hoàn thành Capstone Project

---

## 📈 Tiến độ hiện tại

- **Week 01–12:** ✅ Đã thực hành, có các bài về file I/O, xử lý ngoại lệ và Pytest.
- **Week 12:** ✅ Đã chạy 4 bài kiểm thử thành công (theo kết quả thực hành).
- **Week 13:** ⏳ Modules & CLI API — ưu tiên tiếp theo.
- **Week 14–15:** ⏳ OOP và Capstone — chưa xác nhận hoàn thành.
- **Mini project 3 Agent:** đang nâng cấp từ mô phỏng vai trò sang agent sử dụng AI thật.

*Cập nhật: 28/10/2026.*
---

## 🌟 Learning Journey

> **Code → Practice → Error → Fix → Improve 🚀**

Mỗi bài tập là một bước tiến trong hành trình học lập trình Python.

---

⭐ **Keep learning. Keep coding.**