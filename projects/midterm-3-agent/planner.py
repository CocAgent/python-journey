def plan_task(task: str) -> list[str]:
    """Break a nonempty task into three verifiable steps."""
    if not isinstance(task, str) or not task.strip():
        raise ValueError("Yeu cau khong duoc rong")
    task = task.strip()
    return [f"Phan tich: {task}", "Xay dung demo Python nho", "Kiem thu va ghi bao cao"]
