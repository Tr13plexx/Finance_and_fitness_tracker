from fastapi import FastAPI

from app.shared.infrastructure.db import Base, engine
from app.modules.finance.infrastructure.models.account_model import AccountModel
from app.modules.finance.infrastructure.models.category_model import CategoryModel
from app.modules.finance.infrastructure.models.transaction_model import TransactionModel

app = FastAPI()

# создать таблицы, если их нет
Base.metadata.create_all(bind=engine)