from health.repositories.health import HealthRepository


class HealthService:

    def __init__(self, repository: HealthRepository):
        self.__repository = repository

    async def check_service_is_up(self) -> None:
        await self.__repository.check_health()
