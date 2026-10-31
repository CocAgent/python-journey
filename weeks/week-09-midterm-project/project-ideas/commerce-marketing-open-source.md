# Phụ lục: Mã nguồn mở Thương mại & Marketing — Python Journey

> **Ngày đối chiếu repository:** 28/10/2026, GitHub metadata. Đây là **phụ lục 13 nguồn mở** của danh mục [20 dự án Week 09](catalog-20-du-an.md), không thay thế 20 nguồn cốt lõi hoặc danh mục lưu chiểu Word. Mọi repository trong bảng được xác minh công khai, không archived và có hoạt động cập nhật mã nguồn. Đó **không phải** chứng nhận bảo mật, giấy phép sử dụng thương mại hay tính tương thích với máy sinh viên.

## Vì sao học Commerce & Marketing?

- **Commerce engineering:** sản phẩm, giá, giỏ hàng, tồn kho, đơn hàng và workflow bán hàng.
- **Business operations:** CRM, ERP, đơn sự kiện, báo cáo.
- **Marketing technology (MarTech):** content, campaigns, consent, funnel analytics, A/B experimentation.
- **Nghề nghiệp:** Python backend, business software, data analytics, QA, automation, product analyst, marketing engineer.

**Nguyên tắc:** sinh viên giữa kỳ chỉ cần *một* MVP Python 3.12+ offline, dùng W01–W08 (`if`, `for`, hàm, `list/dict/set`). **Không** bắt buộc cài Saleor/Odoo/ERPNext/PostHog, học PHP/Go/TypeScript, có server, chạy Docker, kết nối thanh toán, gửi email hay gọi API trả phí. Đề tài khác cũng được chấp nhận. Chấm cùng [rubric 10 điểm](rubric-10-diem.md); không cộng điểm vì công cụ lớn.

## Chọn nhanh theo hướng nghề

| ID | Nguồn mở | Chủ đề thực hành | Ngôn ngữ chính / hệ sinh thái | Hướng mở rộng |
|---|---|---|---|:---:|
| C01 | [Saleor](https://github.com/saleor/saleor) | Commerce API | Python | B |
| C02 | [Django Oscar](https://github.com/django-oscar/django-oscar) | E-commerce / promotion | Python | B |
| C03 | [ERPNext](https://github.com/frappe/erpnext) | ERP / inventory | Python | B |
| C04 | [Odoo](https://github.com/odoo/odoo) | CRM / sales operations | Python | B |
| C05 | [Pretix](https://github.com/pretix/pretix) | Event commerce / tickets | Python | B |
| C06 | [Medusa](https://github.com/medusajs/medusa) | Headless commerce comparison | TypeScript | C |
| M01 | [Wagtail](https://github.com/wagtail/wagtail) | Content marketing / CMS | Python | B |
| M02 | [PostHog](https://github.com/PostHog/posthog) | Product analytics / funnel | Python + đa ngôn ngữ | C |
| M03 | [Umami](https://github.com/umami-software/umami) | Privacy-first marketing analytics | TypeScript | B |
| M04 | [Mautic](https://github.com/mautic/mautic) | Marketing automation / CRM | PHP | C |
| M05 | [listmonk](https://github.com/knadh/listmonk) | Newsletter / mailing lists | Go | B |
| M06 | [Matomo](https://github.com/matomo-org/matomo) | Web analytics / privacy | PHP | C |
| M07 | [GrowthBook](https://github.com/growthbook/growthbook) | A/B testing / experimentation | TypeScript | C |

Nhãn **B**: dễ nối sang công nghệ gốc sau W10–W15 nếu muốn. **C**: nền tảng lớn/chuyên sâu hoặc khác ngôn ngữ, chỉ nghiên cứu kiến trúc; các MVP đều vẫn viết Python thuần được. Nhãn **không** thể hiện điểm số hay chất lượng repo.

## Bài toán cụ thể — Commerce (C01–C06)

### C01 · Saleor

- **Bài toán MVP W09:** Giỏ hàng và kiểm tra tồn kho.
- **Input:** Danh sách SKU, đơn giá VND, tồn kho; giỏ gồm (SKU, số lượng).
- **Output:** Hóa đơn tạm tính, tổng tiền, số lượng tồn dự kiến.
- **Biên/sai cần chứng minh:** SKU không tồn tại, số lượng 0/âm, mua vượt tồn; không cập nhật tồn khi đơn lỗi.
- **Sau W09 (tùy chọn):** W10 lưu JSON; W13 mô phỏng API; W15 xây service + tests/CLI. Không gọi Saleor thật.

### C02 · Django Oscar

- **Bài toán MVP W09:** Công cụ mã khuyến mãi cho giỏ hàng.
- **Input:** Giỏ hàng và mã khuyến mãi giả lập, quy định ngưỡng đơn tối thiểu.
- **Output:** Chiết khấu hợp lệ và số tiền phải trả (VND nguyên).
- **Biên/sai cần chứng minh:** Mã hết hạn hoặc không hợp lệ, tổng 0, giảm lớn hơn tiền hàng.
- **Sau W09 (tùy chọn):** W13 xem Django views; W15 kiểm thử các chính sách giảm giá.

### C03 · ERPNext

- **Bài toán MVP W09:** Quản lý kho và đề xuất nhập hàng.
- **Input:** Danh sách tồn kho, mức tối thiểu và dự báo bán hàng giả lập.
- **Output:** Danh sách SKU phải nhập thêm và số lượng gợi ý.
- **Biên/sai cần chứng minh:** SKU trùng, tồn âm, số lượng bán vượt tồn.
- **Sau W09 (tùy chọn):** W10 CSV/JSON tồn kho; W15 quản lý purchase orders giả lập và báo cáo.

### C04 · Odoo

- **Bài toán MVP W09:** Theo dõi pipeline khách hàng tiềm năng (CRM).
- **Input:** Leads giả lập với nguồn, giai đoạn và giá trị dự kiến.
- **Output:** Số lead từng giai đoạn và tổng giá trị cơ hội.
- **Biên/sai cần chứng minh:** Trạng thái lạ, lead trùng, giá trị âm; không dùng dữ liệu khách thật.
- **Sau W09 (tùy chọn):** W10 lưu CSV; W13 API adapter nội bộ; W15 CRM mini-project.

### C05 · Pretix

- **Bài toán MVP W09:** Đăng ký vé sự kiện không có thanh toán.
- **Input:** Sức chứa, loại vé, số ghế yêu cầu.
- **Output:** Số vé còn, trạng thái đăng ký hoặc từ chối.
- **Biên/sai cần chứng minh:** Đặt vượt sức chứa, vé âm, double booking bằng ID trùng.
- **Sau W09 (tùy chọn):** W10 persistence; W12 test biên; W15 demo ticket app offline.

### C06 · Medusa

- **Bài toán MVP W09:** Bộ máy chuyển trạng thái đơn hàng.
- **Input:** Đơn hàng và trạng thái: new/paid/packed/shipped/cancelled (giả lập).
- **Output:** Trạng thái mới và nhật ký hành động hợp lệ.
- **Biên/sai cần chứng minh:** Chuyển shipped → new, giao hàng khi chưa paid, hủy trùng.
- **Sau W09 (tùy chọn):** W13 đối chiếu kiến trúc commerce API; không yêu cầu học TypeScript hoặc chạy Medusa.

## Bài toán cụ thể — Marketing (M01–M07)

### M01 · Wagtail

- **Bài toán MVP W09:** Lịch biên tập bài viết và trạng thái duyệt.
- **Input:** Danh sách bài viết, chủ đề, ngày dự kiến và trạng thái.
- **Output:** Lịch đăng, danh sách bài trễ hạn và thống kê chủ đề.
- **Biên/sai cần chứng minh:** Trùng slug, ngày không hợp lệ, đăng khi chưa duyệt.
- **Sau W09 (tùy chọn):** W10 lưu JSON; W13 web CMS; W15 portfolio về content operations.

### M02 · PostHog

- **Bài toán MVP W09:** Đo phễu chuyển đổi trên dữ liệu sự kiện giả lập.
- **Input:** Các sự kiện visit → signup → purchase theo anonymous ID mẫu.
- **Output:** Số người ở từng bước và tỷ lệ chuyển đổi.
- **Biên/sai cần chứng minh:** Event trùng, thiếu bước, mẫu 0; không theo dõi người dùng thực.
- **Sau W09 (tùy chọn):** W10 CSV; W15 dashboard cohort/funnel với dữ liệu được phép.

### M03 · Umami

- **Bài toán MVP W09:** Báo cáo hiệu quả chiến dịch bằng UTM.
- **Input:** Dữ liệu giả lập campaign, channel, visits, conversions.
- **Output:** Bảng conversion rate từng kênh; kênh tốt nhất.
- **Biên/sai cần chứng minh:** 0 visits, duplicate campaign, conversion > visits.
- **Sau W09 (tùy chọn):** W10 import CSV; W15 dashboard marketing không dùng cookie hay user tracking thật.

### M04 · Mautic

- **Bài toán MVP W09:** Phân nhóm khách hàng dựa trên quy tắc.
- **Input:** Hồ sơ khách hàng tổng hợp/giả lập với sở thích, lịch sử mua, opt-in.
- **Output:** Nhóm khách hàng và chiến dịch được gợi ý (không gửi thư).
- **Biên/sai cần chứng minh:** Chưa đồng ý nhận tin, thiếu dữ liệu, hủy đăng ký.
- **Sau W09 (tùy chọn):** W15 xây journey simulator kèm audit, không gửi marketing thật hay tự động spam.

### M05 · listmonk

- **Bài toán MVP W09:** Quản lý danh sách nhận bản tin có consent.
- **Input:** Danh sách email giả lập và trạng thái opt-in/unsubscribe.
- **Output:** Danh sách đủ điều kiện nhận tin và thống kê.
- **Biên/sai cần chứng minh:** Email trùng, unsubscribe, chưa consent; không gửi email thật.
- **Sau W09 (tùy chọn):** W10 nhập/xuất CSV; W15 kiểm soát unsubscribe, audit logs.

### M06 · Matomo

- **Bài toán MVP W09:** Tổng hợp lượt truy cập theo nguồn giới thiệu.
- **Input:** Dữ liệu tổng hợp theo ngày và kênh traffic; không có IP/cookie.
- **Output:** Báo cáo lượt xem, sessions, xu hướng theo nguồn.
- **Biên/sai cần chứng minh:** Thiếu ngày, số âm, dữ liệu rỗng; không suy số người từ page views.
- **Sau W09 (tùy chọn):** W15 phân tích analytics có kiểm soát riêng tư, giải thích metrics.

### M07 · GrowthBook

- **Bài toán MVP W09:** Báo cáo A/B test giả lập cho hai biến thể.
- **Input:** Mỗi nhóm: số người thử nghiệm và số chuyển đổi giả lập.
- **Output:** Tỷ lệ chuyển đổi và chênh lệch giữa A/B, không tuyên bố thắng tuyệt đối.
- **Biên/sai cần chứng minh:** Mẫu 0, conversion > sample size, dữ liệu thiếu; không suy ý nghĩa thống kê khi chưa học.
- **Sau W09 (tùy chọn):** W15 nghiên cứu assignment, guardrails, statistical tests sau khi học đủ nền tảng.

## Lộ trình mở rộng từ Week 09 sang Week 15

| Giai đoạn | Nội dung | Evidence |
|---|---|---|
| W09 | MVP logic với `list/dict/function`, offline | Demo input/output thường và biên, README, commit |
| W10–11 | CSV/JSON, pathlib, xử lý lỗi dữ liệu | Snapshot data, missing/invalid input, debug story |
| W12 | pytest và hồi quy | Ít nhất 5 test có ý nghĩa nếu chuyển thành capstone W15 |
| W13 | Modules, package, CLI, khái niệm API | Service core độc lập framework; adapter tùy chọn |
| W14 | Thành phần OOP/composition nếu hữu ích | Giải thích class vs function, trade-offs |
| W15 | Project tích hợp, test, README, demo/bảo vệ | Tuân thủ **duy nhất** [FINAL_PROJECT.md](../../../FINAL_PROJECT.md) |

**Ví dụ đường học xuyên khóa:**

```text
W09  Cart & inventory simulator (Saleor-inspired)
  ↓
W10  CSV/JSON persistence of SKUs and orders
  ↓
W11  Reject invalid quantity / missing SKU / corrupt data
  ↓
W12  pytest for stock safety and pricing
  ↓
W13  CLI and optional local-only API adapter
  ↓
W14  Compose pricing, stock and order services
  ↓
W15  Commerce capstone: complete demo + tests + README + defense
```

**Một đường Marketing:** campaign CSV → tính conversion rate → loại dữ liệu lỗi → regression tests → dashboard offline. Dùng data tổng hợp/giả lập thay vì dữ liệu người dùng thực.

## Công thức minh bạch cho MVP Marketing

- **Conversion rate** (đơn vị %): `conversions / visits × 100` khi `visits > 0`. Nêu rõ mẫu số và đơn vị chuyển đổi; với 0 visits trả N/A, không chia 0.
- **CTR**: `clicks / impressions × 100` khi impressions > 0. Không suy CTR chỉ từ số sessions.
- **CPA**: `campaign_cost / conversions` khi conversions > 0; 0 conversions → N/A.
- **A/B test:** báo tỷ lệ từng nhóm và kích thước mẫu; không gọi biến thể “thắng” khi chưa có kiểm định thích hợp.
- **Giá bán/chiết khấu:** với VND nên biểu diễn bằng **số nguyên đồng**, tránh dùng `float` cho số tiền; không mô phỏng thanh toán thật.

## Quy tắc nguồn mở, đạo đức và bảo mật

1. **Đọc để học ≠ được quyền sao chép tùy ý.** Trước khi fork, sửa hay phân phối mã bên thứ ba, đọc `LICENSE`, dependency licenses, notices và điều kiện đúng phiên bản; một số repo có phần mã/edition/asset theo các giấy phép khác nhau. Metadata `NOASSERTION` không chứng minh vô giấy phép.
2. **Marketing có đồng ý:** chỉ sử dụng email/dữ liệu giả lập; không gửi email thật, không thu thập cookies, IP, mã định danh cá nhân hay chạy tracking thật. Opt-out phải được tôn trọng.
3. **Không xử lý thanh toán thật:** không lưu thẻ, không thanh toán qua gateway, không sử dụng API key hoặc webhook production. Chỉ mô phỏng luồng trạng thái.
4. **Không thao túng chỉ số:** báo rõ dữ liệu giả lập, công thức, mẫu số, edge cases và giới hạn; không gọi mô hình rule-based là “AI được huấn luyện”.
5. **Cài hệ thống upstream là tự chọn sau W09:** không chấm framework hoạt động thay cho việc hiểu, sửa và test code mình viết. Nếu cài Docker hay dịch vụ phức tạp, dùng môi trường tách biệt và cấu hình theo upstream.

## Dành cho giảng viên

- Danh mục [20 dự án chính](catalog-20-du-an.md) **vẫn đúng 20**, nguồn Word ban đầu vẫn được lưu chiểu riêng.
- Phụ lục này chỉ giúp chọn thêm **13 đề tài theo ngành**, không thêm rubric hoặc deliverable bắt buộc.
- Với các đề tài thương mại, đánh giá tính đúng đắn của giá/tồn kho/đơn và xử lý lỗi. Với marketing, đánh giá đúng mẫu số/công thức, consent và giới hạn diễn giải.
- Khi xét nâng cấp thành capstone, tham chiếu [đề cương Week 15](../../week-15-capstone-project/README.md) và [FINAL_PROJECT.md](../../../FINAL_PROJECT.md); không tạo tiêu chí thứ hai.
