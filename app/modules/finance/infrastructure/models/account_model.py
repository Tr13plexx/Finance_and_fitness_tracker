# app/modules/finance/infrastructure/models/account_model.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.shared.infrastructure.db import Base

class AccountModel(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=False)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    currency = Column(String(3), nullable=False, default="RUB")

    transactions = relationship("TransactionModel", back_populates="account")

