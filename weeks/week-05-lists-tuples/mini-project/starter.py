"""Starter for the Week 05 Collection Workflow."""

tasks = [("Learn lists", "done"), ("Observe mutability", "doing")]

# 1. Thêm item
tasks.append(("Practice unpacking", "todo"))

# 2. Unpack một tuple
first_title, first_status = tasks[0]
print(f"Unpacked first task: title={first_title}, status={first_status}")

# 3. Chứng minh alias và copy khác nhau
alias_tasks = tasks
copied_tasks = tasks.copy()

# Cập nhật item (ảnh hưởng alias, không ảnh hưởng copy)
tasks[1] = ("Observe mutability", "done")

# 4. Xóa item
removed_task = tasks.pop()
print(f"Removed task: {removed_task[0]} - {removed_task[1]}")

print(f"Current tasks: {tasks}")
print(f"Alias tasks: {alias_tasks}")
print(f"Copied tasks: {copied_tasks}")
