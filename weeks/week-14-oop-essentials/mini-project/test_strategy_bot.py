"""Tests for the Week 14 strategy-composition mini-project."""
import unittest

from strategy_bot import Bot, aggressive, balanced, defensive


class StrategyBotTests(unittest.TestCase):
    def test_balanced_moves_right_toward_higher_goal(self):
        self.assertEqual(Bot(balanced).choose_action({"position": 1, "goal": 4}), "right")

    def test_balanced_moves_left_toward_zero(self):
        self.assertEqual(Bot(balanced).choose_action({"position": 3, "goal": 0}), "left")

    def test_waits_when_already_at_goal(self):
        self.assertEqual(Bot(balanced).choose_action({"position": 2, "goal": 2}), "wait")

    def test_defensive_waits_when_opponent_is_adjacent(self):
        state = {"position": 3, "opponent_position": 4, "goal": 0}
        self.assertEqual(Bot(defensive).choose_action(state), "wait")

    def test_aggressive_strategy_can_be_injected(self):
        bot = Bot(aggressive)
        self.assertEqual(bot.choose_action({"position": 1, "goal": 4}), "right")


if __name__ == "__main__":
    unittest.main()
