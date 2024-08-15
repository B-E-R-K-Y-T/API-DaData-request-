from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, Query, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from src.schemas.geolocate import Suggestion
from src.service.client.api_worker import APIWorker
from src.service.util.address_tool import get_full_address

router = APIRouter(
    prefix="/geolocate",
)
templates = Jinja2Templates(directory="src/templates")

_RADIUS_METERS_CONSTRAIN = Query(100, ge=1, le=1000)
_COUNT_CONSTRAIN = Query(10, ge=1, le=100)


@router.get(
    "/addresses",
    description="Находит ближайшие адреса (дома, улицы, города) по географическим координатам. Только для России.",
    response_model=list[Suggestion],
    status_code=HTTPStatus.OK,
)
async def get_address(
    lat: float,
    lon: float,
    radius_meters: int = _RADIUS_METERS_CONSTRAIN,
    count: int = _COUNT_CONSTRAIN,
    api_worker: APIWorker = Depends(APIWorker),
) -> list[dict]:
    return await api_worker.get_address(lat, lon, radius_meters, count)


@router.get(
    "/addresses_view",
    description="Находит ближайшие адреса (дома, улицы, города) по географическим координатам. "
    "И возвращает HTML. Только для России.",
    response_class=HTMLResponse,
    status_code=HTTPStatus.OK,
)
async def get_address_view(
    request: Request,
    lat: float,
    lon: float,
    radius_meters: int = _RADIUS_METERS_CONSTRAIN,
    count: int = _COUNT_CONSTRAIN,
    api_worker: APIWorker = Depends(APIWorker),
) -> HTMLResponse:
    resp_data = await api_worker.get_address(lat, lon, radius_meters, count)
    addresses = []

    for item in resp_data:
        res = {
                "value": item.get("value"),
                "full_address": "Отсутствует",
                "unrestricted_value": str(item.get("unrestricted_value")).split(","),
            }
        data: dict[str, Optional[str]] = item.get("data")

        if data is not None:
            res["full_address"] = get_full_address(data)

        addresses.append(res)

    return templates.TemplateResponse(
        request=request, name="address.html", context={"addresses": addresses}
    )
