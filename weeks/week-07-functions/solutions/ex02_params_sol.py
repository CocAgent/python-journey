"""Lời giải Bài tập 02: Tham số nâng cao"""

# TODO 1
def gioi_thieu(ten, tuoi=18, thanh_pho="Hà Nội"):
    print(f"Tôi là {ten}, {tuoi} tuổi, ở {thanh_pho}")

gioi_thieu("An")
gioi_thieu("Bình", 25)
gioi_thieu("Châu", thanh_pho="HCM")

# TODO 2
def tinh_tong(*numbers):
    return sum(numbers)

print(tinh_tong(1, 2, 3))
print(tinh_tong(1, 2, 3, 4, 5))

# TODO 3
def tao_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

tao_profile(ten="An", tuoi=25, nghe="Developer")

# TODO 4
binh_phuong = lambda x: x ** 2
la_chan = lambda x: x % 2 == 0
print(binh_phuong(5), la_chan(4))

students = [("An", 8.5), ("Bình", 7.0), ("Châu", 9.2)]
students.sort(key=lambda s: s[1], reverse=True)
print(students)
