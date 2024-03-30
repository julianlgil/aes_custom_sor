from datetime import datetime
from typing import Dict, Any
from uuid import UUID

from ofertas.repositories.ofertas import OfertasRepository
from ofertas.services.models import Oferta


class OfertasService:

    def __init__(self, repository: OfertasRepository):
        self.__repository = repository

    async def create(self, oferta: Oferta) -> Dict[str, Any]:
        return await self.__repository.create(oferta=oferta)

    async def update(self, id: UUID, is_accepted: bool) -> Dict[str, Any]:
        return await self.__repository.update(id=id, is_accepted=is_accepted)

    async def get(self, id: UUID) -> Oferta:
        return await self.__repository.get(id=id)

