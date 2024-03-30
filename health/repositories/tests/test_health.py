import unittest
from unittest.mock import MagicMock, AsyncMock

from health.repositories.health import HealthRepository


class HealthRepositoryTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_check_health_works_when_database_is_up(self) -> None:
        session_maker_mock = MagicMock()
        async with session_maker_mock() as session_mock:
            session_mock.execute = AsyncMock()

        health_repository = HealthRepository(session_maker_mock)

        await health_repository.check_health()

    async def test_check_health_forwards_exception_when_database_fails(self) -> None:
        expected_exception = Exception('database is down')

        session_maker_mock = MagicMock()
        async with session_maker_mock() as session_mock:
            session_mock.execute.side_effect = expected_exception

        health_repository = HealthRepository(session_maker_mock)

        with self.assertRaises(Exception) as context:
            await health_repository.check_health()

        self.assertEqual(expected_exception, context.exception)


if __name__ == '__main__':
    unittest.main()
