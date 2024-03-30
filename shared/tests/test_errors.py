import unittest

from fastapi import status
from httpx import Response

from shared.errors import ErrorDTO


class ErrorDTOTestCase(unittest.TestCase):
    def test_with_message_creates_a_new_dto_with_the_given_message(self) -> None:
        status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        code = 100
        original_message = 'original message'

        original_error = ErrorDTO(http_status=status_code, code=code, message=original_message)

        new_message = 'new message'
        new_error = original_error.with_message(new_message)

        self.assert_expected_error_dto(new_error, status_code, code, new_message)
        self.assert_expected_error_dto(original_error, status_code, code, original_message)

    def assert_expected_error_dto(
            self,
            error: ErrorDTO,
            expected_status: int,
            expected_code: int,
            expected_message: str,
    ) -> None:
        self.assertEqual(expected_status, error.http_status)
        self.assertEqual(expected_code, error.code)
        self.assertEqual(expected_message, error.message)


def assert_expected_response_error(
        self: unittest.TestCase,
        response: Response,
        expected_error: ErrorDTO,
) -> None:
    self.assertEqual(expected_error.http_status, response.status_code)

    response_error = response.json()

    self.assertEqual(expected_error.http_status, response_error['http_status'])
    self.assertEqual(expected_error.code, response_error['code'])
    self.assertEqual(expected_error.message, response_error['message'])


def assert_expected_response_error_containing_message(
        self: unittest.TestCase,
        response: Response,
        expected_error: ErrorDTO,
        message: str,
) -> None:
    self.assertEqual(expected_error.http_status, response.status_code)

    response_error = response.json()

    self.assertEqual(expected_error.http_status, response_error['http_status'])
    self.assertEqual(expected_error.code, response_error['code'])
    self.assertIn(message, response_error['message'])


if __name__ == '__main__':
    unittest.main()
