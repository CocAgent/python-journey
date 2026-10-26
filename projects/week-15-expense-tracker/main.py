"""Console interface for the Week 15 Expense Tracker capstone."""
from pathlib import Path

from src.expense_tracker import (
    Transaction,
    add_transaction,
    category_totals,
    filter_by_category,
    largest_transaction,
    load_transactions,
    monthly_total,
    save_transactions,
    total_expenses,
)

DATA_FILE = Path(__file__).parent / "data" / "transactions.json"


def ask_amount() -> float:
    while True:
        raw = input("Số tiền (VNĐ): ").strip()
        try:
            amount = float(raw)
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")
            continue
        if amount <= 0:
            print("Số tiền phải lớn hơn 0.")
            continue
        return amount


def show_transactions(transactions: list[Transaction]) -> None:
    if not transactions:
        print("Chưa có giao dịch.")
        return
    for item in transactions:
        print(
            f"#{item.transaction_id} | {item.transaction_date} | "
            f"{item.description} | {item.category} | {item.amount:,.0f} VNĐ"
        )


def show_report(transactions: list[Transaction]) -> None:
    raw_year = input("Năm (YYYY): ").strip()
    raw_month = input("Tháng (1-12): ").strip()
    try:
        year = int(raw_year)
        month = int(raw_month)
        month_total = monthly_total(transactions, year, month)
    except ValueError as exc:
        print(f"Năm/tháng không hợp lệ: {exc}")
        return

    print(f"Tổng chi tiêu tháng {month:02d}/{year}: {month_total:,.0f} VNĐ")
    print("Tổng theo danh mục:")
    totals = category_totals(transactions)
    if not totals:
        print("- Chưa có giao dịch.")
    else:
        for category, amount in totals.items():
            print(f"- {category}: {amount:,.0f} VNĐ")
    largest = largest_transaction(transactions)
    if largest is None:
        print("Giao dịch lớn nhất: chưa có dữ liệu.")
    else:
        print(
            f"Giao dịch lớn nhất: {largest.description} — "
            f"{largest.amount:,.0f} VNĐ ({largest.transaction_date})"
        )


def main() -> None:
    try:
        transactions = load_transactions(DATA_FILE)
    except ValueError as exc:
        print(f"Không thể đọc dữ liệu: {exc}")
        return

    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Thêm giao dịch")
        print("2. Xem giao dịch")
        print("3. Xem tổng chi tiêu")
        print("4. Lọc theo danh mục")
        print("5. Báo cáo theo tháng")
        print("6. Lưu và thoát")
        choice = input("Chọn (1-6): ").strip()

        if choice == "1":
            description = input("Mô tả: ").strip()
            category = input("Danh mục: ").strip()
            amount = ask_amount()
            try:
                item = add_transaction(transactions, description, amount, category)
            except ValueError as exc:
                print(f"Dữ liệu không hợp lệ: {exc}")
            else:
                print(f"Đã thêm giao dịch #{item.transaction_id}.")
        elif choice == "2":
            show_transactions(transactions)
        elif choice == "3":
            print(f"Tổng chi tiêu: {total_expenses(transactions):,.0f} VNĐ")
        elif choice == "4":
            category = input("Danh mục cần lọc: ")
            show_transactions(filter_by_category(transactions, category))
        elif choice == "5":
            show_report(transactions)
        elif choice == "6":
            save_transactions(DATA_FILE, transactions)
            print(f"Đã lưu {len(transactions)} giao dịch tại {DATA_FILE}.")
            break
        else:
            print("Lựa chọn không hợp lệ. Hãy nhập từ 1 đến 6.")


if __name__ == "__main__":
    main()
