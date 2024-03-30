# type: ignore
import asyncio
import ssl
from typing import Any, Dict, Optional

import aiohttp

from shared.clients.factory import SupportedClients
from shared.exceptions import CustomTimeoutError
from shared.requests.abstract_request_adapter import AbstractRequestAdapter


class AiohttpAdapter(AbstractRequestAdapter):
    def __init__(self, *args, timeout: int = 30, **kwargs):
        super().__init__(
            client_type=SupportedClients.AIOHTTP,
            timeout=timeout,
            *args,
            **kwargs
        )

    def set_proxy_params(self, proxy_url: str, proxy_cert_path: str):
        self._proxy_cert_path = proxy_cert_path
        self._proxy_url = proxy_url
        sslcontext = ssl.create_default_context(cafile=self._proxy_cert_path)
        self._proxy_params = {'ssl': sslcontext, 'proxy': self._proxy_url}

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
    ):
        self._original_url = url
        try:
            timeout_to_set = timeout if timeout is not None else self._timeout
            timeout_obj = aiohttp.ClientTimeout(total=timeout_to_set)

            self._response = await self._client.session.request(
                method=method,
                url=url,
                data=data,
                json=json,
                params=query_params,
                timeout=timeout_obj,
                *args,
                **kwargs,
                **self._proxy_params
            )
        except asyncio.TimeoutError as e:
            raise CustomTimeoutError(url, method) from e

        self._status_code = self._response.status
        self.raise_for_status()

    async def get_html_response(self) -> str:
        pass

    async def get_binary_response(self) -> bytes:
        return await self._response.read()

    async def get_xml_response(self) -> str:
        pass

    async def get_json_response(self, content_type=None, encoding=None) -> Dict[str, str]:
        return await self._response.json(content_type=content_type, encoding=encoding)

    async def get_plain_text_response(self) -> str:
        return await self._response.text()

    async def get_session(self) -> Any:
        return self._client.session
