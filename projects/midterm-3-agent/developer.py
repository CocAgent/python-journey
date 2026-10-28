def develop(plan: list[str]) -> list[dict[str, str]]:
    """Produce a transparent, simulated development log."""
    if not plan:
        raise ValueError("Ke hoach khong duoc rong")
    return [{"step": step, "status": "simulated"} for step in plan]
