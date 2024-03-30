from typing import Any

from shared.clients.factory import SupportedClients
from shared.requests.abstract_request_adapter import AbstractRequestAdapter  # type: ignore
from shared.requests.aiohttp_adapter import AiohttpAdapter  # type: ignore


class RequestAdapterFactory:
    creators = {
        'AIOHTTP': AiohttpAdapter,
    }

    @staticmethod
    def get_adapter(client_type: SupportedClients, **config: Any) -> AbstractRequestAdapter:  # type: ignore
        client_type_name = client_type.value
        if client_type_name not in RequestAdapterFactory.creators:
            raise ValueError(client_type_name)
        return RequestAdapterFactory.creators[client_type_name](**config)
