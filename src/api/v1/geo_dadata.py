from http import HTTPStatus

from fastapi import APIRouter, Depends

from src.schemas.geolocate import Suggestion
from src.service.client.api_worker import APIWorker

router = APIRouter(
    prefix="/geolocate",
)


@router.get(
    "/address",
    description="Находит ближайшие адреса (дома, улицы, города) по географическим координатам. Только для России.",
    response_model=list[Suggestion],
    status_code=HTTPStatus.OK,
)
async def get_address(
    lat: float, lon: float, api_worker: APIWorker = Depends(APIWorker)
) -> list[dict]:
    return await api_worker.get_address(lat, lon)
