from dadata import DadataAsync

from src.config import settings
from src.service.util.singleton import singleton


@singleton
class APIWorker:
    def __init__(self):
        self.__client = DadataAsync(settings.API_KEY)

    async def get_address(
        self,
        lat: float,
        lon: float,
        radius_meters: int = 100,
        count: int = 10,
    ) -> list[dict]:
        return await self.__client.geolocate(
            "address", lat, lon, radius_meters, count=count
        )
