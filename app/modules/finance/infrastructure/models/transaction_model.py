# app/modules/finance/infrastructure/models/transaction_model.py
from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.shared.infrastructure.db import Base

class TransactionModel(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=False)

    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)

    amount = Column(Numeric(12, 2), nullable=False)
    currency = Column(String(3), nullable=False, default="RUB")
    type = Column(String, nullable=False)  # "income" или "expense"

    made_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    description = Column(String, nullable=True)

    account = relationship("AccountModel", back_populates="transactions")
