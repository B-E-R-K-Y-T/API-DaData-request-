from http import HTTPStatus

from fastapi import APIRouter, Depends, Query, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from src.schemas.geolocate import Suggestion
from src.service.client.api_worker import APIWorker

router = APIRouter(
    prefix="/geolocate",
)
templates = Jinja2Templates(directory="src/templates")

_RADIUS_METERS_CONSTRAIN = Query(100, ge=1, le=1000)
_COUNT_CONSTRAIN = Query(10, ge=1, le=100)


@router.get(
    "/address",
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
    "/address_view",
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
    data = await api_worker.get_address(lat, lon, radius_meters, count)
    addresses = []

    for item in data:
        addresses.append(
            {
                "value": item.get("value"),
                "unrestricted_value": str(item.get("unrestricted_value")).split(","),
            }
        )

    return templates.TemplateResponse(
        request=request, name="address.html", context={"addresses": addresses}
    )
