"""Reference Lab 03: validated course-local JSON replay (offline)."""

import json
from pathlib import Path


FORMAT = "COURSE LOCAL FORMAT"
COMPAT = "NOT VUACOC PRODUCTION FORMAT"
ACTIONS = {"left", "right", "wait"}


def validate_replay(data: object) -> bool:
    if not isinstance(data, dict):
        return False
    if (
        data.get("format") != FORMAT
        or data.get("production_compatibility") != COMPAT
        or not isinstance(data.get("turns"), list)
    ):
        return False
    for event in data["turns"]:
        if not isinstance(event, dict):
            return False
        if type(event.get("turn")) is not int or event["turn"] < 1:
            return False
        if type(event.get("action")) is not str or event["action"] not in ACTIONS:
            return False
    return True


def save_replay(path: Path, replay: dict[str, object]) -> Path:
    if not validate_replay(replay):
        raise ValueError("Replay schema không hợp lệ")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as stream:
        json.dump(replay, stream, ensure_ascii=False, indent=2)
    return path


def load_replay(path: Path) -> dict[str, object]:
    with path.open("r", encoding="utf-8") as stream:
        data = json.load(stream)
    if not validate_replay(data):
        raise ValueError("Replay schema không hợp lệ")
    return data


if __name__ == "__main__":
    print("COURSE LOCAL FORMAT — NOT VUACOC PRODUCTION FORMAT")
