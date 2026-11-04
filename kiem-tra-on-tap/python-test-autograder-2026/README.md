# 🧪 Python Test & Auto Grader 2026

Bộ tài liệu thực hành Python gồm đề kiểm tra, mã bài làm mẫu, bộ test và chương trình chấm tự động cho ba nhóm **CBPYTHON**, **NCPYTHON** và **NDPYTHON**.

> Dữ liệu được sắp xếp lại từ bộ tài liệu Python Test 2026. Các file Python được giữ theo nội dung trong bộ ZIP nguồn; dự án không tự ý sửa đáp án hay nội dung đề.

## 📚 Nội dung

| Nhóm | Thư mục | Nội dung |
|---|---|---|
| CBPYTHON | [Test-CBPYTHON-090725](Test-CBPYTHON-090725/) | Test đề 1, đề 2, các phiên bản autograder và bài làm mẫu |
| NCPYTHON | [Test-NCPYTHON-090725](Test-NCPYTHON-090725/) | Test đề 1, đề 2, các phiên bản autograder và bài làm mẫu |
| NDPYTHON | [Test-NDPYTHON-090725](Test-NDPYTHON-090725/) | Test đề 1, đề 2, các phiên bản autograder và bài làm mẫu |

Mỗi nhóm có thể gồm:
- `test_de1.py`, `test_de2.py`: dữ liệu test cho từng đề.
- `autograde_de*_v*.py`: chương trình chấm tự động theo phiên bản.
- `submissions/`, `submissions_de1/`, `submissions_de2/`: các file bài làm mẫu theo từng câu.

## ⚙️ Yêu cầu

- Python 3.10 trở lên (khuyến nghị dùng Python 3.11 hoặc 3.12).
- Windows, macOS hoặc Linux.
- Không cần cài thư viện ngoài nếu chỉ chạy các script hiện có.

Kiểm tra Python:

```bash
python --version
```

Trên Windows nếu lệnh `python` không hoạt động, thử:

```powershell
py --version
```

## ▶️ Cách chạy chương trình chấm

Ví dụ với CBPYTHON, mở Terminal tại thư mục:

```text
kiem-tra-on-tap/python-test-autograder-2026/Test-CBPYTHON-090725
```

Chạy chấm đề 1:

```powershell
py autograde_de1_v1.py
```

Chấm đề 2 (chọn đúng phiên bản có trong thư mục):

```powershell
py autograde_de2_v1.py
```

Với NCPYTHON hoặc NDPYTHON, làm tương tự trong thư mục tương ứng. Tên file autograder có thể khác phiên bản; hãy xem danh sách file trước khi chạy:

```powershell
dir
```

## 🧑‍💻 Chạy một bài làm riêng

Ví dụ:

```powershell
cd Test-CBPYTHON-090725
py submissions_de1/Cau1a.py
```

Một số file bài làm mẫu nhận dữ liệu bằng `input()`, vì vậy hãy nhập dữ liệu khi chương trình yêu cầu.

## 🗂️ Cấu trúc thư mục

```text
python-test-autograder-2026/
├── README.md
├── Test-CBPYTHON-090725/
│   ├── test_de1.py
│   ├── test_de2.py
│   ├── autograde_*.py
│   ├── submissions/
│   ├── submissions_de1/
│   └── submissions_de2/
├── Test-NCPYTHON-090725/
│   └── ...
└── Test-NDPYTHON-090725/
    └── ...
```

## ⚠️ Lưu ý

1. Chạy autograder từ đúng thư mục nhóm để Python tìm được module `test_de1.py` hoặc `test_de2.py`.
2. Giữ nguyên tên file và cấu trúc thư mục `submissions_de1`, `submissions_de2` vì chương trình chấm tham chiếu trực tiếp đến các đường dẫn này.
3. Các phiên bản autograder có thể khác nhau về cách chấm. Hãy dùng đúng phiên bản được yêu cầu trong tài liệu môn học.
4. Điểm từ autograder chỉ mang tính tham khảo theo các test case được lập trình, không thay thế kết quả chấm chính thức.
5. PDF đề thi và tài liệu gốc không được đưa vào thư mục code này; hãy lưu bản gốc riêng nếu cần đối chiếu.

## 🎯 Mục tiêu học tập

- Luyện giải bài tập Python theo từng câu.
- Hiểu cách dữ liệu đầu vào được kiểm thử.
- Biết cách chạy chương trình chấm tự động.
- Tự phát hiện lỗi và cải thiện bài làm trước khi nộp.

---

**Tác giả:** [LeTriDung-A](https://github.com/LeTriDung-A)  
**Repository:** [python-journey-123](https://github.com/LeTriDung-A/python-journey-123)
