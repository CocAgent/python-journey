"""Test bài sinh viên: starter chưa làm phải FAIL chứ không PASS giả."""

import pytest

from exercises.ex01_classes import Progress
from exercises.ex02_composition import Bot, aggressive, balanced, defensive
from exercises.ex03_inheritance import Animal, Dog
from exercises.ex04_dien_thoai import DienThoai


def test_ex01_progress():
    p = Progress(3, 4)
    assert p.completed == 3 and p.total == 4
    assert p.percentage() == 75
    assert str(p) == "Progress: 3/4 (75%)"


@pytest.mark.parametrize("done,total", [(0, 0), (-1, 4), (5, 4)])
def test_ex01_invalid(done, total):
    with pytest.raises(ValueError):
        Progress(done, total)


@pytest.mark.parametrize("strategy", [defensive, balanced, aggressive])
def test_ex02_goal_both_directions(strategy):
    bot = Bot(strategy)
    assert bot.choose_action({"position": 1, "goal": 4}) == "right"
    assert bot.choose_action({"position": 4, "goal": 1}) == "left"
    assert bot.choose_action({"position": 2, "goal": 2}) == "wait"


def test_ex02_strategy_swap():
    bot = Bot(defensive)
    state = {"position": 3, "goal": 0, "opponent_position": 4}
    assert bot.choose_action(state) == "wait"
    bot.strategy = balanced
    assert bot.choose_action(state) == "left"


def test_ex02_strategy_injection():
    called = []

    def record(state):
        called.append(state["goal"])
        return "wait"

    assert Bot(record).choose_action({"goal": 7}) == "wait"
    assert called == [7]


def test_ex03_inheritance():
    dog = Dog("Milo")
    assert isinstance(dog, Animal)
    assert dog.name == "Milo"
    assert dog.speak() == "Milo: woof"


def test_ex04_phone(capsys):
    phone = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28_990_000)
    assert phone.ma_may == "DT01"
    assert phone.dung_luong_pin == 3274
    assert phone.gia_ban == 28_990_000
    info = phone.thongtindienthoai()
    assert isinstance(info, str)
    assert all(x in info for x in ["DT01", "iPhone 15 Pro", "Apple", "3274", "28990000"])
    assert capsys.readouterr().out == ""


@pytest.mark.parametrize(
    ("code", "pin", "price"),
    [("", 3000, 10), ("DT01", 0, 10), ("DT01", 3000, -1)],
)
def test_ex04_invalid_phone(code, pin, price):
    with pytest.raises(ValueError):
        DienThoai(code, "Phone", "Brand", pin, price)


def test_ex04_independent_objects():
    a = DienThoai("DT01", "A", "Apple", 3274, 1)
    b = DienThoai("DT02", "B", "Samsung", 5000, 2)
    assert a is not b
    assert a.ma_may != b.ma_may
