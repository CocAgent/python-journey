"""Behavior checks for Week 14 composition and inheritance."""

import sys
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
if str(WEEK_ROOT) not in sys.path:
    sys.path.insert(0, str(WEEK_ROOT))

from solutions.oop_models import (  # noqa: E402
    Animal,
    Bot,
    Dog,
    Progress,
    aggressive,
    balanced,
    defensive,
)

state = {"position": 1, "opponent_position": 4, "goal": 4}
assert Progress(3, 4).percentage() == 75
assert str(Progress(3, 4)) == "Progress: 3/4 (75%)"
assert Bot(defensive).choose_action(state) == "right"
assert Bot(balanced).choose_action(state) == "right"
assert Bot(aggressive).choose_action(state) == "right"
reverse_state = {"position": 3, "opponent_position": 4, "goal": 0}
assert Bot(defensive).choose_action(reverse_state) == "wait"
assert Bot(balanced).choose_action(reverse_state) == "left"
assert Bot(aggressive).choose_action(reverse_state) == "left"
dog = Dog("Milo")
assert isinstance(dog, Animal)
assert dog.speak() == "Milo: woof"
print("Week 14 solution checks: PASS")
