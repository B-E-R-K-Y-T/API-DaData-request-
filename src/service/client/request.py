from typing import AsyncGenerator, Any

import aiohttp
from aiohttp import ClientResponse


class Request:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def __request(
        self, method: str, url: str, **kwargs: dict[str, Any]
    ) -> AsyncGenerator[aiohttp.ClientResponse, None]:
        async with self.session.request(method, url, **kwargs) as resp:
            yield resp

    async def get(self, url: str, **kwargs: dict[str, Any]) -> ClientResponse:
        return await anext(self.__request("GET", url, **kwargs))

    async def close(self):
        await self.session.close()
