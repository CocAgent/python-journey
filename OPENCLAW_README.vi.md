# OpenClaw 🦞 — Trợ lý của bạn, trên thiết bị của bạn, trong các cuộc trò chuyện của bạn

> 📌 **Bản dịch tiếng Việt** của [README gốc của OpenClaw](https://github.com/openclaw/openclaw/blob/main/README.md), dùng cho mục đích học tập.
> Dự án gốc: <https://github.com/openclaw/openclaw> — © 2026 OpenClaw Foundation, phát hành theo giấy phép MIT (xem thông báo bản quyền ở cuối tệp).
> Nội dung có thể đã thay đổi so với bản gốc; hãy xem README gốc để có thông tin mới nhất.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/openclaw-banner-light.png">
    <img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/openclaw-banner-dark.png" alt="OpenClaw — Trợ lý AI chạy ngay trên thiết bị của chính bạn.">
  </picture>
</p>

<p align="center">
  <a href="https://github.com/openclaw/openclaw/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/openclaw/openclaw/ci.yml?branch=main&style=flat-square&label=ci" alt="Trạng thái CI"></a>
  <a href="https://www.npmjs.com/package/openclaw"><img src="https://img.shields.io/npm/v/openclaw?style=flat-square&label=npm" alt="Phiên bản npm"></a>
  <a href="https://nodejs.org"><img src="https://img.shields.io/node/v/openclaw?style=flat-square" alt="Phiên bản Node.js"></a>
  <a href="https://github.com/openclaw/openclaw/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="Giấy phép: MIT"></a>
  <a href="https://discord.gg/clawd"><img src="https://img.shields.io/discord/1456350064065904867?label=discord&logo=discord&logoColor=white&color=5865F2&style=flat-square" alt="Discord"></a>
</p>

OpenClaw là một trợ lý AI mã nguồn mở chạy trên máy tính của chính bạn và đồng hành cùng bạn trong những kênh bạn vẫn dùng hằng ngày: Discord, iMessage, Slack, Teams, Telegram, WhatsApp và hơn 20 kênh khác, cùng các ứng dụng gốc cho macOS, iOS, Android, Windows và Linux. Một Gateway duy nhất có thể chạy như trợ lý cá nhân trên laptop hoặc như một [hệ thống triển khai cho nhóm](https://docs.openclaw.ai/start/teams); khác biệt duy nhất nằm ở cấu hình.

**Của bạn, không có điều kiện ràng buộc.** Trạng thái, bộ nhớ và thông tin xác thực đều nằm trên phần cứng của bạn. Các mô hình và agent harness (Claude, Codex, mô hình chạy cục bộ) là các plugin có thể thay thế mà không ảnh hưởng đến phần còn lại. Các prompt của bạn được gửi đến nhà cung cấp mô hình và các nền tảng trò chuyện mà bạn cấu hình, cùng với bất kỳ bản xuất chẩn đoán nào bạn tự bật; theo mặc định, bản thân OpenClaw chỉ "gọi về" để kiểm tra phiên bản mỗi ngày, thống kê tính năng ẩn danh là tùy chọn (opt-in), và `update.checkOnStart: false` sẽ tắt cả hai ([OpenClaw gửi những gì](https://docs.openclaw.ai/gateway/telemetry)). OpenClaw do [OpenClaw Foundation](https://openclaw.org) — một tổ chức 501(c)(3) độc lập — điều hành, không có gói trả phí, dịch vụ lưu trữ hay token. Lập luận về kiến trúc — gateway đáng tin cậy, môi trường thực thi không đáng tin cậy, chính sách được thực thi bằng code — có trong bài [Vì sao chọn OpenClaw](https://docs.openclaw.ai/start/why-openclaw).

[Website](https://openclaw.ai) · [Tài liệu](https://docs.openclaw.ai) · [Bắt đầu](https://docs.openclaw.ai/start/getting-started) · [Vì sao chọn OpenClaw](https://docs.openclaw.ai/start/why-openclaw) · [FAQ](https://docs.openclaw.ai/help/faq) · [Tầm nhìn](https://github.com/openclaw/openclaw/blob/main/VISION.md) · [DeepWiki](https://deepwiki.com/openclaw/openclaw)

## Cài đặt

Trình cài đặt hỗ trợ macOS, Linux và Windows. Nó sẽ tự cài một phiên bản Node.js được hỗ trợ khi cần.

```bash
# macOS / Linux / WSL2
curl -fsSL https://openclaw.ai/install.sh | bash
```

```powershell
# Windows PowerShell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

Bạn đã tự quản lý Node.js? Hãy cài gói đã phát hành (Node 24.16+ hoặc 26.1+; khuyến nghị Node 26):

```bash
npm install -g openclaw@latest --allow-scripts=openclaw
```

Lệnh trên dành cho npm 12 hoặc npm 11.16+. Với npm 11.15 trở xuống, hãy bỏ `--allow-scripts=openclaw`. Xem [hướng dẫn cài đặt](https://docs.openclaw.ai/install) để biết quy ước về lifecycle script, Docker, Nix và các cách triển khai khác.

## Bắt đầu nhanh

Với bản cài mới, các script cài đặt sẽ tự khởi chạy phần onboarding. Hãy hoàn thành trình hướng dẫn mà chúng mở ra. Nếu bạn cài gói trực tiếp bằng npm, pnpm hoặc Bun, hãy chạy:

```bash
openclaw onboard --install-daemon
```

Sau khi onboarding xong:

```bash
openclaw gateway status
openclaw dashboard
```

Onboarding sẽ kiểm tra quyền truy cập mô hình, tạo workspace và cấu hình Gateway. Lệnh cuối cùng mở Control UI; hãy gửi một tin nhắn tại đó để xác nhận trợ lý hoạt động. Xem [hướng dẫn bắt đầu](https://docs.openclaw.ai/start/getting-started) để cài đặt kênh và xử lý sự cố.

## Các thành phần kết nối với nhau như thế nào

- [Gateway](https://docs.openclaw.ai/gateway) là mặt phẳng điều khiển cục bộ cho phiên làm việc, công cụ, sự kiện và kết nối kênh.
- [Control UI](https://docs.openclaw.ai/web/control-ui), CLI và [TUI](https://docs.openclaw.ai/web/tui) kết nối đến Gateway.
- [Các kênh](https://docs.openclaw.ai/channels) đưa trợ lý đến WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage và các dịch vụ nhắn tin khác.
- [Ứng dụng đồng hành và node](https://docs.openclaw.ai/platforms) bổ sung giọng nói, Canvas, camera, màn hình và các hành động cục bộ trên thiết bị ở những nền tảng được hỗ trợ.

OpenClaw hoạt động với cả [nhà cung cấp mô hình](https://docs.openclaw.ai/concepts/model-providers) trên đám mây lẫn cục bộ. Các [công cụ](https://docs.openclaw.ai/tools), [skill](https://docs.openclaw.ai/tools/skills) và [plugin](https://docs.openclaw.ai/plugins) giúp mở rộng khả năng của trợ lý.

## Bảo mật

Hãy coi tin nhắn đến là dữ liệu đầu vào không đáng tin cậy. Các kênh có DM sẽ ghép cặp (pairing) với người gửi lạ theo mặc định; duyệt yêu cầu ghép cặp bằng `openclaw pairing approve <channel> <code>`.

Các công cụ chạy trực tiếp trên máy chủ cho phiên chính, trừ khi bạn cấu hình sandbox. Hãy đọc [hướng dẫn bảo mật](https://docs.openclaw.ai/gateway/security), [runbook về việc để lộ Gateway](https://docs.openclaw.ai/gateway/security/exposure-runbook) và [hướng dẫn sandbox](https://docs.openclaw.ai/gateway/sandboxing) trước khi kết nối người dùng khác hoặc mở Gateway ra bên ngoài.

## Tài liệu

| Mục tiêu                              | Bắt đầu từ đây |
| ------------------------------------- | -------------- |
| Cấu hình mô hình và xác thực          | [Mô hình](https://docs.openclaw.ai/concepts/models) · [Nhà cung cấp mô hình](https://docs.openclaw.ai/concepts/model-providers) |
| Kết nối dịch vụ nhắn tin              | [Các kênh](https://docs.openclaw.ai/channels) |
| Thêm công cụ, skill và plugin         | [Công cụ](https://docs.openclaw.ai/tools) · [Skills](https://docs.openclaw.ai/tools/skills) · [Plugins](https://docs.openclaw.ai/plugins) · [ClawHub](https://clawhub.ai) |
| Chạy ứng dụng và node thiết bị        | [Nền tảng](https://docs.openclaw.ai/platforms) · [Nodes](https://docs.openclaw.ai/nodes) |
| Dùng CLI và lệnh trò chuyện           | [Tham chiếu CLI](https://docs.openclaw.ai/cli) · [Lệnh slash](https://docs.openclaw.ai/tools/slash-commands) |
| Cấu hình hoặc vận hành Gateway        | [Cấu hình](https://docs.openclaw.ai/gateway/configuration) · [Kiến trúc](https://docs.openclaw.ai/concepts/architecture) · [Cập nhật](https://docs.openclaw.ai/install/updating) · [Kênh phát hành](https://docs.openclaw.ai/install/development-channels) |

## Phát triển

Repository này là một pnpm workspace. Chạy `npm install` thông thường ở thư mục gốc **không** được hỗ trợ.

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw
pnpm install
pnpm build
pnpm ui:build
```

Xem [CONTRIBUTING.md](https://github.com/openclaw/openclaw/blob/main/CONTRIBUTING.md) để biết quy trình đóng góp và [hướng dẫn thiết lập từ mã nguồn](https://docs.openclaw.ai/start/setup) để biết vòng lặp phát triển.

## Quản trị

OpenClaw được phát triển công khai bởi [OpenClaw Foundation](https://openclaw.org), một tổ chức 501(c)(3) độc lập. Foundation tuyển dụng đội ngũ cốt lõi và ký các bản phát hành. Các nhà tài trợ và đơn vị hỗ trợ hạ tầng ủng hộ Foundation; không bên nào sở hữu hay chi phối dự án. OpenAI là nhà tài trợ, không phải chủ sở hữu.

## Cộng đồng

Xem [CONTRIBUTING.md](https://github.com/openclaw/openclaw/blob/main/CONTRIBUTING.md) để biết thông tin về người bảo trì và hướng dẫn đóng góp; các PR có sự hỗ trợ của AI đều được chào đón.

Dùng [issue chooser](https://github.com/openclaw/openclaw/issues/new/choose) để báo lỗi và đề xuất tính năng, nhận hỗ trợ chính thức của OpenClaw tại [community.openclaw.ai](https://community.openclaw.ai/), và báo cáo lỗ hổng bảo mật qua [SECURITY.md](https://github.com/openclaw/openclaw/blob/main/SECURITY.md). Các khả năng mới thường nên được xây dưới dạng plugin dựa trên [plugin SDK](https://docs.openclaw.ai/plugins/building-plugins) và chia sẻ qua [ClawHub](https://clawhub.ai).

OpenClaw được tạo ra cho **Molty**, một trợ lý AI hình tôm hùm không gian, bởi Peter Steinberger cùng cộng đồng. Hãy khám phá [câu chuyện nền của dự án](https://docs.openclaw.ai/start/lore), [soul.md](https://soul.md), [trang của Peter](https://steipete.me), [Star History](https://www.star-history.com/#openclaw/openclaw&type=date&legend=top-left) và [@openclaw](https://x.com/openclaw).

Xin cảm ơn đặc biệt [Mario Zechner](https://mariozechner.at/) vì sự hỗ trợ và vì [pi](https://github.com/earendil-works/pi), và Adam Doppelt vì tên miền lobster.bot.

## Nhà tài trợ

Foundation được tài trợ bởi các nhà đóng góp gồm Amazon, Lobster Computer Company, Offline Holdings, OpenAI, Red Hat và Đại học Michigan, cùng sự hỗ trợ hạ tầng từ Blacksmith, Convex, GitHub, NVIDIA và Vercel.

## Người đóng góp

Cảm ơn tất cả các "clawtributor". Xem danh sách đầy đủ tại: <https://github.com/openclaw/openclaw/graphs/contributors>

---

## Thông báo bản quyền và giấy phép

Bản dịch này dựa trên README của dự án OpenClaw, phát hành theo giấy phép MIT:

```text
MIT License

Copyright (c) 2026 OpenClaw Foundation

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

Toàn văn giấy phép: <https://github.com/openclaw/openclaw/blob/main/LICENSE>
