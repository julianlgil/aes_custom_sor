from __future__ import annotations

import logging

from fastapi import status, Request, FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel


logger = logging.getLogger(__name__)


class ErrorDTO(BaseModel):
    http_status: int
    code: int
    message: str

    class Config:
        allow_mutation = False

    def with_message(self, message: str) -> ErrorDTO:
        return ErrorDTO(http_status=self.http_status, code=self.code, message=message)


BAD_REQUEST_ERROR = ErrorDTO(
    http_status=status.HTTP_400_BAD_REQUEST,
    code=status.HTTP_400_BAD_REQUEST,
    message='Bad Request',
)


NOT_FOUND_ERROR = ErrorDTO(
    http_status=status.HTTP_404_NOT_FOUND,
    code=status.HTTP_404_NOT_FOUND,
    message='Entity not found',
)


SERVICE_UNAVAILABLE_ERROR = ErrorDTO(
    http_status=status.HTTP_503_SERVICE_UNAVAILABLE,
    code=status.HTTP_503_SERVICE_UNAVAILABLE,
    message='Service Unavailable',
)


UNAUTHORIZED_ERROR = ErrorDTO(
    http_status=status.HTTP_403_FORBIDDEN,
    code=status.HTTP_403_FORBIDDEN,
    message='Forbidden',
)


SERVER_ERROR = ErrorDTO(
    http_status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    message='Internal Server Error',
)


class ResponseException(Exception):
    def __init__(self, error: ErrorDTO):
        super().__init__(error.message)

        self.error = error


def register_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(RequestValidationError)
    async def handle_request_errors(_: Request, e: RequestValidationError) -> JSONResponse:
        logger.info('Request error', exc_info=e)

        error = BAD_REQUEST_ERROR.with_message(str(e))

        return JSONResponse(
            status_code=error.http_status,
            content=error.dict(),
        )

    @app.exception_handler(ResponseException)
    async def handle_custom_errors(_: Request, e: ResponseException) -> JSONResponse:
        logger.warning('Handled error', exc_info=e)

        return JSONResponse(
            status_code=e.error.http_status,
            content=e.error.dict(),
        )

    # We can't use exception_handler for the base exception, see
    # https://stackoverflow.com/a/66416119. So we have to use a middleware instead
    @app.middleware('http')
    # type: ignore
    async def catch_exceptions_middleware(request: Request, call_next):
        try:
            return await call_next(request)
        # pylint: disable=broad-exception-caught
        except Exception:
            logger.exception('Unhandled error')

            return JSONResponse(
                status_code=SERVER_ERROR.http_status,
                content=SERVER_ERROR.dict(),
            )
