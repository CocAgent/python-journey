"""Test tham chiếu Tuần 14, không chấm bài sinh viên."""

import pytest

from solutions.dien_thoai import DienThoai
from solutions.oop_models import (
    Animal,
    Bot,
    Dog,
    Progress,
    aggressive,
    balanced,
    defensive,
)


@pytest.mark.parametrize(
    ("done", "total", "expected"),
    [(0, 4, 0), (3, 4, 75), (4, 4, 100)],
)
def test_progress_normal_and_edges(done, total, expected):
    progress = Progress(done, total)
    assert progress.percentage() == expected
    assert progress.completed == done
    assert progress.total == total


@pytest.mark.parametrize(
    ("done", "total"),
    [(0, 0), (0, -1), (-1, 4), (5, 4)],
)
def test_progress_rejects_invalid(done, total):
    # Không tạo object sai để rồi gây chia cho 0 hoặc tỷ lệ > 100%.
    with pytest.raises(ValueError):
        Progress(done, total)


def test_progress_string_does_not_print(capsys):
    assert str(Progress(3, 4)) == "Progress: 3/4 (75%)"
    assert capsys.readouterr().out == ""


@pytest.mark.parametrize("strategy", [defensive, balanced, aggressive])
@pytest.mark.parametrize(
    ("position", "goal", "expected"),
    [(1, 4, "right"), (4, 1, "left"), (2, 2, "wait")],
)
def test_strategy_moves_both_directions(strategy, position, goal, expected):
    state = {"position": position, "goal": goal}
    before = state.copy()
    assert Bot(strategy).choose_action(state) == expected
    assert state == before


def test_defensive_waits_for_near_opponent():
    state = {"position": 3, "goal": 0, "opponent_position": 4}
    assert Bot(defensive).choose_action(state) == "wait"
    assert Bot(balanced).choose_action(state) == "left"
    assert Bot(aggressive).choose_action(state) == "left"


def test_defensive_moves_when_safe():
    assert defensive({"position": 3, "goal": 0, "opponent_position": 8}) == "left"
    assert defensive({"position": 0, "goal": 4}) == "right"


def test_bot_changes_strategy_without_inheritance():
    bot = Bot(defensive)
    state = {"position": 3, "goal": 0, "opponent_position": 4}
    assert bot.choose_action(state) == "wait"
    bot.strategy = balanced
    assert bot.choose_action(state) == "left"


def test_bot_really_calls_its_strategy():
    calls = []

    def custom_strategy(state):
        calls.append(state["goal"])
        return "wait"

    assert Bot(custom_strategy).choose_action({"goal": 7}) == "wait"
    assert calls == [7]


def test_dog_inherits_name():
    dog = Dog("Milo")
    assert isinstance(dog, Animal)
    assert dog.name == "Milo"
    assert dog.speak() == "Milo: woof"


def test_phone_attributes_and_display(capsys):
    phone = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28_990_000)
    assert (
        phone.ma_may,
        phone.ten_may,
        phone.hang_san_xuat,
        phone.dung_luong_pin,
        phone.gia_ban,
    ) == ("DT01", "iPhone 15 Pro", "Apple", 3274, 28_990_000)
    info = phone.thongtindienthoai()
    assert isinstance(info, str)
    assert all(x in info for x in ["DT01", "iPhone 15 Pro", "Apple", "3274", "28990000"])
    # Hàm tạo chuỗi không được tự in, để người gọi quyết định nơi hiển thị.
    assert capsys.readouterr().out == ""


def test_phone_objects_are_independent():
    a = DienThoai("DT01", "A", "Apple", 3274, 1)
    b = DienThoai("DT02", "B", "Samsung", 5000, 2)
    assert a is not b
    assert a.ma_may != b.ma_may


@pytest.mark.parametrize(
    ("code", "name", "brand", "battery", "price"),
    [
        ("", "A", "B", 1000, 1),
        ("DT", "", "B", 1000, 1),
        ("DT", "A", "  ", 1000, 1),
        ("DT", "A", "B", 0, 1),
        ("DT", "A", "B", -1, 1),
        ("DT", "A", "B", 1000, -1),
    ],
)
def test_phone_rejects_invalid(code, name, brand, battery, price):
    with pytest.raises(ValueError):
        DienThoai(code, name, brand, battery, price)


def test_phone_accepts_free_item():
    assert DienThoai("GIFT", "Quà tặng", "A", 1000, 0).gia_ban == 0
