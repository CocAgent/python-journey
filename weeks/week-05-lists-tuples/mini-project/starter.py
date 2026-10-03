"""Collection Workflow for Week 05: Lists, Tuples, Mutability & Unpacking."""

# Khởi tạo workflow với danh sách các tuple (title, status)
tasks = [("Learn lists", "done"), ("Observe mutability", "doing")]

# 1. Thêm công việc mới vào list
tasks.append(("Practice unpacking", "todo"))

# 2. Unpack một tuple để hiển thị title và status
first_title, first_status = tasks[0]
print(f"first={first_title}, status={first_status}")

# 3. Tạo alias và shallow copy để chứng minh mutability
alias_tasks = tasks
copied_tasks = tasks.copy()

# 4. Cập nhật một item trong list
tasks[1] = ("Observe mutability", "done")

# 5. Xóa một item khỏi list
removed_task = tasks.pop(0)
print(f"removed={removed_task}")

# 6. Thao tác qua alias và so sánh
alias_tasks.append(("Submit evidence", "todo"))

print(f"current={tasks}")
print(f"alias={alias_tasks}")
print(f"copy={copied_tasks}")
print(f"alias shares changes: {tasks == alias_tasks}")
print(f"copy remains isolated: {tasks != copied_tasks}")
