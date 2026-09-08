# Hints — Week 09

Midterm không có official solution: bạn tự chọn track và tự chứng minh behavior.
Hints dưới đây gợi hướng suy nghĩ, không đưa lời giải.

## Chọn track

- Chọn track bạn giải thích được, không phải track trông "khó hơn".
- Cả hai track dùng chung tiêu chí evidence, nên không có track nào dễ điểm hơn.

## Planning

- Viết trước một câu: "Chương trình này nhận gì, làm gì, in ra gì?"
- Liệt kê 3–5 chức năng rồi cắt xuống phần bạn chắc chắn hoàn thành.

## Decomposition

- Tách input/print khỏi phần tính toán để test được logic.
- Một hàm nên trả về giá trị thay vì vừa tính vừa in.
- Nếu phải truyền quá nhiều tham số rời rạc, hãy gom thành dict có khóa rõ nghĩa.

## Track A — VuaCóc Bot V1

- `choose_action(state)` chỉ được trả về action hợp lệ trong course-local model.
- Heuristic cần giải thích được bằng lời: "khi X thì ưu tiên Y vì Z".
- Chạy đủ ba baseline; thua vẫn đạt nếu bạn đọc được điểm yếu và ghi lại.

## Track B — Student Manager

- Mô hình học sinh bằng nested data trước, rồi mới viết hàm xử lý.
- Điểm trung bình cần xác định rõ cách xử lý danh sách điểm rỗng.
- Report terminal nên tách phần format khỏi phần tính toán.

## Testing và evidence

- Chạy ít nhất một normal case và một boundary case cho mỗi chức năng chính.
- Boundary thường là: rỗng, một phần tử, giá trị lớn nhất, giá trị không hợp lệ.
- Ghi lại một bug đã sửa: triệu chứng → input tối thiểu → nguyên nhân → cách sửa.

## Trước khi nộp

- Điền [`evidence-template.md`](evidence-template.md).
- Chạy machine check trong [`checks/`](checks/) nếu bạn theo Track A.
- Commit sạch, message mô tả kết quả, không commit file tạm.
