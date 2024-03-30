import unittest
from unittest.mock import Mock

from shared.clients.factory import SupportedClients
from shared.requests.aiohttp_adapter import AiohttpAdapter # type: ignore
from shared.requests.factory import RequestAdapterFactory


class RequestsAdapterFactoryTestCase(unittest.IsolatedAsyncioTestCase):

    def test_aiohttp_adapter_instance(self) -> None:
        client_type = SupportedClients.AIOHTTP
        instance = RequestAdapterFactory.get_adapter(client_type=client_type)
        self.assertIsInstance(instance, AiohttpAdapter)

    def test_factory_when_client_type_not_exist(self) -> None:
        mocked_client_type = Mock()
        mocked_client_type.value.return_value('INVALID_CLIENT')
        with self.assertRaises(ValueError):
            RequestAdapterFactory.get_adapter(client_type=mocked_client_type)
