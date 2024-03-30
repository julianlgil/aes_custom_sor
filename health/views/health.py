from fastapi import FastAPI, status
from pydantic import BaseModel

from health.services.health import HealthService
from shared.errors import SERVICE_UNAVAILABLE_ERROR, ResponseException


class _HealthDTO(BaseModel):
    message: str

    class Config:
        allow_mutation = False


def register_health_view(app: FastAPI, service: HealthService) -> None:
    @app.get(
        '/health',
        status_code=status.HTTP_200_OK,
        summary='Check if the service is healthy',
        response_description='A success message if the service is up. An error if not',
        tags=['Health']
    )
    async def health() -> _HealthDTO:
        """
        Check if the service and it's dependencies are up
        """
        try:
            await service.check_service_is_up()
        except Exception as e:
            raise ResponseException(SERVICE_UNAVAILABLE_ERROR) from e

        return _HealthDTO(message='Service is up!')
