"""Starter for the Week 05 Collection Workflow."""

tasks = [("Learn lists", "done"), ("Observe mutability", "doing")]
tasks.append(("Practice unpacking", "todo"))

first_title, first_status = tasks[0]
print(f"first={first_title}, status={first_status}")

copied_tasks = tasks.copy()
tasks[1] = ("Observe mutability", "done")

print(f"current={tasks}")
print(f"copy={copied_tasks}")
