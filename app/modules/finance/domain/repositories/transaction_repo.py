# app/modules/finance/domain/repositories/transaction_repo.py
from typing import Protocol, List
from datetime import datetime
from app.modules.finance.domain.entities.transaction import Transaction

class ITransactionRepository(Protocol):
    def add(self, tx: Transaction) -> Transaction: ...
    def update(self, tx: Transaction) -> Transaction: ...
    def delete(self, tx_id: int, user_id: int) -> None: ...
    def list(
        self,
        user_id: int,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
        account_id: int | None = None,
        category_id: int | None = None,
    ) -> List[Transaction]: ...


