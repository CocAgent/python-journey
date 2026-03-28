"""Lời giải Bài tập 02: Nhiều loại Exception"""
# TODO 1
try:
    with open("numbers.txt", "w") as f:
        f.write("10\n5")
    with open("numbers.txt", "r") as f:
        lines = f.readlines()
        a, b = int(lines[0].strip()), int(lines[1].strip())
        result = a / b
except FileNotFoundError:
    print("File không tồn tại!")
except ValueError:
    print("File chứa dữ liệu không hợp lệ!")
except ZeroDivisionError:
    print("Không thể chia cho 0!")
else:
    print(f"{a} / {b} = {result}")
finally:
    print("Hoàn tất.")

# TODO 2
def get_value(data, key, index):
    try:
        return data[key][index]
    except KeyError:
        print(f"Key \"{key}\" không tồn tại")
    except IndexError:
        print(f"Index {index} ngoài phạm vi")
    except TypeError:
        print("Kiểu dữ liệu không hợp lệ")
    return None

data = {"scores": [85, 92, 78]}
print(get_value(data, "scores", 1))   # 92
print(get_value(data, "grades", 0))   # KeyError
print(get_value(data, "scores", 10))  # IndexError

# TODO 3
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Vui lòng nhập số!")

# price = get_float("Nhập giá: ")
