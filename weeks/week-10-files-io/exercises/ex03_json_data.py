"""Exercise 03: JSON-compatible replay data."""

import json
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "replay.json"
replay = {
    "format": "COURSE LOCAL FORMAT",
    "production_compatibility": "NOT VUACOC PRODUCTION FORMAT",
    "turns": [],
}
# TODO: tạo thư mục cha trước khi ghi file.
path.parent.mkdir(parents=True, exist_ok=True)

# TODO: lưu replay với ensure_ascii=False và indent=2.
json_string = json.dumps(replay, ensure_ascii=False, indent=2)
path.write_text(json_string, encoding="utf-8")
print("✓ Đã lưu file replay dạng JSON thành công.\n")

# TODO: tải lại và kiểm tra cả hai nhãn trước khi đọc turns.
try:
    raw_content = path.read_text(encoding="utf-8")
    loaded_data = json.loads(raw_content)

    current_format = loaded_data.get("format")
    current_compatibility = loaded_data.get("production_compatibility")

    print("--- KIỂM TRA NHÃN DỮ LIỆU REPLAY ---")
    print(f"Nhãn định dạng: {current_format}")
    print(f"Nhãn tương thích: {current_compatibility}")

    if current_format == "COURSE LOCAL FORMAT" and current_compatibility == "NOT VUACOC PRODUCTION FORMAT":
        print("=> Trạng thái: Dữ liệu hợp lệ. Sẵn sàng xử lý danh sách lượt đi (turns).")
        turns_list = loaded_data.get("turns", [])
        print(f"=> Số lượng turns hiện tại: {len(turns_list)}")
    else:
        print("❌ Cảnh báo: File JSON chứa nhãn định dạng không khớp với yêu cầu khóa học!")

except FileNotFoundError:
    print("❌ Lỗi: File dữ liệu replay.json không tồn tại trên hệ thống!")
except json.JSONDecodeError as error:
    print(f"❌ Lỗi: File JSON bị sai cấu trúc hoặc bị hỏng dữ liệu! Chi tiết: {error}")
