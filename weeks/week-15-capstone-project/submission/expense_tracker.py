"""Core logic and JSON persistence for the Personal Expense Tracker."""
import json
from pathlib import Path


def add_expense(expenses, description, amount, category):
    description = description.strip()
    category = category.strip()
    if not description:
        raise ValueError("description cannot be empty")
    if not category:
        raise ValueError("category cannot be empty")
    if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount <= 0:
        raise ValueError("amount must be a positive number")
    expense = {
        "id": max((item["id"] for item in expenses), default=0) + 1,
        "description": description,
        "amount": int(amount),
        "category": category,
    }
    expenses.append(expense)
    return expense


def total_expenses(expenses):
    return sum(item["amount"] for item in expenses)


def filter_expenses(expenses, category):
    target = category.strip().casefold()
    return [item for item in expenses if item["category"].casefold() == target]


def save_expenses(path, expenses):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(expenses, ensure_ascii=False, indent=2), encoding="utf-8")


def load_expenses(path):
    path = Path(path)
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError("expense file contains invalid JSON") from error
    if not isinstance(data, list):
        raise ValueError("expense data must be a list")
    for item in data:
        if not isinstance(item, dict) or not {"id", "description", "amount", "category"} <= item.keys():
            raise ValueError("expense record is missing required fields")
        if not isinstance(item["id"], int) or item["id"] < 1:
            raise ValueError("expense ID must be a positive integer")
        if not isinstance(item["description"], str) or not item["description"].strip():
            raise ValueError("expense description cannot be empty")
        if not isinstance(item["category"], str) or not item["category"].strip():
            raise ValueError("expense category cannot be empty")
        if not isinstance(item["amount"], (int, float)) or isinstance(item["amount"], bool) or item["amount"] <= 0:
            raise ValueError("expense amount must be positive")
    return data
