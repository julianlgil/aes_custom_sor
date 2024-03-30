import asyncio
from asyncio import get_event_loop
from typing import Any, Dict

import aiohttp

from shared.clients.abstract_client import AbstractClient


class AiohttpClient(AbstractClient):
    def _create_session(self, **kwargs: Any) -> aiohttp.ClientSession:  # type: ignore
        headers = kwargs.pop('headers', {})

        session = aiohttp.ClientSession(
            cookies=kwargs.pop('cookies', {}),
            headers=headers,
            timeout=kwargs.pop('timeout', aiohttp.ClientTimeout(total=60)),
            connector=kwargs.pop('connector', aiohttp.TCPConnector(limit=4)),
            **kwargs
        )

        return session

    def __del__(self) -> None:
        self.close()

    @property
    def headers(self) -> Dict[str, str]:
        return dict(self.session.headers)

    @property
    def cookies(self) -> Dict[str, str]:
        return dict(self.session.cookie_jar._cookies)  # pylint: disable=W0212

    @headers.setter  # type: ignore
    def headers(self, headers: Dict[str, str]) -> None:
        pass

    @cookies.setter  # type: ignore
    def cookies(self, cookies: Dict[str, str]) -> None:
        pass

    def close(self) -> None:
        try:
            asyncio.ensure_future(self.session.close())
        except RuntimeError:
            loop = get_event_loop()
            loop.run_until_complete(self.session.close())

    @property
    def user_agent(self) -> str:
        return self.session.headers.get('User-Agent')
