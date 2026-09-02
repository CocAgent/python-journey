"""Behavior checks for official Week 10 solutions."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from tempfile import TemporaryDirectory

SOLUTIONS = Path(__file__).resolve().parents[1] / "solutions"


def load(name: str):
    path = SOLUTIONS / name
    spec = spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    text = load("ex01_read_write_sol.py")
    csv_data = load("ex02_csv_data_sol.py")
    json_data = load("ex03_json_data_sol.py")
    with TemporaryDirectory() as directory:
        root = Path(directory)
        assert text.load_lines(text.save_text(root / "a.txt", ["Một", "Hai"])) == [
            "Một",
            "Hai",
        ]
        rows = [{"bot": "student", "wins": 2}]
        assert csv_data.load_rows(csv_data.save_rows(root / "a.csv", rows)) == [
            {"bot": "student", "wins": "2"}
        ]
        payload = {"format": "COURSE LOCAL FORMAT", "turns": []}
        assert json_data.load_json(json_data.save_json(root / "a.json", payload)) == payload
    print("Week 10 solution checks: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
