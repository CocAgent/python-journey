"""Course-local serialization boundary, not a production adapter."""

from bot_course.core import choose_action


def course_local_action(payload: dict[str, int]) -> dict[str, str]:
    action = choose_action(payload["position"], payload["goal"])
    return {
        "format": "COURSE LOCAL FORMAT",
        "production_compatibility": "NOT VUACOC PRODUCTION FORMAT",
        "action": action,
    }
