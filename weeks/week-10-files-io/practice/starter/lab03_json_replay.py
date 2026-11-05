"""Lab 03: JSON course-local replay, parse is not schema validation.

COURSE LOCAL FORMAT — NOT VUACOC PRODUCTION FORMAT.
"""

import json
from pathlib import Path


FORMAT = "COURSE LOCAL FORMAT"
COMPAT = "NOT VUACOC PRODUCTION FORMAT"
ACTIONS = {"left", "right", "wait"}


def validate_replay(data: object) -> bool:
    """Required labels + turns list; each turn int >=1 and legal action."""
    # TODO: reject non-dict, missing/wrong labels, non-list turns.
    # TODO: each turn must be dict with type(turn) is int, turn >=1,
    #       action in ACTIONS and type(action) is str.
    raise NotImplementedError("Hoàn thiện validate_replay")


def save_replay(path: Path, replay: dict[str, object]) -> Path:
    """Validate before writing, UTF-8 JSON with ensure_ascii=False."""
    # TODO: invalid => ValueError; mkdir parent, json.dump via with.
    raise NotImplementedError("Hoàn thiện save_replay")


def load_replay(path: Path) -> dict[str, object]:
    """Read/parse/validate; JSONDecodeError or FileNotFoundError propagate."""
    # TODO: json.load via with; invalid schema => ValueError.
    raise NotImplementedError("Hoàn thiện load_replay")


if __name__ == "__main__":
    print("COURSE LOCAL FORMAT — NOT VUACOC PRODUCTION FORMAT")
