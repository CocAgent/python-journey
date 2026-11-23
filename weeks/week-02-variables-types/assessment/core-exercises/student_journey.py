"""Friendly, offline Week 02 learner journey. No third-party packages or uploads.

Run only code you wrote/trust locally: the underlying subprocess is NOT a sandbox.
"""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

from autograde_w02 import ROOT, WEEK, grade

REPO = WEEK.parents[1]
DEFAULT_REPORT = REPO / ".learner-output" / "week02-journey.html"

STAGES = (
    ("01", "Chiếc ba lô biến", "Đặt tên và quan sát dữ liệu"),
    ("02", "Phép thuật chuyển kiểu", "Từ văn bản đến phép tính"),
    ("03", "Xưởng máy tính mini", "Biến dữ liệu thành kết quả"),
)

# Three levels, tied to the SAME ten mandatory TODOs. Not additional exercises.
HINTS: dict[str, tuple[str, str, str]] = {
    "W02.EX01.PROFILE": (
        "Mỗi biến cần mang một loại dữ liệu khác nhau.",
        "Quan sát kết quả type() cho ten, tuoi, diem_tb, dang_hoc.",
        "Hãy in cả giá trị và kiểu của từng biến; chú ý bool khác chuỗi 'True'.",
    ),
    "W02.EX01.SWAP": (
        "Giá trị của a và b cần đổi chỗ nhưng không thêm biến thứ ba.",
        "Python cho phép gán nhiều biến cùng lúc.",
        "Thử a, b = b, a sau khi khởi tạo đúng 10 và 20.",
    ),
    "W02.EX01.AUG": (
        "Bắt đầu từ x = 100 và thay đổi x qua bốn bước.",
        "Quan sát sự khác nhau giữa phép toán thường và phép gán tăng cường.",
        "Dùng +=, -=, *=, //= theo thứ tự và print(x) sau mỗi bước.",
    ),
    "W02.EX02.TEXT": (
        "Chuỗi '42' chưa phải là số.",
        "Hãy chuyển str sang int trước khi cộng.",
        "int(so_text) + 8 cần tạo ra giá trị 50.",
    ),
    "W02.EX02.PI": (
        "Chuyển float thành int khác với làm tròn.",
        "Hãy gọi int() trên biến pi, không chỉ in một số bất kỳ.",
        "int(3.14159) cho kết quả 3.",
    ),
    "W02.EX02.BOOL": (
        "Thử đoán tính đúng/sai của 0, 1, chuỗi và danh sách.",
        "Giá trị rỗng thường được coi là False.",
        "In sáu biểu thức bool() theo đúng thứ tự trong bài.",
    ),
    "W02.EX02.BMI": (
        "input() nhận chuỗi; tính BMI cần số thực.",
        "Nhập chiều cao (m) rồi cân nặng (kg), đổi bằng float().",
        "BMI = cân nặng / (chiều cao ** 2); in một chữ số thập phân.",
    ),
    "W02.EX03.FOUR": (
        "Dùng hai đầu vào để tạo bốn kết quả khác nhau.",
        "Chuyển hai chuỗi nhập vào thành số trước khi + - * /.",
        "In tổng, hiệu, tích, thương đúng thứ tự cho cả số thập phân và số âm.",
    ),
    "W02.EX03.CIRCLE": (
        "Một bán kính dùng để tính hai đại lượng khác nhau.",
        "Diện tích phụ thuộc bình phương bán kính, chu vi phụ thuộc bán kính.",
        "Với pi=3.14159: diện tích pi*r**2, chu vi 2*pi*r.",
    ),
    "W02.EX03.DISCOUNT": (
        "Giảm giá là một phần của giá gốc, không phải số tiền cố định.",
        "Tính số tiền giảm từ phần trăm trên giá nhập.",
        "Giá còn lại = giá gốc * (1 - phần trăm / 100).",
    ),
}


def safe(value: object) -> str:
    return html.escape(str(value), quote=True)


def render_report(result: dict) -> str:
    """Render a single self-contained, offline HTML page with no JS/network."""
    reference = result["mode"] == "reference"
    completed = sum(
        int(c["passed"]) for task in result["tasks"] for c in task["criteria"]
    )
    total = sum(len(task["criteria"]) for task in result["tasks"])
    progress = round(100 * completed / total) if total else 0
    cards = []

    for index, task in enumerate(result["tasks"]):
        number, title, subtitle = STAGES[index]
        criteria = task["criteria"]
        done = sum(int(item["passed"]) for item in criteria)
        earned = sum(item["earned"] for item in criteria)
        maximum = sum(item["maximum"] for item in criteria)
        stage_state = "Hoàn thành" if done == len(criteria) else "Đang luyện tập"
        detail_rows = []
        for item in criteria:
            cid = item["id"]
            if item["passed"]:
                status, cls = "ĐẠT", "passed"
            elif item["reason"].startswith("REVIEW:"):
                status, cls = "CẦN XEM LẠI", "review"
            else:
                status, cls = "THỬ LẠI", "retry"
            tips = HINTS.get(cid, ("Đọc lại đề gốc.",) * 3)
            hints = "".join(
                '<details class="hint"><summary>Gợi ý mức '
                + str(level) + '</summary><p>' + safe(tip) + '</p></details>'
                for level, tip in enumerate(tips, 1)
            ) if not item["passed"] else ""
            detail_rows.append(
                '<article class="todo"><div class="todo-head">'
                '<span class="tag ' + cls + '">' + status + '</span>'
                '<strong>TODO ' + safe(item["todo"]) + '</strong>'
                '<span class="points">' + f'{item["earned"]:.2f}/{item["maximum"]:.2f}'
                + ' điểm</span></div>'
                '<div class="criterion">' + safe(cid) + '</div>'
                '<p>' + safe(item["reason"]) + '</p>' + hints + '</article>'
            )
        filename = safe(task["file"])
        cards.append(
            '<section class="stage" aria-label="Chặng ' + number + '">'
            '<header class="stage-head"><div class="number">' + number + '</div>'
            '<div><h2>' + safe(title) + '</h2><p>' + safe(subtitle)
            + '</p></div></header><div class="stage-stats"><span>'
            + safe(stage_state) + ' · ' + str(done) + '/' + str(len(criteria))
            + ' TODO</span><strong>' + f'{earned:.2f}/{maximum:.2f}'
            + ' điểm</strong></div>'
            '<p class="path">Bài gốc: <a href="../weeks/week-02-variables-types/exercises/'
            + filename + '">' + filename + '</a></p>'
            + "".join(detail_rows) + '</section>'
        )

    mode_label = (
        "MẪU GIẢNG VIÊN — không phải thành tích học viên"
        if reference else "KẾT QUẢ TỰ LUYỆN TRÊN MÁY CÁ NHÂN"
    )
    css = """
    :root{color-scheme:light;--ink:#172843;--muted:#59687d;--blue:#245bd0;
      --line:#dfe8f3;--good:#166d50;--warn:#87531b}
    *{box-sizing:border-box}body{margin:0;background:#f5f8fe;color:var(--ink);
      font-family:system-ui,-apple-system,'Segoe UI',sans-serif;line-height:1.55}
    .wrap{max-width:1040px;margin:auto;padding:20px}
    .hero{background:linear-gradient(120deg,#123a82,#325ec2 58%,#687ce8);
      color:#fff;border-radius:24px;padding:30px;margin:20px 0}
    .eyebrow{letter-spacing:.09em;font-size:.78rem;font-weight:750;opacity:.94}
    h1{font-size:clamp(1.7rem,4vw,2.5rem);margin:10px 0}h2{margin:0;font-size:1.3rem}
    .hero p{color:#edf2ff;max-width:700px}
    .metrics{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;
      margin:20px 0}.metric{background:rgba(255,255,255,.14);border-radius:14px;
      padding:14px}.metric strong{display:block;font-size:1.8rem}
    .track{background:#dbe6fc;border-radius:999px;height:12px;overflow:hidden}
    .fill{height:100%;background:#73e6bc;border-radius:inherit}
    .small{font-size:.86rem;color:var(--muted)}
    .stage{background:#fff;border:1px solid var(--line);border-radius:22px;
      padding:22px;margin:18px 0;box-shadow:0 8px 28px rgba(24,50,96,.05)}
    .stage-head{display:flex;gap:15px;align-items:center}
    .number{background:#e7efff;color:#174aa2;border-radius:15px;padding:12px 17px;
      font-weight:800}.stage-head p{margin:3px 0;color:var(--muted)}
    .stage-stats{display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap;
      padding:14px 0;margin-top:14px;border-bottom:1px solid var(--line)}
    .path{font-size:.86rem;color:var(--muted);overflow-wrap:anywhere}
    a{color:var(--blue)}.todo{border-top:1px solid var(--line);padding:14px 0}
    .todo-head{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
    .points{margin-left:auto;color:var(--muted);font-variant-numeric:tabular-nums}
    .tag{font-size:.7rem;font-weight:800;padding:5px 9px;border-radius:999px}
    .tag.passed{color:#07563b;background:#dcf9e9}
    .tag.retry{color:#88460b;background:#fff1dc}
    .tag.review{color:#683591;background:#f1e8ff}
    .criterion{color:var(--muted);font-size:.74rem;overflow-wrap:anywhere}
    .todo p{margin:7px 0;color:#485a72}.hint{margin-top:7px;border:1px solid #d7e3f5;
      border-radius:10px;padding:8px 12px;background:#f7faff}
    summary{cursor:pointer;font-weight:600;color:#234a87}
    .notice{padding:18px;border:1px solid var(--line);border-radius:16px;
      background:#fff;margin:20px 0}.footer{color:var(--muted);padding:20px 0}
    :focus-visible{outline:3px solid #ffba4b;outline-offset:3px}
    @media(max-width:560px){.wrap{padding:12px}.hero{padding:22px}
      .stage{padding:16px}.metrics{grid-template-columns:1fr 1fr}}
    @media print{body{background:#fff}.hero{color:#172843;background:#fff;
      border:1px solid #dfe8f3}.hero p{color:#172843}.hint{break-inside:avoid}}
    """
    return (
        '<!doctype html><html lang="vi"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="referrer" content="no-referrer">'
        '<title>Week 02 — Hành trình tự luyện Python</title><style>'
        + css + '</style></head><body><main class="wrap">'
        '<div class="hero"><div class="eyebrow">' + safe(mode_label)
        + '</div><h1>Hành trình khám phá Python · Tuần 02</h1>'
        '<p>Ba bài tập gốc, mười TODO bắt buộc. Học từ lỗi sai, '
        'thử lại theo nhịp độ của mình.</p>'
        '<div class="metrics"><div class="metric">Điểm tự luyện'
        '<strong>' + f'{result["auto_score"]:.2f}/10' + '</strong></div>'
        '<div class="metric">TODO hoàn thành<strong>' + str(completed)
        + '/' + str(total) + '</strong></div></div>'
        '<div class="track" role="progressbar" aria-label="Tiến độ TODO" '
        'aria-valuenow="' + str(completed) + '" aria-valuemin="0" '
        'aria-valuemax="' + str(total) + '"><div class="fill" style="width:'
        + str(progress) + '%"></div></div></div>'
        '<div class="notice"><strong>Đây là điểm tự luyện, không phải điểm học phần.</strong>'
        '<p>Chỉ kiểm TODO bắt buộc trong 3 file exercises/. Phần thử thách, '
        'practice và mini-project không tính điểm. Khi mã đúng nhưng máy '
        'báo THỬ LẠI/CẦN XEM LẠI, nhờ giảng viên xem phương án giải.</p>'
        '<p class="small">Báo cáo lưu ngoại tuyến; không tự tải lên Internet, '
        'không chứa mã nguồn, tên hay đầu ra cá nhân của sinh viên.</p></div>'
        + "".join(cards)
        + '<div class="footer">Vòng tự học: Đọc yêu cầu → Dự đoán → Viết mã '
        '→ Chạy tự kiểm → Mở gợi ý nếu cần → Sửa và thử lại.'
        '<p>Đã kiểm tự động: ' + safe(result["rubric_sha256"][:12])
        + ' (mã kiểm tra rubric). official_score: null.</p></div>'
        '</main></body></html>'
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Hành trình tự luyện Week 02 — báo cáo HTML ngoại tuyến"
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--student", action="store_true", help="Chấm bài gốc của em")
    mode.add_argument("--reference", action="store_true", help="Chỉ dành cho người bảo trì")
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--json-out", type=Path, help="Báo cáo JSON không chứa output cá nhân")
    args = parser.parse_args(argv)

    reference = args.reference
    source = ROOT / "fixtures" / "reference" if reference else WEEK / "exercises"
    try:
        result = grade(source, "reference" if reference else "student")
        target = args.report.resolve()
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render_report(result), encoding="utf-8")
        if args.json_out:
            json_target = args.json_out.resolve()
            json_target.parent.mkdir(parents=True, exist_ok=True)
            json_target.write_text(
                json.dumps(result, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
    except (OSError, ValueError) as exc:
        parser.exit(2, f"Lỗi xuất báo cáo: {exc}\n")

    print("=== HÀNH TRÌNH WEEK 02 · TỰ LUYỆN ===")
    print("KẾT QUẢ BỘ MẪU (không phải điểm sinh viên)" if reference else "BÀI GỐC CỦA EM")
    for task in result["tasks"]:
        passed = sum(int(c["passed"]) for c in task["criteria"])
        count = len(task["criteria"])
        print(f"  {task['title']}: {passed}/{count} TODO đạt")
        for check in task["criteria"]:
            if not check["passed"]:
                state = "XEM LẠI" if check["reason"].startswith("REVIEW:") else "THỬ LẠI"
                print(f"    {state} · TODO {check['todo']}: {check['reason']}")
    print(f"Điểm tự luyện: {result['auto_score']:.2f}/10 (không phải điểm chính thức)")
    print(f"Báo cáo HTML: {target}")
    print("Mở file HTML trong trình duyệt, bấm vào từng mức gợi ý khi cần.")
    return 0 if result["auto_score"] == 10 else 1


if __name__ == "__main__":
    raise SystemExit(main())
