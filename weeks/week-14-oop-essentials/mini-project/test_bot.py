"""Kiểm thử tự động cho mini-project Bot chiến lược theo yêu cầu README."""

import pytest

from bot import Bot
from strategies import aggressive, balanced, defensive


def test_defensive_waits_when_opponent_near() -> None:
    bot = Bot(defensive)
    # Đối thủ cách 1 ô về phía phải
    assert bot.choose_action({"position": 5, "goal": 10, "opponent_position": 6}) == "wait"
    # Đối thủ cách 1 ô về phía trái
    assert bot.choose_action({"position": 5, "goal": 10, "opponent_position": 4}) == "wait"
    # Đối thủ cùng ô
    assert bot.choose_action({"position": 5, "goal": 10, "opponent_position": 5}) == "wait"


def test_balanced_moves_both_directions() -> None:
    bot = Bot(balanced)
    # Đích bên phải
    assert bot.choose_action({"position": 2, "goal": 8}) == "right"
    # Đích bên trái
    assert bot.choose_action({"position": 8, "goal": 2}) == "left"


def test_bot_waits_at_goal() -> None:
    for strategy in [defensive, balanced, aggressive]:
        bot = Bot(strategy)
        assert bot.choose_action({"position": 7, "goal": 7}) == "wait"


def test_runtime_strategy_swap() -> None:
    state = {"position": 4, "goal": 1, "opponent_position": 5}
    bot = Bot(defensive)
    assert bot.choose_action(state) == "wait"

    # Đổi chiến lược mà không thay đổi cấu trúc lớp Bot
    bot.strategy = balanced
    assert bot.choose_action(state) == "left"


def test_defensive_without_opponent_position() -> None:
    bot = Bot(defensive)
    state = {"position": 2, "goal": 6}
    assert bot.choose_action(state) == "right"


def test_state_immutability() -> None:
    state = {"position": 3, "goal": 0, "opponent_position": 4}
    original_state = state.copy()

    bot = Bot(defensive)
    _ = bot.choose_action(state)
    assert state == original_state, "Chiến lược không được làm biến đổi state đầu vào!"

    bot.strategy = balanced
    _ = bot.choose_action(state)
    assert state == original_state, "Chiến lược không được làm biến đổi state đầu vào!"

