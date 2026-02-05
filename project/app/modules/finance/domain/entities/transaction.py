# app/modules/finance/domain/entities/transaction.py
from dataclasses import dataclass
from datetime import datetime
from app.modules.finance.domain.value_objects.money import Money

@dataclass
class Transaction:
    id: int | None
    user_id: int
    account_id: int
    category_id: int | None
    money: Money
    type: str      # "income" или "expense"
    made_at: datetime
    description: str | None = None
