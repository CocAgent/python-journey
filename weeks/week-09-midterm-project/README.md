# Tuần 09 — Midterm Project

Midterm trả lời một câu hỏi: bạn có thể kết hợp nền tảng Week 01–08 thành một
project Python nhỏ, chạy ổn định và giải thích được không?

```text
Learn → Build → Test → Debug → Improve → Commit → Prove
```

## Outcomes

Sau Week 09, bạn có thể:

- lập kế hoạch một project vừa sức;
- chia project thành các function có trách nhiệm rõ;
- dùng structured data thay cho nhiều biến rời rạc;
- chạy normal case và boundary case;
- đọc output để tìm và sửa lỗi;
- đánh giá behavior bằng evidence thay vì cảm giác;
- ghi lại commit, bug, cách sửa và known weakness.

## Prerequisites

Hoàn thành Week 01–08 và machine checks của Week 07–08 trước khi bắt đầu.

## Chọn track

Xem [`tracks/README.md`](tracks/README.md):

1. **VuaCóc Bot V1** — flagship track dùng structured state và Local Arena.
2. **Student Manager** — track thay thế giữ bài toán quản lý học sinh legacy.
3. **Dự án nhóm lấy cảm hứng từ nguồn mở được tuyển chọn** — chọn trong [thư viện ý tưởng](project-ideas/README.md) gồm **20 nguồn lõi**, **13 Commerce/Marketing** và **11 Agent tự chọn**, hoặc tự đề xuất dự án Python khác.

Ba track đều dùng chung minh chứng về kế hoạch, phân rã, tính đúng và khả năng chạy lại. Mỗi nhóm 1–3 sinh viên (hoặc cá nhân) **chỉ cần hoàn thành một track**. Đối với Track C, có thể làm MVP Python thuần; không bắt buộc cài nguyên framework nâng cao.

## Learning path

```text
choose → plan → decompose → implement → run
       → inspect → debug → evaluate → explain → commit
```

1. Đọc [`notes.md`](notes.md).
2. Chọn brief trong [`tracks/`](tracks/).
3. Copy hoặc hoàn thiện artifact phù hợp trong [`starter/`](starter/).
4. Chạy project nhiều lần với các case đã lên kế hoạch. Khi bí, xem
   [`hints.md`](hints.md).
5. Dùng [`evidence-template.md`](evidence-template.md) để ghi bằng chứng.
6. Chạy [machine check](checks/README.md) cho reference artifacts.
7. Commit project bằng message có ý nghĩa. Nếu quan tâm **thương mại và marketing**, xem thêm
   [13 lựa chọn Saleor/ERP/MarTech](project-ideas/commerce-marketing-open-source.md).
   Nếu theo Track C, điền thêm [phiếu đề xuất nhóm](project-ideas/phieu-de-xuat-nhom.md) và chọn một mục trong [danh mục 20 ý tưởng được cập nhật](project-ideas/catalog-20-du-an.md).

## Evaluation

Áp dụng [rubric 10 điểm của giảng viên](project-ideas/rubric-10-diem.md): Python là chính, cài/chạy được, demo, input/output, README, cấu trúc, test/checklist, Git, phạm vi MVP và đạo đức dữ liệu. Đánh giá dựa trên bằng chứng thực tế, **không có ưu tiên điểm cho công cụ khó hoặc đắt tiền**. Với Bot không yêu cầu win-rate.

Week 09 milestone: [Midterm Bot V1](../../projects/vuacoc-bot-journey/milestones/w09-midterm-bot-v1.md).

## Definition of done

- [ ] Project chạy local bằng một command được ghi trong README.
- [ ] Core behavior được chia thành function.
- [ ] Structured state được dùng có chủ đích.
- [ ] Normal và boundary cases hoàn tất.
- [ ] Một bug và cách sửa được ghi lại.
- [ ] Một known weakness được ghi lại.
- [ ] Evidence template có commit SHA.
- [ ] Không có global state không cần thiết.
