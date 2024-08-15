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
        """
        Получает адреса по заданным координатам.

        :param lat: Широта координат.
        :param lon: Долгота координат.
        :param radius_meters: Радиус поиска в метрах (по умолчанию 100).
        :param count: Количество результатов для возврата (по умолчанию 10).
        :return: Список словарей с адресами.
        """
        return await self.__client.geolocate(
            "address", lat, lon, radius_meters, count=count
        )


__all__ = (
    APIWorker.__name__,
)
