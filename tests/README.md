# Hướng dẫn kiểm thử mã nguồn Python Journey

Thư mục `tests/` chứa **các bài kiểm thử tự động do nhóm bảo trì quản lý**. Mục đích là phát hiện lỗi hồi quy, kiểm tra tính nhất quán của mã nguồn và học liệu, đồng thời cung cấp bằng chứng chất lượng có thể chạy lại trước khi hợp nhất thay đổi.

Đây **không phải** nơi nộp bài của sinh viên, hệ thống chấm thi chính thức hoặc môi trường bảo mật để thực thi mã không đáng tin cậy.

## 1. Phạm vi và trách nhiệm

| Nhóm kiểm thử | Vị trí thường gặp | Mục đích |
|---|---|---|
| Kiểm thử cấu trúc khóa học | `tests/test_course_structure.py`, `tests/test_week_owned_checks.py` | Kiểm tra thư mục, tài liệu, đường dẫn và quy ước dùng chung |
| Kiểm thử học liệu | `tests/test_week*_guided_practice.py` và các file `tests/test_week*.py` khác | Xác nhận ví dụ chạy được, lời giải tham khảo đúng với các trường hợp đã định nghĩa và liên kết tài liệu tồn tại |
| Kiểm thử thành phần dùng chung | Các file kiểm thử và tiện ích trong `tests/` | Xác nhận hành vi của các công cụ, dữ liệu mẫu và giao diện tích hợp nội bộ |
| Kiểm thử theo tuần | `weeks/<week>/checks/` hoặc thư mục kiểm thử của từng tuần | Kiểm tra những yêu cầu thuộc riêng bài học hoặc tuần đó |
| Bộ tự luyện | `review/`, `weeks/<week>/practice/` | Kiểm trực tiếp mã sinh viên khi người học chủ động chọn chế độ thích hợp |

Một bài kiểm thử ở cấp repository có thể gọi công cụ kiểm tra của từng tuần để phát hiện lỗi tích hợp. Tuy nhiên, **yêu cầu bài tập, dữ liệu kiểm thử và lời giải mẫu nên được quản lý tại nơi sở hữu bài tập**; tránh sao chép cùng một tiêu chuẩn đánh giá sang nhiều thư mục.

## 2. Chạy kiểm thử

Mở terminal tại **thư mục gốc** của repository `python-journey` và sử dụng phiên bản Python được dự án hỗ trợ.

```bash
# Chạy tập kiểm thử mặc định theo cấu hình dự án
python -m pytest

# Chỉ chạy các bài kiểm thử trong thư mục tests
python -m pytest tests -q

# Kiểm tra một nhóm cụ thể khi cần chẩn đoán
python -m pytest tests/test_course_structure.py -q

# Kiểm tra các quy tắc khóa học khi công cụ này có sẵn
python scripts/verify_course.py

# Kiểm tra chất lượng mã theo cấu hình hiện hành
ruff check scripts tests projects/vuacoc-bot-journey
```

Tham khảo `pyproject.toml` và `.github/workflows/` để xác định phiên bản Python, phạm vi kiểm thử và các bước kiểm soát chất lượng đang được áp dụng. **Kết quả PASS trên máy cá nhân cần được phân biệt với trạng thái CI đã xác nhận trên GitHub.**

## 3. Hiểu đúng kết quả PASS và FAIL

- **PASS của lời giải tham khảo:** các trường hợp kiểm thử đã chạy thành công trên **mã mẫu**, không chứng minh sinh viên hoàn thành bài.
- **FAIL có chủ đích của mã khởi đầu:** các file `starter` còn `TODO` hoặc `NotImplementedError` có thể FAIL trước khi sinh viên viết code; đây là trạng thái được thiết kế.
- **PASS của sinh viên:** chỉ có ý nghĩa khi bộ kiểm thực sự chạy trên **mã do sinh viên viết** và đúng chế độ kiểm tra.
- **PASS của CI:** cho biết các yêu cầu tự động hiện có đã đạt; không bảo đảm mã đúng với mọi dữ liệu, không chứng minh quyền tác giả và không thay đánh giá sư phạm hoặc bảo mật.

Kết quả hiển thị cần làm rõ **đã kiểm mã nào** và **bằng chế độ nào**. Không lấy PASS của `--solutions` hoặc `--reference` để thay cho kết quả `--starter` hoặc `--student`.

## 4. Nguyên tắc thiết kế bài kiểm thử

1. **Lặp lại được:** dùng dữ liệu cố định và kết quả mong đợi rõ ràng; hạn chế phụ thuộc vào đồng hồ, mạng, số ngẫu nhiên hoặc thứ tự duyệt của `set`.
2. **Độc lập:** dùng dữ liệu mẫu và thư mục tạm; không ghi đè bài nộp, dữ liệu thật, tài khoản hoặc bí mật.
3. **Kiểm hành vi thực:** ưu tiên giá trị `return`, kiểu dữ liệu, thay đổi trạng thái, ngoại lệ và mã thoát; không chỉ kiểm một chuỗi được `print`.
4. **Bao phủ trường hợp:** có dữ liệu bình thường, biên, rỗng, thiếu, sai kiểu và tình huống hồi quy phù hợp.
5. **Dễ chẩn đoán:** mỗi bài kiểm thử nên thể hiện một yêu cầu cụ thể, có thông báo giúp xác định nguyên nhân.
6. **Thay đổi có kiểm soát:** cập nhật tài liệu, mã nguồn và bài kiểm thử liên quan trong cùng thay đổi; không nới lỏng điều kiện chỉ để làm CI chuyển sang PASS.
7. **Phân định nơi sở hữu:** đặt kiểm thử riêng của từng bài ở gần bài đó; giữ `tests/` cho các quy tắc và kiểm tra tích hợp ở cấp repository.
8. **An toàn:** timeout của subprocess chỉ giúp phát hiện một số chương trình chạy quá lâu, **không tạo môi trường cách ly bảo mật**. Bài nộp từ nguồn không tin cậy phải chạy trong container/VM có giới hạn tài nguyên, quyền truy cập và mạng.

## 5. Quy trình thêm hoặc chỉnh sửa bài kiểm thử

Xác định yêu cầu hoặc lỗi cần khắc phục, tìm thư mục sở hữu, tạo trường hợp tái hiện tối thiểu, bổ sung kiểm tra bình thường và dữ liệu sai nếu cần. Chạy kiểm thử cụ thể, sau đó chạy bộ kiểm phù hợp ở cấp repository. Khi thay đổi cách sử dụng, cập nhật README hoặc hướng dẫn tương ứng. Chỉ hợp nhất sau khi đã xác nhận các bước CI cần thiết.

Các tài liệu phân tích trước đây tại [LEGACY_ASSESSMENT_REVIEW.md](LEGACY_ASSESSMENT_REVIEW.md) là **nguồn tham khảo lịch sử**, không phải quy tắc chấm điểm mặc định.

Các đề tự luyện trong [`review/`](../review/README.md) có thể quy định thời lượng, thang điểm và lệnh tự chấm riêng. **Không áp dụng cố định thời gian 60 phút, 90 phút hoặc thang điểm của một đề cho toàn bộ `tests/`.**

Tài liệu này quy định **trách nhiệm và cách tổ chức kiểm thử**, không phải phê duyệt triển khai, quy chế thi chính thức hoặc cam kết mã nguồn an toàn tuyệt đối.