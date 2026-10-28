def review(plan: list[str], work: list[dict[str, str]]) -> dict:
    """Check that every planned step has a matching simulated result."""
    expected = [step for step in plan]
    actual = [item.get("step") for item in work]
    passed = bool(expected) and expected == actual and all(
        item.get("status") == "simulated" for item in work
    )
    return {"passed": passed, "checked": len(work), "mode": "offline simulation"}
