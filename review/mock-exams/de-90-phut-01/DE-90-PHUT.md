# ĐỀ ÔN TẬP SỐ 01 — LẬP TRÌNH PYTHON (90 PHÚT)

**Thời gian:** 90 phút. **Thang điểm:** 10 điểm;
**5 câu × 2 điểm**, mỗi câu gồm **hai ý × 1 điểm**.
Đây là đề ôn tập thực hành, **không phải đề thi chính thức**.

**Quy định:** Python >=3.12, dùng thư viện chuẩn. Mỗi ý
được thực hiện trong đúng file `submissions_de1/Cau*.py`.
Giữ nguyên chữ ký hàm/lớp, xử lý dữ liệu đầu vào sai như yêu
cầu, **return** kết quả (không chỉ print). Không cần nhập
`input()` trong các hàm: bộ tự kiểm sẽ truyền tham số trực tiếp.

## Câu 1 — Số nguyên và vòng lặp (2 điểm)

**1a.** `count_divisible_by_three_digits(n: int) -> int`:
với `n` nguyên thật trong **1..1500**, đếm số chữ số
trong dạng thập phân thuộc **0, 3, 6, 9**.
Chữ số `0` cũng chia hết cho 3. Input không hợp lệ
(nằm ngoài khoảng, bool, chuỗi, float) → `ValueError`.

Ví dụ: `909` → 3; `1500` → 2.

**1b.** `harmonic_sum(n: int) -> float`: với
`1 <= n <= 1500`, tính tổng
`1 + 1/2 + 1/3 + ... + 1/n`, trả **float**.
Input sai → `ValueError`.

Ví dụ: `harmonic_sum(2)` → `1.5`.
Độ chính xác được so sánh bằng tolerance, không yêu cầu
so sánh chuỗi biểu diễn float.

## Câu 2 — Xử lý chuỗi (2 điểm)

**2a.** `count_uppercase(text: str) -> int`:
đếm chữ cái viết hoa theo phương thức Python
`str.isupper()` (gồm ký tự Unicode phù hợp).
Chuỗi rỗng → 0, input không phải str → `ValueError`.

Ví dụ: `"AbC"` → 2.

**2b.** `is_palindrome(text: str) -> bool`: kiểm
chuỗi đối xứng **sau khi loại dấu câu/khoảng trắng và
không phân biệt hoa/thường**: chỉ giữ ký tự có
`isalnum()`, chuyển `casefold()`.
Nếu chuỗi sau chuẩn hóa rỗng, trả `False`.
Input sai kiểu → `ValueError`.

Ví dụ: `"A man, a plan, a canal: Panama!"` → `True`.

## Câu 3 — List, sentinel và vòng lặp (2 điểm)

**3a.** `count_even_before_zero(values: list[int]) -> int`:
đếm số chẵn trong dãy số nguyên **dương** trước số
`0` đầu tiên. `0` là **dấu hiệu dừng**, không được
tính là số chẵn. Phải có 0; các phần tử trước 0 chỉ
được phép là int thật, không âm.
Sau 0 được bỏ qua. Sai → `ValueError`.

Ví dụ: `[2,3,4,0,6]` → 2.

**3b.** `count_value_before_zero(values: list[int],
target: int) -> int`: số lần `target` (**số nguyên
dương**) xuất hiện trước 0 đầu tiên. Cùng quy tắc
dừng và validation như 3a. Sai → `ValueError`.

Ví dụ: `[2,2,3,0,2]`, `target=2` → 2.

## Câu 4 — Dictionary quản lý sách (2 điểm)

**4a.** `make_book(book_id, title, author, year, price)
-> dict[str, object]`: tạo dict đúng năm key
`id,title,author,year,price`.
Ba chuỗi phải khác rỗng sau `strip()`, năm xuất bản
nguyên thật **1900..2100**, giá nguyên thật **>=0** (VND).
Sai → `ValueError`.

**4b.** `remove_book(books: list[dict[str,object]],
book_id: str) -> list[dict[str,object]]`: xóa đúng
cuốn sách có mã trùng `book_id`, trả **danh sách
mới gồm những dict bản sao**, không thay đổi dữ liệu
do caller truyền vào. Mỗi sách phải là dict, mã
`id` là chuỗi không rỗng và không trùng nhau.
Không tìm thấy / đầu vào sai → `ValueError`.
Giữ nguyên thứ tự sách còn lại.

## Câu 5 — Lập trình hướng đối tượng (2 điểm)

**5a.** Trong `Cau5a.py`, định nghĩa
`class DienThoai` với các thuộc tính:
`MaMay`, `TenMay`, `HangSanXuat`,
`DungLuongPin`, `GiaBan`.

- `__init__(self, MaMay, TenMay, HangSanXuat,
  DungLuongPin, GiaBan)` kiểm chuỗi không rỗng;
  pin int thật >0, giá int thật >=0; sai → `ValueError`.
  Chuỗi được `strip()`.
- `thongtindienthoai(self) -> str` **trả chuỗi**
  theo định dạng:
  `MaMay | TenMay | HangSanXuat | DungLuongPin mAh | GiaBan VND`.

Ví dụ: `DienThoai("DT01","Thiết bị A","Hãng A",
4500,12000000).thongtindienthoai()` trả
`"DT01 | Thiết bị A | Hãng A | 4500 mAh | 12000000 VND"`.

**5b.** Trong `Cau5b.py`, dùng
`from Cau5a import DienThoai`; viết
`tao_danh_sach_dien_thoai() -> list[DienThoai]`
trả đúng hai **đối tượng thật** của class này:

- `DT01`, `Thiết bị A`, `Hãng A`, 4500, 12000000.
- `DT02`, `Thiết bị B`, `Hãng B`, 5000, 15000000.

Không định nghĩa lại `DienThoai` ở `Cau5b.py`.
Đây là bài học OOP cơ bản, không phải chương trình
quản lý điện thoại sản xuất.

## Tự kiểm

```bash
python review/mock-exams/de-90-phut-01/autograde_de1.py --student
```

Bộ kiểm có **78 ca công khai**; mỗi ý tối đa 1 điểm,
tổng 10 điểm. Bài tự luyện cho phép xem gợi ý và kiểm lại
sau khi thử; điểm không thay thế đánh giá của giảng viên.
