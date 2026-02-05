# app/modules/finance/infrastructure/models/category_model.py
from sqlalchemy import Column, Integer, String
from app.shared.infrastructure.db import Base

class CategoryModel(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=False)
    name = Column(String, nullable=False)
    kind = Column(String, nullable=False)   # "income" или "expense"
