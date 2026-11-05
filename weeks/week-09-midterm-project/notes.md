# Week 09 — Từ nền tảng đến project có evidence

Week 09 không thêm một nhóm cú pháp mới. Trọng tâm là ghép các kỹ năng đã học
thành một vòng phát triển có thể quan sát và giải thích.

## 1. Plan

Viết project goal trong một câu. Sau đó liệt kê input, output và ba behavior
quan trọng nhất. Nếu danh sách quá dài, giảm scope trước khi code.

```text
goal → inputs → outputs → core behaviors → evidence
```

## 2. Decompose

Chia behavior thành function nhỏ. Data thuộc caller được truyền bằng parameter;
function trả kết quả thay vì phụ thuộc vào nhiều biến global.

Ví dụ Bot V1:

```text
structured state → choose_action(state) → course-local action
```

Ví dụ Student Manager:

```text
student data → calculate_average(student) → average
```

## 3. Implement

Hoàn thiện happy path nhỏ nhất trước. Dùng tên function và key thể hiện đúng ý
nghĩa của model. Không thêm feature chỉ vì có thể thêm.

## 4. Run và inspect

Chạy từng behavior với data nhỏ. So sánh actual output với expected output đã
viết trước. Đừng chỉ nhìn chương trình “không crash”.

## 5. Debug

Khi có lỗi:

1. ghi lại input và output sai;
2. xác định function đầu tiên tạo giá trị sai;
3. thay đổi một nguyên nhân;
4. chạy lại case lỗi và một case đã từng đúng;
5. ghi ngắn gọn bug và cách sửa.

## 6. Evaluate

Evidence trả lời câu hỏi cụ thể:

- project có chạy không;
- output có thuộc contract của track không;
- behavior có lặp lại được không;
- boundary case có kết quả rõ không;
- known weakness hiện tại là gì.

Bot track chạy riêng với WaitBot, ForwardBot và CautiousBot. Kết quả từng match
được ghi riêng; không chuyển chúng thành rating hoặc tỷ lệ thắng bắt buộc.

## 7. Explain

Bạn cần giải thích data model, rules, một tradeoff và bước cải thiện tiếp theo.
Một project nhỏ được hiểu rõ có giá trị hơn project lớn không giải thích được.

## 8. Commit và prove

Commit sau khi một behavior hoặc evidence hoàn tất. Điền SHA cuối vào evidence
template để người khác có thể đối chiếu đúng phiên bản đã chạy.

```text
COURSE TEACHING MODEL
NOT VUACOC PRODUCTION CONTRACT
```

Local Arena và Bot V1 chỉ dùng teaching contract của Python Journey. Không suy
ra production state, action, protocol, rating hoặc compatibility từ project này.
