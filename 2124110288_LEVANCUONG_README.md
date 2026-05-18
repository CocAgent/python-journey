# 📚 HỆ THỐNG QUẢN LÝ THƯ VIỆN

> Đồ án môn học: Lập trình & Cấu trúc dữ liệu Python

---

## 👨‍🎓 Thông tin sinh viên
- **Họ và tên:** Lê Văn Cường
- **MSSV:** 2124110288
- **Đề tài:** Hệ thống Quản lý Thư viện

---

## 🌟 1. Giới thiệu
Ứng dụng hỗ trợ quản lý sách và độc giả trong thư viện bằng giao diện Menu dòng lệnh đơn giản, trực quan.

## 🏗️ 2. Cấu trúc dữ liệu sử dụng
- **Cây nhị phân (BST):** Lưu trữ danh mục sách, giúp tìm kiếm theo mã hoặc tên cực nhanh với tốc độ O(log N).
- **Hàng đợi (Queue):** Quản lý danh sách độc giả xếp hàng chờ mượn khi sách tạm hết.
- **Ngăn xếp (Stack):** Ghi nhớ lịch sử thao tác để hỗ trợ tính năng Hoàn tác (Undo) tức thì.

## 🚀 3. Hướng dẫn chạy chương trình
```bash
python src/main.py
```

## 🛠️ 4. Các chức năng chính
1. Thêm / Sửa / Xóa thông tin sách
2. Tìm kiếm sách theo Mã hoặc Tên
3. Mượn sách (tự động vào Queue chờ nếu hết)
4. Trả sách (thông báo người xếp hàng tiếp theo)
5. Hoàn tác thao tác gần nhất (Undo)

## 🧪 5. Danh sách 5 Test cases chính
- **TC01:** Thêm mới 100 đầu sách và tìm kiếm thành công.
- **TC02:** Độc giả mượn sách đã hết -> tự động được đưa vào danh sách chờ Queue.
- **TC03:** Lỡ tay xóa nhầm sách -> bấm nút Undo để khôi phục lại.
- **TC04:** Nhập tìm kiếm mã sách không tồn tại -> hiển thị thông báo lỗi thân thiện.
- **TC05:** Tắt chương trình và mở lại -> toàn bộ dữ liệu tự động được nạp lại từ file.
