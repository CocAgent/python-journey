"""Predict JSON parse vs schema validation, using temporary UTF-8 files."""

import json
from pathlib import Path
from tempfile import TemporaryDirectory


FORMAT = "COURSE LOCAL FORMAT"
COMPAT = "NOT VUACOC PRODUCTION FORMAT"


def is_valid_replay(data: object) -> bool:
    if not isinstance(data, dict):
        return False
    return (
        data.get("format") == FORMAT
        and data.get("production_compatibility") == COMPAT
        and isinstance(data.get("turns"), list)
    )


def main() -> None:
    replay = {
        "format": FORMAT,
        "production_compatibility": COMPAT,
        "turns": [{"turn": 1, "action": "wait"}],
    }
    with TemporaryDirectory() as directory:
        root = Path(directory)
        saved = root / "replay.json"
        saved.write_text(json.dumps(replay, ensure_ascii=False), encoding="utf-8")
        loaded = json.loads(saved.read_text(encoding="utf-8"))
        print(f"Round-trip valid: {is_valid_replay(loaded)}")
        print(f"Turns: {len(loaded['turns'])}")
        print(f"Top-level type: {type(loaded).__name__}")

        # Valid JSON syntax does not mean correct application schema.
        print(f"JSON list accepted by parser: {json.loads('[]') == []}")
        print(f"JSON list valid as replay: {is_valid_replay(json.loads('[]'))}")
        bad = root / "broken.json"
        bad.write_text("{broken", encoding="utf-8")
        try:
            json.loads(bad.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("Malformed JSON: JSONDecodeError (expected)")


if __name__ == "__main__":
    main()
