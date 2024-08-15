from dadata import DadataAsync

from src.config import settings
from src.service.util.singleton import singleton


@singleton
class AsyncAPIWorker:
    def __init__(self):
        self.__client = DadataAsync(settings.API_KEY)

    async def get_data(self, name: str, lat: float, lon: float):
        return await self.__client.geolocate(name, lat, lon)
