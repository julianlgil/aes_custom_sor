from dataclasses import dataclass
from datetime import datetime
from typing import List
from uuid import UUID


@dataclass(frozen=True)
class Oferta:
    id: UUID
    client_id: str
    amount: float
    provider: str
    invoices: List[str]
    accepted: bool
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
