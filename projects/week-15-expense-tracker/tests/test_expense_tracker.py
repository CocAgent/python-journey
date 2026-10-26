"""Tests for the Expense Tracker core logic."""
import json
from pathlib import Path

import pytest

from src.expense_tracker import (
    Transaction,
    add_transaction,
    filter_by_category,
    load_transactions,
    save_transactions,
    total_expenses,
)


def sample_transactions():
    return [
        Transaction(1, "Lunch", 45000, "Food", "2026-10-01"),
        Transaction(2, "Bus", 12000, "Transport", "2026-10-02"),
    ]


def test_add_transaction_assigns_next_id():
    items = sample_transactions()
    item = add_transaction(items, "Coffee", 20000, "Food", "2026-10-03")
    assert item.transaction_id == 3
    assert len(items) == 3


def test_rejects_blank_description():
    with pytest.raises(ValueError, match="Mô tả"):
        add_transaction([], "   ", 10000, "Food", "2026-10-01")


def test_rejects_non_positive_amount():
    with pytest.raises(ValueError, match="Số tiền"):
        add_transaction([], "Lunch", 0, "Food", "2026-10-01")


def test_total_of_empty_list_is_zero():
    assert total_expenses([]) == 0


def test_total_expenses():
    assert total_expenses(sample_transactions()) == 57000


def test_category_filter_is_case_insensitive():
    items = filter_by_category(sample_transactions(), "fOoD")
    assert [item.description for item in items] == ["Lunch"]


def test_save_and_load_round_trip(tmp_path: Path):
    path = tmp_path / "data" / "transactions.json"
    original = sample_transactions()
    save_transactions(path, original)
    assert load_transactions(path) == original


def test_missing_file_returns_empty_list(tmp_path: Path):
    assert load_transactions(tmp_path / "missing.json") == []


def test_malformed_json_raises_clear_error(tmp_path: Path):
    path = tmp_path / "broken.json"
    path.write_text("{not json", encoding="utf-8")
    with pytest.raises(ValueError, match="JSON"):
        load_transactions(path)


def test_non_list_json_is_rejected(tmp_path: Path):
    path = tmp_path / "object.json"
    path.write_text(json.dumps({"id": 1}), encoding="utf-8")
    with pytest.raises(ValueError, match="danh sách"):
        load_transactions(path)
