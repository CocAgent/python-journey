"""Exercise 03: JSON-compatible replay data."""

import json
from pathlib import Path

path = Path("replay.json")
replay = {
    "format": "COURSE LOCAL FORMAT",
    "production_compatibility": "NOT VUACOC PRODUCTION FORMAT",
    "turns": [],
}
# TODO: save replay with ensure_ascii=False and indent=2.
# TODO: load it and verify both labels before inspecting turns.
print(json.__name__, path, replay)
