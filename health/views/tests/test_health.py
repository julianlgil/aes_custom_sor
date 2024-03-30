import unittest
from unittest.mock import create_autospec, Mock

from fastapi import status
from fastapi.testclient import TestClient
from httpx import Response

from app.app import new_app
from health.services.health import HealthService
from shared.errors import SERVICE_UNAVAILABLE_ERROR
from shared.tests.test_errors import assert_expected_response_error


class HealthViewTestCase(unittest.TestCase):
    def test_health_when_service_is_up_returns_success(self) -> None:
        health_service = create_autospec(HealthService)

        client = HealthViewTestCase.__new_test_client(health_service)

        response = client.get('/health')

        self.check_up_response(response)

    def test_health_when_service_is_down_returns_service_unavailable(self) -> None:
        health_service = create_autospec(HealthService)
        health_service.check_service_is_up.side_effect = Exception('something is down')

        client = HealthViewTestCase.__new_test_client(health_service)

        response = client.get('/health')

        assert_expected_response_error(self, response, SERVICE_UNAVAILABLE_ERROR)

    def check_up_response(self, response: Response) -> None:
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        parsed_response = response.json()
        self.assertEqual('Service is up!', parsed_response['message'])

    @staticmethod
    def __new_test_client(health_service: HealthService) -> TestClient:
        app = new_app(health_service, Mock(), Mock(), Mock(), Mock(), ['*'])
        return TestClient(app)


if __name__ == '__main__':
    unittest.main()
