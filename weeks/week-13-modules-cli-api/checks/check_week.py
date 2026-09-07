"""Offline behavior checks for Week 13."""

import sys
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
if str(WEEK_ROOT) not in sys.path:
    sys.path.insert(0, str(WEEK_ROOT))

from bot_course.adapter import course_local_action  # noqa: E402
from bot_course.http_foundation import (  # noqa: E402
    build_get_request,
    parse_json_response,
)

assert course_local_action({"position": 1, "goal": 4})["action"] == "right"
request = build_get_request("https://example.invalid/fixture")
assert request.method == "GET"
assert parse_json_response(200, b'{"ok": true}') == {"ok": True}
try:
    parse_json_response(503, b"{}")
except ValueError:
    pass
else:
    raise AssertionError("non-2xx response was accepted")
print("Week 13 solution checks: PASS")
