"""Exercise 03: inspect an offline HTTP fixture."""

from bot_course.http_foundation import parse_json_response

fixture = b'{"lesson": 13}'
# TODO: parse status 200 and assert lesson == 13.
# TODO: observe ValueError for status 500.
print(parse_json_response(200, fixture))
