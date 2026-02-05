# app/modules/finance/domain/value_objects/money.py
from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: str

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Amount must be non-negative")
        if len(self.currency) != 3:
            raise ValueError("Currency must be ISO code like 'USD'")
