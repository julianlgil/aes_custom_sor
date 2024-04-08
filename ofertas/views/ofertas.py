from typing import Any, Dict
from uuid import UUID

from fastapi import FastAPI, status
from pydantic import BaseModel

from ofertas.services.models import Oferta
from shared.errors import SERVICE_UNAVAILABLE_ERROR, ResponseException

from ofertas.services.ofertas import OfertasService
from ofertas.views.models import OfertaCreateRequestDTO, OfertaUpdateRequestDTO, RiskScore


def register_ofertas_view(app: FastAPI, service: OfertasService) -> None:
    @app.post(
        '/ofertas',
        status_code=status.HTTP_200_OK,
        tags=['Ofertas']
    )
    async def create(request_dto: OfertaCreateRequestDTO) -> Dict[str, Any]:
        try:
            oferta = request_dto.to_oferta()
            return await service.create(oferta=oferta)
        except Exception as e:
            raise ResponseException(SERVICE_UNAVAILABLE_ERROR) from e

    @app.put(
        '/ofertas/{id}/accept',
        status_code=status.HTTP_200_OK,
        tags=['Ofertas']
    )
    async def update(id: UUID, request_dto: OfertaUpdateRequestDTO) -> Dict[str, Any]:
        try:
            return await service.update(id=id, is_accepted=request_dto.accepted)
        except Exception as e:
            raise ResponseException(SERVICE_UNAVAILABLE_ERROR) from e

    @app.get(
        '/ofertas/{id}',
        status_code=status.HTTP_200_OK,
        tags=['Ofertas']
    )
    async def update(id: UUID) -> Oferta:
        try:
            return await service.get(id=id)
        except Exception as e:
            raise ResponseException(SERVICE_UNAVAILABLE_ERROR) from e

    @app.post("/validar_score_riego")
    def validar_score_riego(risk_score: RiskScore):
        if risk_score.provider == 'WORLDOFFICE':
            return {"score": 50.86}
        return {"score": 95}

    @app.post("/ceder_facturas")
    def ceder_facturas(payload: Dict[str, Any]):
        print(payload)
        return {"resultado": True if payload.get('facturas') else False}