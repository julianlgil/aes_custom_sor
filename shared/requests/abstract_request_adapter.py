# type: ignore
from abc import abstractmethod, ABC
from typing import Optional, Dict, Any

from aiohttp import ClientResponseError

from shared.clients.factory import SupportedClients
from shared.exceptions import CustomHTTPError


class AbstractRequestAdapter(ABC):
    # pylint: disable=too-many-instance-attributes
    # pylint:disable=duplicate-code
    # pylint: disable=too-many-arguments

    def __init__(
            self,
            client_type: SupportedClients,
            timeout: int = 30,
            ssl_certificate: Optional[bytes] = b'',
            **kwargs
    ) -> None:

        self._client_type = client_type
        self._client = self._client_type.get_client_instance(**kwargs)
        self._response = None
        self._status_code = None
        self._original_url = None
        self._proxy_params: Dict[str, str] = {}
        self._proxy_cert_path = None
        self._proxy_url = None
        self._timeout = timeout
        self._ssl_certificate = ssl_certificate

    @abstractmethod
    def set_proxy_params(self, proxy_url: str, proxy_cert_path: str) -> None:
        pass

    @abstractmethod
    async def do_request(
            self,
            *args,
            url: str,
            method: str,
            data: Optional[Any] = None,
            query_params: Optional[Dict] = None,
            json: Optional[Any] = None,
            timeout: Optional[int] = None,
            **kwargs
    ) -> None:
        pass

    @abstractmethod
    async def get_html_response(self) -> str:
        pass

    @abstractmethod
    async def get_binary_response(self) -> bytes:
        pass

    @abstractmethod
    async def get_xml_response(self) -> str:
        pass

    @abstractmethod
    async def get_json_response(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def get_plain_text_response(self) -> str:
        pass

    @abstractmethod
    async def get_session(self) -> Any:
        pass

    def raise_for_status(self):
        """Method for raise an exception related with error http status code.
        This method allows handle the different exceptions raised by each supported adapter
        for only have handle the CustomHttpError in the logic using the adapters. This approach
        keeps the adapters and logic using it uncoupled of the adapter type.

        Raises:
            CustomHTTPError: Raised when is handled an exception related with
            HTTP Errors
        """
        try:
            self._response.raise_for_status()
        except ClientResponseError as e:
            reason = self._response.reason
            message = (
                self._response.reason.encode('utf-8', 'surrogateescape').decode('iso-8859-15')
                if isinstance(reason, str)
                else reason
            )
            raise CustomHTTPError(self._status_code, message, self._original_url) from e
