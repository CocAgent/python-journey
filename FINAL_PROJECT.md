# Dự án cuối khóa — Python Journey 🎓

> **Capstone Project**  
> Xây dựng một chương trình Python hoàn chỉnh để chứng minh rằng bạn có thể **phân tích vấn đề, tổ chức code, kiểm thử, xử lý lỗi và cải tiến chương trình**.

---

## 1. Mục tiêu

Dự án cuối khóa không kiểm tra việc ghi nhớ cú pháp.

Bạn cần chứng minh rằng mình có thể thực hiện một vòng phát triển chương trình nhỏ:

```text
Vấn đề
   ↓
Thiết kế
   ↓
Viết code
   ↓
Chạy thử
   ↓
Test
   ↓
Debug
   ↓
Cải tiến
   ↓
Giải thích
```

Sau dự án, bạn cần có khả năng:

- chia vấn đề thành các phần nhỏ;
- tổ chức chương trình bằng hàm và module;
- lựa chọn cấu trúc dữ liệu Python phù hợp;
- lưu và đọc dữ liệu khi cần;
- xử lý input sai và các lỗi có thể dự đoán;
- kiểm thử logic chính;
- đọc traceback và sửa lỗi;
- viết code dễ đọc;
- sử dụng Git/GitHub;
- giải thích được các quyết định quan trọng trong code.

---

## 2. Nguyên tắc thiết kế

Dự án được đánh giá theo **chất lượng giải pháp**, không theo số lượng kỹ thuật được sử dụng.

Không bắt buộc:

- số lượng class;
- inheritance;
- sử dụng mọi cấu trúc dữ liệu;
- thư viện bên ngoài;
- giao diện đồ họa;
- số lượng dòng code.

> **Giải pháp đơn giản, đúng và dễ hiểu tốt hơn giải pháp phức tạp không cần thiết.**

---

## 3. Yêu cầu chức năng

Dự án phải giải quyết một vấn đề rõ ràng và có ít nhất **4 chức năng có ý nghĩa**.

Ví dụ với Expense Tracker:

```text
1. Thêm giao dịch
2. Xem giao dịch
3. Tính tổng chi tiêu
4. Lọc theo danh mục
5. Lưu dữ liệu
```

Các thao tác như `Thoát`, `In menu`, `In tiêu đề` không được tính là chức năng nghiệp vụ.

---

## 4. Yêu cầu Python

### Functions

Logic chính phải được chia thành các hàm có trách nhiệm rõ ràng.

```python
def add_transaction(...):
    ...

def calculate_total(...):
    ...

def load_data(...):
    ...

def save_data(...):
    ...
```

Không viết toàn bộ chương trình trong một hàm `main()` rất dài.

### Data structures

Sử dụng cấu trúc phù hợp:

```text
list
dict
set
tuple
```

Không cần cố sử dụng tất cả.

Bạn cần giải thích được tại sao cấu trúc đã chọn phù hợp với bài toán.

### Files và dữ liệu

Khi ứng dụng cần lưu trạng thái, có thể sử dụng:

```text
JSON
CSV
text file
```

Ưu tiên `pathlib` khi làm việc với đường dẫn.

### Exceptions

Xử lý hợp lý các trường hợp như:

- file chưa tồn tại;
- input sai kiểu;
- dữ liệu thiếu;
- giá trị không hợp lệ;
- JSON lỗi.

Không dùng:

```python
except:
    pass
```

để che lỗi.

### Modules

Khi chương trình lớn dần, nên tách trách nhiệm:

```text
project/
├── main.py
└── src/
    ├── storage.py
    ├── models.py
    └── utils.py
```

### OOP

Class chỉ nên được dùng khi giúp mô hình hóa bài toán rõ hơn.

OOP và inheritance **không phải yêu cầu bắt buộc**.

Không tạo class chỉ để đủ tiêu chí chấm điểm.

---

## 5. Kiểm thử

Dự án phải có ít nhất **5 test có ý nghĩa** cho logic chính.

Nên kiểm tra cả:

```text
normal case
boundary case
empty input
invalid input
unexpected data
```

Ví dụ:

```python
def test_calculate_total():
    ...

def test_empty_transactions():
    ...

def test_negative_amount_rejected():
    ...
```

Mục tiêu của test là phát hiện hành vi sai, không phải chỉ tạo ra kết quả PASS.

---

## 6. Debugging

Trước khi nộp, hãy chủ động thử các tình huống:

- file không tồn tại;
- danh sách rỗng;
- nhập chữ thay vì số;
- nhập giá trị không hợp lệ;
- dữ liệu bị thiếu;
- dữ liệu JSON sai định dạng.

Mục tiêu không phải chương trình “không bao giờ lỗi”.

Mục tiêu là bạn **biết tìm nguyên nhân và xử lý những lỗi hợp lý**.

---

## 7. Cấu trúc dự án đề nghị

```text
my-project/
├── README.md
├── main.py
├── src/
│   ├── __init__.py
│   ├── models.py
│   ├── storage.py
│   └── utils.py
├── tests/
│   └── test_core.py
├── data/
│   └── .gitkeep
└── AI_USAGE.md
```

Cấu trúc có thể đơn giản hơn nếu project nhỏ.

Không tạo file hoặc module không cần thiết.

---

## 8. README

README của project phải trả lời được:

1. Project giải quyết vấn đề gì?
2. Có những chức năng nào?
3. Chạy như thế nào?
4. Test như thế nào?
5. Các file/module chính có vai trò gì?
6. Những quyết định thiết kế quan trọng là gì?

Ví dụ:

```bash
python main.py
```

và khi khóa học đã học pytest:

```bash
pytest
```

---

## 9. Git và GitHub

Không nên chỉ có một commit cuối cùng.

Ví dụ lịch sử tốt:

```text
feat: add transaction input
feat: save transactions to json
test: cover expense calculations
fix: reject invalid amount
docs: complete project readme
```

Commit nên phản ánh quá trình xây dựng và sửa chương trình.

---

## 10. Sử dụng AI có trách nhiệm

AI có thể hỗ trợ:

- giải thích traceback;
- giải thích khái niệm;
- gợi ý test case;
- review code;
- gợi ý cách chia nhỏ vấn đề;
- giải thích tại sao một cách làm chưa đúng.

Không chấp nhận:

- sinh toàn bộ project rồi nộp nguyên trạng;
- nộp code mà người học không hiểu;
- che giấu lỗi bằng output do AI tạo.

Tạo file:

```text
AI_USAGE.md
```

và trả lời ba câu:

1. Tôi đã dùng AI cho những việc gì?
2. Tôi đã tự viết hoặc thay đổi phần nào?
3. Tôi kiểm chứng câu trả lời của AI bằng cách nào?

Sử dụng AI không bị trừ điểm khi người học **hiểu và kiểm chứng sản phẩm của mình**.

---

## 11. Demo và bảo vệ

Thời gian đề nghị: **5–8 phút**.

Trình bày:

```text
1. Vấn đề
2. Giải pháp
3. Demo
4. Một quyết định thiết kế
5. Một lỗi đã gặp
6. Cách kiểm thử
7. Điều muốn cải tiến
```

Bạn cần giải thích được code mình nộp.

---

## 12. Rubric — 10 điểm

| Tiêu chí | Điểm |
|---|:---:|
| Chức năng và tính đúng đắn | 3.0 |
| Phân rã và thiết kế chương trình | 1.5 |
| Xử lý lỗi và edge cases | 1.0 |
| Testing | 1.5 |
| Chất lượng code | 1.0 |
| README và Git | 1.0 |
| Hiểu và bảo vệ sản phẩm | 1.0 |
| **Tổng** | **10.0** |

Không có điểm riêng cho:

- số lượng class;
- inheritance;
- số dòng code;
- số thư viện;
- số lượng file.

Các yếu tố này chỉ có giá trị khi chúng làm thiết kế tốt hơn.

---

## VuaCóc Bot Journey — Flagship Capstone Track

[VuaCóc Bot Journey](projects/vuacoc-bot-journey/README.md) là flagship track
để người học phát triển cùng một bot từ Week 07 đến Week 15. Đây là một lựa
chọn nổi bật, không phải đề tài bắt buộc duy nhất.

Track này dùng toàn bộ yêu cầu, checklist và rubric canonical trong file này.
Nó không tạo rubric riêng hoặc thay đổi tiêu chí capstone.

---

## 13. Đề tài gợi ý

### A. Personal Expense Tracker 💰

Chức năng:

- thêm giao dịch;
- xem giao dịch;
- phân loại;
- tính tổng;
- tìm/lọc;
- lưu dữ liệu.

Edge cases:

- số tiền không hợp lệ;
- file chưa tồn tại;
- JSON lỗi;
- danh sách rỗng.

---

### B. Notes / Knowledge Manager 📝

Chức năng:

- tạo ghi chú;
- xem;
- sửa;
- xóa;
- tìm theo từ khóa;
- lọc theo tag;
- lưu dữ liệu.

Edge cases:

- tiêu đề rỗng;
- ID không tồn tại;
- tag trùng;
- file dữ liệu lỗi.

---

### C. Quiz / Learning App 🧠

Chức năng:

- đọc câu hỏi;
- hiển thị câu hỏi;
- nhận câu trả lời;
- chấm điểm;
- báo cáo;
- lưu lịch sử hoặc high score.

Edge cases:

- file câu hỏi rỗng;
- answer không hợp lệ;
- câu hỏi thiếu đáp án;
- không có câu hỏi.

---

## 14. Dự án tự chọn

Bạn được khuyến khích giải quyết một vấn đề thực tế của chính mình.

Một đề tài phù hợp khi:

- nằm trong phạm vi Python Journey;
- hoàn thành được trong thời gian quy định;
- có dữ liệu hoặc trạng thái rõ ràng;
- có logic có thể kiểm thử;
- bạn có thể giải thích toàn bộ code.

Không cần chọn dự án lớn.

Capstone nhằm chứng minh **nền tảng Python vững chắc**, không phải xây hệ thống phức tạp nhất.

---

## 15. Checklist trước khi nộp

### Chức năng

- [ ] Chương trình chạy được
- [ ] Có ít nhất 4 chức năng có ý nghĩa
- [ ] Luồng chính hoạt động đúng

### Code

- [ ] Logic được chia thành hàm/module hợp lý
- [ ] Tên biến và hàm rõ ràng
- [ ] Không có code thừa lớn
- [ ] Không dùng bare `except:`

### Testing

- [ ] Có ít nhất 5 test có ý nghĩa
- [ ] Có edge cases
- [ ] Tests chạy được

### Tài liệu

- [ ] Có README.md
- [ ] Có hướng dẫn chạy
- [ ] Có hướng dẫn test
- [ ] Có AI_USAGE.md

### Git

- [ ] Có lịch sử commit hợp lý
- [ ] Không commit secret hoặc file tạm

### Hiểu sản phẩm

- [ ] Giải thích được các hàm chính
- [ ] Giải thích được lựa chọn dữ liệu
- [ ] Giải thích được một bug đã sửa
- [ ] Giải thích được các test quan trọng

---

# Hoàn thành Python Journey

Mục tiêu cuối cùng là chuyển từ:

> “Tôi đã học cú pháp Python.”

sang:

> **“Tôi có thể dùng Python để giải quyết một vấn đề, kiểm chứng chương trình và giải thích tại sao giải pháp hoạt động.”**

Đây là nền tảng để tiếp tục với:

- **Python Mastery**
- **DSA with Python**
- **Data Python**
- các hướng ứng dụng Python khác.

---

> **Build it. Test it. Understand it. Improve it.**
