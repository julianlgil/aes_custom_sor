import json
from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from ofertas.services.models import Oferta


class Base(DeclarativeBase):
    pass


class OfertaDAO(Base):
    __tablename__ = 'ofertas'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    client_id: Mapped[str]
    amount: Mapped[float]
    provider: Mapped[str]
    invoices: Mapped[str]
    accepted: Mapped[bool]
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]

    @staticmethod
    def from_oferta(oferta: Oferta):
        return OfertaDAO(
            id=oferta.id,
            client_id=oferta.client_id,
            amount=oferta.amount,
            provider=oferta.provider,
            invoices=json.dumps(oferta.invoices),
            accepted=oferta.accepted,
            created_at=oferta.created_at,
            updated_at=oferta.updated_at
        )

    def to_oferta(self) -> Oferta:
        return Oferta(
            id=self.id,
            client_id=self.client_id,
            amount=self.amount,
            provider=self.provider,
            invoices=json.loads(self.invoices),
            accepted=self.accepted,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
