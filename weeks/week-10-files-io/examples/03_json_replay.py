"""Serialize and inspect a course-local replay-shaped value."""

import json

replay = {
    "format": "COURSE LOCAL FORMAT",
    "production_compatibility": "NOT VUACOC PRODUCTION FORMAT",
    "turns": [{"turn": 1, "action": "wait"}],
}
encoded = json.dumps(replay, ensure_ascii=False, indent=2)
loaded = json.loads(encoded)
print(loaded["format"], len(loaded["turns"]))
