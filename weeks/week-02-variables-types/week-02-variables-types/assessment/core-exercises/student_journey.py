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


RANKS = ((9, "Xuất sắc"), (8, "Giỏi"), (6.5, "Khá"), (0, "Cần cải thiện"))


def rank_of(score: float) -> str:
    return next(label for floor, label in RANKS if score >= floor)


REPORT_CSS = """
:root{--bg:#f6f1e7;--card:#fffdf8;--ink:#1f2a2e;--muted:#6b6a60;--line:#e6dcc8;
  --accent:#0f766e;--soft:#d9f0ec;--track:#e9e1cf;--ok:#15803d;--okbg:#dcfce7;
  --retry:#b45309;--retrybg:#fef3c7;--review:#6d28d9;--reviewbg:#ede9fe}
@media(prefers-color-scheme:dark){:root{--bg:#10181a;--card:#172326;--ink:#e8efe9;
  --muted:#9db0aa;--line:#2a3b3d;--accent:#2dd4bf;--soft:#12332f;--track:#27393b;
  --ok:#4ade80;--okbg:#14351f;--retry:#fbbf24;--retrybg:#3a2a0a;--review:#c4b5fd;--reviewbg:#2b2150}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);line-height:1.55;
  font-family:'Segoe UI Variable Text','Segoe UI',system-ui,-apple-system,Roboto,'Helvetica Neue',Arial,'Noto Sans',sans-serif;font-variant-numeric:lining-nums}
h1,h2{font-weight:800;letter-spacing:-.02em;margin:0}
.page{max-width:980px;margin:auto;padding:24px 18px 48px}
.sheet{display:grid;grid-template-columns:200px 1fr;gap:28px;align-items:center;
  background:var(--card);border:1px solid var(--line);border-radius:6px 28px 6px 28px;
  padding:28px 32px;box-shadow:0 14px 34px -22px rgba(0,0,0,.35)}
.stamp{font-size:.74rem;font-weight:800;letter-spacing:.12em;color:var(--accent)}
.sheet h1{font-size:clamp(1.6rem,4vw,2.3rem);margin:8px 0}
.sheet p{margin:4px 0;color:var(--muted)}
@property --p{syntax:'<number>';inherits:false;initial-value:0}
.ring{--p:0;animation:ringIn 1.2s ease-out both;box-shadow:0 10px 24px -14px var(--accent);width:180px;height:180px;border-radius:50%;display:grid;place-items:center;
  background:conic-gradient(#0f766e,#14b8a6 60%,#f59e0b calc(var(--p)*1%),var(--track) 0)}@keyframes ringIn{from{--p:0}}
.ring>div{width:140px;height:140px;border-radius:50%;background:var(--card);
  display:grid;place-content:center;text-align:center}
.ring strong{font-weight:800;font-size:2.4rem;line-height:1;font-variant-numeric:lining-nums tabular-nums}
.ring span{font-size:.78rem;color:var(--muted)}
.chips{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}
.cell:hover{transform:translateY(-3px)}
details.stage{transition:box-shadow .2s}details.stage:hover{box-shadow:0 14px 28px -20px rgba(15,60,55,.5)}
.bar i{background:linear-gradient(90deg,#0f766e,#14b8a6)}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
.chip{background:var(--soft);color:var(--accent);border-radius:999px;padding:5px 13px;
  font-size:.82rem;font-weight:700}
.matrix{display:flex;gap:6px;flex-wrap:wrap;margin:22px 0 6px}
.cell{transition:transform .15s;width:42px;height:42px;border-radius:10px;display:grid;place-items:center;
  font-weight:800;font-size:.85rem;text-decoration:none;border:2px solid transparent}
.cell.passed{background:var(--okbg);color:var(--ok)}
.cell.retry{background:var(--retrybg);color:var(--retry)}
.cell.review{background:var(--reviewbg);color:var(--review)}
.legend{font-size:.8rem;color:var(--muted)}
.note{margin:18px 0;padding:14px 18px;border-left:5px solid var(--accent);
  background:var(--card);border-radius:0 12px 12px 0;border:1px solid var(--line);
  border-left:5px solid var(--accent)}
.note p{margin:4px 0;color:var(--muted);font-size:.9rem}
details.stage{background:var(--card);border:1px solid var(--line);border-radius:16px;
  margin:14px 0;overflow:hidden}
details.stage>summary{list-style:none;cursor:pointer;display:grid;
  grid-template-columns:auto 1fr 170px;gap:16px;align-items:center;padding:16px 20px}
details.stage>summary::-webkit-details-marker{display:none}
.no{font-size:1.6rem;color:var(--accent);font-weight:800;font-variant-numeric:lining-nums}
.stage h2{font-size:1.15rem}.stage small{color:var(--muted)}
.bar{height:9px;border-radius:99px;background:var(--track);overflow:hidden}
.bar i{display:block;height:100%;background:var(--accent);border-radius:inherit}
.sum-score{text-align:right;font-variant-numeric:tabular-nums;font-weight:700}
.rows{margin:0;padding:0 20px 14px;list-style:none}
.row{display:grid;grid-template-columns:96px 1fr 110px;gap:6px 14px;
  padding:13px 0;border-top:1px dashed var(--line);align-items:center}
.tag{font-size:.7rem;font-weight:800;padding:4px 10px;border-radius:6px;text-align:center}
.tag.passed{color:var(--ok);background:var(--okbg)}
.tag.retry{color:var(--retry);background:var(--retrybg)}
.tag.review{color:var(--review);background:var(--reviewbg)}
.cid{font-size:.74rem;color:var(--muted);font-family:ui-monospace,Consolas,monospace}
.pts{text-align:right;font-variant-numeric:tabular-nums}
.why{grid-column:2/-1;margin:0;color:var(--muted);font-size:.9rem}
.hints{grid-column:1/-1;display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.hints details{border:1px solid var(--line);border-radius:10px;padding:7px 11px;background:var(--bg)}
.hints summary{cursor:pointer;font-weight:700;font-size:.84rem;color:var(--accent)}
.hints p{margin:6px 0 2px;font-size:.88rem}
.src{padding:0 20px 6px;font-size:.84rem;color:var(--muted)}
a{color:var(--accent)}
.next{background:var(--soft);border-radius:14px;padding:14px 18px;margin:18px 0}
.next h2{font-size:1.05rem;margin-bottom:6px}
.foot{color:var(--muted);font-size:.82rem;padding-top:14px}
:focus-visible{outline:3px solid #f59e0b;outline-offset:2px}
@media(max-width:640px){.sheet{grid-template-columns:1fr;justify-items:center;text-align:center}
  details.stage>summary{grid-template-columns:auto 1fr}.sum-score{grid-column:1/-1;text-align:left}
  .row{grid-template-columns:80px 1fr}.pts{text-align:left}.why{grid-column:1/-1}
  .hints{grid-template-columns:1fr}}
@media print{body{background:#fff}details.stage{break-inside:avoid}.hints details{break-inside:avoid}}
"""


def render_report(
    result: dict,
    *,
    exercise_href_prefix: str | None = "../weeks/week-02-variables-types/exercises/",
) -> str:
    """Render the gradebook-style report: one self-contained page, no JS/network."""
    reference = result["mode"] == "reference"
    all_items = [c for t in result["tasks"] for c in t["criteria"]]
    completed = sum(int(c["passed"]) for c in all_items)
    total = len(all_items)
    score = result["auto_score"]
    percent = round(100 * score / 10)

    def state(item: dict) -> tuple[str, str]:
        if item["passed"]:
            return "ĐẠT", "passed"
        if item["reason"].startswith("REVIEW:"):
            return "CẦN XEM LẠI", "review"
        return "THỬ LẠI", "retry"

    matrix, stages, todo_next = [], [], []
    for index, task in enumerate(result["tasks"]):
        number, title, subtitle = STAGES[index]
        criteria = task["criteria"]
        done = sum(int(c["passed"]) for c in criteria)
        earned = sum(c["earned"] for c in criteria)
        maximum = sum(c["maximum"] for c in criteria)
        rows = []
        for item in criteria:
            status, cls = state(item)
            anchor = f"t-{number}-{item['todo']}"
            matrix.append(
                f'<a class="cell {cls}" href="#{anchor}" title="{safe(item["id"])}">'
                f'{number[-1]}.{safe(item["todo"])}</a>'
            )
            hints = ""
            if not item["passed"]:
                tips = HINTS.get(item["id"], ("Đọc lại đề gốc.",) * 3)
                hints = '<div class="hints">' + "".join(
                    f'<details><summary>Gợi ý mức {n}</summary><p>{safe(tip)}</p></details>'
                    for n, tip in enumerate(tips, 1)
                ) + "</div>"
                todo_next.append(f"{number}.{item['todo']} · {item['id']}")
            rows.append(
                f'<li class="row" id="{anchor}"><span class="tag {cls}">{status}</span>'
                f'<div><strong>TODO {safe(item["todo"])}</strong> '
                f'<span class="cid">{safe(item["id"])}</span></div>'
                f'<span class="pts">{item["earned"]:.2f}/{item["maximum"]:.2f}</span>'
                f'<p class="why">{safe(item["reason"])}</p>{hints}</li>'
            )
        filename = safe(task["file"])
        src = (
            f'<a href="{safe(exercise_href_prefix)}{filename}">{filename}</a>'
            if exercise_href_prefix is not None else filename
        )
        width = round(100 * earned / maximum) if maximum else 0
        stages.append(
            f'<details class="stage" id="stage-{number}" open>'
            f'<summary><span class="no">{number}</span><div><h2>{safe(title)}</h2>'
            f'<small>{safe(subtitle)} · {done}/{len(criteria)} TODO</small></div>'
            f'<div><div class="sum-score">{earned:.2f}/{maximum:.2f}</div>'
            f'<div class="bar"><i style="width:{width}%"></i></div></div></summary>'
            f'<p class="src">Bài gốc: {src}</p><ul class="rows">{"".join(rows)}</ul></details>'
        )

    stamp = (
        "MẪU GIẢNG VIÊN — không phải thành tích học viên"
        if reference else "BẢNG ĐIỂM TỰ LUYỆN · CHẠY TRÊN MÁY CÁ NHÂN"
    )
    if todo_next:
        nxt = ('<div class="next"><h2>Việc nên làm tiếp</h2>Mở gợi ý ở các TODO: '
               + safe(", ".join(todo_next)) + ". Sửa từng TODO rồi chạy lại lệnh chấm.</div>")
    else:
        nxt = ('<div class="next"><h2>Hoàn thành mười TODO bắt buộc</h2>'
               'Có thể thử phần thử thách (TODO tùy chọn) và mini-project để luyện thêm.</div>')
    return (
        '<!doctype html><html lang="vi"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="referrer" content="no-referrer">'
        '<title>Week 02 — Bảng điểm tự luyện Python</title><style>'
        + REPORT_CSS + '</style></head><body><main class="page">'
        '<header class="sheet"><div class="ring" style="--p:' + str(percent)
        + '" role="img" aria-label="Điểm ' + f'{score:.2f}' + ' trên 10"><div><strong>'
        + f'{score:.2f}' + '</strong><span>trên 10</span></div></div><div>'
        '<div class="stamp">' + safe(stamp) + '</div>'
        '<h1>Bảng điểm Python · Tuần 02</h1>'
        '<p>Ba bài tập gốc, mười TODO bắt buộc. Học từ lỗi sai, thử lại theo nhịp của mình.</p>'
        '<div class="chips"><span class="chip">Xếp loại: ' + safe(rank_of(score)) + '</span>'
        '<span class="chip">' + str(completed) + '/' + str(total) + ' TODO đạt</span>'
        '<span class="chip">Chưa phải điểm học phần</span></div></div></header>'
        '<div class="matrix" aria-label="Bản đồ mười TODO">' + "".join(matrix) + '</div>'
        '<div class="legend">Bấm ô số để nhảy tới TODO · xanh = đạt · vàng = thử lại · tím = cần xem lại</div>'
        '<div class="note"><strong>Đây là điểm tự luyện, không phải điểm học phần.</strong>'
        '<p>Chỉ kiểm TODO bắt buộc trong 3 file exercises/. Phần thử thách, practice và '
        'mini-project không tính điểm. Khi mã đúng nhưng máy báo THỬ LẠI/CẦN XEM LẠI, '
        'nhờ giảng viên xem phương án giải.</p>'
        '<p>Báo cáo lưu ngoại tuyến; không tự tải lên Internet, không chứa mã nguồn, '
        'tên hay đầu ra cá nhân của sinh viên.</p></div>'
        + "".join(stages) + nxt +
        '<div class="foot">Vòng tự học: Đọc yêu cầu → Dự đoán → Viết mã → Chạy tự kiểm → '
        'Mở gợi ý nếu cần → Sửa và thử lại.<br>Đã kiểm tự động: '
        + safe(result["rubric_sha256"][:12]) + ' (mã kiểm tra rubric). official_score: null.</div>'
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
