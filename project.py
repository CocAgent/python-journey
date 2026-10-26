"""
╔══════════════════════════════════════════════════════╗
║           HỆ THỐNG ATM - NGÂN HÀNG SỐ VIỆT NAM     ║
║         Viet Digital Bank - ATM Simulator            ║
╚══════════════════════════════════════════════════════╝

Hệ thống mô phỏng máy ATM với đầy đủ chức năng:
- Đăng nhập bằng mã PIN
- Rút tiền (nhanh & tùy chỉnh)
- Kiểm tra số dư
- Chuyển khoản
- Lịch sử giao dịch
- Đổi mã PIN
- In biên lai

Tác giả: ATM System v2.0
"""

import tkinter as tk
from tkinter import messagebox
import time
import random
import string
from datetime import datetime


# ════════════════════════════════════════════════════════
#  CẤU HÌNH MÀU SẮC & THIẾT KẾ
# ════════════════════════════════════════════════════════

class Theme:
    """Bảng màu thiết kế hiện đại cho ATM"""
    # Nền chính
    BG_DARK = "#0a0e1a"
    BG_CARD = "#111827"
    BG_SURFACE = "#1a2035"
    BG_ELEVATED = "#1f2a44"
    BG_INPUT = "#0d1321"
    
    # Màu chủ đạo
    PRIMARY = "#6366f1"        # Indigo
    PRIMARY_HOVER = "#818cf8"
    PRIMARY_DARK = "#4338ca"
    SECONDARY = "#22d3ee"      # Cyan
    ACCENT = "#f472b6"         # Pink
    
    # Gradient colors
    GRADIENT_START = "#6366f1"
    GRADIENT_END = "#8b5cf6"
    
    # Trạng thái
    SUCCESS = "#10b981"
    SUCCESS_BG = "#064e3b"
    WARNING = "#f59e0b"
    WARNING_BG = "#78350f"
    DANGER = "#ef4444"
    DANGER_BG = "#7f1d1d"
    
    # Text
    TEXT_PRIMARY = "#f1f5f9"
    TEXT_SECONDARY = "#94a3b8"
    TEXT_MUTED = "#64748b"
    TEXT_ACCENT = "#a5b4fc"
    
    # Border
    BORDER = "#1e293b"
    BORDER_FOCUS = "#6366f1"
    
    # Font
    FONT_FAMILY = "Segoe UI"
    FONT_MONO = "Consolas"


# ════════════════════════════════════════════════════════
#  DỮ LIỆU MẪU
# ════════════════════════════════════════════════════════

class AccountData:
    """Dữ liệu tài khoản mẫu"""
    def __init__(self):
        self.holder_name = "NGUYỄN VĂN A"
        self.account_number = "0123456789"
        self.card_number = "4567 8901 2345 6789"
        self.card_display = "****6789"
        self.pin = "1234"
        self.balance = 50_000_000
        self.frozen = 0
        self.daily_limit = 30_000_000
        self.withdrawn_today = 0
        self.transactions: list[dict] = []

    def format_currency(self, amount: int) -> str:
        """Format số tiền theo kiểu Việt Nam"""
        return f"{amount:,.0f} ₫".replace(",", ".")

    def generate_txn_id(self) -> str:
        """Tạo mã giao dịch"""
        chars = string.ascii_uppercase + string.digits
        return "TXN" + "".join(random.choices(chars, k=8))

    def add_transaction(self, txn_type: str, amount: int, description: str = ""):
        """Thêm giao dịch vào lịch sử"""
        txn = {
            "id": self.generate_txn_id(),
            "type": txn_type,
            "amount": amount,
            "balance_after": self.balance,
            "datetime": datetime.now(),
            "description": description
        }
        self.transactions.insert(0, txn)
        return txn


# ════════════════════════════════════════════════════════
#  LỚP ATM CHÍNH
# ════════════════════════════════════════════════════════

class ATMApp:
    """Ứng dụng ATM chính"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("💳 Hệ Thống ATM - Viet Digital Bank")
        self.root.geometry("520x820")
        self.root.resizable(False, False)
        self.root.configure(bg=Theme.BG_DARK)
        
        # Center window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - 260
        y = (self.root.winfo_screenheight() // 2) - 410
        self.root.geometry(f"520x820+{x}+{y}")
        
        # Data
        self.account = AccountData()
        self.pin_entered = ""
        self.pin_attempts = 0
        self.max_attempts = 3
        self.selected_amount = 0
        self.current_screen = None
        self.balance_visible = False
        
        # Build UI
        self._build_header()
        self._build_screen_container()
        self._build_footer()
        
        # Show first screen
        self.show_screen_insert()
        
        # Update clock
        self._update_clock()
    
    # ──────────────────────────────────────────────────
    #  UI BUILDER HELPERS
    # ──────────────────────────────────────────────────
    
    def _build_header(self):
        """Xây dựng header"""
        header = tk.Frame(self.root, bg=Theme.BG_CARD, height=70)
        header.pack(fill="x", padx=0, pady=0)
        header.pack_propagate(False)
        
        # Left: Bank name
        left = tk.Frame(header, bg=Theme.BG_CARD)
        left.pack(side="left", padx=20, pady=10)
        
        tk.Label(left, text="💳 VIET DIGITAL BANK",
                 font=(Theme.FONT_FAMILY, 14, "bold"),
                 fg=Theme.PRIMARY_HOVER, bg=Theme.BG_CARD).pack(anchor="w")
        tk.Label(left, text="Ngân Hàng Số Việt Nam",
                 font=(Theme.FONT_FAMILY, 9),
                 fg=Theme.TEXT_MUTED, bg=Theme.BG_CARD).pack(anchor="w")
        
        # Right: Clock
        self.clock_label = tk.Label(header, text="",
                                     font=(Theme.FONT_MONO, 10),
                                     fg=Theme.SECONDARY, bg=Theme.BG_CARD)
        self.clock_label.pack(side="right", padx=20)
        
        # Separator line
        tk.Frame(self.root, bg=Theme.PRIMARY, height=2).pack(fill="x")
    
    def _build_screen_container(self):
        """Container chứa các màn hình"""
        self.screen_container = tk.Frame(self.root, bg=Theme.BG_DARK)
        self.screen_container.pack(fill="both", expand=True, padx=16, pady=10)
    
    def _build_footer(self):
        """Footer ATM"""
        tk.Frame(self.root, bg=Theme.PRIMARY, height=2).pack(fill="x")
        footer = tk.Frame(self.root, bg=Theme.BG_CARD, height=40)
        footer.pack(fill="x")
        footer.pack_propagate(False)
        tk.Label(footer, text="© 2026 Viet Digital Bank • ATM Simulator v2.0",
                 font=(Theme.FONT_FAMILY, 8),
                 fg=Theme.TEXT_MUTED, bg=Theme.BG_CARD).pack(pady=10)
    
    def _update_clock(self):
        """Cập nhật đồng hồ"""
        now = datetime.now().strftime("%H:%M:%S  •  %d/%m/%Y")
        self.clock_label.config(text=now)
        self.root.after(1000, self._update_clock)
    
    def _clear_screen(self):
        """Xóa toàn bộ nội dung màn hình"""
        for widget in self.screen_container.winfo_children():
            widget.destroy()
    
    def _create_btn(self, parent, text, command, style="primary", width=30, height=2, font_size=11):
        """Tạo nút bấm đẹp"""
        colors = {
            "primary": (Theme.PRIMARY, Theme.TEXT_PRIMARY, Theme.PRIMARY_HOVER),
            "secondary": (Theme.BG_ELEVATED, Theme.TEXT_SECONDARY, Theme.BG_SURFACE),
            "success": (Theme.SUCCESS, Theme.TEXT_PRIMARY, "#059669"),
            "danger": (Theme.DANGER, Theme.TEXT_PRIMARY, "#dc2626"),
            "accent": (Theme.ACCENT, Theme.TEXT_PRIMARY, "#ec4899"),
        }
        bg, fg, hover_bg = colors.get(style, colors["primary"])
        
        btn = tk.Button(parent, text=text, command=command,
                        font=(Theme.FONT_FAMILY, font_size, "bold"),
                        fg=fg, bg=bg, activeforeground=fg, activebackground=hover_bg,
                        relief="flat", cursor="hand2",
                        width=width, height=height, bd=0,
                        highlightthickness=0)
        
        btn.bind("<Enter>", lambda e: btn.config(bg=hover_bg))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg))
        
        return btn
    
    def _create_card(self, parent, **kwargs):
        """Tạo card UI"""
        card = tk.Frame(parent, bg=kwargs.get("bg", Theme.BG_CARD),
                        highlightbackground=Theme.BORDER,
                        highlightthickness=1, bd=0)
        padx = kwargs.get("padx", 20)
        pady = kwargs.get("pady", 15)
        card.pack(fill="x", padx=kwargs.get("outer_padx", 0), 
                  pady=kwargs.get("outer_pady", 8))
        inner = tk.Frame(card, bg=kwargs.get("bg", Theme.BG_CARD))
        inner.pack(fill="x", padx=padx, pady=pady)
        return inner
    
    def _show_toast(self, message, toast_type="info"):
        """Hiển thị thông báo toast"""
        colors = {
            "info": (Theme.PRIMARY, Theme.TEXT_PRIMARY),
            "success": (Theme.SUCCESS, Theme.TEXT_PRIMARY),
            "error": (Theme.DANGER, Theme.TEXT_PRIMARY),
            "warning": (Theme.WARNING, "#000000"),
        }
        bg, fg = colors.get(toast_type, colors["info"])
        
        toast = tk.Toplevel(self.root)
        toast.overrideredirect(True)
        toast.attributes("-topmost", True)
        
        x = self.root.winfo_x() + 60
        y = self.root.winfo_y() + 100
        toast.geometry(f"400x45+{x}+{y}")
        
        frame = tk.Frame(toast, bg=bg)
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text=message, font=(Theme.FONT_FAMILY, 10, "bold"),
                 fg=fg, bg=bg).pack(expand=True)
        
        toast.after(2500, toast.destroy)
    
    # ──────────────────────────────────────────────────
    #  MÀN HÌNH 1: ĐƯA THẺ VÀO
    # ──────────────────────────────────────────────────
    
    def show_screen_insert(self):
        """Màn hình chờ đưa thẻ"""
        self._clear_screen()
        self.current_screen = "insert"
        self.pin_entered = ""
        self.pin_attempts = 0
        
        frame = tk.Frame(self.screen_container, bg=Theme.BG_DARK)
        frame.pack(expand=True)
        
        # Card animation area
        card_frame = tk.Frame(frame, bg=Theme.BG_SURFACE,
                              highlightbackground=Theme.BORDER,
                              highlightthickness=1)
        card_frame.pack(pady=(40, 20))
        
        card_inner = tk.Frame(card_frame, bg=Theme.BG_SURFACE)
        card_inner.pack(padx=40, pady=30)
        
        # Card visual
        tk.Label(card_inner, text="💳", font=(Theme.FONT_FAMILY, 60),
                 bg=Theme.BG_SURFACE).pack()
        
        tk.Label(card_inner, text="•••• •••• •••• ••••",
                 font=(Theme.FONT_MONO, 16, "bold"),
                 fg=Theme.TEXT_MUTED, bg=Theme.BG_SURFACE).pack(pady=(5, 0))
        
        tk.Label(card_inner, text="CARDHOLDER NAME",
                 font=(Theme.FONT_MONO, 9),
                 fg=Theme.TEXT_MUTED, bg=Theme.BG_SURFACE).pack(pady=(5, 0))
        
        # Title
        tk.Label(frame, text="Chào Mừng Đến ATM",
                 font=(Theme.FONT_FAMILY, 22, "bold"),
                 fg=Theme.TEXT_PRIMARY, bg=Theme.BG_DARK).pack(pady=(25, 5))
        
        tk.Label(frame, text="Nhấn nút bên dưới để bắt đầu giao dịch",
                 font=(Theme.FONT_FAMILY, 11),
                 fg=Theme.TEXT_SECONDARY, bg=Theme.BG_DARK).pack(pady=(0, 30))
        
        # Insert button
        btn = self._create_btn(frame, "🏦  Đưa Thẻ Vào Máy", self.show_screen_pin,
                               style="primary", width=28, height=2, font_size=13)
        btn.pack(pady=5)
        
        # Hint
        tk.Label(frame, text="Mã PIN mặc định: 1234",
                 font=(Theme.FONT_FAMILY, 9),
                 fg=Theme.TEXT_MUTED, bg=Theme.BG_DARK).pack(pady=(25, 0))
    
    # ──────────────────────────────────────────────────
    #  MÀN HÌNH 2: NHẬP PIN
    # ──────────────────────────────────────────────────
    
    def show_screen_pin(self):
        """Màn hình nhập mã PIN"""
        self._clear_screen()
        self.current_screen = "pin"
        self.pin_entered = ""
        
        frame = tk.Frame(self.screen_container, bg=Theme.BG_DARK)
        frame.pack(expand=True)
        
        # Lock icon
        tk.Label(frame, text="🔒", font=(Theme.FONT_FAMILY, 36),
                 bg=Theme.BG_DARK).pack(pady=(20, 5))
        
        tk.Label(frame, text="Nhập Mã PIN",
                 font=(Theme.FONT_FAMILY, 20, "bold"),
                 fg=Theme.TEXT_PRIMARY, bg=Theme.BG_DARK).pack(pady=(0, 5))
        
        attempts_left = self.max_attempts - self.pin_attempts
        if self.pin_attempts > 0:
            tk.Label(frame, text=f"⚠ Còn {attempts_left} lần thử",
                     font=(Theme.FONT_FAMILY, 10),
                     fg=Theme.WARNING, bg=Theme.BG_DARK).pack()
        
        # PIN dots display
        self.pin_frame = tk.Frame(frame, bg=Theme.BG_DARK)
        self.pin_frame.pack(pady=20)
        
        self.pin_dots = []
        for i in range(4):
            dot = tk.Label(self.pin_frame, text="○",
                           font=(Theme.FONT_FAMILY, 28),
                           fg=Theme.TEXT_MUTED, bg=Theme.BG_DARK, width=3)
            dot.pack(side="left", padx=5)
            self.pin_dots.append(dot)
        
        # Error label
        self.pin_error_label = tk.Label(frame, text="",
                                         font=(Theme.FONT_FAMILY, 10),
                                         fg=Theme.DANGER, bg=Theme.BG_DARK)
        self.pin_error_label.pack(pady=(0, 10))
        
        # Keypad
        keypad_frame = tk.Frame(frame, bg=Theme.BG_DARK)
        keypad_frame.pack(pady=5)
        
        keys = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["✕", "0", "→"]
        ]
        
        for row in keys:
            row_frame = tk.Frame(keypad_frame, bg=Theme.BG_DARK)
            row_frame.pack(pady=3)
            for key in row:
                if key == "✕":
                    bg_color = Theme.DANGER
                    hover_color = "#dc2626"
                elif key == "→":
                    bg_color = Theme.SUCCESS
                    hover_color = "#059669"
                else:
                    bg_color = Theme.BG_ELEVATED
                    hover_color = Theme.BG_SURFACE
                
                btn = tk.Button(row_frame, text=key, 
                                font=(Theme.FONT_FAMILY, 16, "bold"),
                                width=5, height=2,
                                fg=Theme.TEXT_PRIMARY, bg=bg_color,
                                activeforeground=Theme.TEXT_PRIMARY,
                                activebackground=hover_color,
                                relief="flat", cursor="hand2", bd=0,
                                highlightthickness=0,
                                command=lambda k=key: self._handle_pin_key(k))
                btn.pack(side="left", padx=3)
                btn.bind("<Enter>", lambda e, b=btn, c=hover_color: b.config(bg=c))
                btn.bind("<Leave>", lambda e, b=btn, c=bg_color: b.config(bg=c))
        
        # Cancel button
        self._create_btn(frame, "Hủy Giao Dịch", self.show_screen_insert,
                         style="secondary", width=20, height=1, font_size=10).pack(pady=(15, 0))
    
    def _handle_pin_key(self, key):
        """Xử lý phím bấm PIN"""
        if key == "✕":
            # Clear
            self.pin_entered = ""
            self._update_pin_display()
            self.pin_error_label.config(text="")
        elif key == "→":
            # Enter
            self._verify_pin()
        else:
            # Number
            if len(self.pin_entered) < 4:
                self.pin_entered += key
                self._update_pin_display()
                if len(self.pin_entered) == 4:
                    self.root.after(300, self._verify_pin)
    
    def _update_pin_display(self):
        """Cập nhật hiển thị PIN"""
        for i, dot in enumerate(self.pin_dots):
            if i < len(self.pin_entered):
                dot.config(text="●", fg=Theme.PRIMARY_HOVER)
            else:
                dot.config(text="○", fg=Theme.TEXT_MUTED)
    
    def _verify_pin(self):
        """Xác thực mã PIN"""
        if self.pin_entered == self.account.pin:
            self._show_toast("✅ Đăng nhập thành công!", "success")
            self.pin_attempts = 0
            self.root.after(500, self.show_screen_menu)
        else:
            self.pin_attempts += 1
            if self.pin_attempts >= self.max_attempts:
                self._show_toast("🚫 Thẻ đã bị khóa do nhập sai PIN 3 lần!", "error")
                self.root.after(2000, self.show_screen_insert)
            else:
                self.pin_error_label.config(
                    text=f"❌ Sai mã PIN! Còn {self.max_attempts - self.pin_attempts} lần thử")
                self.pin_entered = ""
                self._update_pin_display()
                # Shake animation
                self._shake_widget(self.pin_frame)
    
    def _shake_widget(self, widget):
        """Hiệu ứng rung khi nhập sai"""
        original_x = widget.winfo_x()
        offsets = [10, -10, 8, -8, 5, -5, 2, -2, 0]
        
        def do_shake(i=0):
            if i < len(offsets):
                widget.place_configure(x=original_x + offsets[i])
                self.root.after(40, lambda: do_shake(i + 1))
        
        # Only shake if using place manager, otherwise just flash color
        for dot in self.pin_dots:
            dot.config(fg=Theme.DANGER)
        self.root.after(500, lambda: [d.config(fg=Theme.TEXT_MUTED) for d in self.pin_dots])
    
    # ──────────────────────────────────────────────────
    #  MÀN HÌNH 3: MENU CHÍNH
    # ──────────────────────────────────────────────────
    
    def show_screen_menu(self):
        """Màn hình menu chính"""
        self._clear_screen()
        self.current_screen = "menu"
        
        frame = tk.Frame(self.screen_container, bg=Theme.BG_DARK)
        frame.pack(fill="both", expand=True)
        
        # Welcome banner
        banner = tk.Frame(frame, bg=Theme.PRIMARY_DARK,
                          highlightbackground=Theme.PRIMARY,
                          highlightthickness=1)
        banner.pack(fill="x", pady=(10, 5))
        banner_inner = tk.Frame(banner, bg=Theme.PRIMARY_DARK)
        banner_inner.pack(fill="x", padx=20, pady=15)
        
        top_row = tk.Frame(banner_inner, bg=Theme.PRIMARY_DARK)
        top_row.pack(fill="x")
        
        tk.Label(top_row, text="👤 Xin chào,",
                 font=(Theme.FONT_FAMILY, 10),
                 fg=Theme.TEXT_ACCENT, bg=Theme.PRIMARY_DARK).pack(anchor="w")
        tk.Label(top_row, text=self.account.holder_name,
                 font=(Theme.FONT_FAMILY, 14, "bold"),
                 fg=Theme.TEXT_PRIMARY, bg=Theme.PRIMARY_DARK).pack(anchor="w")
        
        bal_row = tk.Frame(banner_inner, bg=Theme.PRIMARY_DARK)
        bal_row.pack(fill="x", pady=(10, 0))
        tk.Label(bal_row, text="Số dư khả dụng:",
                 font=(Theme.FONT_FAMILY, 9),
                 fg=Theme.TEXT_ACCENT, bg=Theme.PRIMARY_DARK).pack(side="left")
        tk.Label(bal_row, text=self.account.format_currency(self.account.balance),
                 font=(Theme.FONT_FAMILY, 14, "bold"),
                 fg=Theme.SECONDARY, bg=Theme.PRIMARY_DARK).pack(side="right")
        
        # Menu title
        tk.Label(frame, text="── Chọn Giao Dịch ──",
                 font=(Theme.FONT_FAMILY, 12, "bold"),
                 fg=Theme.TEXT_SECONDARY, bg=Theme.BG_DARK).pack(pady=(15, 10))
        
        # Menu grid
        menu_items = [
            ("💰", "Rút Tiền", self.show_screen_withdraw, "primary"),
            ("🔍", "Kiểm Tra Số Dư", self.show_screen_balance, "accent"),
            ("💸", "Chuyển Khoản", self.show_screen_transfer, "success"),
            ("📋", "Lịch Sử Giao Dịch", self.show_screen_history, "secondary"),
            ("🔐", "Đổi Mã PIN", self.show_screen_changepin, "secondary"),
            ("🚪", "Rút Thẻ & Thoát", self.show_screen_insert, "danger"),
        ]
        
        grid_frame = tk.Frame(frame, bg=Theme.BG_DARK)
        grid_frame.pack(fill="x", padx=10)
        
        for i, (icon, label, cmd, style) in enumerate(menu_items):
            row = i // 2
            col = i % 2
            
            btn_frame = tk.Frame(grid_frame, bg=Theme.BG_DARK)
            btn_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            grid_frame.columnconfigure(col, weight=1)
            
            colors_map = {
                "primary": (Theme.BG_CARD, Theme.PRIMARY_HOVER, Theme.BG_SURFACE),
                "accent": (Theme.BG_CARD, Theme.ACCENT, Theme.BG_SURFACE),
                "success": (Theme.BG_CARD, Theme.SUCCESS, Theme.BG_SURFACE),
                "secondary": (Theme.BG_CARD, Theme.TEXT_SECONDARY, Theme.BG_SURFACE),
                "danger": (Theme.BG_CARD, Theme.DANGER, Theme.BG_SURFACE),
            }
            bg_c, fg_c, hover_c = colors_map[style]
            
            btn = tk.Button(btn_frame, text=f"{icon}\n{label}",
                            font=(Theme.FONT_FAMILY, 10, "bold"),
                            fg=fg_c, bg=bg_c,
                            activeforeground=fg_c,
                            activebackground=hover_c,
                            relief="flat", cursor="hand2",
                            bd=0, highlightthickness=1,
                            highlightbackground=Theme.BORDER,
                            width=18, height=4,
                            command=cmd)
            btn.pack(fill="both", expand=True)
            btn.bind("<Enter>", lambda e, b=btn, c=hover_c: b.config(bg=c))
            btn.bind("<Leave>", lambda e, b=btn, c=bg_c: b.config(bg=c))
    
    # ──────────────────────────────────────────────────
    #  MÀN HÌNH 4: RÚT TIỀN
    # ──────────────────────────────────────────────────
    
    def show_screen_withdraw(self):
        """Màn hình rút tiền"""
        self._clear_screen()
        self.current_screen = "withdraw"
        self.selected_amount = 0
        
        frame = tk.Frame(self.screen_container, bg=Theme.BG_DARK)
        frame.pack(fill="both", expand=True)
        
        # Title
        tk.Label(frame, text="💰 Chọn Số Tiền Rút",
                 font=(Theme.FONT_FAMILY, 18, "bold"),
                 fg=Theme.TEXT_PRIMARY, bg=Theme.BG_DARK).pack(pady=(15, 5))
        
        tk.Label(frame, text=f"Số dư: {self.account.format_currency(self.account.balance)}",
                 font=(Theme.FONT_FAMILY, 11),
                 fg=Theme.SECONDARY, bg=Theme.BG_DARK).pack(pady=(0, 15))
        
        # Quick amounts
        amounts = [
            (100_000, "100.000 ₫"),
            (200_000, "200.000 ₫"),
            (500_000, "500.000 ₫"),
            (1_000_000, "1.000.000 ₫"),
            (2_000_000, "2.000.000 ₫"),
            (5_000_000, "5.000.000 ₫"),
        ]
        
        grid = tk.Frame(frame, bg=Theme.BG_DARK)
        grid.pack(fill="x", padx=20, pady=5)
        
        self.amount_buttons = []
        
        for i, (amount, label) in enumerate(amounts):
            row = i // 2
            col = i % 2
            
            is_popular = amount in (1_000_000, 2_000_000)
            bg = Theme.PRIMARY_DARK if is_popular else Theme.BG_CARD
            fg = Theme.SECONDARY if is_popular else Theme.TEXT_PRIMARY
            border_color = Theme.PRIMARY if is_popular else Theme.BORDER
            
            btn = tk.Button(grid, text=label,
                            font=(Theme.FONT_FAMILY, 12, "bold"),
                            fg=fg, bg=bg,
                            activeforeground=Theme.TEXT_PRIMARY,
                            activebackground=Theme.PRIMARY,
                            relief="flat", cursor="hand2",
                            bd=0, highlightthickness=1,
                            highlightbackground=border_color,
                            height=2,
                            command=lambda a=amount: self._select_amount(a))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            grid.columnconfigure(col, weight=1)
            self.amount_buttons.append((btn, amount, bg))
        
        # Custom amount
        custom_frame = self._create_card(frame)
        tk.Label(custom_frame, text="Hoặc nhập số tiền khác:",
                 font=(Theme.FONT_FAMILY, 10),
                 fg=Theme.TEXT_SECONDARY, bg=Theme.BG_CARD).pack(anchor="w")
        
        input_row = tk.Frame(custom_frame, bg=Theme.BG_CARD)
        input_row.pack(fill="x", pady=(8, 0))
        
        self.custom_amount_entry = tk.Entry(input_row,
                                             font=(Theme.FONT_MONO, 14),
                                             fg=Theme.TEXT_PRIMARY,
                                             bg=Theme.BG_INPUT,
                                             insertbackground=Theme.PRIMARY_HOVER,
                                             relief="flat", bd=0,
                                             highlightthickness=2,
                                             highlightbackground=Theme.BORDER,
                                             highlightcolor=Theme.PRIMARY)
        self.custom_amount_entry.pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 5))
        
        tk.Label(input_row, text="₫", font=(Theme.FONT_FAMILY, 14, "bold"),
                 fg=Theme.TEXT_MUTED, bg=Theme.BG_CARD).pack(side="right")
        
        tk.Label(custom_frame, text="Số tiền phải là bội số của 50.000₫",
                 font=(Theme.FONT_FAMILY, 9),
                 fg=Theme.TEXT_MUTED, bg=Theme.BG_CARD).pack(anchor="w", pady=(5, 0))
        
        # Buttons
        btn_frame = tk.Frame(frame, bg=Theme.BG_DARK)
        btn_frame.pack(fill="x", padx=20, pady=(15, 10))
        
        self._create_btn(btn_frame, "Xác Nhận Rút Tiền", self._confirm_withdraw,
                         style="primary", width=22, font_size=11).pack(side="left", expand=True, padx=3)
        self._create_btn(btn_frame, "Quay Lại", self.show_screen_menu,
                         style="secondary", width=12, font_size=11).pack(side="right", padx=3)
    
    def _select_amount(self, amount):
        """Chọn số tiền nhanh"""
        self.selected_amount = amount
        # Update button visuals
        for btn, btn_amount, original_bg in self.amount_buttons:
            if btn_amount == amount:
                btn.config(bg=Theme.PRIMARY, fg=Theme.TEXT_PRIMARY,
                           highlightbackground=Theme.SECONDARY)
            else:
                is_popular = btn_amount in (1_000_000, 2_000_000)
                bg = Theme.PRIMARY_DARK if is_popular else Theme.BG_CARD
                fg = Theme.SECONDARY if is_popular else Theme.TEXT_PRIMARY
                border = Theme.PRIMARY if is_popular else Theme.BORDER
                btn.config(bg=bg, fg=fg, highlightbackground=border)
        # Clear custom input
        self.custom_amount_entry.delete(0, tk.END)
    
    def _confirm_withdraw(self):
        """Xác nhận số tiền rút"""
        # Check custom amount first
        custom_text = self.custom_amount_entry.get().strip().replace(".", "").replace(",", "")
        
        if custom_text:
            try:
                amount = int(custom_text)
            except ValueError:
                self._show_toast("❌ Số tiền không hợp lệ!", "error")
                return
        elif self.selected_amount > 0:
            amount = self.selected_amount
        else:
            self._show_toast("⚠ Vui lòng chọn hoặc nhập số tiền!", "warning")
            return
        
        # Validations
        if amount <= 0:
            self._show_toast("❌ Số tiền phải lớn hơn 0!", "error")
            return
        if amount % 50_000 != 0:
            self._show_toast("❌ Số tiền phải là bội số của 50.000₫!", "error")
            return
        if amount > self.account.balance:
            self._show_toast("❌ Số dư không đủ!", "error")
            return
        if amount > self.account.daily_limit - self.account.withdrawn_today:
            remaining = self.account.daily_limit - self.account.withdrawn_today
            self._show_toast(f"❌ Vượt hạn mức! Còn lại: {self.account.format_currency(remaining)}", "error")
            return
        if amount > 10_000_000:
            self._show_toast("❌ Tối đa mỗi lần rút: 10.000.000₫!", "error")
            return
        
        self.selected_amount = amount
        self.show_screen_confirm()
    
    # ──────────────────────────────────────────────────
    #  MÀN HÌNH 5: XÁC NHẬN GIAO DỊCH
    # ──────────────────────────────────────────────────
    
    def show_screen_confirm(self):
        """Màn hình xác nhận giao dịch"""
        self._clear_screen()
        self.current_screen = "confirm"
        
        amount = self.selected_amount
        fee = 1_100 if amount < 1_000_000 else 0  # Phí GD nhỏ
        total = amount + fee
        remaining = self.account.balance - total
        
        frame = tk.Frame(self.screen_container, bg=Theme.BG_DARK)
        frame.pack(expand=True)
        
        # Warning icon
        tk.Label(frame, text="⚠️", font=(Theme.FONT_FAMILY, 48),
                 bg=Theme.BG_DARK).pack(pady=(20, 5))
        
        tk.Label(frame, text="Xác Nhận Giao Dịch",
                 font=(Theme.FONT_FAMILY, 20, "bold"),
                 fg=Theme.TEXT_PRIMARY, bg=Theme.BG_DARK).pack(pady=(0, 15))
        
        # Details card
        detail_card = self._create_card(frame, outer_padx=20)
        
        details = [
            ("Số tiền rút:", self.account.format_currency(amount), Theme.TEXT_PRIMARY),
            ("Phí giao dịch:", self.account.format_currency(fee), Theme.WARNING if fee > 0 else Theme.SUCCESS),
        ]
        
        for label, value, color in details:
            row = tk.Frame(detail_card, bg=Theme.BG_CARD)
            row.pack(fill="x", pady=4)
            tk.Label(row, text=label, font=(Theme.FONT_FAMILY, 11),
                     fg=Theme.TEXT_SECONDARY, bg=Theme.BG_CARD).pack(side="left")
            tk.Label(row, text=value, font=(Theme.FONT_FAMILY, 11, "bold"),
                     fg=color, bg=Theme.BG_CARD).pack(side="right")
        
        # Divider
        tk.Frame(detail_card, bg=Theme.BORDER, height=1).pack(fill="x", pady=10)
        
        # Total
        total_row = tk.Frame(detail_card, bg=Theme.BG_CARD)
        total_row.pack(fill="x", pady=4)
        tk.Label(total_row, text="Tổng trừ:", font=(Theme.FONT_FAMILY, 13, "bold"),
                 fg=Theme.TEXT_PRIMARY, bg=Theme.BG_CARD).pack(side="left")
        tk.Label(total_row, text=self.account.format_currency(total),
                 font=(Theme.FONT_FAMILY, 13, "bold"),
                 fg=Theme.ACCENT, bg=Theme.BG_CARD).pack(side="right")
        
        remain_row = tk.Frame(detail_card, bg=Theme.BG_CARD)
        remain_row.pack(fill="x", pady=4)
        tk.Label(remain_row, text="Số dư còn lại:", font=(Theme.FONT_FAMILY, 11),
                 fg=Theme.TEXT_SECONDARY, bg=Theme.BG_CARD).pack(side="left")
        tk.Label(remain_row, text=self.account.format_currency(remaining),
                 font=(Theme.FONT_FAMILY, 11, "bold"),
                 fg=Theme.SUCCESS, bg=Theme.BG_CARD).pack(side="right")
        
        # Store for processing
        self._txn_fee = fee
        self._txn_total = total
        
        # Buttons
        btn_frame = tk.Frame(frame, bg=Theme.BG_DARK)
        btn_frame.pack(fill="x", padx=30, pady=(25, 10))
        
        self._create_btn(btn_frame, "✅ Đồng Ý", self._do_withdraw,
                         style="success", width=15, font_size=12).pack(side="left", expand=True, padx=5)
        self._create_btn(btn_frame, "❌ Hủy Bỏ", self.show_screen_withdraw,
                         style="danger", width=15, font_size=12).pack(side="right", expand=True, padx=5)
    
    # ──────────────────────────────────────────────────
    #  MÀN HÌNH 6: ĐANG XỬ LÝ
    # ──────────────────────────────────────────────────
    
    def _do_withdraw(self):
        """Thực hiện rút tiền"""
        self._clear_screen()
        self.current_screen = "processing"
        
        frame = tk.Frame(self.screen_container, bg=Theme.BG_DARK)
        frame.pack(expand=True)
        
        # Spinner
        self.spinner_label = tk.Label(frame, text="⏳",
                                       font=(Theme.FONT_FAMILY, 56),
                                       bg=Theme.BG_DARK)
        self.spinner_label.pack(pady=(40, 10))
        
        tk.Label(frame, text="Đang Xử Lý Giao Dịch",
                 font=(Theme.FONT_FAMILY, 18, "bold"),
                 fg=Theme.TEXT_PRIMARY, bg=Theme.BG_DARK).pack(pady=(0, 5))
        
        self.processing_msg = tk.Label(frame, text="Vui lòng chờ trong giây lát...",
                                        font=(Theme.FONT_FAMILY, 11),
                                        fg=Theme.TEXT_SECONDARY, bg=Theme.BG_DARK)
        self.processing_msg.pack(pady=(0, 30))
        
        # Processing steps
        steps = ["Xác thực giao dịch", "Kiểm tra số dư", "Xuất tiền"]
        self.step_labels = []
        
        for step_text in steps:
            step_frame = tk.Frame(frame, bg=Theme.BG_DARK)
            step_frame.pack(fill="x", padx=80, pady=5)
            
            icon = tk.Label(step_frame, text="⏸",
                            font=(Theme.FONT_FAMILY, 12),
                            fg=Theme.TEXT_MUTED, bg=Theme.BG_DARK)
            icon.pack(side="left")
            
            label = tk.Label(step_frame, text=step_text,
                             font=(Theme.FONT_FAMILY, 11),
                             fg=Theme.TEXT_MUTED, bg=Theme.BG_DARK)
            label.pack(side="left", padx=(10, 0))
            
            self.step_labels.append((icon, label))
        
        # Animate steps
        self.root.after(800, lambda: self._animate_step(0))
    
    def _animate_step(self, step_index):
        """Animate từng bước xử lý"""
        if step_index >= len(self.step_labels):
            # Done - process the transaction
            self._complete_withdraw()
            return
        
        icon, label = self.step_labels[step_index]
        icon.config(text="⏳", fg=Theme.WARNING)
        label.config(fg=Theme.TEXT_PRIMARY)
        
        messages = [
            "Đang xác thực giao dịch...",
            "Đang kiểm tra số dư tài khoản...",
            "Đang xuất tiền..."
        ]
        self.processing_msg.config(text=messages[step_index])
        
        def complete_step():
            icon.config(text="✅", fg=Theme.SUCCESS)
            label.config(fg=Theme.SUCCESS)
            self.root.after(600, lambda: self._animate_step(step_index + 1))
        
        self.root.after(900, complete_step)
    
    def _complete_withdraw(self):
        """Hoàn tất rút tiền"""
        amount = self.selected_amount
        fee = self._txn_fee
        total = self._txn_total
        
        # Update account
        self.account.balance -= total
        self.account.withdrawn_today += amount
        
        # Record transaction
        txn = self.account.add_transaction(
            "withdraw", amount,
            f"Rút tiền mặt tại ATM (phí: {self.account.format_currency(fee)})"
        )
        self._last_txn = txn
        
        self.root.after(800, self.show_screen_success)
    
    # ──────────────────────────────────────────────────
    #  MÀN HÌNH 7: THÀNH CÔNG
    # ──────────────────────────────────────────────────
    
    def show_screen_success(self):
        """Màn hình giao dịch thành công"""
        self._clear_screen()
        self.current_screen = "success"
        
        frame = tk.Frame(self.screen_container, bg=Theme.BG_DARK)
        frame.pack(expand=True)
        
        # Success icon
        tk.Label(frame, text="✅", font=(Theme.FONT_FAMILY, 64),
                 bg=Theme.BG_DARK).pack(pady=(30, 10))
        
        tk.Label(frame, text="Giao Dịch Thành Công!",
                 font=(Theme.FONT_FAMILY, 22, "bold"),
                 fg=Theme.SUCCESS, bg=Theme.BG_DARK).pack(pady=(0, 10))
        
        # Amount
        tk.Label(frame, text=self.account.format_currency(self.selected_amount),
                 font=(Theme.FONT_FAMILY, 28, "bold"),
                 fg=Theme.TEXT_PRIMARY, bg=Theme.BG_DARK).pack(pady=5)
        
        tk.Label(frame, text="Vui lòng nhận tiền bên dưới 💵",
                 font=(Theme.FONT_FAMILY, 12),
                 fg=Theme.SECONDARY, bg=Theme.BG_DARK).pack(pady=(5, 10))
        
        # Cash animation
        cash_frame = tk.Frame(frame, bg=Theme.SUCCESS_BG,
                               highlightbackground=Theme.SUCCESS,
                               highlightthickness=2)
        cash_frame.pack(padx=60, pady=15)
        cash_inner = tk.Frame(cash_frame, bg=Theme.SUCCESS_BG)
        cash_inner.pack(padx=30, pady=15)
        
        bills_text = "💵 " * min(self.selected_amount // 500_000 + 1, 8)
        tk.Label(cash_inner, text=bills_text,
                 font=(Theme.FONT_FAMILY, 24),
                 bg=Theme.SUCCESS_BG).pack()
        tk.Label(cash_inner, text="── Khe nhận tiền ──",
                 font=(Theme.FONT_FAMILY, 10),
                 fg=Theme.SUCCESS, bg=Theme.SUCCESS_BG).pack(pady=(5, 0))
        
        # Remaining balance
        tk.Label(frame, text=f"Số dư còn lại: {self.account.format_currency(self.account.balance)}",
                 font=(Theme.FONT_FAMILY, 11),
                 fg=Theme.TEXT_MUTED, bg=Theme.BG_DARK).pack(pady=(10, 0))
        
        # Buttons
        btn_frame = tk.Frame(frame, bg=Theme.BG_DARK)
        btn_frame.pack(fill="x", padx=30, pady=(25, 10))
        
        self._create_btn(btn_frame, "🧾 In Biên Lai", self.show_screen_receipt,
                         style="primary", width=15, font_size=11).pack(side="left", expand=True, padx=5)
        self._create_btn(btn_frame, "🔄 Giao Dịch Khác", self.show_screen_menu,
                         style="secondary", width=15, font_size=11).pack(side="right", expand=True, padx=5)
    
    # ──────────────────────────────────────────────────
    #  MÀN HÌNH 8: BIÊN LAI
    # ──────────────────────────────────────────────────
    
    def show_screen_receipt(self):
        """Màn hình in biên lai"""
        self._clear_screen()
        self.current_screen = "receipt"
        
        txn = self._last_txn
        
        frame = tk.Frame(self.screen_container, bg=Theme.BG_DARK)
        frame.pack(fill="both", expand=True)
        
        # Receipt paper
        receipt = tk.Frame(frame, bg="#fef9ef",
                           highlightbackground="#d4c5a0",
                           highlightthickness=2)
        receipt.pack(fill="x", padx=30, pady=(15, 10))
        receipt_inner = tk.Frame(receipt, bg="#fef9ef")
        receipt_inner.pack(fill="x", padx=20, pady=20)
        
        # Receipt content
        lines = [
            ("VIET DIGITAL BANK", ("bold", 14), "#1a1a2e"),
            ("Chi nhánh: ATM Online", ("normal", 9), "#666"),
            ("", ("normal", 6), "#666"),
            ("═══ BIÊN LAI GIAO DỊCH ═══", ("bold", 11), "#333"),
            ("", ("normal", 6), "#666"),
        ]
        
        for text, (weight, size), color in lines:
            tk.Label(receipt_inner, text=text,
                     font=(Theme.FONT_MONO, size, weight),
                     fg=color, bg="#fef9ef").pack()
        
        # Detail rows
        receipt_data = [
            ("Mã GD:", txn["id"]),
            ("Ngày:", txn["datetime"].strftime("%d/%m/%Y")),
            ("Giờ:", txn["datetime"].strftime("%H:%M:%S")),
            ("Thẻ:", self.account.card_display),
            ("─" * 30, ""),
            ("Loại GD:", "Rút tiền mặt"),
            ("Số tiền:", self.account.format_currency(txn["amount"])),
            ("Phí GD:", self.account.format_currency(self._txn_fee)),
            ("─" * 30, ""),
            ("Số dư còn lại:", self.account.format_currency(self.account.balance)),
        ]
        
        for label, value in receipt_data:
            row = tk.Frame(receipt_inner, bg="#fef9ef")
            row.pack(fill="x", pady=1)
            
            if not value:  # Divider
                tk.Label(row, text=label, font=(Theme.FONT_MONO, 8),
                         fg="#999", bg="#fef9ef").pack()
            else:
                tk.Label(row, text=label, font=(Theme.FONT_MONO, 9),
                         fg="#555", bg="#fef9ef").pack(side="left")
                weight = "bold" if "Số tiền" in label or "Số dư" in label else "normal"
                color = "#1a1a2e" if "bold" in weight else "#333"
                tk.Label(row, text=value, font=(Theme.FONT_MONO, 9, weight),
                         fg=color, bg="#fef9ef").pack(side="right")
        
        # Footer
        tk.Label(receipt_inner, text="", font=(Theme.FONT_MONO, 4),
                 bg="#fef9ef").pack()
        tk.Label(receipt_inner, text="Cảm ơn quý khách đã sử dụng",
                 font=(Theme.FONT_MONO, 8), fg="#666", bg="#fef9ef").pack()
        tk.Label(receipt_inner, text="dịch vụ của chúng tôi!",
                 font=(Theme.FONT_MONO, 8), fg="#666", bg="#fef9ef").pack()
        tk.Label(receipt_inner, text="Hotline: 1900-xxxx",
                 font=(Theme.FONT_MONO, 8, "bold"), fg="#999", bg="#fef9ef").pack(pady=(5, 0))
        
        # Buttons
        btn_frame = tk.Frame(frame, bg=Theme.BG_DARK)
        btn_frame.pack(fill="x", padx=30, pady=(15, 10))
        
        self._create_btn(btn_frame, "🔄 Giao Dịch Khác", self.show_screen_menu,
                         style="primary", width=16, font_size=11).pack(side="left", expand=True, padx=5)
        self._create_btn(btn_frame, "🚪 Rút Thẻ & Thoát", self.show_screen_insert,
                         style="danger", width=16, font_size=11).pack(side="right", expand=True, padx=5)
    
    # ──────────────────────────────────────────────────
    #  MÀN HÌNH 9: KIỂM TRA SỐ DƯ
    # ──────────────────────────────────────────────────
    
    def show_screen_balance(self):
        """Màn hình kiểm tra số dư"""
        self._clear_screen()
        self.current_screen = "balance"
        self.balance_visible = False
        
        frame = tk.Frame(self.screen_container, bg=Theme.BG_DARK)
        frame.pack(fill="both", expand=True)
        
        # Balance card
        card = tk.Frame(frame, bg=Theme.PRIMARY_DARK,
                        highlightbackground=Theme.PRIMARY,
                        highlightthickness=2)
        card.pack(fill="x", padx=20, pady=(20, 10))
        card_inner = tk.Frame(card, bg=Theme.PRIMARY_DARK)
        card_inner.pack(fill="x", padx=25, pady=25)
        
        # Header row
        header_row = tk.Frame(card_inner, bg=Theme.PRIMARY_DARK)
        header_row.pack(fill="x")
        
        tk.Label(header_row, text="💳 Số Dư Tài Khoản",
                 font=(Theme.FONT_FAMILY, 12),
                 fg=Theme.TEXT_ACCENT, bg=Theme.PRIMARY_DARK).pack(side="left")
        
        self.toggle_btn = tk.Button(header_row, text="👁",
                                      font=(Theme.FONT_FAMILY, 14),
                                      fg=Theme.TEXT_ACCENT, bg=Theme.PRIMARY_DARK,
                                      activeforeground=Theme.TEXT_PRIMARY,
                                      activebackground=Theme.PRIMARY,
                                      relief="flat", cursor="hand2", bd=0,
                                      command=self._toggle_balance)
        self.toggle_btn.pack(side="right")
        
        # Balance amount
        self.balance_display = tk.Label(card_inner, text="••••••••• ₫",
                                         font=(Theme.FONT_FAMILY, 28, "bold"),
                                         fg=Theme.TEXT_PRIMARY, bg=Theme.PRIMARY_DARK)
        self.balance_display.pack(anchor="w", pady=(15, 10))
        
        # Account info
        info_row = tk.Frame(card_inner, bg=Theme.PRIMARY_DARK)
        info_row.pack(fill="x")
        
        left_info = tk.Frame(info_row, bg=Theme.PRIMARY_DARK)
        left_info.pack(side="left")
        tk.Label(left_info, text="Số tài khoản",
                 font=(Theme.FONT_FAMILY, 9), fg=Theme.TEXT_MUTED,
                 bg=Theme.PRIMARY_DARK).pack(anchor="w")
        tk.Label(left_info, text=f"****{self.account.account_number[-4:]}",
                 font=(Theme.FONT_MONO, 11, "bold"), fg=Theme.TEXT_PRIMARY,
                 bg=Theme.PRIMARY_DARK).pack(anchor="w")
        
        right_info = tk.Frame(info_row, bg=Theme.PRIMARY_DARK)
        right_info.pack(side="right")
        tk.Label(right_info, text="Loại TK",
                 font=(Theme.FONT_FAMILY, 9), fg=Theme.TEXT_MUTED,
                 bg=Theme.PRIMARY_DARK).pack(anchor="e")
        tk.Label(right_info, text="Thanh toán",
                 font=(Theme.FONT_MONO, 11, "bold"), fg=Theme.TEXT_PRIMARY,
                 bg=Theme.PRIMARY_DARK).pack(anchor="e")
        
        # Details
        detail_card = self._create_card(frame, outer_padx=20)
        
        details = [
            ("Số dư khả dụng", "••••••••• ₫", "balance_avail"),
            ("Số dư đóng băng", self.account.format_currency(self.account.frozen), None),
            ("Hạn mức rút/ngày", self.account.format_currency(self.account.daily_limit), None),
            ("Đã rút hôm nay", self.account.format_currency(self.account.withdrawn_today), None),
        ]
        
        self.balance_detail_labels = {}
        
        for label, value, key in details:
            row = tk.Frame(detail_card, bg=Theme.BG_CARD)
            row.pack(fill="x", pady=5)
            tk.Label(row, text=label, font=(Theme.FONT_FAMILY, 10),
                     fg=Theme.TEXT_SECONDARY, bg=Theme.BG_CARD).pack(side="left")
            val_label = tk.Label(row, text=value,
                                 font=(Theme.FONT_FAMILY, 10, "bold"),
                                 fg=Theme.TEXT_PRIMARY, bg=Theme.BG_CARD)
            val_label.pack(side="right")
            if key:
                self.balance_detail_labels[key] = val_label
        
        # Back button
        self._create_btn(frame, "Quay Lại Menu", self.show_screen_menu,
                         style="secondary", width=20, font_size=11).pack(pady=(20, 10))
    
    def _toggle_balance(self):
        """Ẩn/hiện số dư"""
        self.balance_visible = not self.balance_visible
        if self.balance_visible:
            self.balance_display.config(text=self.account.format_currency(self.account.balance))
            self.toggle_btn.config(text="🙈")
            if "balance_avail" in self.balance_detail_labels:
                self.balance_detail_labels["balance_avail"].config(
                    text=self.account.format_currency(self.account.balance))
        else:
            self.balance_display.config(text="••••••••• ₫")
            self.toggle_btn.config(text="👁")
            if "balance_avail" in self.balance_detail_labels:
                self.balance_detail_labels["balance_avail"].config(text="••••••••• ₫")
    
    # ──────────────────────────────────────────────────
    #  MÀN HÌNH 10: LỊCH SỬ GIAO DỊCH
    # ──────────────────────────────────────────────────
    
    def show_screen_history(self):
        """Màn hình lịch sử giao dịch"""
        self._clear_screen()
        self.current_screen = "history"
        
        frame = tk.Frame(self.screen_container, bg=Theme.BG_DARK)
        frame.pack(fill="both", expand=True)
        
        tk.Label(frame, text="📋 Lịch Sử Giao Dịch",
                 font=(Theme.FONT_FAMILY, 18, "bold"),
                 fg=Theme.TEXT_PRIMARY, bg=Theme.BG_DARK).pack(pady=(15, 10))
        
        if not self.account.transactions:
            # Empty state
            empty_frame = tk.Frame(frame, bg=Theme.BG_DARK)
            empty_frame.pack(expand=True)
            tk.Label(empty_frame, text="📭",
                     font=(Theme.FONT_FAMILY, 48),
                     bg=Theme.BG_DARK).pack(pady=(20, 10))
            tk.Label(empty_frame, text="Chưa có giao dịch nào",
                     font=(Theme.FONT_FAMILY, 13),
                     fg=Theme.TEXT_MUTED, bg=Theme.BG_DARK).pack()
            tk.Label(empty_frame, text="Các giao dịch sẽ xuất hiện ở đây",
                     font=(Theme.FONT_FAMILY, 10),
                     fg=Theme.TEXT_MUTED, bg=Theme.BG_DARK).pack(pady=(5, 0))
        else:
            # Scrollable list with canvas
            list_frame = tk.Frame(frame, bg=Theme.BG_DARK)
            list_frame.pack(fill="both", expand=True, padx=10)
            
            canvas = tk.Canvas(list_frame, bg=Theme.BG_DARK,
                               highlightthickness=0, bd=0)
            scrollbar = tk.Scrollbar(list_frame, orient="vertical",
                                      command=canvas.yview)
            scrollable = tk.Frame(canvas, bg=Theme.BG_DARK)
            
            scrollable.bind("<Configure>",
                            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
            canvas.create_window((0, 0), window=scrollable, anchor="nw",
                                 width=460)
            canvas.configure(yscrollcommand=scrollbar.set)
            
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            
            # Bind mouse wheel
            def on_mousewheel(event):
                canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            canvas.bind_all("<MouseWheel>", on_mousewheel)
            
            for txn in self.account.transactions[:20]:
                txn_card = tk.Frame(scrollable, bg=Theme.BG_CARD,
                                     highlightbackground=Theme.BORDER,
                                     highlightthickness=1)
                txn_card.pack(fill="x", pady=4, padx=5)
                txn_inner = tk.Frame(txn_card, bg=Theme.BG_CARD)
                txn_inner.pack(fill="x", padx=15, pady=10)
                
                # Top row
                top = tk.Frame(txn_inner, bg=Theme.BG_CARD)
                top.pack(fill="x")
                
                type_icons = {
                    "withdraw": ("💰 Rút tiền", Theme.DANGER),
                    "transfer": ("💸 Chuyển khoản", Theme.WARNING),
                }
                icon_text, type_color = type_icons.get(
                    txn["type"], ("📝 Giao dịch", Theme.TEXT_SECONDARY))
                
                tk.Label(top, text=icon_text,
                         font=(Theme.FONT_FAMILY, 10, "bold"),
                         fg=type_color, bg=Theme.BG_CARD).pack(side="left")
                tk.Label(top, text=f"-{self.account.format_currency(txn['amount'])}",
                         font=(Theme.FONT_FAMILY, 11, "bold"),
                         fg=Theme.DANGER, bg=Theme.BG_CARD).pack(side="right")
                
                # Bottom row
                bottom = tk.Frame(txn_inner, bg=Theme.BG_CARD)
                bottom.pack(fill="x", pady=(4, 0))
                
                tk.Label(bottom, text=txn["id"],
                         font=(Theme.FONT_MONO, 8),
                         fg=Theme.TEXT_MUTED, bg=Theme.BG_CARD).pack(side="left")
                tk.Label(bottom, text=txn["datetime"].strftime("%d/%m/%Y %H:%M"),
                         font=(Theme.FONT_MONO, 8),
                         fg=Theme.TEXT_MUTED, bg=Theme.BG_CARD).pack(side="right")
        
        # Back button
        self._create_btn(frame, "Quay Lại Menu", self.show_screen_menu,
                         style="secondary", width=20, font_size=11).pack(pady=(10, 10))
    
    # ──────────────────────────────────────────────────
    #  MÀN HÌNH 11: CHUYỂN KHOẢN
    # ──────────────────────────────────────────────────
    
    def show_screen_transfer(self):
        """Màn hình chuyển khoản"""
        self._clear_screen()
        self.current_screen = "transfer"
        
        frame = tk.Frame(self.screen_container, bg=Theme.BG_DARK)
        frame.pack(fill="both", expand=True)
        
        tk.Label(frame, text="💸 Chuyển Khoản",
                 font=(Theme.FONT_FAMILY, 18, "bold"),
                 fg=Theme.TEXT_PRIMARY, bg=Theme.BG_DARK).pack(pady=(15, 15))
        
        form_card = self._create_card(frame, outer_padx=15)
        
        # Form fields
        fields = [
            ("Số tài khoản người nhận", "Nhập số tài khoản..."),
            ("Tên người nhận", "Nhập tên người nhận..."),
            ("Số tiền chuyển (₫)", "Nhập số tiền..."),
            ("Nội dung chuyển khoản", "Nội dung..."),
        ]
        
        self.transfer_entries = []
        
        for label, placeholder in fields:
            tk.Label(form_card, text=label,
                     font=(Theme.FONT_FAMILY, 10, "bold"),
                     fg=Theme.TEXT_SECONDARY, bg=Theme.BG_CARD).pack(anchor="w", pady=(10, 3))
            
            entry = tk.Entry(form_card,
                             font=(Theme.FONT_FAMILY, 12),
                             fg=Theme.TEXT_PRIMARY, bg=Theme.BG_INPUT,
                             insertbackground=Theme.PRIMARY_HOVER,
                             relief="flat", bd=0,
                             highlightthickness=2,
                             highlightbackground=Theme.BORDER,
                             highlightcolor=Theme.PRIMARY)
            entry.pack(fill="x", ipady=8)
            
            # Placeholder
            entry.insert(0, placeholder)
            entry.config(fg=Theme.TEXT_MUTED)
            
            def on_focus_in(e, ent=entry, ph=placeholder):
                if ent.get() == ph:
                    ent.delete(0, tk.END)
                    ent.config(fg=Theme.TEXT_PRIMARY)
            
            def on_focus_out(e, ent=entry, ph=placeholder):
                if not ent.get():
                    ent.insert(0, ph)
                    ent.config(fg=Theme.TEXT_MUTED)
            
            entry.bind("<FocusIn>", on_focus_in)
            entry.bind("<FocusOut>", on_focus_out)
            
            self.transfer_entries.append((entry, placeholder))
        
        # Buttons
        btn_frame = tk.Frame(frame, bg=Theme.BG_DARK)
        btn_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        self._create_btn(btn_frame, "💸 Chuyển Khoản", self._do_transfer,
                         style="success", width=16, font_size=11).pack(side="left", expand=True, padx=5)
        self._create_btn(btn_frame, "Quay Lại", self.show_screen_menu,
                         style="secondary", width=12, font_size=11).pack(side="right", padx=5)
    
    def _do_transfer(self):
        """Thực hiện chuyển khoản"""
        values = []
        for entry, placeholder in self.transfer_entries:
            val = entry.get().strip()
            if val == placeholder or not val:
                self._show_toast("⚠ Vui lòng điền đầy đủ thông tin!", "warning")
                return
            values.append(val)
        
        account_num, name, amount_str, note = values
        
        try:
            amount = int(amount_str.replace(".", "").replace(",", ""))
        except ValueError:
            self._show_toast("❌ Số tiền không hợp lệ!", "error")
            return
        
        if amount <= 0:
            self._show_toast("❌ Số tiền phải lớn hơn 0!", "error")
            return
        if amount > self.account.balance:
            self._show_toast("❌ Số dư không đủ!", "error")
            return
        
        # Confirm
        confirm = messagebox.askyesno(
            "Xác nhận chuyển khoản",
            f"Bạn có chắc chắn muốn chuyển\n"
            f"{self.account.format_currency(amount)}\n"
            f"đến tài khoản {account_num}\n"
            f"({name})?\n\n"
            f"Nội dung: {note}")
        
        if confirm:
            self.account.balance -= amount
            self.account.add_transaction(
                "transfer", amount,
                f"Chuyển khoản đến {name} ({account_num}): {note}")
            self._show_toast("✅ Chuyển khoản thành công!", "success")
            self.root.after(1500, self.show_screen_menu)
    
    # ──────────────────────────────────────────────────
    #  MÀN HÌNH 12: ĐỔI MÃ PIN
    # ──────────────────────────────────────────────────
    
    def show_screen_changepin(self):
        """Màn hình đổi mã PIN"""
        self._clear_screen()
        self.current_screen = "changepin"
        
        frame = tk.Frame(self.screen_container, bg=Theme.BG_DARK)
        frame.pack(expand=True)
        
        tk.Label(frame, text="🔐", font=(Theme.FONT_FAMILY, 36),
                 bg=Theme.BG_DARK).pack(pady=(20, 5))
        
        tk.Label(frame, text="Đổi Mã PIN",
                 font=(Theme.FONT_FAMILY, 20, "bold"),
                 fg=Theme.TEXT_PRIMARY, bg=Theme.BG_DARK).pack(pady=(0, 20))
        
        form_card = self._create_card(frame, outer_padx=30)
        
        pin_fields = [
            ("Mã PIN hiện tại", "old_pin"),
            ("Mã PIN mới", "new_pin"),
            ("Xác nhận PIN mới", "confirm_pin"),
        ]
        
        self.pin_change_entries = {}
        
        for label, key in pin_fields:
            tk.Label(form_card, text=label,
                     font=(Theme.FONT_FAMILY, 10, "bold"),
                     fg=Theme.TEXT_SECONDARY, bg=Theme.BG_CARD).pack(anchor="w", pady=(10, 3))
            
            entry = tk.Entry(form_card,
                             font=(Theme.FONT_MONO, 18),
                             fg=Theme.TEXT_PRIMARY, bg=Theme.BG_INPUT,
                             insertbackground=Theme.PRIMARY_HOVER,
                             relief="flat", bd=0, show="●",
                             highlightthickness=2,
                             highlightbackground=Theme.BORDER,
                             highlightcolor=Theme.PRIMARY,
                             justify="center")
            entry.pack(fill="x", ipady=8)
            entry.config(validate="key",
                         validatecommand=(self.root.register(
                             lambda p: len(p) <= 4 and (p.isdigit() or p == "")), "%P"))
            self.pin_change_entries[key] = entry
        
        # Error message
        self.pin_change_error = tk.Label(form_card, text="",
                                          font=(Theme.FONT_FAMILY, 10),
                                          fg=Theme.DANGER, bg=Theme.BG_CARD)
        self.pin_change_error.pack(pady=(10, 0))
        
        # Buttons
        btn_frame = tk.Frame(frame, bg=Theme.BG_DARK)
        btn_frame.pack(fill="x", padx=40, pady=(20, 10))
        
        self._create_btn(btn_frame, "Đổi PIN", self._do_change_pin,
                         style="primary", width=14, font_size=11).pack(side="left", expand=True, padx=5)
        self._create_btn(btn_frame, "Quay Lại", self.show_screen_menu,
                         style="secondary", width=14, font_size=11).pack(side="right", expand=True, padx=5)
    
    def _do_change_pin(self):
        """Thực hiện đổi mã PIN"""
        old = self.pin_change_entries["old_pin"].get()
        new = self.pin_change_entries["new_pin"].get()
        confirm = self.pin_change_entries["confirm_pin"].get()
        
        if old != self.account.pin:
            self.pin_change_error.config(text="❌ Mã PIN hiện tại không đúng!")
            return
        if len(new) != 4:
            self.pin_change_error.config(text="❌ Mã PIN mới phải có 4 chữ số!")
            return
        if new != confirm:
            self.pin_change_error.config(text="❌ Mã PIN xác nhận không khớp!")
            return
        if new == old:
            self.pin_change_error.config(text="❌ Mã PIN mới phải khác PIN cũ!")
            return
        
        self.account.pin = new
        self._show_toast("✅ Đổi mã PIN thành công!", "success")
        self.root.after(1500, self.show_screen_menu)
    
    # ──────────────────────────────────────────────────
    #  CHẠY ỨNG DỤNG
    # ──────────────────────────────────────────────────
    
    def run(self):
        """Khởi chạy ứng dụng ATM"""
        self.root.mainloop()


# ════════════════════════════════════════════════════════
#  ENTRY POINT
# ════════════════════════════════════════════════════════

if __name__ == "__main__":
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    print("[ATM] He Thong ATM - Viet Digital Bank")
    print("[ATM] Dang khoi dong giao dien...")
    
    app = ATMApp()
    app.run()
