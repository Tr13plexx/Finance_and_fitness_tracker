# app/modules/finance/domain/use_cases/add_transaction.py
from datetime import datetime
from decimal import Decimal
from app.modules.finance.domain.value_objects.money import Money
from app.modules.finance.domain.entities.transaction import Transaction
from app.modules.finance.domain.repositories.transaction_repo import ITransactionRepository

class AddTransactionUseCase:
    def __init__(self, tx_repo: ITransactionRepository):
        self.tx_repo = tx_repo

    def execute(
        self,
        user_id: int,
        account_id: int,
        category_id: int | None,
        amount: Decimal,
        currency: str,
        type_: str,
        made_at: datetime,
        description: str | None = None,
    ) -> Transaction:
        money = Money(amount=amount, currency=currency)
        tx = Transaction(
            id=None,
            user_id=user_id,
            account_id=account_id,
            category_id=category_id,
            money=money,
            type=type_,
            made_at=made_at,
            description=description,
        )
        return self.tx_repo.add(tx)
