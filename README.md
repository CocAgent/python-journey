# 🎨 Drawing Score Predictor

> **Dự đoán số điểm bài vẽ dựa trên hình ảnh và các tiêu chí đánh giá.**


**Learning loop:** `Upload → Analyze → Predict → Explain → Improve`
# 🎨 Drawing Score Predictor

> Dự đoán số điểm bài vẽ dựa trên phân tích hình ảnh và các tiêu chí đánh giá.
![Image](<img width="596" height="335" alt="images (3)" src="https://github.com/user-attachments/assets/a2ee0f94-4af1-4c83-84bc-572ffd331c0f" />)
[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)](#-công-nghệ-sử-dụng)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)](#-công-nghệ-sử-dụng)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](#-công-nghệ-sử-dụng)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Project-6366f1?style=flat-square)](#-mô-hình-dự-đoán)


## 🌐 Demo

👉 [**Mở Drawing Score Predictor**](https://username.github.io/drawing-score-predictor/)
---
## 📌 Giới thiệu

**Drawing Score Predictor** là một dự án xây dựng hệ thống có khả năng phân tích hình ảnh của một bài vẽ và đưa ra **mức điểm dự đoán** dựa trên các tiêu chí đánh giá được thiết lập trước.

Thay vì chỉ đưa ra một con số, hệ thống hướng đến việc cung cấp thêm thông tin giúp người dùng hiểu:

* Bài vẽ đang đạt điểm tốt ở tiêu chí nào.
* Những yếu tố nào làm điểm số giảm.
* Bài vẽ có thể cải thiện ở đâu.
* Điểm dự đoán được hình thành như thế nào.

---

## 🎯 Mục tiêu

Project hướng đến các mục tiêu:

1. Xây dựng hệ thống nhận ảnh bài vẽ từ người dùng.
2. Phân tích một số đặc điểm của bài vẽ.
3. Sử dụng dữ liệu đã có để xây dựng mô hình dự đoán điểm.
4. Trả về điểm dự đoán trên thang điểm 10.
5. Hiển thị kết quả theo cách trực quan và dễ hiểu.
6. Giúp người dùng biết những điểm cần cải thiện trong bài vẽ.

---

## 🔄 Quy trình hoạt động

```text
Ảnh bài vẽ
    │
    ▼
Upload ảnh
    │
    ▼
Tiền xử lý hình ảnh
    │
    ▼
Trích xuất đặc trưng
    │
    ├── Bố cục
    ├── Màu sắc
    ├── Độ tương phản
    ├── Chi tiết
    └── Độ hoàn thiện
    │
    ▼
Mô hình Machine Learning
    │
    ▼
Điểm dự đoán
    │
    ▼
Phân tích kết quả
```

---

## ⭐ Kết quả đầu ra

Ví dụ hệ thống có thể trả về:

```text
┌─────────────────────────────────┐
│         KẾT QUẢ ĐÁNH GIÁ        │
├─────────────────────────────────┤
│                                 │
│             8.2 / 10            │
│                                 │
│  Bố cục          8.5            │
│  Màu sắc         8.0            │
│  Chi tiết        8.3            │
│  Hoàn thiện      8.0            │
│                                 │
├─────────────────────────────────┤
│  # Điểm mạnh                    │
│ • Bố cục cân đối                │
│ • Màu sắc hài hòa               │
│                                 │
│  # Cần cải thiện                │
│ • Tăng độ tương phản            │
│ • Bổ sung chi tiết              │
└─────────────────────────────────┘
```

---

## 🛠️ Công nghệ sử dụng

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend / Machine Learning

* Python
* Machine Learning
* Xử lý hình ảnh

### Công cụ

* Visual Studio Code
* Git
* GitHub

---

## 📂 Cấu trúc repository

```text
drawing-score-predictor/
│
├── README.md
│
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── assets/
│       ├── images/
│       └── icons/
│
├── backend/
│   ├── app.py
│   ├── model/
│   │   └── model.pkl
│   └── utils/
│
├── dataset/
│   ├── images/
│   └── labels.csv
│
├── notebooks/
│   └── training.ipynb
│
├── tests/
│
└── requirements.txt
```

---

## 📊 Tiêu chí đánh giá

Project có thể sử dụng các tiêu chí như:

| Tiêu chí         | Trọng số |
| ---------------- | -------: |
| Bố cục           |      20% |
| Màu sắc          |      20% |
| Tỷ lệ / hình thể |      20% |
| Chi tiết         |      20% |
| Độ hoàn thiện    |      20% |

> Các tiêu chí và trọng số có thể được thay đổi tùy theo loại bài vẽ và yêu cầu của người chấm.

---

## 🤖 Mô hình dự đoán

Hệ thống có thể được xây dựng theo quy trình:

```text
Dataset
   ↓
Preprocessing
   ↓
Feature Extraction
   ↓
Train / Validation
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Prediction
```

Mục tiêu không chỉ là tạo ra một con số điểm mà còn đánh giá mức độ phù hợp của mô hình thông qua các chỉ số kiểm tra.

---

## 🚀 Cách chạy project

### 1. Clone repository

```bash
git clone <repository-url>
cd drawing-score-predictor
```

### 2. Cài đặt thư viện Python

```bash
pip install -r requirements.txt
```

### 3. Chạy backend

```bash
python backend/app.py
```

### 4. Mở frontend

Mở:

```text
frontend/index.html
```

hoặc sử dụng **Live Server** trong Visual Studio Code.

---

## 🧪 Kiểm thử

Project sẽ kiểm tra:

* Upload ảnh hợp lệ.
* Upload ảnh không hợp lệ.
* Ảnh có kích thước khác nhau.
* Dự đoán điểm với nhiều bài vẽ.
* Kiểm tra kết quả của mô hình.
* Kiểm tra trường hợp ảnh không thể phân tích.

---

## 📸 Demo

### Trang chính

![Home](assets/demo-home.png)

### Upload bài vẽ

![Upload](assets/demo-upload.png)

### Kết quả dự đoán

![Result](assets/demo-result.png)

---

## ⚠️ Lưu ý

Điểm số được hệ thống đưa ra là **điểm dự đoán**, không phải điểm chính thức của giáo viên hoặc giám khảo.

Độ chính xác của hệ thống phụ thuộc vào:

* Chất lượng dataset.
* Số lượng bài vẽ dùng để huấn luyện.
* Tiêu chí chấm điểm.
* Chất lượng hình ảnh đầu vào.
* Mô hình Machine Learning được sử dụng.

---

## 🎓 Mục đích project

Project được thực hiện với mục đích học tập và nghiên cứu, nhằm kết hợp:

* Lập trình web.
* Xử lý hình ảnh.
* Machine Learning.
* Phân tích dữ liệu.
* Thiết kế giao diện.
* Git và GitHub.

---

## 👨‍💻 Tác giả

**Kannoc**

Sinh viên ngành Công nghệ Thông tin.

---

## 📄 License

Project được thực hiện cho mục đích học tập.
