🎓 Chương trình Thẻ Sinh Viên Tự Động
📌 Giới thiệu

Đây là chương trình Python đơn giản dùng để tạo và hiển thị thông tin thẻ sinh viên tự động dựa trên thông tin do người dùng nhập vào.

Chương trình cho phép nhập:

Họ và tên sinh viên
Mã số sinh viên (MSSV)
Ngành học
Năm nhập học

Sau đó chương trình sẽ tự động tính năm tốt nghiệp dự kiến và hiển thị thông tin theo dạng một chiếc thẻ sinh viên trên màn hình.

🛠️ Công nghệ sử dụng
Ngôn ngữ: Python 3
Kiến thức sử dụng:
input() để nhập dữ liệu
int() để chuyển dữ liệu sang số nguyên
Biến và phép tính
F-string để định dạng chuỗi
print() để xuất kết quả
📂 Cấu trúc chương trình

Ví dụ cấu trúc thư mục:

the-sinh-vien/
│
├── main.py
└── README.md


Trong đó:

main.py: Chương trình chính.
README.md: Tài liệu hướng dẫn sử dụng chương trình.
🚀 Cách chạy chương trình
1. Cài đặt Python

Đảm bảo máy tính đã cài Python 3.

Kiểm tra phiên bản Python bằng lệnh:

python --version


hoặc:

python3 --version

2. Chạy chương trình

Mở Terminal hoặc Command Prompt tại thư mục chứa file Python và chạy:

python main.py


Nếu máy sử dụng python3:

python3 main.py

💻 Cách sử dụng

Sau khi chạy chương trình, hệ thống sẽ lần lượt yêu cầu nhập thông tin.

Ví dụ:

Nhap ho ten: Nguyen Van An
Nhap MSSV: 22123456
Nganh hoc: Cong nghe thong tin
Nam nhap hoc: 2022


Chương trình sẽ tự động tính:

Nam tot nghiep = Nam nhap hoc + 3


Kết quả:

=============================================
         THE SINH VIEN
=============================================
Ho ten:  Nguyen Van An
  MSSV                : 22123456
  Nganh               : Cong nghe thong tin
  Nam nhap hoc        : 2022
  Nam tot nghiep      : 2025
=============================================

🧮 Nguyên lý hoạt động

Chương trình thực hiện các bước:

Nhập họ tên sinh viên.
Nhập MSSV.
Nhập ngành học.
Nhập năm nhập học.
Tính năm tốt nghiệp dự kiến bằng công thức:
nam_tot_nghiep = nam_nhap_hoc + 3

In toàn bộ thông tin sinh viên ra màn hình theo định dạng thẻ.
📝 Mã nguồn
ho_ten = input("Nhap ho ten: ")
mssv = input("Nhap MSSV: ")
nganh = input("Nganh hoc: ")
nam_nhap_hoc = int(input("Nam nhap hoc: "))

nam_tot_nghiep = nam_nhap_hoc + 3

print("\n" + "=" * 45)
print("         THE SINH VIEN")
print("=" * 45)
print(f"Ho ten:  {ho_ten}")
print(f"  MSSV                : {mssv}")
print(f"  Nganh               : {nganh}")
print(f"  Nam nhap hoc        : {nam_nhap_hoc}")
print(f"  Nam tot nghiep      : {nam_tot_nghiep}")
print("=" * 45)


Lưu ý: Trong code ban đầu của bạn, "/n" là sai. Ký tự xuống dòng trong Python phải là "\n".

🎯 Mục tiêu của bài tập

Chương trình được xây dựng nhằm giúp người học làm quen với các kiến thức Python cơ bản như:

Khai báo và sử dụng biến.
Nhập dữ liệu từ bàn phím.
Ép kiểu dữ liệu.
Thực hiện phép tính.
Sử dụng f-string.
Định dạng dữ liệu khi xuất ra màn hình.
🔮 Hướng phát triển

Trong tương lai, chương trình có thể được nâng cấp thêm:

Kiểm tra dữ liệu nhập vào.
Tự động xác định năm tốt nghiệp theo chương trình đào tạo.
Thêm ngày sinh, giới tính, lớp và khóa học.
Tạo thẻ sinh viên bằng giao diện đồ họa.
Xuất thẻ sinh viên thành file ảnh hoặc PDF.
Lưu thông tin nhiều sinh viên vào file.
Xây dựng giao diện web hoặc ứng dụng desktop.
👨‍💻 Tác giả

Sinh viên: Lê Thanh Dĩnh

Dự án: Chương trình Thẻ Sinh Viên Tự Động