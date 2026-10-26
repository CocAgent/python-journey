"""Core logic for a small JSON-backed expense tracker."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
import json


@dataclass(frozen=True)
class Transaction:
    transaction_id: int
    description: str
    amount: float
    category: str
    transaction_date: str

    def __post_init__(self) -> None:
        if self.transaction_id < 1:
            raise ValueError("ID giao dịch phải lớn hơn 0.")
        if not self.description.strip():
            raise ValueError("Mô tả không được để trống.")
        if self.amount <= 0:
            raise ValueError("Số tiền phải lớn hơn 0.")
        if not self.category.strip():
            raise ValueError("Danh mục không được để trống.")
        date.fromisoformat(self.transaction_date)


def add_transaction(
    transactions: list[Transaction],
    description: str,
    amount: float,
    category: str,
    transaction_date: str | None = None,
) -> Transaction:
    """Validate and append a transaction, returning the new record."""
    next_id = max((item.transaction_id for item in transactions), default=0) + 1
    item = Transaction(
        transaction_id=next_id,
        description=description.strip(),
        amount=float(amount),
        category=category.strip(),
        transaction_date=transaction_date or date.today().isoformat(),
    )
    transactions.append(item)
    return item


def total_expenses(transactions: list[Transaction]) -> float:
    return sum(item.amount for item in transactions)


def filter_by_category(
    transactions: list[Transaction], category: str
) -> list[Transaction]:
    target = category.strip().casefold()
    return [item for item in transactions if item.category.casefold() == target]


def save_transactions(path: Path, transactions: list[Transaction]) -> None:
    """Persist records as readable UTF-8 JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = [asdict(item) for item in transactions]
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def load_transactions(path: Path) -> list[Transaction]:
    """Load records; a missing file means an empty tracker."""
    if not path.exists():
        return []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"File JSON không hợp lệ: {path}") from exc
    if not isinstance(payload, list):
        raise ValueError("Dữ liệu phải là một danh sách giao dịch.")
    try:
        return [Transaction(**row) for row in payload]
    except (TypeError, ValueError, KeyError) as exc:
        raise ValueError("Dữ liệu giao dịch bị thiếu hoặc không hợp lệ.") from exc
