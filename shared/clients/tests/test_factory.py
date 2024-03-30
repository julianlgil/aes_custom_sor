import unittest

from shared.clients.aiohttp_client import AiohttpClient
from shared.clients.factory import SupportedClients


class SupportedClientsFactoryTestCase(unittest.IsolatedAsyncioTestCase):

    def test_aiohttp_client_instance(self) -> None:
        client_type = SupportedClients.AIOHTTP
        instance = client_type.get_client_instance()
        self.assertIsInstance(instance, AiohttpClient)
