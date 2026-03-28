# Tuần 01 — Cài Đặt Môi Trường & Chương Trình Đầu Tiên

> **Python Journey** — Khóa học Python cơ bản cho người mới bắt đầu  
> Thời lượng: 2h lý thuyết + 2h thực hành

---

## 🎯 Mục Tiêu Tuần Này

Sau buổi học, bạn có thể:
- Cài đặt Python và VS Code trên máy tính của mình
- Giải thích Python là gì và tại sao nên học
- Viết và chạy chương trình Python đầu tiên
- Hiểu sự khác biệt giữa `print()` và biểu thức
- Dùng Python như một chiếc máy tính thông minh

---

## 1. Python Là Gì? Tại Sao Học?

### 1.1 Python Là Ngôn Ngữ Lập Trình

Hãy tưởng tượng bạn muốn ra lệnh cho máy tính làm gì đó — tính toán, sắp xếp dữ liệu, gửi email tự động. Máy tính không hiểu tiếng Việt hay tiếng Anh, nhưng nó hiểu **ngôn ngữ lập trình**. Python là một trong những ngôn ngữ đó.

**Điều đặc biệt của Python**: Cú pháp gần với tiếng Anh tự nhiên, dễ đọc, dễ học hơn hầu hết các ngôn ngữ khác.

```python
# Ví dụ: Python đọc như tiếng Anh
if tuoi >= 18:
    print("Bạn đã đủ tuổi lái xe")
```

So sánh với ngôn ngữ khác khó đọc hơn nhiều.

### 1.2 Python Dùng Để Làm Gì?

| Lĩnh vực | Ví dụ thực tế |
|---------|-------------|
| **Data Science / AI** | ChatGPT, các mô hình AI đều dùng Python |
| **Web Development** | Instagram, Pinterest xây bằng Django (Python) |
| **Automation** | Tự động điền form, scrape dữ liệu, gửi báo cáo |
| **Khoa học** | NASA, CERN dùng Python phân tích dữ liệu |
| **Tài chính** | Phân tích cổ phiếu, trading bot |

### 1.3 Tại Sao Python Phổ Biến Nhất?

- **Dễ học**: Người mới có thể viết code chạy được trong 30 phút
- **Cộng đồng lớn**: Hàng triệu người, hàng triệu thư viện có sẵn
- **Lương cao**: Developer Python thuộc nhóm lương cao nhất
- **Đa năng**: Một ngôn ngữ, muôn vàn ứng dụng

---

## 2. Cài Đặt Môi Trường

### 2.1 Cài Python

**Bước 1**: Truy cập [python.org/downloads](https://python.org/downloads)

**Bước 2**: Tải Python 3.11 hoặc mới hơn (phiên bản có chữ "Latest")

**Bước 3**: Chạy file cài đặt
> ⚠️ **Quan trọng**: Tích chọn **"Add Python to PATH"** trước khi nhấn Install!

**Bước 4**: Xác nhận cài đặt thành công:
```bash
# Mở Command Prompt (Windows) hoặc Terminal (Mac/Linux)
python --version
# Kết quả mong đợi: Python 3.11.x hoặc cao hơn
```

### 2.2 Cài VS Code (Editor)

**VS Code** (Visual Studio Code) là phần mềm soạn thảo code — như Microsoft Word nhưng dành cho lập trình viên.

1. Tải tại [code.visualstudio.com](https://code.visualstudio.com)
2. Cài đặt bình thường (Next → Next → Finish)
3. Mở VS Code → Extensions (biểu tượng ô vuông bên trái) → Tìm "Python" → Install

### 2.3 Cấu Trúc Thư Mục Dự Án

```
python-journey/           ← Thư mục gốc của bạn
├── week-01/
│   ├── hello.py          ← File Python đầu tiên
│   └── calculator.py
├── week-02/
└── ...
```

Tạo thư mục này trên máy tính của bạn ngay bây giờ!

---

## 3. Chương Trình Python Đầu Tiên

### 3.1 Tạo File và Chạy

1. Mở VS Code
2. File → New File → Lưu với tên `hello.py`
3. Gõ đoạn code sau:

```python
# Đây là comment — Python bỏ qua dòng này
# Comment giúp giải thích code cho người đọc

print("Xin chào thế giới!")
print("Tôi đang học Python!")
print("Tuần 1 — bắt đầu hành trình!")
```

4. Nhấn **Ctrl+F5** (hoặc nút ▶ góc trên phải) để chạy

**Kết quả:**
```
Xin chào thế giới!
Tôi đang học Python!
Tuần 1 — bắt đầu hành trình!
```

🎉 **Chúc mừng!** Bạn vừa viết chương trình Python đầu tiên!

### 3.2 Hàm `print()` — In Ra Màn Hình

`print()` là lệnh yêu cầu Python hiển thị nội dung ra màn hình.

```python
# In văn bản (dùng dấu nháy đơn hoặc kép đều được)
print("Xin chào!")
print('Xin chào!')

# In số
print(42)
print(3.14)

# In nhiều thứ cùng lúc (ngăn cách bằng dấu phẩy)
print("Tuổi của tôi:", 25)
print("Pi xấp xỉ:", 3.14)

# In dòng trống
print()

# Thay đổi ký tự ngăn cách (mặc định là dấu cách)
print("Python", "rất", "thú vị", sep="-")
# Kết quả: Python-rất-thú vị

# Không xuống dòng sau khi in
print("Dòng 1 ", end="")
print("tiếp tục ở đây")
# Kết quả: Dòng 1 tiếp tục ở đây
```

### 3.3 Python Như Máy Tính

Bạn có thể dùng Python trực tiếp để tính toán — không cần viết file:

```bash
# Mở Python Interactive Shell
python
```

```python
# Trong Python shell (dấu >>> là dấu nhắc lệnh)
>>> 2 + 3
5
>>> 10 - 4
6
>>> 3 * 7
21
>>> 20 / 4
5.0
>>> 2 ** 10       # 2 mũ 10
1024
>>> 17 % 5        # Phần dư của 17 ÷ 5
2
>>> 17 // 5       # Chia lấy phần nguyên
3
```

**Thứ tự ưu tiên phép tính** (giống toán học):
```python
>>> 2 + 3 * 4       # Nhân trước, cộng sau
14
>>> (2 + 3) * 4     # Ngoặc tính trước
20
```

---

## 4. Comments — Ghi Chú Trong Code

Comments là những dòng Python bỏ qua khi chạy. Dùng để:
- Giải thích code
- Ghi nhớ ý tưởng
- Tắt tạm thời một đoạn code

```python
# Đây là comment một dòng

# Tính diện tích hình chữ nhật
# Công thức: chiều dài × chiều rộng
print(5 * 3)  # In ra: 15

"""
Đây là comment nhiều dòng
Thường dùng để mô tả
chức năng của một đoạn code lớn
"""
print("Code vẫn chạy bình thường")
```

> 💡 **Thói quen tốt**: Viết comment TRƯỚC khi viết code — giải thích bạn định làm gì, rồi mới code. Điều này giúp tư duy rõ ràng hơn.

---

## 5. Lỗi Thường Gặp Tuần Này

### Lỗi 1: SyntaxError — Sai cú pháp

```python
# ❌ Sai — thiếu dấu nháy đóng
print("Xin chào)

# ✅ Đúng
print("Xin chào")
```

### Lỗi 2: NameError — Gọi thứ chưa tồn tại

```python
# ❌ Sai — Python (chữ hoa) không phải tên hàm
Print("Xin chào")

# ✅ Đúng — print viết thường
print("Xin chào")
```

### Lỗi 3: IndentationError — Thụt đầu dòng sai

```python
# ❌ Sai — có thụt đầu dòng thừa
    print("Xin chào")

# ✅ Đúng — không thụt đầu dòng ở cấp này
print("Xin chào")
```

> 💡 **Mẹo đọc lỗi**: Khi có lỗi, Python luôn cho bạn biết:
> - **Dòng số mấy** bị lỗi
> - **Loại lỗi** là gì  
> - **Mô tả** lỗi ngắn gọn
>
> Đọc kỹ thông báo lỗi trước khi hỏi — thường câu trả lời đã có sẵn trong đó!

---

## 6. Bài Tập Thực Hành

### Bài 1 — Tự giới thiệu (Dễ)
Viết chương trình in ra thông tin của bạn:
```
Tên: [Tên của bạn]
Tuổi: [Tuổi của bạn]
Thành phố: [Thành phố của bạn]
Lý do học Python: [...]
```

### Bài 2 — Máy tính cơ bản (Dễ)
Viết code tính và in ra kết quả:
- Tổng của 123 và 456
- Tích của 17 và 38
- 2 mũ 8
- Phần dư của 100 chia 7

### Bài 3 — Hình chữ nhật (Trung bình)
Một căn phòng dài 8m, rộng 5m, cao 3m. Tính và in ra:
- Diện tích sàn
- Chu vi sàn
- Diện tích tường (không tính trần và sàn)
- Thể tích phòng

### Bài 4 — Vẽ hình bằng ký tự (Thử thách)
Dùng `print()` vẽ một ngôi nhà như thế này:
```
    *
   ***
  *****
 *******
   |||
   |||
```

---

## 7. Dự Án Tuần 1 — Card Giới Thiệu Bản Thân

Tạo file `business_card.py` in ra card giới thiệu chuyên nghiệp:

```
╔══════════════════════════════════════╗
║         NGUYỄN VĂN A                ║
║         Python Developer             ║
╠══════════════════════════════════════╣
║  📧 Email: email@example.com         ║
║  📱 Phone: 0123-456-789              ║
║  🌐 GitHub: github.com/yourname      ║
╚══════════════════════════════════════╝
         "Hành trình ngàn dặm
          bắt đầu từ một bước chân"
```

*Gợi ý: Dùng nhiều lệnh `print()`, mỗi lệnh in một dòng của card.*

---

## 📚 Tài Liệu Tham Khảo

| Tài liệu | Mô tả |
|---------|-------|
| [docs.python.org](https://docs.python.org/3/) | Tài liệu chính thức Python |
| [python.org/shell](https://www.python.org/shell/) | Python shell online (không cần cài) |
| [Real Python — Beginners Guide](https://realpython.com/python-first-steps/) | Hướng dẫn bước đầu |

---

## 🔑 Những Điều Quan Trọng Nhất Tuần Này

> 1. **`print()`** là cách Python nói chuyện với bạn — dùng nó thật nhiều lúc mới học
> 2. **Comment** không phải xa xỉ — đó là thói quen của lập trình viên giỏi
> 3. **Đọc thông báo lỗi** — Python luôn chỉ cho bạn vấn đề ở đâu, hãy tận dụng
