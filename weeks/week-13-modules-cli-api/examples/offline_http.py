"""Inspect a neutral GET request and parse a static response offline."""

from bot_course.http_foundation import build_get_request, parse_json_response

request = build_get_request("https://example.invalid/learning")
fixture_body = b'{"topic": "http", "network_used": false}'

print(request.method, request.full_url)
print(parse_json_response(200, fixture_body))
