from planner import plan_task
from developer import develop
from reviewer import review


def run_pipeline(task: str) -> dict:
    """Run the three deterministic roles and return their evidence."""
    plan = plan_task(task)
    work = develop(plan)
    report = review(plan, work)
    return {"task": task.strip(), "plan": plan, "work": work, "report": report}


def main() -> None:
    task = input("Nhap yeu cau: ")
    try:
        result = run_pipeline(task)
    except ValueError as error:
        print(f"Loi: {error}")
        return
    print("\n[Planner]")
    for step in result["plan"]:
        print("-", step)
    print("\n[Developer - mo phong]")
    for item in result["work"]:
        print("-", item["step"], "=>", item["status"])
    print("\n[Reviewer]", result["report"])


if __name__ == "__main__":
    main()
