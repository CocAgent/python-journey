"""Kiểm thử lời giải tham khảo; không dùng để chấm exercises/."""

import pytest

from solutions.ex01_classes import Progress
from solutions.ex02_composition import Bot, aggressive, balanced, defensive
from solutions.ex03_inheritance import Animal, Dog
from solutions.ex04_dien_thoai import DienThoai


def test_progress_valid_and_string():
    progress = Progress(3, 4)
    assert progress.percentage() == 75.0
    assert str(progress) == "Progress: 3/4 (75%)"


@pytest.mark.parametrize("completed,total", [(0, 0), (-1, 4), (5, 4)])
def test_progress_rejects_invalid_values(completed, total):
    with pytest.raises(ValueError):
        Progress(completed, total)


@pytest.mark.parametrize("strategy", [defensive, balanced, aggressive])
def test_strategies_move_left_right_and_wait(strategy):
    bot = Bot(strategy)
    assert bot.choose_action({"position": 1, "goal": 4}) == "right"
    assert bot.choose_action({"position": 4, "goal": 1}) == "left"
    assert bot.choose_action({"position": 2, "goal": 2}) == "wait"


def test_defensive_and_strategy_swap():
    state = {"position": 3, "goal": 0, "opponent_position": 4}
    bot = Bot(defensive)
    assert bot.choose_action(state) == "wait"
    bot.strategy = balanced
    assert bot.choose_action(state) == "left"


def test_dog_inherits_animal():
    dog = Dog("Milo")
    assert isinstance(dog, Animal)
    assert dog.speak() == "Milo: woof"


def test_phone_returns_information_without_printing(capsys):
    phone = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28_990_000)
    info = phone.thongtindienthoai()
    assert all(value in info for value in ("DT01", "iPhone 15 Pro", "Apple", "3274", "28,990,000"))
    assert capsys.readouterr().out == ""


@pytest.mark.parametrize("code,name,brand,pin,price", [
    ("", "Phone", "Brand", 3000, 10),
    ("DT", " ", "Brand", 3000, 10),
    ("DT", "Phone", "", 3000, 10),
    ("DT", "Phone", "Brand", 0, 10),
    ("DT", "Phone", "Brand", 3000, -1),
])
def test_phone_rejects_invalid_values(code, name, brand, pin, price):
    with pytest.raises(ValueError):
        DienThoai(code, name, brand, pin, price)
