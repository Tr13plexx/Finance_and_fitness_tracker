# schemas.py
from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal

class TransactionCreate(BaseModel):
    account_id: int
    category_id: int | None = None
    amount: Decimal = Field(gt=0)
    currency: str = "RUB"
    type: str  # "income" или "expense"
    made_at: datetime
    description: str | None = None

class TransactionRead(BaseModel):
    id: int
    account_id: int
    category_id: int | None
    amount: float
    currency: str
    type: str
    made_at: datetime
    description: str | None
