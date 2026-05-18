# Tuần 15 — Dự Án Cuối Khóa & Tổng Kết Hành Trình

> **Python Journey** — Khóa học Python cơ bản cho người mới bắt đầu  
> Thời lượng: 5h (dự án + tổng kết + demo)

---

## 🎯 Mục Tiêu Tuần Này

- Hoàn thành **Dự án cuối khóa** sử dụng toàn bộ kiến thức 14 tuần
- Thực hành quy trình phát triển phần mềm thực tế
- Viết README và documentation chuyên nghiệp
- Nhìn lại hành trình và xác định bước tiếp theo

---

## 1. Tổng Kết 15 Tuần Học

```
Tuần 01: print(), comment, phép tính        → "Hello World"
Tuần 02: Biến, kiểu dữ liệu, input()       → Calculator
Tuần 03: if/elif/else, logic               → Grade calculator
Tuần 04: Chuỗi, indexing, methods          → Text analyzer
Tuần 05: List, tuple, comprehension        → Shopping list
Tuần 06: for/while, break/continue         → Pattern printer
Tuần 07: Hàm, scope, docstring            → Math toolkit
Tuần 08: Dict, Set, phép toán tập hợp     → Word counter
Tuần 09: DỰ ÁN GIỮA KỲ                   → Student Manager
Tuần 10: File I/O, CSV, JSON              → Data persistence
Tuần 11: try/except, Exception             → Robust programs
Tuần 12: Module, pip, venv                → Library usage
Tuần 13: OOP - Class, Object             → Blueprint thinking
Tuần 14: Kế thừa, Đa hình                → Code reuse
Tuần 15: DỰ ÁN CUỐI KHÓA                 → FULL APPLICATION
```

---

## 2. Dự Án Cuối Khóa — Chọn Một Trong Ba

### Option A — Hệ Thống Ngân Hàng Mini

**Mô tả**: Ứng dụng quản lý tài khoản ngân hàng với các tính năng:
- Tạo tài khoản (tiết kiệm / thanh toán)
- Gửi tiền, rút tiền, chuyển khoản
- Xem lịch sử giao dịch
- Tính lãi (cho tài khoản tiết kiệm)
- Lưu/đọc dữ liệu từ file JSON

**Kỹ năng dùng**: OOP (kế thừa Account → SavingsAccount/CheckingAccount), File I/O, Exception handling, Dict, List

### Option B — Ứng Dụng Ghi Chú (Notes App)

**Mô tả**: Ứng dụng quản lý ghi chú cá nhân:
- Tạo, xem, sửa, xóa ghi chú
- Tìm kiếm theo từ khóa
- Gắn thẻ (tags) cho ghi chú
- Lưu dữ liệu vào file
- Thống kê (số ghi chú, tags phổ biến)

**Kỹ năng dùng**: OOP (Note, NoteManager), File I/O, Dict/Set, String methods, Exception

### Option C — Game Quiz Python

**Mô tả**: Game hỏi đáp kiến thức Python:
- Câu hỏi nhiều lựa chọn với timer
- Nhiều cấp độ khó (Easy/Medium/Hard)
- Hệ thống điểm số và lưu high score
- Sinh câu hỏi ngẫu nhiên từ file JSON
- Báo cáo kết quả sau mỗi session

**Kỹ năng dùng**: OOP, File I/O, Random, Dict/List, Exception, Module

---

## 3. Cấu Trúc Dự Án Chuẩn

```
ten_du_an/
├── README.md          ← Mô tả, hướng dẫn chạy, screenshots
├── requirements.txt   ← Danh sách thư viện (nếu có dùng pip)
├── main.py           ← Điểm vào chương trình
├── src/
│   ├── models.py     ← Các class OOP
│   ├── utils.py      ← Hàm tiện ích
│   └── config.py     ← Cấu hình
├── data/
│   └── .gitkeep      ← File dữ liệu sẽ được tạo khi chạy
└── tests/
    └── test_basic.py ← Kiểm thử cơ bản
```

---

## 4. Template README.md

```markdown
# [Tên Dự Án]

> Mô tả ngắn trong một câu.

## Tính Năng

- Tính năng 1
- Tính năng 2
- ...

## Cách Chạy

```bash
# Clone hoặc tải về
git clone https://github.com/username/ten-du-an

# Cài thư viện (nếu cần)
pip install -r requirements.txt

# Chạy chương trình
python main.py
```

## Demo

[Screenshot hoặc mô tả ngắn luồng chính]

## Tác Giả

- **Họ Tên** — [GitHub Profile](link)

## Kỹ Năng Đã Dùng

Python, OOP, File I/O, Exception Handling, ...
```

---

## 5. Tiêu Chí Đánh Giá Dự Án Cuối Kỳ

| Tiêu chí | Điểm |
|---------|------|
| Chức năng đầy đủ, hoạt động đúng | 3.0 |
| Áp dụng OOP hợp lý (≥2 class có kế thừa) | 2.0 |
| Xử lý lỗi đúng chỗ (file, input, edge cases) | 1.5 |
| Lưu dữ liệu vào file (persist across sessions) | 1.0 |
| Code sạch: tên rõ, docstring, comment | 1.0 |
| README đầy đủ và rõ ràng | 0.5 |
| Tính năng bổ sung sáng tạo | +1.0 |
| **Tổng** | **10** |

---

## 6. Bước Tiếp Theo Sau Python Journey

```
Python Journey (Bạn đang ở đây! ✓)
         ↓
    Chọn hướng đi:
         ├── Web Development  → Django, FastAPI, HTML/CSS
         ├── Data Science     → Pandas, NumPy, Matplotlib, ML
         ├── Automation       → Selenium, BeautifulSoup, APIs
         ├── Game Dev         → Pygame
         └── AI / ML          → scikit-learn, PyTorch, LangChain
```

**Tiếp theo trong AHappyNet**:
- [python-mastery](https://github.com/CocAgent/python-mastery) — OOP nâng cao, design patterns, concurrency
- [dsa-python-course](https://github.com/CocAgent/dsa-python-course) — Cấu trúc dữ liệu và thuật toán
- [data-python-course](https://github.com/CocAgent/data-python-course) — Pandas, NumPy, visualization

---

## 7. Lời Kết Hành Trình

> *"The secret is to get started."* — Mark Twain

15 tuần trước, bạn không biết Python là gì.  
Hôm nay bạn đã xây dựng được một ứng dụng hoàn chỉnh.

Điều đó không nhỏ.

Những gì bạn đã học không chỉ là Python — bạn đã học cách **suy nghĩ như một lập trình viên**: chia nhỏ vấn đề, xây dựng từng phần, test, sửa lỗi, cải tiến. Kỹ năng này áp dụng được cho bất kỳ ngôn ngữ nào.

**Bước tiếp theo đơn giản nhất**: Làm một project nhỏ giải quyết vấn đề thực tế của chính bạn. Không cần hoàn hảo — cần chạy được.

---

## 🔑 Những Điều Quan Trọng Nhất Của Toàn Khóa

> 1. **Python được học qua làm** — đọc code 1 lần < viết code 10 lần
> 2. **Lỗi là bạn, không phải kẻ thù** — mỗi lỗi là một bài học cụ thể
> 3. **Bước tiếp theo**: chọn một project thực tế và bắt đầu ngay hôm nay
