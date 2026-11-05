"""Kiểm thử tự động cho mini-project Tuần 14 bằng pytest."""

from __future__ import annotations

from bot import Bot
from strategies import aggressive, balanced, defensive


def test_bot_defensive_waits_when_opponent_close() -> None:
    bot = Bot(defensive)
    # Đối thủ cách 1 ô bên phải
    assert bot.choose_action({"position": 2, "goal": 5, "opponent_position": 3}) == "wait"
    # Đối thủ trùng ô
    assert bot.choose_action({"position": 2, "goal": 5, "opponent_position": 2}) == "wait"
    # Đối thủ cách 1 ô bên trái
    assert bot.choose_action({"position": 2, "goal": 5, "opponent_position": 1}) == "wait"


def test_bot_defensive_moves_when_opponent_far() -> None:
    bot = Bot(defensive)
    assert bot.choose_action({"position": 1, "goal": 5, "opponent_position": 4}) == "right"


def test_bot_defensive_handles_missing_opponent_position() -> None:
    bot = Bot(defensive)
    assert bot.choose_action({"position": 3, "goal": 1}) == "left"


def test_bot_balanced_moves_both_directions() -> None:
    bot = Bot(balanced)
    assert bot.choose_action({"position": 1, "goal": 4}) == "right"
    assert bot.choose_action({"position": 6, "goal": 2}) == "left"


def test_bot_waits_at_goal() -> None:
    for strat in (defensive, balanced, aggressive):
        bot = Bot(strat)
        assert bot.choose_action({"position": 3, "goal": 3}) == "wait"


def test_strategy_swap_changes_behavior_without_modifying_bot() -> None:
    bot = Bot(defensive)
    state = {"position": 2, "goal": 5, "opponent_position": 3}
    assert bot.choose_action(state) == "wait"

    bot.strategy = balanced
    assert bot.choose_action(state) == "right"


def test_strategies_do_not_mutate_state() -> None:
    state = {"position": 2, "goal": 5, "opponent_position": 4}
    original = state.copy()
    bot = Bot(defensive)
    _ = bot.choose_action(state)
    assert state == original
