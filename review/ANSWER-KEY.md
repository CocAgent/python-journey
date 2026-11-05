# Đáp án giải thích — chỉ mở sau khi tự trả lời

Đây là gợi ý kiểm tra, không phải thang điểm hay rubric.

| Câu | Đáp án | Vì sao |
|---|---|---|
| 1 | `123` và `15` | Chuỗi nối chuỗi; số cộng số |
| 2 | `True` | Chuỗi `"False"` có ký tự nên truthy |
| 3 | Nhánh `>=5` | `if/elif` chọn nhánh đúng đầu tiên |
| 4 | `nohtyP` | Slicing bước `-1` đảo thứ tự |
| 5 | `2`, không phải đếm từ | `str.count` đếm chuỗi con trong `pythonic` |
| 6 | `["An","Chi"]` | `b=a` là alias chung một list |
| 7 | `tuple` và `str` | Dấu phẩy tạo tuple một phần tử |
| 8 | `[1,2,3]` | Cận phải của `range` không được lấy |
| 9 | `break` dừng loop; `continue` bỏ lượt | Hai thao tác điều khiển khác nhau |
| 10 | `None` | `print` không thay `return` |
| 11 | `beginner` | `get` cho default khi key vắng |
| 12 | Không | Set không bảo đảm thứ tự list ban đầu |
| 13 | `str` | CSV lưu ô dữ liệu dạng text; cần parse `int` |
| 14 | Không | JSON hợp cú pháp không đủ chứng minh schema |
| 15 | Không | Bắt đúng exception type; không che bug khác |
| 16 | Có; tránh `return` trong `finally` | `finally` chạy lúc thoát cấu trúc, có thể che return/exception trước |

Nếu trả sai: đọc lại [kế hoạch và liên kết tuần](STUDY-PLAN.md),
tìm đúng ví dụ tương ứng, dự đoán lại trước khi chạy và
ghi câu hỏi vào [evidence](EVIDENCE-TEMPLATE.md).
