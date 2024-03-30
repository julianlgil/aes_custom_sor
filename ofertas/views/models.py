import uuid
from typing import List
from uuid import UUID

from pydantic import BaseModel

from ofertas.services.models import Oferta


class OfertaCreateRequestDTO(BaseModel):
    client_id: str
    amount: float
    provider: str
    invoices: List[str]
    accepted: bool = False

    def to_oferta(self, id: UUID = None) -> Oferta:
        return Oferta(
            id=id if id else uuid.uuid4(),
            client_id=self.client_id,
            amount=self.amount,
            provider=self.provider,
            invoices=self.invoices,
            accepted=self.accepted
        )


class OfertaUpdateRequestDTO(BaseModel):
    accepted: bool
