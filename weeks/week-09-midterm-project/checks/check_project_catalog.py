"""Kiểm tra catalog đề tài hiện hành và lưu chiểu nguồn Word gốc.

Chỉ kiểm tính nhất quán giáo trình, không chấm sản phẩm sinh viên.
Kiểm offline bằng thư viện chuẩn, phù hợp Python 3.12+.
"""

from __future__ import annotations

import re
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
CATALOG = WEEK_ROOT / "project-ideas" / "catalog-20-du-an.md"
ARCHIVE = WEEK_ROOT / "project-ideas" / "archive" / "original-word-sources-20.md"
RUBRIC = WEEK_ROOT / "project-ideas" / "rubric-10-diem.md"
INDUSTRY = WEEK_ROOT / "project-ideas" / "commerce-marketing-open-source.md"

# Provenance được niêm phong từ Word nguồn; KHÔNG phải recommended catalog.
ORIGINAL_WORD_SOURCES = (
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
ARCHIVE_ROW = re.compile(
    r"^\| (?P<id>\d{2}) \| (?P<name>[^|]+?) \| (?P<url>https://github[.]com/[^ |]+) \|$",
    re.MULTILINE,
)
SECTION = re.compile(r"^### (?P<id>\d{2}) · (?P<name>[^\n]+)$", re.MULTILINE)
RUBRIC_ROW = re.compile(r"^\| (?P<id>\d{2}) \| ", re.MULTILINE)
DETAIL_MARKERS = (
    "**MVP W09 (Python thuần):**",
    "**Input → output và trường hợp biên:**",
    "**Định hướng sau giữa kỳ:**",
)


BONUS_ROW = re.compile(
    r"^\| A01 \| \[CrewAI\]\((https://github[.]com/crewAIInc/crewAI)\) \|",
    re.MULTILINE,
)
BONUS_SECTION = re.compile(r"^### A01 · CrewAI$", re.MULTILINE)
BONUS_REQUIRED = (
    "**MVP W09 (Python thuần):**",
    "**Input → output và trường hợp biên:**",
    "**Định hướng sau giữa kỳ:**",
    "**An toàn và minh bạch:**",
)


def verify_optional_agent(text: str, core_urls: list[str]) -> list[str]:
    """CrewAI is one optional extension, never a replacement for the 20 core rows."""
    issues: list[str] = []
    crewai_url = "https://github.com/crewAIInc/crewAI"
    if len(BONUS_ROW.findall(text)) != 1:
        issues.append("Phải có đúng một dòng A01 CrewAI trong catalog")
    if len(BONUS_SECTION.findall(text)) != 1:
        issues.append("Phải có đúng một đề cương ### A01 · CrewAI")
    if crewai_url in core_urls:
        issues.append("CrewAI A01 không được đếm trùng vào 20 nguồn cốt lõi")
    match = BONUS_SECTION.search(text)
    if match:
        next_header = re.search(r"^## ", text[match.end():], re.MULTILINE)
        body = text[match.end():match.end() + next_header.start()] if next_header else text[match.end():]
        for marker in BONUS_REQUIRED:
            if marker not in body:
                issues.append(f"Đề cương CrewAI thiếu: {marker}")
    return issues


INDUSTRY_ROW = re.compile(
    r"^\| (?P<id>[CM]\d{2}) \| \[(?P<name>[^]]+)\]\((?P<url>https://github[.]com/[^)]+)\) \|",
    re.MULTILINE,
)
INDUSTRY_SECTION = re.compile(r"^### (?P<id>[CM]\d{2}) ·", re.MULTILINE)
INDUSTRY_REQUIRED = (
    "**Bài toán MVP W09:**",
    "**Input:**",
    "**Output:**",
    "**Biên/sai cần chứng minh:**",
    "**Sau W09 (tùy chọn):**",
)


def verify_industry_catalog(core_urls: list[str]) -> list[str]:
    """Keep the 20 core options sealed and separately validate the 13 industry choices."""
    if not INDUSTRY.is_file():
        return ["Thiếu phụ lục Commerce & Marketing"]
    text = INDUSTRY.read_text(encoding="utf-8")
    rows = INDUSTRY_ROW.findall(text)
    expected = [f"C{i:02d}" for i in range(1, 7)] + [
        f"M{i:02d}" for i in range(1, 8)
    ]
    issues: list[str] = []
    if [id_ for id_, _, _ in rows] != expected:
        issues.append("Phụ lục Commerce & Marketing phải có 6 nguồn C + 7 nguồn M")
    urls = [url for _, _, url in rows]
    if len(urls) != 13 or len(set(urls)) != 13:
        issues.append("Phụ lục phải có 13 URL GitHub không trùng")
    if set(urls) & set(core_urls):
        issues.append("Phụ lục lặp URL danh mục 20 nguồn cốt lõi")
    sections = list(INDUSTRY_SECTION.finditer(text))
    if [section.group("id") for section in sections] != expected:
        issues.append("Phụ lục thiếu 13 mục chi tiết C01–C06, M01–M07")
    else:
        for index, section in enumerate(sections):
            end = sections[index + 1].start() if index + 1 < len(sections) else len(text)
            detail = text[section.end():end]
            if not all(marker in detail for marker in INDUSTRY_REQUIRED):
                issues.append(f"Phụ lục {section.group('id')} thiếu MVP/input/output/edge/extension")
    return issues


def verify() -> list[str]:
    """Validate curricular evidence without requiring the old 20 as current picks."""
    issues: list[str] = []
    expected_ids = [f"{number:02d}" for number in range(1, 21)]

    if not CATALOG.is_file():
        return [f"Thiếu catalog: {CATALOG}"]
    text = CATALOG.read_text(encoding="utf-8")
    rows = CATALOG_ROW.findall(text)
    ids = [id_ for id_, _, _ in rows]
    urls = [url for _, _, url in rows]
    names = [name.casefold().strip() for _, name, _ in rows]

    if ids != expected_ids:
        issues.append("Danh mục hiện hành phải có đúng 20 dòng STT 01–20")
    if len(urls) != 20 or len(set(urls)) != 20:
        issues.append("Danh mục hiện hành phải có 20 URL GitHub khác nhau")
    issues.extend(verify_industry_catalog(urls))
    issues.extend(verify_optional_agent(text, urls))
    if len(set(names)) != 20:
        issues.append("Tên 20 repository không được trùng")
    if not all(url.count("/") == 4 for url in urls):
        issues.append("URL cần có dạng https://github.com/owner/repository")

    sections = list(SECTION.finditer(text))
    if [item.group("id") for item in sections] != expected_ids:
        issues.append("Phải có đủ 20 hướng dẫn MVP với heading 01–20")
    else:
        for index, item in enumerate(sections):
            end = sections[index + 1].start() if index + 1 < len(sections) else len(text)
            body = text[item.end():end]
            missing = [marker for marker in DETAIL_MARKERS if marker not in body]
            if missing:
                issues.append(f"MVP {item.group('id')} thiếu: {', '.join(missing)}")

    if "Bản này là danh mục được biên tập lại" not in text:
        issues.append("Phải ghi rõ catalog đã biên tập, không phải nguyên văn Word")
    if "archive/original-word-sources-20.md" not in text:
        issues.append("Catalog thiếu link tới lưu chiểu nguyên danh mục Word")

    if not ARCHIVE.is_file():
        issues.append("Thiếu lưu chiểu 20 tên/URL gốc trong tài liệu Word")
    else:
        historical = ARCHIVE_ROW.findall(ARCHIVE.read_text(encoding="utf-8"))
        if [id_ for id_, _, _ in historical] != expected_ids:
            issues.append("Lưu chiểu Word phải có đủ STT 01–20")
        if [(name, url) for _, name, url in historical] != list(ORIGINAL_WORD_SOURCES):
            issues.append("Lưu chiểu phải giữ đúng 20 tên/URL/thứ tự Word ban đầu")

    rubric = RUBRIC.read_text(encoding="utf-8")
    if RUBRIC_ROW.findall(rubric) != [f"{i:02d}" for i in range(1, 11)]:
        issues.append("Rubric phải có đúng 10 tiêu chí theo thứ tự 01–10")
    for marker in ("0 điểm", "0,5 điểm", "1 điểm", "Python 3.10+", "Python 3.12+"):
        if marker not in rubric:
            issues.append(f"Rubric thiếu diễn giải: {marker}")

    required = (
        "project-ideas/README.md",
        "project-ideas/catalog-20-du-an.md",
        "project-ideas/archive/original-word-sources-20.md",
        "project-ideas/commerce-marketing-open-source.md",
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
    print("Phụ lục tùy chọn: A01 CrewAI + 13 nguồn Commerce & Marketing")
    print("Catalog tuyển chọn khác lưu chiểu Word gốc; không chấm bài sinh viên.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
