"""Save, load and inspect a deterministic course-local replay."""

import sys
from pathlib import Path
from tempfile import TemporaryDirectory

PROJECT = Path(__file__).resolve().parents[2]
if str(PROJECT) not in sys.path:
    sys.path.insert(0, str(PROJECT))

from baselines.forward_bot import choose_action as forward_bot  # noqa: E402
from baselines.wait_bot import choose_action as wait_bot  # noqa: E402
from local_arena.arena import run_match  # noqa: E402
from local_arena.replay import load_replay, save_replay  # noqa: E402

with TemporaryDirectory() as directory:
    path = save_replay(run_match(forward_bot, wait_bot), Path(directory) / "replay.json")
    replay = load_replay(path)
    print(replay["format"])
    print(replay["production_compatibility"])
    print(f"turns={len(replay['turns'])}")
