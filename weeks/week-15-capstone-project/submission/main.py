"""Console interface for the Personal Expense Tracker capstone."""
from pathlib import Path

from expense_tracker import add_expense, filter_expenses, load_expenses, save_expenses, total_expenses

DATA_FILE = Path(__file__).with_name("expenses.json")


def show_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    for item in expenses:
        print(f'#{item["id"]} | {item["description"]} | {item["category"]} | {item["amount"]:,} VND')


def read_amount():
    while True:
        try:
            amount = int(input("Amount (VND): ").strip())
            if amount <= 0:
                raise ValueError("amount must be greater than zero")
            return amount
        except ValueError as error:
            print(f"Invalid amount: {error}")


def main():
    try:
        expenses = load_expenses(DATA_FILE)
    except ValueError as error:
        print(f"Cannot load saved data: {error}")
        return

    while True:
        print("\n=== PERSONAL EXPENSE TRACKER ===")
        print("1. Add expense")
        print("2. List expenses")
        print("3. Show total")
        print("4. Filter by category")
        print("5. Save and exit")
        choice = input("Choose 1-5: ").strip()

        if choice == "1":
            description = input("Description: ").strip()
            category = input("Category: ").strip()
            amount = read_amount()
            try:
                add_expense(expenses, description, amount, category)
            except ValueError as error:
                print(f"Invalid expense: {error}")
            else:
                print("Expense added.")
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            print(f"Total expenses: {total_expenses(expenses):,} VND")
        elif choice == "4":
            category = input("Category to find: ")
            show_expenses(filter_expenses(expenses, category))
        elif choice == "5":
            save_expenses(DATA_FILE, expenses)
            print(f"Saved {len(expenses)} expense(s). Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
