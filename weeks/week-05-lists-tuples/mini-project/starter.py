"""Mini-project: Week 05 Collection Workflow."""

# Khởi tạo danh sách ban đầu gồm các task (title, status)
tasks = [("Learn lists", "done"), ("Observe mutability", "doing")]

# 1. Thêm (Add), Cập nhật (Update), và Xóa (Delete) item trong list
tasks.append(("Practice unpacking", "todo"))           # Thêm item mới
tasks[1] = ("Observe mutability", "done")              # Cập nhật status bằng cách gán tuple mới
removed_task = tasks.pop(0)                           # Xóa item đầu tiên và lấy ra

# 2. Unpack một tuple để hiển thị title và status
title, status = tasks[0]
print(f"Task hiện tại: '{title}' - Trạng thái: [{status}]")

# 3. Chứng minh sự khác nhau giữa alias và copy
alias_tasks = tasks
copied_tasks = tasks.copy()

# Thao tác thêm một item thông qua alias
alias_tasks.append(("Review week 05", "todo"))

# Kiểm tra kết quả
print(f"tasks (gốc):        {tasks}")
print(f"alias_tasks (alias): {alias_tasks}")
print(f"copied_tasks (copy): {copied_tasks}")

# Bằng chứng (Evidence):
# - tasks == alias_tasks: True (vì trỏ chung một vùng nhớ đối tượng)
# - tasks == copied_tasks: False (vì copied_tasks là bản sao nông riêng biệt, không bị ảnh hưởng)