"""
Bài tập 01: Vòng lặp for
==============================
Trình bày: 
- Vòng lặp for: Dùng khi biết trước số lần lặp (ví dụ chạy qua danh sách, hoặc chạy từ 1 đến n).
- enumerate: "for loop + số thứ tự tự động" (dùng khi cần đánh số thứ tự).
- zip: "ghép đôi song song" các danh sách có cùng độ dài lại với nhau.
"""

# TODO 1: In bảng cửu chương
# TRÌNH BÀY: Dùng range(start, stop) để xác định số lần chạy cố định từ 1 đến 10
n = int(input("Nhap so de in bang cuu chuong: "))  # Chuyển đổi dữ liệu nhập vào thành số nguyên
print(f"\nBang cuu chuong so {n}:")
for i in range(1, 11):                             # i chạy lần lượt từ 1 đến 10
    print(f"  {n} x {i:2d} = {n * i}")             # :2d dùng để căn phải chữ số giúp thẳng hàng


# TODO 2: Duyệt danh sách với enumerate
# TRÌNH BÀY: Tránh việc phải tự tạo biến đếm index rồi cộng thủ công
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print("\nDanh sach trai cay:")
# enumerate(fruits, start=1) sẽ trả về từng cặp (số thứ tự, phần tử) bắt đầu đếm từ 1
for stt, fruit in enumerate(fruits, start=1):
    print(f"  {stt}. {fruit}")


# TODO 3: Ghép 2 danh sách bằng zip
# TRÌNH BÀY: Duyệt song song nhiều list cùng lúc mà không cần dùng chỉ số index
names = ["An", "Binh", "Chau"]
scores = [8, 9, 7]

print("\nDiem sinh vien:")
# zip(names, scores) lấy phần tử thứ nhất của list1 ghép với phần tử thứ nhất của list2
for name, score in zip(names, scores):
    print(f"  {name}: {score} diem")


# TODO 4: Tính tổng các số chẵn từ 1 đến 100 bằng for + range
# TRÌNH BÀY: Tận dụng tham số bước nhảy (step) của hàm range
tong_chan = 0                            # Tạo biến tích lũy tổng ban đầu bằng 0
for i in range(2, 101, 2):             # Chạy từ 2 đến 100, mỗi bước nhảy cộng thêm 2 (chỉ lấy số chẵn)
    tong_chan += i                       # Cộng dồn số chẵn hiện tại vào tổng
print(f"\nTong cac so chan tu 1 den 100: {tong_chan}")


# TODO 5 (Thử thách): Dãy Fibonacci
# TRÌNH BÀY: Kỹ thuật hoán đổi giá trị đồng thời (multiple assignment) trong vòng lặp
n_fib = int(input("\nNhap so luong phan tu Fibonacci can in: "))
fib = []                  # List lưu trữ dãy số kết quả
a, b = 0, 1               # Khởi tạo 2 số đầu tiên của dãy Fibonacci
for _ in range(n_fib):    # Ký tự gạch dưới _ biểu thị biến lặp không cần dùng đến trong thân vòng lặp
    fib.append(a)         # Thêm số hiện tại vào danh sách kết quả
    a, b = b, a + b       # Dịch chuyển đồng thời: số tiếp theo bằng tổng hai số trước

print(f"{n_fib} so Fibonacci dau tien: {fib}")
