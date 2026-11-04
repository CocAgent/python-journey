# Kế hoạch ôn tập 4 buổi (tự chọn)

Tùy thời gian học viên; đây là **gợi ý ôn tập**, không phải lịch
bắt buộc hay một thay đổi của syllabus.

| Buổi | Ôn nội dung | Làm được gì? |
|---|---|---|
| 1 | Week 01–04 — môi trường, biến/kiểu, điều kiện, chuỗi | Dự đoán output, giải thích `str/int`, validate input |
| 2 | Week 05–08 — list/tuple, loop, function, dict/set | Hoàn thành Lab 01 Gradebook, giải thích không mutate dữ liệu nguồn |
| 3 | Week 09–10 — Midterm, file/pathlib/CSV/JSON | Hoàn thành Lab 02 JSON Report, phân biệt parse và validate |
| 4 | Week 11 — Exceptions, traceback, debugging | Hoàn thành Lab 03, viết regression cho bug logic |

## Buổi 1 — Kiến thức nền

Đọc [Week 01](../weeks/week-01-hello-python/README.md),
[Week 02](../weeks/week-02-variables-types/WORKED-EXAMPLES.md),
[Week 03](../weeks/week-03-conditionals/WORKED-EXAMPLES.md) và
[Week 04](../weeks/week-04-strings/WORKED-EXAMPLES.md).

Tự giải câu 1–5 trong [QUICK-CHECK.md](QUICK-CHECK.md).
Thử thay dữ liệu và giải thích vì sao `bool("False")` là
`True`, và tại sao ngưỡng điều kiện có thứ tự.

## Buổi 2 — Cấu trúc dữ liệu và hàm

Ôn [Week 05](../weeks/week-05-lists-tuples/WORKED-EXAMPLES.md),
[Week 06](../weeks/week-06-loops/WORKED-EXAMPLES.md),
[Week 07](../weeks/week-07-functions/WORKED-EXAMPLES.md) và
[Week 08](../weeks/week-08-dicts-sets/WORKED-EXAMPLES.md).

Giải câu 6–12, sau đó làm `Lab 01`. Trước khi viết,
vẽ dữ liệu `list[dict]` và nêu rõ input sai/empty.
`return` kết quả thay vì chỉ in một dòng mẫu.

## Buổi 3 — Midterm và lưu dữ liệu

Xem [Week 09 Midterm](../weeks/week-09-midterm-project/README.md),
[Week 10](../weeks/week-10-files-io/WORKED-EXAMPLES.md).
Ôn câu 13–14 và làm `Lab 02`.
So sánh một file thiếu, một JSON sai cú pháp, và một
JSON hợp cú pháp nhưng sai schema. Không viết vào dữ liệu thật.

## Buổi 4 — Debugging và kiểm chứng

Đọc [Week 11](../weeks/week-11-exceptions/WORKED-EXAMPLES.md).
Giải câu 15–16, làm `Lab 03`, ghi lại **bug logic**
với input `(4, 1)`, rồi thử regression với `(1, 4)`.
Ghi evidence vào [mẫu](EVIDENCE-TEMPLATE.md).

## Sau khi ôn

- [ ] Tôi dự đoán được kết quả của ít nhất một ca biên trước khi chạy.
- [ ] Tôi biết phân biệt `print` và `return`.
- [ ] Tôi phân biệt được data missing/empty/invalid.
- [ ] Tôi hoàn thành ba lab bằng code của chính mình.
- [ ] Tôi có thể giải thích ít nhất một lỗi và kiểm lại sau khi sửa.

Tiếp tục [Week 12 — Testing with pytest](../weeks/week-12-testing-pytest/)
để biến các ca kiểm thủ công thành test case có cấu trúc.
