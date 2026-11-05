# Gợi ý theo ba mức — chỉ xem khi gặp khó

**Mức 1: tự nghĩ cách giải. Mức 2: xem cấu trúc dữ liệu.
Mức 3: xem cú pháp.** Chỉ mở `solutions_de1/` sau khi
đã tự thử và ghi một lỗi đã sửa.

| Ý | Mức 1 — Ý tưởng | Mức 2 — Cấu trúc | Mức 3 — Gợi ý cú pháp |
|---|---|---|---|
| 1a | Chia 2 dư mấy? | số nguyên thật | `n % 2 == 0`, `type(n) is int` |
| 1b | Chuẩn hóa trước | tên, tuổi hợp lệ | `.strip()`, f-string |
| 2a | Duyệt trọn đoạn | cộng số thỏa điều kiện | `range(start,end+1)` |
| 2b | 1-based khác 0-based | slice, đếm ký tự | `text[start-1:end]`, `"0"<=ch<="9"` |
| 3a | Lọc list không sửa nguồn | tạo `result=[]` | `isinstance(item,str)` |
| 3b | Ghi ba snapshot | list copy từng bước | `.copy()`, `append/remove/reverse` |
| 4a | Đầu, thứ 3, cuối | tuple >=3 | `items[0],items[2],items[-1]` |
| 4b | Cộng và lặp tuple | tuple của hai tuple | `first+second`, `first*3` |
| 5a | Mỗi ký tự tăng tần suất | dict key=ký tự | `counts.get(ch,0)+1` |
| 5b | Chọn tên theo điểm | duyệt `.items()` | `if score >= minimum` |

**Nếu checker báo FAIL:** kiểm tên hàm/signature, kiểu trả về
(không dùng `print` thay `return`), input biên, dữ liệu sai
phải raise `ValueError`, và việc list/dict của caller
có bị thay đổi không.

**Không sửa checker/test để tạo PASS giả.**
