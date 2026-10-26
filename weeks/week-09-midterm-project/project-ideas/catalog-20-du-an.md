# Danh mục 20 dự án mã nguồn mở tham khảo — Tuần 09

> **Nguồn:** tài liệu giảng viên *Bài tập nhóm thực hành Python.docx*, mục “Tổng hợp 20 dự án mã nguồn mở tiềm năng (Python – AI – Agent – Edge – Robotics – Game)”. Danh sách tên, lĩnh vực và liên kết bên dưới được đối chiếu với tài liệu gốc. **Ý tưởng MVP, đầu vào/đầu ra, phép thử và mức gợi ý là phần biên soạn bổ sung cho Python Journey**, không phải nội dung được tài liệu Word quy định.

**Không cần sao chép, viết lại hoặc cài đặt cả dự án mã nguồn mở.** Chọn *một ý tưởng nhỏ được gợi cảm hứng*, dùng Python 3.12+ cùng kiến thức Tuần 01–08: `if`, `list`, `dict`, vòng lặp và hàm. Có thể trình bày demo CLI ngoại tuyến, không cần GPU, mô hình AI, robot, server hoặc tài khoản dịch vụ.

Các nhãn “Dễ bắt đầu”, “Mở rộng”, “Định hướng” chỉ mô tả độ khó khi muốn **dùng chính framework**; *không quyết định điểm*. MVP Python thuần vẫn được chấm đầy đủ theo [rubric 10 điểm](rubric-10-diem.md). Mỗi nhóm 1–3 sinh viên chọn **một đề tài**; cũng có thể tự đề xuất ngoài danh sách nếu dùng Python là chính.

## Toàn bộ 20 dự án và MVP vừa sức

| STT | Dự án / repository gốc | Lĩnh vực theo tài liệu | Ý tưởng MVP Python 01–08 | Mức tham khảo |
|---:|---|---|---|---|
| 01 | [FastAPI](https://github.com/fastapi/fastapi) | Web/API | Sổ quản lý công việc dạng CLI với thêm/xem/tìm/lọc | Mở rộng |
| 02 | [Streamlit](https://github.com/streamlit/streamlit) | Data app | Báo cáo điểm học tập từ danh sách dict | Dễ bắt đầu |
| 03 | [Gradio](https://github.com/gradio-app/gradio) | AI demo UI | Bộ phân loại câu ngắn bằng quy tắc từ khóa, chạy CLI | Dễ bắt đầu |
| 04 | [Apache Airflow](https://github.com/apache/airflow) | Data pipeline | Chuỗi ba hàm nạp → lọc → tổng hợp dữ liệu mẫu | Mở rộng |
| 05 | [Prefect](https://github.com/PrefectHQ/prefect) | Data pipeline | Quy trình kiểm tra đặt hàng bằng các hàm tuần tự | Mở rộng |
| 06 | [DVC](https://github.com/iterative/dvc) | MLOps/Data versioning | So sánh hai bộ dữ liệu mẫu và ghi thủ công thay đổi | Mở rộng |
| 07 | [JupyterLab](https://github.com/jupyterlab/jupyterlab) | Notebook/IDE | Notebook hoặc script khảo sát thống kê điểm số | Dễ bắt đầu |
| 08 | [Polars](https://github.com/pola-rs/polars) | DataFrame | Thống kê bán hàng theo loại với list/dict | Dễ bắt đầu |
| 09 | [PyTorch](https://github.com/pytorch/pytorch) | Deep Learning | Hệ thống dự đoán điểm bằng quy tắc tuyến tính đơn giản | Định hướng |
| 10 | [Transformers (Hugging Face)](https://github.com/huggingface/transformers) | Model zoo | Gắn nhãn văn bản bằng từ khóa và kiểm tra kết quả | Định hướng |
| 11 | [LangGraph](https://github.com/langchain-ai/langgraph) | Multi-agent/workflow | Sơ đồ quyết định tư vấn học tập bằng if/elif/hàm | Định hướng |
| 12 | [CrewAI](https://github.com/crewAIInc/crewAI) | Multi-agent/team | Quy trình nhóm ba vai trò bằng ba hàm Python | Định hướng |
| 13 | [ONNX Runtime](https://github.com/microsoft/onnxruntime) | Edge/Inference | Phân loại dữ liệu cảm biến bằng ngưỡng cố định | Định hướng |
| 14 | [OpenVINO](https://github.com/openvinotoolkit/openvino) | Edge optimization | Bộ lọc kết quả mô phỏng phát hiện đối tượng | Định hướng |
| 15 | [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local LLM | Trợ lý FAQ dựa trên từ điển câu hỏi–câu trả lời | Định hướng |
| 16 | [TensorFlow Lite Micro (tflite-micro)](https://github.com/tensorflow/tflite-micro) | TinyML | Hệ thống cảnh báo cảm biến giả lập bằng quy tắc | Định hướng |
| 17 | [ROS 2](https://github.com/ros2/ros2) | Robotics platform | Robot đi trong lưới 1 chiều/2 chiều trên terminal | Mở rộng |
| 18 | [PyBullet (Bullet3)](https://github.com/bulletphysics/bullet3) | Robot simulation | Mô phỏng vị trí chuyển động theo thời gian bằng phép tính | Mở rộng |
| 19 | [Pygame](https://github.com/pygame/pygame) | Game 2D | Trò chơi đoán số hoặc di chuyển nhân vật dạng terminal | Dễ bắt đầu |
| 20 | [Panda3D](https://github.com/panda3d/panda3d) | Game 3D | Mô hình bản đồ ô vuông bằng ký tự với nhân vật | Mở rộng |

## Cách chọn đề tài

1. Ưu tiên đề tài mà nhóm **giải thích được từng hàm**, không chọn vì công cụ đang “hot”.
2. Dùng dữ liệu mẫu hợp lệ, mô tả nguồn; không lấy API key, dữ liệu cá nhân hoặc tài nguyên trả phí.
3. Viết trước một câu mục tiêu, một ví dụ input/output và 2 phép thử (thường + biên).
4. Bản mở rộng dùng framework gốc là **tùy chọn** sau khi MVP CLI đúng; các mục Deep Learning, Multi-agent, Edge, ROS 2, 3D không phải năng lực bắt buộc của giữa kỳ.
5. Nếu tự chọn đề tài khác trong danh sách, dùng cùng [phiếu đề xuất](phieu-de-xuat-nhom.md) và [rubric](rubric-10-diem.md).

## Gợi ý cụ thể cho từng dự án

### 01 · FastAPI

- **MVP tại Tuần 09:** Sổ quản lý công việc dạng CLI với thêm/xem/tìm/lọc. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** Danh sách công việc mẫu và từ khóa.
- **Output cần chứng minh:** Danh sách kết quả và số việc hoàn thành.
- **Ít nhất một kiểm tra biên/sai:** Danh sách rỗng; lọc không thấy việc.
- **Hướng mở rộng không bắt buộc:** Sau Tuần 13: chuyển CLI sang API GET/POST.

### 02 · Streamlit

- **MVP tại Tuần 09:** Báo cáo điểm học tập từ danh sách dict. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** Ba học sinh với các điểm số.
- **Output cần chứng minh:** Bảng tổng kết, điểm trung bình, số đạt.
- **Ít nhất một kiểm tra biên/sai:** Danh sách lớp rỗng; học sinh không có điểm.
- **Hướng mở rộng không bắt buộc:** Làm dashboard Streamlit sau khi nắm dependencies.

### 03 · Gradio

- **MVP tại Tuần 09:** Bộ phân loại câu ngắn bằng quy tắc từ khóa, chạy CLI. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** Một câu tiếng Việt đơn giản.
- **Output cần chứng minh:** Nhãn chủ đề và lý do lựa chọn.
- **Ít nhất một kiểm tra biên/sai:** Chuỗi rỗng; câu không có từ khóa.
- **Hướng mở rộng không bắt buộc:** Gắn giao diện Gradio; mô hình AI là tùy chọn.

### 04 · Apache Airflow

- **MVP tại Tuần 09:** Chuỗi ba hàm nạp → lọc → tổng hợp dữ liệu mẫu. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** List bản ghi doanh thu.
- **Output cần chứng minh:** Tổng doanh thu hợp lệ và số bản ghi bị loại.
- **Ít nhất một kiểm tra biên/sai:** Nguồn rỗng; giá trị âm; bước sai dữ liệu.
- **Hướng mở rộng không bắt buộc:** Sau giữa kỳ: tìm hiểu DAG, scheduler và retry.

### 05 · Prefect

- **MVP tại Tuần 09:** Quy trình kiểm tra đặt hàng bằng các hàm tuần tự. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** Các đơn hàng dạng dict.
- **Output cần chứng minh:** Danh sách đơn hợp lệ và báo cáo lỗi.
- **Ít nhất một kiểm tra biên/sai:** Đơn trống; thiếu trường; số lượng 0.
- **Hướng mở rộng không bắt buộc:** Nghiên cứu workflow/task có trạng thái, retry.

### 06 · DVC

- **MVP tại Tuần 09:** So sánh hai bộ dữ liệu mẫu và ghi thủ công thay đổi. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** Hai list/dict phiên bản A và B.
- **Output cần chứng minh:** Các bản ghi được thêm, bớt, cập nhật.
- **Ít nhất một kiểm tra biên/sai:** Hai phiên bản bằng nhau; danh sách rỗng.
- **Hướng mở rộng không bắt buộc:** Học quản lý phiên bản dữ liệu bằng DVC.

### 07 · JupyterLab

- **MVP tại Tuần 09:** Notebook hoặc script khảo sát thống kê điểm số. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** List số hoặc điểm của nhóm.
- **Output cần chứng minh:** Min/max, trung bình, bảng tần suất.
- **Ít nhất một kiểm tra biên/sai:** Không có dữ liệu; chỉ một giá trị.
- **Hướng mở rộng không bắt buộc:** Dùng notebook JupyterLab để trình bày kết quả.

### 08 · Polars

- **MVP tại Tuần 09:** Thống kê bán hàng theo loại với list/dict. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** Các hóa đơn mẫu: loại, số lượng, giá.
- **Output cần chứng minh:** Doanh thu và mặt hàng bán chạy theo loại.
- **Ít nhất một kiểm tra biên/sai:** Không có giao dịch; số lượng bằng 0.
- **Hướng mở rộng không bắt buộc:** Chuyển dữ liệu sang Polars để so sánh.

### 09 · PyTorch

- **MVP tại Tuần 09:** Hệ thống dự đoán điểm bằng quy tắc tuyến tính đơn giản. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** Giờ học và số bài làm.
- **Output cần chứng minh:** Điểm dự đoán và sai số so với dữ liệu mẫu.
- **Ít nhất một kiểm tra biên/sai:** Giờ học 0; đầu vào âm; ngưỡng điểm.
- **Hướng mở rộng không bắt buộc:** Mới tìm hiểu tensor/model; không bắt buộc huấn luyện.

### 10 · Transformers (Hugging Face)

- **MVP tại Tuần 09:** Gắn nhãn văn bản bằng từ khóa và kiểm tra kết quả. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** Danh sách câu ngắn mẫu.
- **Output cần chứng minh:** Nhãn cho từng câu và đếm số nhãn.
- **Ít nhất một kiểm tra biên/sai:** Không có nhãn phù hợp; câu rỗng.
- **Hướng mở rộng không bắt buộc:** Sau giữa kỳ thử inference có sẵn và kiểm tra giấy phép.

### 11 · LangGraph

- **MVP tại Tuần 09:** Sơ đồ quyết định tư vấn học tập bằng if/elif/hàm. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** Điểm hiện tại và mục tiêu học.
- **Output cần chứng minh:** Đề xuất một bước tiếp theo có giải thích.
- **Ít nhất một kiểm tra biên/sai:** Không nhập điểm; điểm biên 0/10.
- **Hướng mở rộng không bắt buộc:** Mở rộng thành state graph khi đã học framework.

### 12 · CrewAI

- **MVP tại Tuần 09:** Quy trình nhóm ba vai trò bằng ba hàm Python. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** Mô tả một yêu cầu đơn giản.
- **Output cần chứng minh:** Kế hoạch, bản kiểm tra và báo cáo cuối.
- **Ít nhất một kiểm tra biên/sai:** Đầu vào thiếu; thiếu một bước kiểm tra.
- **Hướng mở rộng không bắt buộc:** Sau giữa kỳ tìm hiểu agent phối hợp vai trò.

### 13 · ONNX Runtime

- **MVP tại Tuần 09:** Phân loại dữ liệu cảm biến bằng ngưỡng cố định. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** Danh sách số đo nhiệt độ.
- **Output cần chứng minh:** Nhãn bình thường/cảnh báo và thống kê.
- **Ít nhất một kiểm tra biên/sai:** Giá trị đúng ngưỡng; danh sách rỗng.
- **Hướng mở rộng không bắt buộc:** Thử chạy mô hình ONNX có sẵn khi có điều kiện.

### 14 · OpenVINO

- **MVP tại Tuần 09:** Bộ lọc kết quả mô phỏng phát hiện đối tượng. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** Danh sách nhãn và độ tin cậy giả lập.
- **Output cần chứng minh:** Chỉ giữ nhãn vượt ngưỡng đã định.
- **Ít nhất một kiểm tra biên/sai:** Đúng bằng ngưỡng; độ tin cậy ngoài 0–1.
- **Hướng mở rộng không bắt buộc:** Nghiên cứu tối ưu inference trên thiết bị tương thích.

### 15 · llama.cpp

- **MVP tại Tuần 09:** Trợ lý FAQ dựa trên từ điển câu hỏi–câu trả lời. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** Câu hỏi mẫu không chứa dữ liệu cá nhân.
- **Output cần chứng minh:** Câu trả lời có nguồn từ bảng FAQ hoặc 'chưa biết'.
- **Ít nhất một kiểm tra biên/sai:** Câu hỏi chưa có; chuỗi trống.
- **Hướng mở rộng không bắt buộc:** Tìm hiểu mô hình cục bộ, nguồn tải và yêu cầu thiết bị.

### 16 · TensorFlow Lite Micro (tflite-micro)

- **MVP tại Tuần 09:** Hệ thống cảnh báo cảm biến giả lập bằng quy tắc. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** Chuỗi giá trị ánh sáng/nhiệt độ giả lập.
- **Output cần chứng minh:** Thông báo vượt ngưỡng, tổng số lần cảnh báo.
- **Ít nhất một kiểm tra biên/sai:** Dữ liệu rỗng; giá trị ở ngưỡng.
- **Hướng mở rộng không bắt buộc:** Tìm hiểu MCU/TinyML, không bắt buộc mua thiết bị.

### 17 · ROS 2

- **MVP tại Tuần 09:** Robot đi trong lưới 1 chiều/2 chiều trên terminal. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** Vị trí xuất phát, đích và giới hạn.
- **Output cần chứng minh:** Dãy bước hợp lệ hoặc 'không có đường đi'.
- **Ít nhất một kiểm tra biên/sai:** Đã ở đích; đích ngoài lưới.
- **Hướng mở rộng không bắt buộc:** Tìm hiểu ROS 2 node/topic sau khi học modules.

### 18 · PyBullet (Bullet3)

- **MVP tại Tuần 09:** Mô phỏng vị trí chuyển động theo thời gian bằng phép tính. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** Vị trí, vận tốc, số bước đơn giản.
- **Output cần chứng minh:** Bảng trạng thái sau từng bước.
- **Ít nhất một kiểm tra biên/sai:** Vận tốc 0; số bước 0; số bước âm.
- **Hướng mở rộng không bắt buộc:** Thử môi trường mô phỏng PyBullet.

### 19 · Pygame

- **MVP tại Tuần 09:** Trò chơi đoán số hoặc di chuyển nhân vật dạng terminal. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** Lệnh di chuyển hoặc lựa chọn của người chơi.
- **Output cần chứng minh:** Trạng thái lượt chơi, thắng/thua.
- **Ít nhất một kiểm tra biên/sai:** Lệnh sai; trúng đích; hết lượt.
- **Hướng mở rộng không bắt buộc:** Vẽ sprite/cửa sổ Pygame là tự chọn.

### 20 · Panda3D

- **MVP tại Tuần 09:** Mô hình bản đồ ô vuông bằng ký tự với nhân vật. Không phụ thuộc việc cài framework gốc.
- **Input mẫu:** Tọa độ nhân vật và lệnh di chuyển.
- **Output cần chứng minh:** Bản đồ hiển thị và vị trí hiện tại.
- **Ít nhất một kiểm tra biên/sai:** Đi ra ngoài bản đồ; va chạm vật cản.
- **Hướng mở rộng không bắt buộc:** Chuyển demo sang không gian 3D với Panda3D.

## Bản quyền, nguồn và giới hạn

- Các liên kết dẫn tới **repository bên thứ ba để đọc/tham khảo**; không có cam kết chúng đang hoạt động, hỗ trợ một phiên bản Python nhất định, hay được phép sao chép không điều kiện.
- Kiểm tra giấy phép, README, phiên bản và điều kiện cài đặt **trước khi** dùng mã/tài nguyên của dự án gốc; không cần cài đặt để hoàn thành MVP.
- Nội dung giả lập/dữ liệu mẫu phải được giới thiệu rõ là giả lập; không quảng bá chatbot quy tắc là LLM hay bot mô phỏng là robot thật.
- Danh mục này nhằm **gợi ý vấn đề**; bài nộp cần là sản phẩm Python của sinh viên, có dấu vết Git và chứng cứ chạy lại.
