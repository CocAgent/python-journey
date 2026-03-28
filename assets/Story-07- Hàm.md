# 🐸🐢🦗 Cóc, bác Rùa và ván trốn tìm của những chiếc Hàm

> **“Chia để trị — nguyên tắc vàng trong lập trình.”**

Một câu chuyện vui để bắt đầu bài học về **Hàm (Functions)**.

## 1. Một ván trốn tìm bắt đầu quá rối

Chiều xuống bên bờ ao, gió thổi xào xạc qua đám cỏ. Dế nhảy tót lên một phiến đá, mắt long lanh:

— Anh Cóc ơi, hôm nay mình chơi gì thế?

Cóc chống nạnh, cười bí hiểm:

— Hôm nay không chỉ chơi đâu. Hôm nay ta vừa chơi **trốn tìm**, vừa học một bí mật cực mạnh của lập trình: **Hàm**.

Bác Rùa từ từ bò tới, đeo trên lưng một cuốn sổ dày cộp:

— Ừm. Muốn chơi trốn tìm hấp dẫn mà không rối tung lên, phải biết **chia việc lớn thành việc nhỏ**. Đó chính là tinh thần của hàm.

Dế nghiêng đầu:

— Hàm là gì mà nghe oai vậy bác?

Bác Rùa mỉm cười:

— Cứ tưởng tượng thế này: thay vì mỗi lần chơi lại phải nói lại cả đống luật, ta gom từng việc vào từng “gói nhiệm vụ”. Mỗi gói đó chính là một **function**.

## 2. Khi trò chơi quá lớn, ta dùng `def`

Hôm ấy, cả ba quyết định tổ chức một ván trốn tìm lớn nhất từ trước tới nay.

Nhưng mới bàn một lúc, mọi thứ đã rối như tơ vò.

Cóc nói:

— Ta cần đếm số.

Dế chen vào:

— Rồi phải chọn người đi tìm.

Bác Rùa gật gù:

— Còn phải kiểm tra ai đã bị tìm thấy, ai còn trốn, ai báo hiệu kết thúc.

Cả ba nhìn nhau.

Dế ôm đầu:

— Trời ơi, chỉ là trốn tìm thôi mà sao lắm việc thế?

Bác Rùa cười hiền:

— Đây chính là lúc dùng **hàm**. Ta không làm tất cả trong một cục to đùng. Ta **chia để trị**.

Bác Rùa lấy que viết lên cát:

```python
def dem_so():
    print("1... 2... 3... 4... 5...")
```

— `def` là cách ta **định nghĩa một hàm**.

Dế tròn mắt:

— Nghĩa là mình đặt tên cho một việc?

— Đúng. `dem_so()` là một việc. Khi muốn dùng, chỉ cần **gọi hàm**:

```python
dem_so()
```

Cóc vỗ đùi:

— A ha! Giống như ra lệnh: “Này, làm giúp tôi phần đếm số!”

## 3. Tham số và đối số: chỗ trống và món đồ thật

Ván chơi bắt đầu. Cóc là người đi tìm đầu tiên. Nhưng Cóc chợt hỏi:

— Nếu mỗi lần mình muốn đếm số khác nhau thì sao? Lúc 5, lúc 10, lúc 20?

Bác Rùa gật đầu:

— Lúc ấy ta cho hàm một **tham số**.

```python
def dem_so(so_cuoi):
    print(f"1... 2... 3... đến {so_cuoi}!")
```

Dế chớp chớp mắt:

— Tham số là gì ạ?

— Là chỗ trống để nhận dữ liệu. Còn khi con thật sự truyền vào một giá trị, ví dụ số `10`, thì đó gọi là **đối số**.

```python
dem_so(10)
```

— Trong đó, `so_cuoi` là **tham số**, còn `10` là **đối số**.

Dế cười toe:

— À, vậy tham số là cái giỏ còn đối số là thứ mình bỏ vào giỏ!

Cóc bật cười:

— Ví dụ này nghe là hiểu ngay.

## 4. `return`: mang kết quả về sau cuộc truy tìm

Ván chơi càng lúc càng hấp dẫn. Dế lẩn vào bụi lau. Cóc nhảy vòng quanh. Bác Rùa thì quan sát rất kỹ.

Một lúc sau, Cóc hỏi:

— Nếu một hàm làm xong việc rồi, nó có thể mang kết quả về cho mình không?

Bác Rùa gật đầu chắc nịch:

— Có. Đó là lúc dùng `return`.

```python
def tinh_so_noi_tron(bui_co, goc_cay):
    return bui_co + goc_cay
```

— Hàm này làm xong thì **trả về** kết quả. Giống như một người đi tìm xong quay lại báo cáo: “Có tất cả 7 chỗ trốn!”

Dế gật gù:

— Vậy hàm có `return` là hàm **có báo cáo**.

— Chính xác. Trong C++ người ta hay phân biệt kiểu trả về như `int` và `void`.

- Hàm kiểu **`int`**: làm xong phải mang về một con số cụ thể.
- Hàm kiểu **`void`**: chỉ thực hiện hành động, làm xong là thôi.

Ví dụ C++:

```cpp
int tinhTong(int a, int b) {
    return a + b;
}

void chaoHoi() {
    std::cout << "Xin chao ban!\n";
}
```

Bác Rùa nói tiếp:

— Còn trong **Python** thì thoải mái hơn. Ta chỉ cần `def`. Nếu có `return`, hàm trả về giá trị. Nếu không có `return`, Python âm thầm trả về `None`.

```python
def chao_hoi(ten):
    print(f"Xin chao, {ten}!")
```

Dế nghiêng đầu:

— `None` là gì?

— Là “không có gì để báo cáo cả”.

Cóc vỗ tay:

— Vậy là em hiểu rồi:

- Có `return` → mang kết quả về
- Không `return` → làm việc xong là thôi

## 5. Tham số mặc định và keyword arguments: luật chơi dẻo dai hơn

Dế từ bụi lau thò đầu ra, cười láu lỉnh:

— Nhưng lỡ có hôm mình muốn đếm 5, có hôm 10, có hôm lại muốn chạy chậm chậm cho bác Rùa kịp theo thì sao?

Bác Rùa cười mỉm:

— Ta có thể đặt **tham số mặc định**.

```python
def bat_dau_tim(so_giay=10, toc_do="vua"):
    print(f"Bắt đầu tìm trong {so_giay} giây, tốc độ {toc_do}.")
```

— Nếu không truyền gì, hàm tự dùng `10` và `"vua"`.

```python
bat_dau_tim()
```

— Còn nếu muốn đổi, ta truyền vào:

```python
bat_dau_tim(5, "nhanh")
```

Dế gật đầu lia lịa:

— Hay quá. Nhưng em hay quên thứ tự.

— Không sao, có **keyword arguments**.

```python
bat_dau_tim(toc_do="cham", so_giay=15)
```

Cóc reo lên:

— À, lúc này mình gọi rõ tên từng tham số nên đảo thứ tự vẫn ổn!

— Chính xác. Nó làm câu lệnh dễ đọc hơn, đặc biệt khi hàm có nhiều tham số.

## 6. Scope: bí mật trong bụi cỏ và chiếc chuông giữa vườn

Ván trốn tìm sang vòng ba. Dế nghĩ ra trò mới: mỗi lần bị phát hiện sẽ để lại một chiếc lá làm dấu.

Dế hỏi:

— Anh Cóc ơi, em có một biến tên là `so_la`. Nếu em tạo nó trong hàm, bên ngoài có nhìn thấy không?

Cóc định trả lời nhưng bác Rùa đã lên tiếng:

— Đây là chuyện **scope** — phạm vi của biến.

Bác vẽ hai vòng tròn trên đất.

— Biến ở **local scope** giống như bí mật giấu trong một bụi cỏ. Chỉ người ở trong bụi đó mới biết.

```python
def choi_tron():
    vi_tri_bi_mat = "sau_goc_sen"
    print(vi_tri_bi_mat)
```

— `vi_tri_bi_mat` chỉ sống bên trong `choi_tron()`.

Dế nghiêng đầu:

— Thế còn biến global?

— Global giống như **chuông báo ở giữa vườn**. Ai trong khu vườn cũng nghe được.

```python
chuong_bao = 0

def bao_hieu():
    global chuong_bao
    chuong_bao += 1
```

Cóc gãi đầu:

— Vậy local thì an toàn hơn cho từng việc nhỏ, còn global là thứ cả nơi cùng dùng?

— Đúng. Và vì global dùng chung nên phải cẩn thận. Nếu ai cũng sửa linh tinh, khu vườn sẽ loạn.

Dế phá lên:

— Tức là bí mật thì nên để trong bụi cỏ, đừng treo giữa sân!

## 7. Docstring: tấm biển chỉ đường cho người đến sau

Chơi được một lúc, Dế nhìn lại đống hàm bác Rùa viết mà hoa cả mắt.

— Bác ơi, lỡ mai mốt em quên hàm này dùng để làm gì thì sao?

Bác Rùa lấy ra một mẩu giấy, chậm rãi nói:

— Người viết code giỏi không chỉ viết cho máy hiểu. Họ còn viết cho **người khác** hiểu. Thậm chí là cho **chính mình của một tuần sau**.

Rồi bác viết:

```python
def tim_kiem(ten_nguoi_choi, so_giay=10):
    """
    Bắt đầu một lượt đi tìm trong trò trốn tìm.

    Args:
        ten_nguoi_choi (str): Tên người đi tìm.
        so_giay (int): Thời gian đếm số trước khi đi tìm.

    Returns:
        str: Thông báo bắt đầu lượt chơi.
    """
    return f"{ten_nguoi_choi} bắt đầu tìm sau {so_giay} giây."
```

Dế mắt sáng rực:

— Ô, đây như một tấm biển chỉ đường!

— Đúng thế. Đó là **docstring**. Viết docstring chuyên nghiệp giúp hàm rõ ràng, dễ học, dễ bảo trì.

## 8. Tóm lại, cả ván trốn tìm hóa thành một chương trình đẹp

Bác Rùa gom mọi thứ lại:

```python
def dem_so(so_cuoi=10):
    """Đếm số trước khi bắt đầu lượt tìm."""
    print(f"Đếm đến {so_cuoi} rồi bắt đầu!")


def chon_noi_tron(nguoi_choi):
    """Trả về vị trí trốn bí mật của người chơi."""
    return f"{nguoi_choi} đang trốn sau bụi cỏ."


def bao_hieu(ten="Dế", am_luong="vừa"):
    """Phát tín hiệu gọi người chơi ra ngoài."""
    print(f"Gọi {ten} với âm lượng {am_luong}.")


def ket_qua_tim_kiem(da_tim_thay):
    """Trả về kết quả đúng/sai của lượt tìm."""
    return da_tim_thay
```

Dế nhảy cẫng:

— Em hiểu rồi! Trước đây em nghĩ trốn tìm chỉ là chạy lung tung. Giờ em thấy có thể chia trò chơi thành từng phần rất rõ.

Cóc cười tươi:

— Và đó cũng là cách lập trình bớt rối.

Bác Rùa chậm rãi kết luận:

— Khi bài toán lớn quá, đừng ôm cả cục. Hãy tách nó thành những việc nhỏ, đặt tên tử tế cho từng việc, rồi ghép lại. Đó là sức mạnh của **functions**.

## 9. Dế tổng kết sau khi… bị tìm thấy

Cuối cùng, sau một hồi truy lùng căng thẳng, Cóc phát hiện ra Dế đang núp trong chiếc chum úp cạnh gốc chuối.

Dế chui ra, phủi bụi, cười hì hì:

— Được rồi, em thua. Nhưng bù lại em học được cả một rổ kiến thức!

Rồi Dế đọc to:

- Biết **định nghĩa và gọi hàm** bằng `def`
- Hiểu **tham số**, **đối số** và `return`
- Biết dùng **tham số mặc định** và **keyword arguments**
- Hiểu **scope**: `local` và `global`
- Biết viết **docstring** chuyên nghiệp

Cóc vỗ tay:

— Giỏi lắm!

Bác Rùa khẽ gật đầu:

— Sau tuần này, con không chỉ biết viết hàm. Con còn hiểu vì sao hàm là một trong những công cụ đẹp nhất của lập trình.

Dế nhìn hai người, mắt long lanh:

— Vậy ra học hàm cũng giống chơi trốn tìm nhỉ?

Cóc hỏi:

— Giống chỗ nào?

Dế cười tinh nghịch:

— Vì muốn tìm được đáp án, mình phải biết chia từng chỗ mà tìm. Không thể lao vào cả khu vườn một cách bừa bãi được!

Bác Rùa bật cười hiền hậu:

— Chính xác. Và đó là lúc lập trình bắt đầu trở nên thật sự thông minh.

## 🐸 Ghi nhớ cuối bài

> **Hàm là cách chia việc lớn thành việc nhỏ.**  
> **`return` là mang kết quả về.**  
> **Tham số là chỗ chờ dữ liệu, đối số là dữ liệu thật sự truyền vào.**  
> **Scope giúp ta biết biến sống ở đâu.**  
> **Docstring là lời giải thích tử tế cho người đến sau.**

🐸 Đây là lời chào mở đầu cho hành trình học Python: vui vẻ, gần gũi và đủ nhẹ nhàng để ai cũng có thể bắt đầu. 🦗
