import unittest
from unittest.mock import create_autospec

from health.repositories.health import HealthRepository
from health.services.health import HealthService


class HealthServiceTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_check_service_is_up_works_when_all_services_are_up(self) -> None:
        health_repository = create_autospec(HealthRepository)

        service = HealthService(health_repository)

        await service.check_service_is_up()

    async def test_check_service_forwards_exception_when_database_fails(self) -> None:
        health_repository = create_autospec(HealthRepository)

        expected_error = Exception('database is down')
        health_repository.check_health.side_effect = expected_error

        service = HealthService(health_repository)

        with self.assertRaises(Exception) as context:
            await service.check_service_is_up()

        self.assertEqual(expected_error, context.exception)


if __name__ == '__main__':
    unittest.main()
