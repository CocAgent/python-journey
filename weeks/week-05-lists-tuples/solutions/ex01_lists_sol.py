"""Lời giải Bài tập 01: List"""
# TODO 1
mon_hoc = ["Toán", "Văn", "Anh", "Lý", "Hóa"]
mon_hoc.append("Tin")
mon_hoc.insert(2, "Sinh")
mon_hoc.remove("Lý")
print(mon_hoc)

# TODO 2
diem = [7, 9, 5, 8, 10, 6, 4, 9]
diem.sort()
print(f"Sắp xếp: {diem}")
print(f"Max: {max(diem)}, Min: {min(diem)}, TB: {sum(diem)/len(diem):.1f}")
dat = len([d for d in diem if d >= 5])
print(f"Số điểm đạt: {dat}/{len(diem)}")

# TODO 3
n = int(input("Nhập n: "))
nums = [float(input(f"Số {i+1}: ")) for i in range(n)]
print(f"Tổng: {sum(nums)}, TB: {sum(nums)/len(nums):.1f}")
print(f"Min: {min(nums)}, Max: {max(nums)}")

# TODO 4
nums = [1, 3, 2, 3, 1, 5, 2, 4]
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
print(unique)
