# Cóc và Dế mở chiếc ba lô Python

Một câu chuyện ngắn, vui vẻ để bắt đầu tuần học thứ hai với Python.

## 1. Dế mang ba lô đến gặp Cóc

Sáng đầu tuần, trời mát, gió thổi nhè nhẹ qua bụi cỏ. Dế ôm một chiếc ba lô nhỏ, chạy lạch bạch đến gặp Cóc.

— Cóc ơi, tuần này mình học gì thế? Em nghe nói Python dễ thương lắm, mà mở vào vẫn thấy hơi run.

Cóc đang ngồi trên phiến đá, cười khì:

— Run là đúng rồi. Chưa học mà không run thì lại lạ. Nhưng đừng lo, tuần này ta chỉ mở đúng **một chiếc ba lô Python** thôi.

Dế tròn mắt:

— Trong ba lô có gì?

Cóc vỗ vỗ chiếc lá sen bên cạnh:

— Có bốn món rất quan trọng. Học xong là chú mày sẽ nói chuyện với Python tự tin hơn nhiều.

Dế ngồi xuống ngay ngắn:

— Em sẵn sàng. Cóc nói đi!

## 2. Biến là gì?

Cóc nhặt một hòn sỏi, giơ lên:

— Giả sử anh nhặt được **7 hòn sỏi**, mà cứ mỗi lần muốn nhắc đến lại phải nói “bảy hòn sỏi cạnh bờ ao” thì dài dòng lắm.

Dế gật gù:

— Chuẩn luôn.

— Thế nên ta đặt cho nó một cái tên. Ví dụ:

```python
so_soi = 7
```

Cóc cười:

— Tên `so_soi` này gọi là **biến**. Biến giống như một chiếc hộp có dán nhãn. Trong hộp đang chứa giá trị `7`.

Dế reo lên:

— À! Vậy biến là cách để mình **đặt tên cho dữ liệu**!

— Chính xác. Mà đặt tên cũng nên cho tử tế. Nhìn vào là hiểu ngay.

Ví dụ tốt:

```python
ten = "Dế"
tuoi = 2
diem_trung_binh = 8.5
```

Ví dụ không tốt:

```python
a = "Dế"
x1 = 2
zzz = 8.5
```

Dế cười ngượng:

— Em mà đặt kiểu `abcxyz` chắc mai em quên luôn em viết gì.

Cóc gật đầu:

— Đó. Nên mục tiêu đầu tiên tuần này là hiểu **biến** là gì và biết **cách đặt tên biến rõ ràng, dễ hiểu**.

## 3. Bốn anh em kiểu dữ liệu

Dế chống cằm:

— Thế trong hộp biến có thể chứa những gì?

Cóc lấy que vẽ xuống đất:

— Có mấy kiểu dữ liệu rất hay gặp. Tuần này chú học 4 anh em nổi tiếng nhất.

### `int`
— Đây là **số nguyên**, không có phần thập phân.

```python
tuoi = 3
so_la = 25
```

### `float`
— Đây là **số thực**, có phần thập phân.

```python
can_nang = 1.5
diem = 9.25
```

### `str`
— Đây là **chuỗi ký tự**, tức là chữ, câu, hay đoạn văn.

```python
ten = "Dế Mèn"
loi_chao = "Xin chào Python"
```

### `bool`
— Đây là kiểu chỉ có hai giá trị: **Đúng** hoặc **Sai**.

```python
da_hoc_bai = True
troi_mua = False
```

Dế vỗ đùi cái đét:

— Hay quá! Vậy tuần này em phải làm quen với `int`, `float`, `str`, `bool`.

Cóc gật đầu:

— Đúng. Phải nhìn dữ liệu là biết nó thuộc kiểu gì. Không thì Python nhìn mình, mình nhìn Python, cả hai cùng bối rối.

## 4. Chuỗi không chỉ để nhìn, còn để “gọt giũa”

Dế hỏi tiếp:

— Em thấy chữ nghĩa thì chỉ để in ra thôi chứ?

Cóc phá lên cười:

— Ôi giời, chuỗi mà chỉ để ngắm thì phí lắm. Chuỗi còn có nhiều phép xử lý rất vui.

Cóc viết:

```python
ten = "de men"
```

— Muốn viết hoa toàn bộ:

```python
print(ten.upper())
```

— Muốn viết thường:

```python
print(ten.lower())
```

— Muốn viết đẹp từng chữ:

```python
print(ten.title())
```

— Muốn bỏ khoảng trắng thừa:

```python
cau = "   xin chao Python   "
print(cau.strip())
```

— Muốn thay chữ:

```python
cau = "Em thich hoc Java"
print(cau.replace("Java", "Python"))
```

Dế cười bò:

— Nghĩa là chuỗi giống cục đất sét, mình nhào nặn kiểu gì cũng được?

— Gần đúng đấy. Cho nên mục tiêu tiếp theo tuần này là thành thạo các **phương thức xử lý chuỗi**.

## 5. F-string: chiếc nơ buộc câu chữ cho đẹp

Dế lại hỏi:

— Cóc ơi, nếu em muốn ghép tên với tuổi thành một câu đẹp thì làm sao?

Cóc mỉm cười bí hiểm:

— Đây là lúc **f-string** xuất hiện. Nó giống như chiếc nơ buộc món quà cho đẹp đẽ, gọn gàng.

```python
ten = "Dế"
tuoi = 2
print(f"Tên của em là {ten}, năm nay em {tuoi} tuổi.")
```

Dế mắt sáng lên:

— Ô, nhìn gọn thật!

— Đúng rồi. Không cần ghép loằng ngoằng. Chỉ cần đặt chữ `f` trước chuỗi, rồi bỏ biến vào trong dấu `{}`.

Ví dụ khác:

```python
diem = 9.5
print(f"Hôm nay em được {diem} điểm, vui quá!")
```

Dế cười toe:

— Vậy mục tiêu cuối cùng là biết dùng **f-string để format chuỗi đẹp**!

— Chính xác. Viết chương trình mà in ra đẹp, rõ ràng, người đọc thích lắm.

## 6. Cóc tổng kết chiếc ba lô tuần này

Cóc phủi tay, nhìn Dế:

— Nào, nhắc lại xem tuần này chú học gì?

Dế đứng bật dậy, đọc như hô khẩu hiệu:

- Hiểu **biến** là gì và biết **đặt tên biến** cho rõ ràng
- Làm việc với các kiểu dữ liệu: **int, float, str, bool**
- Thành thạo các **phương thức xử lý chuỗi**
- Sử dụng **f-string** để format chuỗi đẹp

Cóc gật đầu hài lòng:

— Khá lắm. Chỉ cần học chắc bốn món này, chú đã có thể viết được những chương trình nhỏ rất xinh rồi.

Dế hí hửng:

— Ví dụ như gì?

Cóc đáp:

— Ví dụ như chương trình tự giới thiệu bản thân, in thông báo điểm số, hay làm một chiếc “máy chào hỏi” lịch sự.

Dế bật cười:

— Em tưởng học Python là phải đấu boss ngay, ai ngờ tuần này chỉ là học cách sắp đồ vào ba lô.

Cóc chống nạnh:

— Muốn đi xa thì ba lô phải gọn. Muốn code tốt thì nền phải chắc.

Dế ôm sổ, cười rạng rỡ:

— Vậy tuần này em không sợ nữa. Em sẽ làm bạn với biến, kết thân với chuỗi, rồi đội f-string lên đầu như cái nón!

Cóc phá lên:

— Đội vừa thôi, không là f-string lại thành “ếch-string” bây giờ!

Hai thầy trò nhìn nhau cười vang. Bờ cỏ sáng lên bởi một tuần học mới — nhẹ nhàng, vui vẻ, và đầy hứng khởi.

## 7. Ghi nhớ cuối tuần

> **Biến** là chiếc hộp có tên.  
> **Kiểu dữ liệu** là thứ nằm trong hộp.  
> **Chuỗi** là phần chữ có thể chỉnh sửa rất linh hoạt.  
> **f-string** giúp mình viết câu đẹp, rõ, gọn.

## 8. Thông điệp cuối cùng

Python không bắt đầu bằng những thứ to tát. Python bắt đầu bằng việc hiểu những điều rất nhỏ nhưng rất quan trọng.

Và tuần này, Dế đã mở được chiếc ba lô đầu tiên rồi.
