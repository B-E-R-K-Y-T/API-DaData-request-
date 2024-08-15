from abc import ABC, abstractmethod
from typing import AsyncGenerator, Any

import aiohttp
from aiohttp import ClientResponse

from src.service.util.singleton import singleton


class BaseRequest(ABC):
    @abstractmethod
    def get(self, url: str, **kwargs: dict[str, Any]) -> Any:
        pass

    @abstractmethod
    def close(self):
        pass


@singleton
class AsyncRequest(BaseRequest):
    def __init__(self):
        self.__session = aiohttp.ClientSession()

    async def __request(
            self, method: str, url: str, **kwargs: dict[str, Any]
    ) -> AsyncGenerator[aiohttp.ClientResponse, None]:
        async with self.__session.request(method, url, **kwargs) as resp:
            yield resp

    async def get(self, url: str, **kwargs: dict[str, Any]) -> ClientResponse:
        return await anext(self.__request("GET", url, **kwargs))

    async def close(self):
        await self.__session.close()
