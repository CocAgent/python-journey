"""Test hành vi composition qua hai module, không chỉ test import."""

from oop_team.bot import Bot
from oop_team.strategies import balanced, defensive


def test_swap_changes_action_on_same_bot() -> None:
    state = {"position": 3, "goal": 0, "opponent_position": 4}
    original = state.copy()
    bot = Bot(defensive)
    assert bot.choose_action(state) == "wait"
    bot.strategy = balanced
    assert bot.choose_action(state) == "left"
    assert state == original


def test_balanced_moves_both_ways_and_waits_at_goal() -> None:
    bot = Bot(balanced)
    assert bot.choose_action({"position": 0, "goal": 4}) == "right"
    assert bot.choose_action({"position": 4, "goal": 0}) == "left"
    assert bot.choose_action({"position": 4, "goal": 4}) == "wait"


def test_defensive_without_opponent_data() -> None:
    assert Bot(defensive).choose_action({"position": 4, "goal": 0}) == "left"
