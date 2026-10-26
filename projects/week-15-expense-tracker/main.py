"""Console interface for the Week 15 Expense Tracker capstone."""
from pathlib import Path

from src.expense_tracker import (
    Transaction,
    add_transaction,
    filter_by_category,
    load_transactions,
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
        print("5. Lưu và thoát")
        choice = input("Chọn (1-5): ").strip()

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
            save_transactions(DATA_FILE, transactions)
            print(f"Đã lưu {len(transactions)} giao dịch tại {DATA_FILE}.")
            break
        else:
            print("Lựa chọn không hợp lệ. Hãy nhập từ 1 đến 5.")


if __name__ == "__main__":
    main()
