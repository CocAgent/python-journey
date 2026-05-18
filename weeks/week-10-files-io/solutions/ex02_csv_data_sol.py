"""Lời giải Bài tập 02: CSV"""
import csv

# TODO 1
with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Tên", "Tuổi", "Toán", "Văn", "Anh"])
    writer.writerows([
        ["An", 20, 8, 7, 9],
        ["Bình", 21, 7, 8, 6],
        ["Châu", 20, 9, 9, 10],
        ["Dũng", 22, 6, 5, 7],
        ["Em", 19, 8, 8, 8],
    ])

# TODO 2
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"{row[0]:<8} {row[1]:>4} {row[2]:>5} {row[3]:>5} {row[4]:>5}")

# TODO 3
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        tb = (int(row["Toán"]) + int(row["Văn"]) + int(row["Anh"])) / 3
        xep = "Giỏi" if tb >= 8 else "Khá" if tb >= 6.5 else "TB" if tb >= 5 else "Yếu"
        print(f"{row['Tên']}: {tb:.1f} ({xep})")
