from enum import Enum
from typing import Any

from shared.clients.abstract_client import AbstractClient
from shared.clients.aiohttp_client import AiohttpClient


class SupportedClients(Enum):
    AIOHTTP = 'AIOHTTP'

    def __init__(self, client_type: str) -> None:
        self.client_type = client_type
        self.__creators = {
            'AIOHTTP': AiohttpClient,
        }

    def get_client_instance(self, **config: Any) -> AbstractClient:  # type: ignore
        return self.__creators[self.client_type](**config)
