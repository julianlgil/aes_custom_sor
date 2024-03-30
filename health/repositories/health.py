from sqlalchemy import text
from sqlalchemy.ext.asyncio import async_sessionmaker,AsyncSession


class HealthRepository:
    # pylint: disable=unsubscriptable-object
    def __init__(self, session_maker: async_sessionmaker[AsyncSession]):
        self.__session_maker = session_maker

    async def check_health(self) -> None:
        async with self.__session_maker() as session:
            await session.execute(text('select 1'))
