# Tuần 06 — Vòng Lặp — for và while

> **Python Journey** — Khóa học Python cơ bản cho người mới bắt đầu  
> Thời lượng: 2h lý thuyết + 2h thực hành

---

## 🎯 Mục Tiêu Tuần Này

Sau buổi học, bạn có thể:
- Dùng vòng lặp for để duyệt chuỗi, list, range
- Dùng while với điều kiện kiểm soát
- Kiểm soát vòng lặp với break, continue
- Tránh vòng lặp vô hạn

---

## 1. Vòng Lặp for

```python
# Duyệt list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Trái: {fruit}")

# Duyệt chuỗi
for char in "Python":
    print(char, end=" ")  # P y t h o n

# range() — dãy số
for i in range(5):         # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 11):     # 1 đến 10
    print(i)

for i in range(0, 20, 2):  # 0, 2, 4, ..., 18
    print(i)

# enumerate() — index + giá trị
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# zip() — duyệt hai list song song
names = ["An", "Bình", "Châu"]
scores = [8, 9, 7]
for name, score in zip(names, scores):
    print(f"{name}: {score} điểm")
```

## 2. Vòng Lặp while

```python
# Lặp khi điều kiện True
dem = 0
while dem < 5:
    print(f"Đếm: {dem}")
    dem += 1   # BẮT BUỘC tăng, không sẽ lặp vô hạn!

# Nhập liệu đến khi hợp lệ
while True:
    tuoi_str = input("Nhập tuổi (1-120): ")
    if tuoi_str.isdigit() and 1 <= int(tuoi_str) <= 120:
        tuoi = int(tuoi_str)
        break
    print("Tuổi không hợp lệ, thử lại!")

print(f"Tuổi: {tuoi}")
```

## 3. break, continue, else

```python
# break — thoát ngay lập tức
for i in range(10):
    if i == 5:
        break
    print(i)   # 0 1 2 3 4

# continue — bỏ qua iteration hiện tại
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)   # 1 3 5 7 9

# else trong vòng lặp: chạy khi loop hoàn thành KHÔNG có break
for i in range(5):
    if i == 10:   # Không xảy ra
        break
else:
    print("Vòng lặp hoàn thành!")   # In ra
```

## 4. Vòng Lặp Lồng Nhau

```python
# Bảng nhân 3x3
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j:2d}", end="  ")
    print()

# Vẽ tam giác
n = 5
for i in range(1, n+1):
    print("*" * i)
```

## 5. Bài Tập

### Bài 1 — Bảng cửu chương (Dễ)
In bảng cửu chương từ 2 đến 9, mỗi bảng cách nhau một dòng trắng.

### Bài 2 — FizzBuzz (Trung bình)
In 1-100: số chia hết 3 in "Fizz", chia hết 5 in "Buzz", cả hai in "FizzBuzz", còn lại in số.

### Bài 3 — Số nguyên tố (Trung bình)
In tất cả số nguyên tố từ 2 đến 100.

### Bài 4 — Sắp xếp nổi bọt (Thử thách)
Cài đặt thuật toán Bubble Sort bằng vòng lặp lồng nhau.

---

## 🔑 Những Điều Quan Trọng Nhất Tuần Này

> 1. **for** dùng khi biết số lần lặp; **while** khi không biết trước
> 2. **LUÔN có cơ chế thoát** trong while — quên là treo máy!
> 3. **enumerate() và zip()** giúp tránh dùng index thủ công — Pythonic hơn
