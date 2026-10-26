"""Kiểm tra danh mục 20 dự án Word được chuyển vào Week 09.

Chỉ kiểm tra tính nhất quán của tài liệu giáo trình, không chấm bài sinh viên.
Dùng thư viện chuẩn để chạy trên Python 3.12+ mà không cài dependency mới.
"""

from __future__ import annotations

import re
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
CATALOG = WEEK_ROOT / "project-ideas" / "catalog-20-du-an.md"
RUBRIC = WEEK_ROOT / "project-ideas" / "rubric-10-diem.md"
EXPECTED_SOURCE = (
    ("FastAPI", "https://github.com/fastapi/fastapi"),
    ("Streamlit", "https://github.com/streamlit/streamlit"),
    ("Gradio", "https://github.com/gradio-app/gradio"),
    ("Apache Airflow", "https://github.com/apache/airflow"),
    ("Prefect", "https://github.com/PrefectHQ/prefect"),
    ("DVC", "https://github.com/iterative/dvc"),
    ("JupyterLab", "https://github.com/jupyterlab/jupyterlab"),
    ("Polars", "https://github.com/pola-rs/polars"),
    ("PyTorch", "https://github.com/pytorch/pytorch"),
    ("Transformers (Hugging Face)", "https://github.com/huggingface/transformers"),
    ("LangGraph", "https://github.com/langchain-ai/langgraph"),
    ("CrewAI", "https://github.com/crewAIInc/crewAI"),
    ("ONNX Runtime", "https://github.com/microsoft/onnxruntime"),
    ("OpenVINO", "https://github.com/openvinotoolkit/openvino"),
    ("llama.cpp", "https://github.com/ggml-org/llama.cpp"),
    ("TensorFlow Lite Micro (tflite-micro)", "https://github.com/tensorflow/tflite-micro"),
    ("ROS 2", "https://github.com/ros2/ros2"),
    ("PyBullet (Bullet3)", "https://github.com/bulletphysics/bullet3"),
    ("Pygame", "https://github.com/pygame/pygame"),
    ("Panda3D", "https://github.com/panda3d/panda3d"),
)
CATALOG_ROW = re.compile(
    r"^\| (?P<id>\d{2}) \| \[(?P<name>[^]]+)\]\((?P<url>https://github[.]com/[^)]+)\) \|",
    re.MULTILINE,
)
RUBRIC_ROW = re.compile(r"^\| (?P<id>\d{2}) \| ", re.MULTILINE)


def verify() -> list[str]:
    """Trả danh sách sai lệch; không tự sửa tài liệu sinh viên."""
    issues: list[str] = []
    text = CATALOG.read_text(encoding="utf-8")
    rows = CATALOG_ROW.findall(text)
    actual = [(name, url) for _, name, url in rows]

    if actual != list(EXPECTED_SOURCE):
        issues.append("Danh mục khác 20 tên/URL và thứ tự từ tài liệu gốc")
    if [id_ for id_, _, _ in rows] != [f"{n:02d}" for n in range(1, 21)]:
        issues.append("STT dự án phải đúng 01–20, không trùng hoặc thiếu")
    if len(set(url for _, url in actual)) != 20:
        issues.append("Phải có 20 URL GitHub gốc khác nhau")

    rubric = RUBRIC.read_text(encoding="utf-8")
    scores = RUBRIC_ROW.findall(rubric)
    if scores != [f"{n:02d}" for n in range(1, 11)]:
        issues.append("Rubric phải có đúng 10 tiêu chí theo thứ tự 01–10")
    for text_label in ("0 điểm", "0,5 điểm", "1 điểm", "Python 3.10+", "Python 3.12+"):
        if text_label not in rubric:
            issues.append(f"Rubric thiếu diễn giải: {text_label}")

    # Kiểm tra riêng các đường dẫn liên quan Track C; checker chính của repo
    # vẫn kiểm tra toàn bộ Markdown links trên tất cả các tuần.
    required = (
        "project-ideas/README.md",
        "project-ideas/catalog-20-du-an.md",
        "project-ideas/rubric-10-diem.md",
        "project-ideas/phieu-de-xuat-nhom.md",
        "tracks/open-source-inspired.md",
    )
    for relative in required:
        if not (WEEK_ROOT / relative).is_file():
            issues.append(f"Thiếu file: {relative}")
    return issues


def main() -> int:
    issues = verify()
    if issues:
        print("Week 09 project catalog: FAIL")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Week 09 project catalog: PASS — 20 nguồn, 10 tiêu chí, đủ tài liệu")
    print("Chỉ kiểm tra giáo trình; KHÔNG chấm bài sinh viên.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
