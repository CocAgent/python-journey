"""Lời giải Bài tập 01: Module chuẩn Python"""
import math
import random
from datetime import datetime, timedelta
import os

# TODO 1
print(f"sqrt(144) = {math.sqrt(144)}")
print(f"ceil(3.2) = {math.ceil(3.2)}")
print(f"floor(3.8) = {math.floor(3.8)}")

# TODO 2
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
print([random.randint(1, 100) for _ in range(5)])
print(random.sample(cards, 3))
random.shuffle(cards)
print(cards[:5])

# TODO 3
now = datetime.now()
print(f"Bây giờ: {now.strftime('%d/%m/%Y %H:%M')}")
birthday = datetime(2000, 1, 15)
print(f"Số ngày sống: {(now - birthday).days}")
future = now + timedelta(days=100)
print(f"100 ngày nữa: {future.strftime('%d/%m/%Y')}")

# TODO 4
print(f"Thư mục hiện tại: {os.getcwd()}")
print(f"Files: {os.listdir('.')}")
