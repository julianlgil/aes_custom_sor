from datetime import datetime
from typing import Any, Dict
from uuid import UUID

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import update, select

from ofertas.repositories.models import OfertaDAO
from ofertas.services.models import Oferta


class OfertasRepository:
    def __init__(self, session_maker: async_sessionmaker[AsyncSession]):
        self.__session_maker = session_maker

    async def create(self, oferta: Oferta) -> Dict[str, Any]:
        async with self.__session_maker() as session:
            async with session.begin():
                current_datetime = datetime.now()
                oferta_dao = OfertaDAO.from_oferta(oferta)
                insert_stmt = insert(OfertaDAO).values(  # type: ignore
                    id=oferta_dao.id,
                    client_id=oferta_dao.client_id,
                    amount=oferta_dao.amount,
                    provider=oferta_dao.provider,
                    invoices=oferta_dao.invoices,
                    accepted=oferta_dao.accepted,
                    created_at=current_datetime,
                    updated_at=current_datetime
                )

                await session.execute(insert_stmt)
                return {
                    "id": oferta_dao.id
                }

    async def update(self, id: UUID, is_accepted: bool) -> Dict[str, Any]:
        async with (self.__session_maker() as session):
            async with session.begin():
                current_datetime = datetime.now()
                insert_stmt = update(OfertaDAO).where(
                    OfertaDAO.id == id
                ).values(  # type: ignore
                    accepted=is_accepted,
                    updated_at=current_datetime
                )

                await session.execute(insert_stmt)
                return {
                    "id": id
                }


    async def get(self, id: UUID) -> Oferta:
        async with (self.__session_maker() as session):
            async with session.begin():
                query = select(OfertaDAO).where(
                            OfertaDAO.id == id
                    )
                oferta_result = await session.execute(query)

                return oferta_result.scalar_one().to_oferta()
