# Học Python với AI mà vẫn hiểu được chương trình

> Tài liệu bổ trợ cho Python Journey (15 tuần). AI là người gợi ý và phản biện, không thay thế việc tự lập trình.

## 1. Quy trình 5 bước cho mỗi bài tập

1. **Tự phân tích:** viết đầu vào, đầu ra, 1 ví dụ đúng và 1 trường hợp biên.
2. **Tự thử:** viết cách giải đơn giản trước; ghi lại lỗi đang gặp.
3. **Hỏi AI theo mức cần thiết:** xin giải thích khái niệm, gợi ý từng bước hoặc nhờ đọc traceback; chưa xin đáp án hoàn chỉnh.
4. **Kiểm chứng độc lập:** tự chạy chương trình, thử đầu vào mới, đọc kết quả và sửa lỗi.
5. **Giải thích bằng lời của mình:** trình bày lựa chọn cấu trúc dữ liệu, điều kiện biên và vì sao code đúng.

## 2. Ba mức hỗ trợ của AI

- **Mức 1 — Giải thích:** hỏi “Vì sao `input()` trả về chuỗi?”.
- **Mức 2 — Gợi ý:** hỏi “Hãy cho tôi hai gợi ý, không viết lời giải, về cách kiểm tra số nguyên dương”.
- **Mức 3 — Phản biện:** đưa code tự viết và hỏi “Chỉ ra trường hợp phản ví dụ; đừng sửa toàn bộ code”.

Chỉ xem một lời giải tham khảo sau khi đã tự thử và ghi được điểm vướng mắc. Không sao chép mã nguồn rồi xem đó là bằng chứng đã hiểu.

## 3. Prompt mẫu để sinh viên sử dụng

> Tôi đang học Python tuần [số tuần]. Bài toán là [mô tả]. Tôi đã thử [cách làm] nhưng gặp [lỗi hoặc kết quả]. Hãy giải thích bằng tiếng Việt, chỉ gợi ý từng bước, hỏi một câu giúp tôi tự suy nghĩ và đề xuất ba trường hợp kiểm thử. Chưa đưa mã hoàn chỉnh trừ khi tôi yêu cầu.

## 4. Khi AI có thể sai

- Kết quả tự tin chưa chắc đúng. Hãy thử **normal / boundary / invalid input**.
- Không sửa `assert` thành một kết quả sai chỉ để test chuyển màu xanh.
- Không tự cho rằng `type hints` sẽ tự kiểm tra kiểu dữ liệu khi chương trình chạy.
- Không gửi mật khẩu, token, thông tin cá nhân của sinh viên hoặc dữ liệu bí mật vào công cụ AI.
- Tự đọc và giải thích mọi thư viện hoặc đoạn code mà bạn quyết định dùng.

## 5. Nộp minh bạch

Nếu đã dùng AI, điền `AI_USAGE.md` từ [biểu mẫu](../templates/AI_USAGE.template.md):

- Tôi đã hỏi AI điều gì?
- Tôi đã tự viết, sửa và kiểm thử phần nào?
- Có đề xuất nào của AI sai hoặc chưa phù hợp?
- Tôi học thêm được điều gì mà tôi có thể giải thích không cần AI?

**Giảng viên đánh giá hành vi chạy được và khả năng giải thích, không dùng văn phong comment hoặc nghi ngờ “giống AI” làm bằng chứng kết luận gian lận.**

## 6. Hai loại kiểm chứng khác nhau

- `checks/check_solutions.py` thường kiểm thử **lời giải mẫu trong `solutions/`**: PASS chứng minh tài liệu mẫu chạy, **không chứng minh bài của bạn đúng**.
- Test do sinh viên viết hoặc chạy trực tiếp trên file của sinh viên mới tạo bằng chứng cho bài nộp.

Khi nộp, ghi rõ lệnh đã chạy, đầu ra thực tế và một trường hợp kiểm tra lỗi.
